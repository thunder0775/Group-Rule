#!/usr/bin/env python3
"""Proxy-category policy consistency helpers for Group-Rule.

No domain allowlists. Uses semantic parent/child DOMAIN-SUFFIX coverage to:
1) strip reject rules covered by proxy categories
2) audit children that land in a different proxy category than their parent
3) optionally collapse children into the parent category
"""
from __future__ import annotations

from collections import defaultdict

PROXY_CATEGORIES = ("ai", "streaming", "social", "developer", "service", "global")
DOMAIN_TYPES = {"DOMAIN", "DOMAIN-SUFFIX"}
ROOT_TLDS = {
    "com", "net", "org", "cn", "uk", "de", "fr", "jp", "kr", "us", "io", "ai",
    "app", "dev", "me", "tv", "co", "xyz", "info", "biz", "site", "online", "tech", "top", "pro",
}


def domain_norm(value: str) -> str:
    return value.strip().lower().rstrip(".")


def parent_suffixes(domain: str, kind: str) -> list[str]:
    domain = domain_norm(domain)
    labels = domain.split(".")
    parents = [".".join(labels[i:]) for i in range(1, len(labels))]
    if kind == "DOMAIN":
        parents = [domain] + parents
    return parents


def build_proxy_domain_index(categories):
    exact, suffixes, owners = set(), set(), {}
    for category in PROXY_CATEGORIES:
        for name, rules in categories.get(category, {}).items():
            for rule in rules:
                kind, value = rule.split(",", 1)
                if kind not in DOMAIN_TYPES:
                    continue
                value = domain_norm(value)
                if kind == "DOMAIN":
                    exact.add(value)
                    owners.setdefault(("DOMAIN", value), []).append((category, name, rule))
                else:
                    suffixes.add(value)
                    owners.setdefault(("DOMAIN-SUFFIX", value), []).append((category, name, rule))
    return exact, suffixes, owners


def covered_by_proxy(kind: str, value: str, exact: set, suffixes: set):
    value = domain_norm(value)
    if kind == "DOMAIN" and value in exact:
        return True, value
    labels = value.split(".")
    for i in range(len(labels)):
        parent = ".".join(labels[i:])
        if parent in suffixes:
            return True, parent
    return False, None


def sanitize_reject_against_proxy(categories, exact, suffixes, limit, write_list, atomic_path):
    removed_total = 0
    samples = []
    per_item = {}
    reject_items = categories.get("reject", {})
    for name, rules in list(reject_items.items()):
        kept = []
        removed_here = []
        for rule in rules:
            kind, value = rule.split(",", 1)
            if kind not in DOMAIN_TYPES:
                kept.append(rule)
                continue
            hit, covering = covered_by_proxy(kind, value, exact, suffixes)
            if hit:
                removed_here.append({"rule": rule, "covered_by_suffix": covering})
            else:
                kept.append(rule)
        if removed_here:
            removed_total += len(removed_here)
            reject_items[name] = kept
            write_list(atomic_path("reject", name), kept, f"atomic:reject/{name}:proxy-overlap-sanitized")
            for item in removed_here[: max(0, limit - len(samples))]:
                samples.append({"item": name, **item})
        per_item[name] = {"before": len(rules), "after": len(kept), "removed": len(removed_here)}
    return {"removed_count": removed_total, "per_item": per_item, "samples": samples[:limit]}


def find_covering_parent_suffix(domain: str, kind: str, suffix_owners: dict):
    for parent in parent_suffixes(domain, kind):
        if "." not in parent or parent in ROOT_TLDS:
            continue
        if parent in suffix_owners:
            return parent, suffix_owners[parent]
    return None, []


def audit_child_policy_split(categories, limit):
    suffix_owners = defaultdict(list)
    for category in PROXY_CATEGORIES:
        for name, rules in categories.get(category, {}).items():
            for rule in rules:
                kind, value = rule.split(",", 1)
                if kind != "DOMAIN-SUFFIX":
                    continue
                value = domain_norm(value)
                if "." not in value or value in ROOT_TLDS:
                    continue
                suffix_owners[value].append((category, name, rule))

    findings = []
    seen = set()
    for category in PROXY_CATEGORIES:
        for name, rules in categories.get(category, {}).items():
            for rule in rules:
                kind, value = rule.split(",", 1)
                if kind not in DOMAIN_TYPES:
                    continue
                domain = domain_norm(value)
                parent, owners = find_covering_parent_suffix(domain, kind, suffix_owners)
                if not parent:
                    continue
                parent_categories = sorted({c for c, _, _ in owners})
                if category in parent_categories and len(parent_categories) == 1:
                    continue
                foreign_parents = [(c, n, r) for c, n, r in owners if c != category]
                if not foreign_parents:
                    continue
                key = (rule, parent, category, tuple(parent_categories))
                if key in seen:
                    continue
                seen.add(key)
                pcat, pname, prule = foreign_parents[0]
                findings.append({
                    "type": "child_policy_split",
                    "child": {"category": category, "item": name, "rule": rule},
                    "parent": {"category": pcat, "item": pname, "rule": prule},
                    "parent_categories": parent_categories,
                })
    findings.sort(key=lambda x: (x["child"]["rule"], x["parent"]["rule"]))
    return {"count": len(findings), "samples": findings[:limit]}


