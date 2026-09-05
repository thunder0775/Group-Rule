#!/usr/bin/env python3
"""Fetch, validate, isolate, audit and compile Shadowrocket rules."""
from __future__ import annotations

import hashlib
import ipaddress
import json
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CFG, RULES, REPORTS = ROOT / "config", ROOT / "rules", ROOT / "reports"
ALLOWED = {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD", "IP-CIDR", "IP-CIDR6", "USER-AGENT", "URL-REGEX", "PROCESS-NAME", "DEST-PORT", "DST-PORT", "GEOIP"}
DOMAIN_TYPES = {"DOMAIN", "DOMAIN-SUFFIX"}
IP_TYPES = {"IP-CIDR", "IP-CIDR6"}
BROAD_KEYWORDS = {"api", "cdn", "mail", "cloud", "data", "login", "live", "app"}
ROOT_TLDS = {"com", "net", "org", "cn", "uk", "de", "fr", "jp", "kr", "us", "io", "ai", "app", "dev", "me", "tv", "co", "xyz", "info", "biz", "site", "online", "tech", "top", "pro"}


def now():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def norm(line):
    line = line.replace("\ufeff", "").strip()
    if not line or line.startswith(("#", ";")):
        return None
    parts = [x.strip() for x in line.split(",")]
    if len(parts) < 2 or parts[0] not in ALLOWED or not parts[1]:
        return None
    return f"{parts[0]},{parts[1]}"


def domain_norm(value):
    return value.strip().lower().rstrip(".")


def valid_domain(value):
    value = domain_norm(value)
    if not value or " " in value or "/" in value or ":" in value or len(value) > 253:
        return False
    labels = value.split(".")
    if any(not x or len(x) > 63 for x in labels):
        return False
    try:
        value.encode("idna")
    except UnicodeError:
        return False
    return True


def parse(text, mode="rules", expected_policy=None):
    rules, seen = [], set()
    in_rule = mode != "shadowrocket_conf"
    for line in text.splitlines():
        s = line.replace("\ufeff", "").strip()
        if not s:
            continue
        if mode == "shadowrocket_conf" and s.startswith("[") and s.endswith("]"):
            in_rule = s.lower() == "[rule]"
            continue
        if mode == "shadowrocket_conf" and not in_rule:
            continue
        if mode == "domains":
            rule = None if s.startswith(("#", ";")) or "," in s or not valid_domain(s) else f"DOMAIN-SUFFIX,{domain_norm(s)}"
        else:
            parts = [x.strip() for x in s.split(",")]
            if expected_policy is not None and (len(parts) < 3 or parts[2].upper() != expected_policy.upper()):
                continue
            rule = norm(s)
        if rule and rule not in seen:
            seen.add(rule)
            rules.append(rule)
    return rules


def source_line_stats(text, mode):
    considered = malformed = 0
    in_rule = mode != "shadowrocket_conf"
    for line in text.splitlines():
        s = line.replace("\ufeff", "").strip()
        if not s:
            continue
        if mode == "shadowrocket_conf" and s.startswith("[") and s.endswith("]"):
            in_rule = s.lower() == "[rule]"
            continue
        if (mode == "shadowrocket_conf" and not in_rule) or s.startswith(("#", ";")):
            continue
        considered += 1
        if (mode == "domains" and ("," in s or not valid_domain(s))) or (mode != "domains" and norm(s) is None):
            malformed += 1
    return considered, malformed


def fetch(url, timeout, max_bytes):
    req = urllib.request.Request(url, headers={"User-Agent": "Group-Rule/7.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        data = resp.read(max_bytes + 1)
        if len(data) > max_bytes:
            raise ValueError("response_too_large")
        headers = {k.lower(): v for k, v in resp.headers.items()}
        return data.decode("utf-8-sig"), {"status_code": getattr(resp, "status", 200), "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(), "final_url": resp.geturl(), "content_type": headers.get("content-type", "")}


def validate_source(text, rules, min_rules, prev_count, min_ratio, max_ratio, max_invalid_ratio, mode):
    considered, malformed = source_line_stats(text, mode)
    low = text.lower()
    if "<html" in low or "<!doctype html" in low:
        return "html_instead_of_rules", considered, malformed
    if len(rules) < min_rules:
        return "too_few_rules", considered, malformed
    if prev_count >= 10 and len(rules) < int(prev_count * min_ratio):
        return "sudden_rule_count_drop", considered, malformed
    if prev_count >= 10 and len(rules) > int(prev_count * max_ratio):
        return "sudden_rule_count_growth", considered, malformed
    if considered >= 10 and malformed / considered > max_invalid_ratio:
        return "high_invalid_rule_ratio", considered, malformed
    return None, considered, malformed


def atomic_path(category, name):
    return RULES / "atomic" / category / f"{name}.list"


def read_previous(path):
    return parse(path.read_text(encoding="utf-8")) if path.exists() else []


def read_history():
    path = REPORTS / "source-history.json"
    if not path.exists():
        return {}
    try:
        return load(path)
    except Exception:
        return {}


def write_list(path, rules, kind):
    path.parent.mkdir(parents=True, exist_ok=True)
    header = ["# Generated by thunder0775/Group-Rule", f"# Type: {kind}", f"# Generated: {now()}", "# Policy intentionally omitted; assign policy in Shadowrocket .conf."]
    path.write_text("\n".join(header + list(dict.fromkeys(rules))) + "\n", encoding="utf-8")


def validate_rule_set(rules):
    invalid_domains, invalid_cidrs, risky_keywords = [], [], []
    type_counts = defaultdict(int)
    for rule in rules:
        kind, value = rule.split(",", 1)
        type_counts[kind] += 1
        if kind in DOMAIN_TYPES and not valid_domain(value):
            invalid_domains.append(rule)
        elif kind in IP_TYPES:
            try:
                ipaddress.ip_network(value, strict=False)
            except ValueError:
                invalid_cidrs.append(rule)
        elif kind == "DOMAIN-KEYWORD":
            keyword = value.strip().lower()
            if len(keyword) < 4 or keyword in BROAD_KEYWORDS:
                risky_keywords.append(rule)
    return {"type_counts": dict(sorted(type_counts.items())), "invalid_domains": invalid_domains, "invalid_cidrs": invalid_cidrs, "risky_keywords": risky_keywords}


def semantic_domain_audit(categories, limit):
    suffixes = defaultdict(set)
    findings = set()
    risky = set()
    for category, items in categories.items():
        for name, rules in items.items():
            for rule in rules:
                kind, value = rule.split(",", 1)
                value = domain_norm(value)
                if kind == "DOMAIN-SUFFIX" and "." in value and value not in ROOT_TLDS:
                    suffixes[value].add((category, name, rule))
                elif kind == "DOMAIN-KEYWORD" and (len(value) < 4 or value in BROAD_KEYWORDS):
                    risky.add((category, name, rule))
    for category, items in categories.items():
        for name, rules in items.items():
            for rule in rules:
                kind, value = rule.split(",", 1)
                if kind not in DOMAIN_TYPES:
                    continue
                domain = domain_norm(value)
                labels = domain.split(".")
                parents = [".".join(labels[i:]) for i in range(1, len(labels))]
                if kind == "DOMAIN":
                    parents = [domain] + parents
                for parent in parents:
                    if "." not in parent or parent in ROOT_TLDS:
                        continue
                    for pcat, pname, prule in suffixes.get(parent, set()):
                        findings.add((rule, prule, category, name, pcat, pname, "exact_domain_covered" if kind == "DOMAIN" else "child_suffix_covered"))
                    if parent in suffixes:
                        break
    sample = [{"type": x[6], "covered": {"category": x[2], "item": x[3], "rule": x[0]}, "covering": {"category": x[4], "item": x[5], "rule": x[1]}} for x in sorted(findings)[:limit]]
    risky_samples = [{"rule": r, "category": c, "item": n, "reason": "broad_or_short_keyword"} for c, n, r in sorted(risky)[:limit]]
    return {"count": len(findings), "samples": sample, "risky_keyword_count": len(risky), "risky_keyword_samples": risky_samples}


class Trie:
    __slots__ = ("children", "owners")
    def __init__(self):
        self.children, self.owners = {}, []


def semantic_cidr_audit(categories, limit):
    networks = []
    for category, items in categories.items():
        for name, rules in items.items():
            for rule in rules:
                kind, value = rule.split(",", 1)
                if kind not in IP_TYPES:
                    continue
                try:
                    network = ipaddress.ip_network(value, strict=False)
                except ValueError:
                    continue
                networks.append((network.version, network.prefixlen, int(network.network_address), category, name, rule))
    findings = set()
    for version in (4, 6):
        root = Trie()
        bits = 32 if version == 4 else 128
        for _, prefix_len, address, category, name, rule in sorted((x for x in networks if x[0] == version), key=lambda x: (x[1], x[2], x[3], x[4])):
            node, covered = root, set()
            for index in range(prefix_len):
                covered.update(node.owners)
                bit = (address >> (bits - 1 - index)) & 1
                node = node.children.setdefault(bit, Trie())
            covered.update(node.owners)
            for owner_category, owner_name in covered:
                findings.add((rule, category, name, owner_category, owner_name))
            node.owners.append((category, name))
    sample = [{"rule": r, "category": c, "item": n, "reason": "covered_by_parent_cidr", "covered_by": {"category": oc, "item": oi}} for r, c, n, oc, oi in sorted(findings)[:limit]]
    return {"count": len(findings), "samples": sample, "cidr_rule_count": len(networks)}


def build_outputs(categories, order):
    rank = {category: index for index, category in enumerate(order)}
    winners = {}
    for category in order + [x for x in categories if x not in order]:
        for rules in categories.get(category, {}).values():
            for rule in rules:
                if rule not in winners or rank.get(category, 10**9) < rank.get(winners[rule], 10**9):
                    winners[rule] = category
    outputs = {category: list(dict.fromkeys(rule for rules in items.values() for rule in rules if winners.get(rule) == category)) for category, items in categories.items()}
    return outputs, winners


def validate_outputs(outputs):
    problems, counts = [], {}
    for category, rules in outputs.items():
        counts[category] = len(rules)
        for rule in rules:
            if norm(rule) != rule:
                problems.append({"category": category, "rule": rule, "reason": "invalid_normalized_rule"})
                continue
            if len(rule.split(",")) != 2:
                problems.append({"category": category, "rule": rule, "reason": "policy_leakage"})
                continue
            kind, value = rule.split(",", 1)
            if kind in DOMAIN_TYPES and not valid_domain(value):
                problems.append({"category": category, "rule": rule, "reason": "invalid_domain"})
            elif kind in IP_TYPES:
                try:
                    ipaddress.ip_network(value, strict=False)
                except ValueError:
                    problems.append({"category": category, "rule": rule, "reason": "invalid_cidr"})
    return {"valid": not problems, "problem_count": len(problems), "problems": problems[:200], "counts": counts}


def config_audit(scfg, pcfg):
    findings = []
    sources = scfg.get("sources")
    if not isinstance(sources, dict) or not sources:
        findings.append({"severity": "BLOCK", "reason": "no_sources_configured"})
    for category, items in (sources or {}).items():
        if not isinstance(items, dict):
            findings.append({"severity": "BLOCK", "category": category, "reason": "category_not_object"})
            continue
        for name, source_list in items.items():
            if not isinstance(source_list, list):
                findings.append({"severity": "BLOCK", "category": category, "item": name, "reason": "sources_not_list"})
                continue
            for source in source_list:
                obj = {"url": source} if isinstance(source, str) else source if isinstance(source, dict) else {}
                url = obj.get("url", "")
                parsed = urllib.parse.urlparse(url)
                if not url or parsed.scheme not in {"http", "https"} or not parsed.netloc:
                    findings.append({"severity": "BLOCK", "category": category, "item": name, "url": url, "reason": "invalid_source_url"})
    order = pcfg.get("category_order", [])
    if len(order) != len(set(order)):
        findings.append({"severity": "BLOCK", "reason": "duplicate_category_order"})
    if set(order) != set(sources or {}):
        findings.append({"severity": "BLOCK", "reason": "priority_categories_mismatch", "configured": order, "sources": sorted((sources or {}).keys())})
    return findings


def main():
    generated = now()
    scfg, pcfg = load(CFG / "sources.json"), load(CFG / "priority.json")
    health = scfg.get("health", {})
    timeout, max_bytes = int(scfg.get("source_timeout", 30)), int(scfg.get("max_bytes", 10 * 1024 * 1024))
    min_default = int(health.get("min_rules", 1)); min_ratio = float(health.get("min_rule_ratio", 0.2)); max_ratio = float(health.get("max_rule_ratio", 10.0)); max_invalid = float(health.get("max_invalid_ratio", 0.8)); limit = min(int(health.get("max_audit_samples", 200)), 1000)

    previous_source_counts = {}
    old_report = REPORTS / "latest.json"
    if old_report.exists():
        try:
            old = load(old_report)
            for status in old.get("status", {}).values():
                for source in status.get("sources", []):
                    if source.get("url"):
                        previous_source_counts[source["url"]] = int(source.get("rules", 0))
        except Exception:
            pass

    history = read_history()
    statuses, categories, quality = {}, defaultdict(dict), {}
    for category, items in scfg.get("sources", {}).items():
        for name, sources in items.items():
            target = atomic_path(category, name); previous = read_previous(target); candidates = []; results = []; healthy = 0
            for raw in sources:
                source = {"url": raw} if isinstance(raw, str) else raw if isinstance(raw, dict) else {}
                url = source.get("url", ""); mode = source.get("mode", "rules"); policy = source.get("policy")
                min_rules = int(source.get("min_rules", min_default)); source_min_ratio = float(source.get("min_rule_ratio", min_ratio)); source_max_ratio = float(source.get("max_rule_ratio", max_ratio)); source_invalid_ratio = float(source.get("max_invalid_ratio", max_invalid)); previous_count = previous_source_counts.get(url, 0)
                try:
                    text, meta = fetch(url, timeout, max_bytes); parsed = parse(text, mode, policy); reason, considered, malformed = validate_source(text, parsed, min_rules, previous_count, source_min_ratio, source_max_ratio, source_invalid_ratio, mode)
                    final_host = urllib.parse.urlparse(meta["final_url"]).netloc; source_host = urllib.parse.urlparse(url).netloc
                    redirect_changed = bool(final_host and source_host and final_host != source_host)
                    item = {"url": url, "mode": mode, "policy_filter": policy, "min_rules": min_rules, "previous_source_rules": previous_count, "considered_lines": considered, "malformed_lines": malformed, "invalid_ratio": round(malformed / considered, 4) if considered else 0, **meta, "rules": len(parsed), "status": "ok" if reason is None else "rejected", "redirect_host_changed": redirect_changed}
                    if reason: item["reason"] = reason
                    if reason is None:
                        candidates.extend(parsed); healthy += 1
                        old = history.get(url, {})
                        history[url] = {"sha256": meta["sha256"], "rules": len(parsed), "first_seen": old.get("first_seen", generated), "last_seen": generated, "last_changed": generated if old.get("sha256") != meta["sha256"] else old.get("last_changed", generated), "unchanged_runs": int(old.get("unchanged_runs", 0)) + 1 if old.get("sha256") == meta["sha256"] else 0}
                except Exception as exc:
                    item = {"url": url, "mode": mode, "policy_filter": policy, "min_rules": min_rules, "previous_source_rules": previous_count, "status": "error", "error": str(exc)}
                results.append(item)
            custom = [norm(x) for x in scfg.get("custom", {}).get(f"{category}/{name}.list", []) if isinstance(x, str)]; custom = [x for x in custom if x]
            candidates = list(dict.fromkeys(candidates + custom))
            if candidates and (healthy > 0 or not sources):
                write_list(target, candidates, f"atomic:{category}/{name}"); current, state = candidates, "updated"
            elif previous:
                write_list(target, previous, f"atomic:{category}/{name}:last-known-good"); current, state = previous, "kept_previous"
            else:
                current, state = [], "unavailable"
            categories[category][name] = current
            statuses[f"{category}/{name}"] = {"state": state, "rule_count": len(current), "previous_count": len(previous), "healthy_sources": healthy, "sources": results}
            quality[f"{category}/{name}"] = validate_rule_set(current)

    order = pcfg.get("category_order", list(categories)); outputs, winners = build_outputs(categories, order); compiled = {}
    for category, rules in outputs.items():
        write_list(RULES / "compiled" / f"{category}.list", rules, f"compiled:{category}"); compiled[category] = len(rules)

    locations = defaultdict(list)
    for category, items in categories.items():
        for name, rules in items.items():
            for rule in rules: locations[rule].append((category, name))
    conflicts = {rule: sorted({category for category, _ in locs}) for rule, locs in locations.items() if len({category for category, _ in locs}) > 1}
    same_category_duplicates = {rule: sorted(locs) for rule, locs in locations.items() if len(locs) > 1 and len({category for category, _ in locs}) == 1}
    domain_audit = semantic_domain_audit(categories, limit); cidr_audit = semantic_cidr_audit(categories, limit); output_audit = validate_outputs(outputs); cfg_findings = config_audit(scfg, pcfg)
    invalid_domain = sum(len(v["invalid_domains"]) for v in quality.values()); invalid_cidr = sum(len(v["invalid_cidrs"]) for v in quality.values()); risky_keywords = domain_audit["risky_keyword_count"] + sum(len(v["risky_keywords"]) for v in quality.values()); exact_duplicates = sum(max(0, len(locs) - 1) for locs in locations.values())

    findings = list(cfg_findings)
    for key, status in statuses.items():
        if status["state"] == "unavailable": findings.append({"severity": "BLOCK", "category": key, "reason": "atomic_rule_unavailable_no_last_known_good"})
        elif status["state"] == "kept_previous": findings.append({"severity": "WARNING", "category": key, "reason": "using_last_known_good"})
        for source in status["sources"]:
            if source.get("status") != "ok": findings.append({"severity": "WARNING", "category": key, "reason": source.get("reason", source.get("error", "source_error")), "url": source.get("url")})
            elif source.get("redirect_host_changed"): findings.append({"severity": "WARNING", "category": key, "reason": "redirect_host_changed", "url": source.get("url"), "final_url": source.get("final_url")})
    if not output_audit["valid"]: findings.append({"severity": "BLOCK", "reason": "compiled_output_invalid", "count": output_audit["problem_count"]})
    if invalid_domain: findings.append({"severity": "BLOCK", "reason": "invalid_domain_in_current_rules", "count": invalid_domain})
    if invalid_cidr: findings.append({"severity": "BLOCK", "reason": "invalid_cidr_in_current_rules", "count": invalid_cidr})
    if risky_keywords: findings.append({"severity": "WARNING", "reason": "risky_domain_keyword", "count": risky_keywords})
    if domain_audit["count"]: findings.append({"severity": "INFO", "reason": "semantic_domain_redundancy", "count": domain_audit["count"]})
    if cidr_audit["count"]: findings.append({"severity": "INFO", "reason": "semantic_cidr_redundancy", "count": cidr_audit["count"]})

    severity_counts = defaultdict(int)
    for finding in findings: severity_counts[finding["severity"]] += 1
    blocked = severity_counts.get("BLOCK", 0) > 0
    report = {
        "generated_at": generated,
        "status": statuses,
        "compiled_counts": compiled,
        "cross_category_conflicts": conflicts,
        "same_category_duplicates": same_category_duplicates,
        "conflict_resolution": {rule: {"winner": winners[rule], "categories": cats} for rule, cats in conflicts.items()},
        "priority": pcfg,
        "source_rule_quality": quality,
        "semantic_domain_audit": domain_audit,
        "semantic_cidr_audit": cidr_audit,
        "compiled_output_audit": output_audit,
        "config_audit": cfg_findings,
        "gate": {"status": "BLOCKED" if blocked else "PASS", "severity_counts": dict(severity_counts), "findings": findings[:limit]},
        "global_quality": {"exact_duplicate_occurrences": exact_duplicates, "same_category_duplicate_rule_count": len(same_category_duplicates), "cross_category_conflict_count": len(conflicts), "semantic_domain_redundancy_count": domain_audit["count"], "semantic_cidr_redundancy_count": cidr_audit["count"], "invalid_domain_count": invalid_domain, "invalid_cidr_count": invalid_cidr, "risky_keyword_count": risky_keywords, "compiled_output_problem_count": output_audit["problem_count"]},
    }
    REPORTS.mkdir(parents=True, exist_ok=True)
    (REPORTS / "latest.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (REPORTS / "source-history.json").write_text(json.dumps(history, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    md = ["# Group-Rule 审计报告", "", f"生成时间：`{generated}`", f"发布闸门：**{'BLOCKED' if blocked else 'PASS'}**", "", "## 审计等级", "", "- `BLOCK`：禁止本次生成结果进入 Git 提交。", "- `ERROR`：严重运行异常。", "- `WARNING`：记录并继续，异常原子规则使用 Last Known Good。", "- `INFO`：信息类质量提示。", "", "## 总体质量", "", f"- 精确重复出现次数：`{exact_duplicates}`", f"- 同分类重复规则：`{len(same_category_duplicates)}`", f"- 跨分类重复规则：`{len(conflicts)}`", f"- DOMAIN 语义冗余：`{domain_audit['count']}`", f"- CIDR 语义冗余：`{cidr_audit['count']}`", f"- 无效 DOMAIN：`{invalid_domain}`", f"- 无效 CIDR：`{invalid_cidr}`", f"- 高风险 DOMAIN-KEYWORD：`{risky_keywords}`", "", "## 分类统计", ""]
    md += [f"- `{category}`：{count} 条" for category, count in compiled.items()]
    md += ["", "## 闸门结果", ""] + [f"- `{key}`：`{value}`" for key, value in sorted(severity_counts.items())]
    if findings: md += ["", "### Findings", ""] + [f"- **{x['severity']}** `{x.get('reason', '')}`" + (f" — `{x.get('category')}`" if x.get('category') else "") for x in findings[:100]]
    md += ["", "## 语义冗余", "", f"DOMAIN 父子覆盖：`{domain_audit['count']}`（排除裸 TLD）", f"CIDR 父网覆盖子网：`{cidr_audit['count']}`"]
    if domain_audit["samples"]: md += ["", "### DOMAIN 示例", ""] + [f"- `{x['covered']['rule']}` ← `{x['covering']['rule']}`" for x in domain_audit["samples"][:50]]
    if cidr_audit["samples"]: md += ["", "### CIDR 示例", ""] + [f"- `{x['rule']}` ← `{x['covered_by']['category']}/{x['covered_by']['item']}`" for x in cidr_audit["samples"][:50]]
    if conflicts: md += ["", "## 跨分类冲突（最多 100 条）", ""] + [f"- `{rule}` → 胜出 `{winners[rule]}`；涉及 {', '.join(cats)}" for rule, cats in list(sorted(conflicts.items()))[:100]]
    md += ["", "## 编译输出校验", "", f"- 状态：**{'PASS' if output_audit['valid'] else 'FAIL'}**", f"- 问题数：`{output_audit['problem_count']}`"]
    (REPORTS / "latest.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps({"ok": not blocked, "gate": "BLOCKED" if blocked else "PASS", "severity": dict(severity_counts), "conflicts": len(conflicts), "domain_redundancy": domain_audit["count"], "cidr_redundancy": cidr_audit["count"], "compiled": compiled}, ensure_ascii=False))
    return 1 if blocked else 0


if __name__ == "__main__":
    sys.exit(main())
