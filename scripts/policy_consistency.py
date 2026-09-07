#!/usr/bin/env python3
"""Proxy-category policy consistency helpers for Group-Rule.

No domain allowlists. Uses semantic parent/child DOMAIN-SUFFIX coverage to:
1) strip reject rules covered by proxy categories
2) dedupe the same rule across proxy categories (priority winner keeps it)
3) optionally collapse children into a higher-priority parent category (never demote)
4) audit remaining demotions / multi-parent inconsistencies
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

PROXY_CATEGORIES = ("ai", "streaming", "social", "developer", "service", "global")
DOMAIN_TYPES = {"DOMAIN", "DOMAIN-SUFFIX"}
ROOT_TLDS = {
    "com", "net", "org", "cn", "uk", "de", "fr", "jp", "kr", "us", "io", "ai",
    "app", "dev", "me", "tv", "co", "xyz", "info", "biz", "site", "online", "tech", "top", "pro",
}

# Default matches config/priority.json category_order (proxy subset, higher priority first).
DEFAULT_PROXY_ORDER = list(PROXY_CATEGORIES)


def domain_norm(value: str) -> str:
    return value.strip().lower().rstrip(".")


def parent_suffixes(domain: str, kind: str) -> list[str]:
    domain = domain_norm(domain)
    labels = domain.split(".")
    parents = [".".join(labels[i:]) for i in range(1, len(labels))]
    if kind == "DOMAIN":
        parents = [domain] + parents
    return parents


def load_proxy_priority_order(scfg: dict | None = None) -> list[str]:
    """Resolve proxy category order: sources.policy override → priority.json → default."""
    policy = (scfg or {}).get("policy") or {}
    override = policy.get("proxy_category_order")
    if isinstance(override, list) and override:
        ordered = [c for c in override if c in PROXY_CATEGORIES]
        for c in PROXY_CATEGORIES:
            if c not in ordered:
                ordered.append(c)
        return ordered

    path = Path(__file__).resolve().parents[1] / "config" / "priority.json"
    if path.exists():
        try:
            pcfg = json.loads(path.read_text(encoding="utf-8"))
            order = pcfg.get("category_order") or []
            ordered = [c for c in order if c in PROXY_CATEGORIES]
            for c in PROXY_CATEGORIES:
                if c not in ordered:
                    ordered.append(c)
            if ordered:
                return ordered
        except Exception:
            pass
    return list(DEFAULT_PROXY_ORDER)


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
        removed = []
        for rule in rules:
            kind, value = rule.split(",", 1)
            if kind not in DOMAIN_TYPES:
                kept.append(rule)
                continue
            hit, _ = covered_by_proxy(kind, value, exact, suffixes)
            if hit:
                removed.append(rule)
            else:
                kept.append(rule)
        if removed:
            categories["reject"][name] = kept
            write_list(atomic_path("reject", name), kept, f"atomic:reject/{name}:reject-proxy-overlap")
            removed_total += len(removed)
            if len(samples) < limit:
                samples.extend(
                    {"item": name, "rule": r, "reason": "covered_by_proxy"} for r in removed[: max(0, limit - len(samples))]
                )
        per_item[name] = {"before": len(rules), "after": len(kept), "removed": len(removed)}
    return {"removed_count": removed_total, "per_item": per_item, "samples": samples}


def find_covering_parent_suffix(domain: str, kind: str, suffix_owners: dict):
    for parent in parent_suffixes(domain, kind):
        if "." not in parent or parent in ROOT_TLDS:
            continue
        if parent in suffix_owners:
            return parent, suffix_owners[parent]
    return None, []


def _rank_map(order: list[str]) -> dict[str, int]:
    return {c: i for i, c in enumerate(order)}


def dedupe_proxy_cross_category(categories, order, limit, write_list, atomic_path):
    """Same rule in multiple proxy categories → keep only the highest-priority category.

    Aligns atomic lists with compiled conflict resolution (priority.json).
    """
    rank = _rank_map(order)
    locations = defaultdict(list)
    for category in PROXY_CATEGORIES:
        for name, rules in categories.get(category, {}).items():
            for rule in rules:
                locations[rule].append((category, name))

    to_remove = defaultdict(set)
    removed = []
    for rule, locs in locations.items():
        cats = {c for c, _ in locs}
        if len(cats) <= 1:
            continue
        winner = min(cats, key=lambda c: rank.get(c, 10**9))
        for cat, name in locs:
            if cat == winner:
                continue
            to_remove[(cat, name)].add(rule)
            removed.append({"rule": rule, "from": {"category": cat, "item": name}, "winner": winner})

    for (cat, name), rules in to_remove.items():
        current = categories[cat][name]
        drop = set(rules)
        categories[cat][name] = [r for r in current if r not in drop]
        write_list(atomic_path(cat, name), categories[cat][name], f"atomic:{cat}/{name}:proxy-dedupe")

    return {"removed_count": len(removed), "samples": removed[:limit]}


def collapse_children_to_parent_category(categories, order, limit, write_list, atomic_path):
    """Move child domain rules into the parent DOMAIN-SUFFIX's winning category."""
    rank = _rank_map(order)
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
                # Prefer highest-priority parent owner (matches priority.json).
                pcat, pname, prule = min(
                    owners, key=lambda x: (rank.get(x[0], 10**9), x[0], x[1], x[2])
                )
                if pcat == category:
                    continue
                # Never demote: do not move a higher-priority category (e.g. ai)
                # into a lower-priority parent (e.g. service/global).
                if rank.get(pcat, 10**9) > rank.get(category, 10**9):
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