def collapse_children_to_parent_category(categories, limit, write_list, atomic_path):
    suffix_owners = defaultdict(list)
    for category in PROXY_CATEGORIES:
        for name, rules in categories.get(category, {}).items():
            for rule in rules:
                kind, value = rule.split(",", 1)
                if kind != "DOMAIN-SUFFIX":
                    continue
                value = domain_norm(value)
                if "." not in value or value in ROOT_TLDS:
                    continue
                suffix_owners[value].append((category, name, rule))

    moved = []
    to_remove = defaultdict(list)
    to_add = defaultdict(list)

    for category in PROXY_CATEGORIES:
        for name, rules in categories.get(category, {}).items():
            for rule in rules:
                kind, value = rule.split(",", 1)
                if kind not in DOMAIN_TYPES:
                    continue
                domain = domain_norm(value)
                parent, owners = find_covering_parent_suffix(domain, kind, suffix_owners)
                if not parent or not owners:
                    continue
                pcat, pname, prule = sorted(owners, key=lambda x: (x[0], x[1], x[2]))[0]
                if pcat == category:
                    continue
                to_remove[(category, name)].append(rule)
                to_add[(pcat, pname)].append(rule)
                moved.append({
                    "rule": rule,
                    "from": {"category": category, "item": name},
                    "to": {"category": pcat, "item": pname},
                    "parent_rule": prule,
                })

    for (cat, name), rules in to_remove.items():
        current = categories[cat][name]
        drop = set(rules)
        categories[cat][name] = [r for r in current if r not in drop]
        write_list(atomic_path(cat, name), categories[cat][name], f"atomic:{cat}/{name}:child-collapsed")

    for (cat, name), rules in to_add.items():
        categories[cat][name] = list(dict.fromkeys(categories[cat].get(name, []) + rules))
        write_list(atomic_path(cat, name), categories[cat][name], f"atomic:{cat}/{name}:child-collapsed")

    return {"moved_count": len(moved), "samples": moved[:limit]}


def apply_policy_consistency(categories, scfg, limit, write_list, atomic_path, validate_rule_set, statuses, quality):
    """Run sanitize / optional collapse / split audit. Mutates categories in place."""
    policy = scfg.get("policy", {})
    reject_sanitize = bool(policy.get("reject_proxy_overlap_sanitize", True))
    collapse_children = bool(policy.get("collapse_child_to_parent_category", False))
    split_severity = str(policy.get("child_policy_split_severity", "WARNING")).upper()
    if split_severity not in {"INFO", "WARNING", "BLOCK"}:
        split_severity = "WARNING"

    exact, suffixes, _owners = build_proxy_domain_index(categories)
    reject_sanitize_stats = {"removed_count": 0, "per_item": {}, "samples": []}
    if reject_sanitize and "reject" in categories:
        reject_sanitize_stats = sanitize_reject_against_proxy(
            categories, exact, suffixes, limit, write_list, atomic_path
        )
        for name, rules in categories.get("reject", {}).items():
            key = f"reject/{name}"
            if key in statuses:
                statuses[key]["rule_count"] = len(rules)
                statuses[key]["reject_proxy_overlap_removed"] = reject_sanitize_stats["per_item"].get(name, {}).get("removed", 0)
            quality[key] = validate_rule_set(rules)

    collapse_stats = {"moved_count": 0, "samples": []}
    if collapse_children:
        collapse_stats = collapse_children_to_parent_category(
            categories, limit, write_list, atomic_path
        )
        for category in PROXY_CATEGORIES:
            for name, rules in categories.get(category, {}).items():
                key = f"{category}/{name}"
                if key in statuses:
                    statuses[key]["rule_count"] = len(rules)
                quality[key] = validate_rule_set(rules)

    split_audit = audit_child_policy_split(categories, limit)
    return {
        "reject_sanitize_stats": reject_sanitize_stats,
        "collapse_stats": collapse_stats,
        "split_audit": split_audit,
        "split_severity": split_severity,
        "reject_sanitize": reject_sanitize,
        "collapse_children": collapse_children,
        "proxy_categories": list(PROXY_CATEGORIES),
    }