def audit_child_policy_split(categories, order, limit):
    rank = _rank_map(order)
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
                winner = min(parent_categories, key=lambda c: rank.get(c, 10**9))
                parent_best = min(rank.get(c, 10**9) for c in parent_categories)
                # Child in a higher-priority category than any covering parent is intentional
                # (e.g. DOMAIN in ai under DOMAIN-SUFFIX,google.com in service).
                if rank.get(category, 10**9) < parent_best:
                    continue
                # OK when child already sits in the winning parent category and
                # parent is not multi-owned (dedupe should have fixed multi-own).
                if category == winner and len(parent_categories) == 1:
                    continue
                if category == winner and len(parent_categories) > 1:
                    # Parent still multi-owned; report so dedupe can be tightened.
                    pass
                foreign_parents = [(c, n, r) for c, n, r in owners if c != category]
                if not foreign_parents and category == winner:
                    continue
                if not foreign_parents:
                    continue
                key = (rule, parent, category, tuple(parent_categories))
                if key in seen:
                    continue
                seen.add(key)
                # Prefer reporting the priority-winning parent.
                pcat, pname, prule = min(
                    foreign_parents, key=lambda x: (rank.get(x[0], 10**9), x[0], x[1], x[2])
                )
                findings.append({
                    "type": "child_policy_split",
                    "child": {"category": category, "item": name, "rule": rule},
                    "parent": {"category": pcat, "item": pname, "rule": prule},
                    "parent_categories": parent_categories,
                    "winner_category": winner,
                })
    findings.sort(key=lambda x: (x["child"]["rule"], x["parent"]["rule"]))
    return {"count": len(findings), "samples": findings[:limit]}


def apply_policy_consistency(categories, scfg, limit, write_list, atomic_path, validate_rule_set, statuses, quality):
    """Run sanitize / dedupe / optional collapse / split audit. Mutates categories in place."""
    policy = scfg.get("policy", {})
    reject_sanitize = bool(policy.get("reject_proxy_overlap_sanitize", True))
    dedupe_proxy = bool(policy.get("dedupe_proxy_cross_category", True))
    collapse_children = bool(policy.get("collapse_child_to_parent_category", False))
    split_severity = str(policy.get("child_policy_split_severity", "WARNING")).upper()
    if split_severity not in {"INFO", "WARNING", "BLOCK"}:
        split_severity = "WARNING"

    order = load_proxy_priority_order(scfg)

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

    dedupe_stats = {"removed_count": 0, "samples": []}
    if dedupe_proxy:
        dedupe_stats = dedupe_proxy_cross_category(
            categories, order, limit, write_list, atomic_path
        )
        for category in PROXY_CATEGORIES:
            for name, rules in categories.get(category, {}).items():
                key = f"{category}/{name}"
                if key in statuses:
                    statuses[key]["rule_count"] = len(rules)
                quality[key] = validate_rule_set(rules)

    collapse_stats = {"moved_count": 0, "samples": []}
    if collapse_children:
        # Two passes: collapse → dedupe residual multi-own → collapse again.
        first = collapse_children_to_parent_category(
            categories, order, limit, write_list, atomic_path
        )
        if dedupe_proxy:
            extra = dedupe_proxy_cross_category(
                categories, order, limit, write_list, atomic_path
            )
            dedupe_stats["removed_count"] += extra["removed_count"]
            room = max(0, limit - len(dedupe_stats["samples"]))
            dedupe_stats["samples"].extend(extra["samples"][:room])
        second = collapse_children_to_parent_category(
            categories, order, limit, write_list, atomic_path
        )
        collapse_stats = {
            "moved_count": first["moved_count"] + second["moved_count"],
            "samples": (first["samples"] + second["samples"])[:limit],
            "passes": 2,
        }
        for category in PROXY_CATEGORIES:
            for name, rules in categories.get(category, {}).items():
                key = f"{category}/{name}"
                if key in statuses:
                    statuses[key]["rule_count"] = len(rules)
                quality[key] = validate_rule_set(rules)

    split_audit = audit_child_policy_split(categories, order, limit)
    return {
        "reject_sanitize_stats": reject_sanitize_stats,
        "dedupe_stats": dedupe_stats,
        "collapse_stats": collapse_stats,
        "split_audit": split_audit,
        "split_severity": split_severity,
        "reject_sanitize": reject_sanitize,
        "dedupe_proxy": dedupe_proxy,
        "collapse_children": collapse_children,
        "proxy_categories": list(PROXY_CATEGORIES),
        "proxy_category_order": order,
    }
