#!/usr/bin/env python3
"""Regression checks for accidental foreign-domain inclusion in China DIRECT rules."""
from __future__ import annotations

import ipaddress
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULE_FILE = ROOT / "rules" / "compiled" / "china.list"

# Known foreign/global domains used as regression fixtures. These came from prior
# conflict samples or documented false-positive investigations.
FORBIDDEN_DOMAINS = {
    "nvidia.net",
    "developer.microsoft.com",
    "1e100.net",
    "google.com",
    "github.com",
    "openai.com",
    "microsoft.com",
    "steamcommunity.com",
    "np-edge.itunes.apple.com",
    "play-edge.itunes.apple.com",
}

BROAD_ROOTS = {
    "com", "net", "org", "edu", "gov", "mil",
}


def parse_rules() -> list[str]:
    if not RULE_FILE.exists():
        raise SystemExit(f"missing generated rule file: {RULE_FILE}")
    return [
        line.strip()
        for line in RULE_FILE.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def domain_matches(rule: str, domain: str) -> bool:
    try:
        kind, value = rule.split(",", 1)
    except ValueError:
        return False
    value = value.lower().rstrip(".")
    domain = domain.lower().rstrip(".")
    if kind == "DOMAIN":
        return value == domain
    if kind == "DOMAIN-SUFFIX":
        return domain == value or domain.endswith("." + value)
    return False


def main() -> int:
    rules = parse_rules()
    failures: list[str] = []

    for rule in rules:
        parts = rule.split(",", 1)
        if len(parts) != 2:
            continue
        kind, value = parts
        value = value.lower().rstrip(".")
        if kind == "DOMAIN-SUFFIX" and value in BROAD_ROOTS:
            failures.append(f"broad root domain rule: {rule}")

    for domain in sorted(FORBIDDEN_DOMAINS):
        matched = [rule for rule in rules if domain_matches(rule, domain)]
        if matched:
            failures.append(f"foreign regression domain matched: {domain} <- {matched[:5]}")

    if failures:
        print("DIRECT RULE REGRESSION: BLOCK")
        for item in failures:
            print(f"- {item}")
        return 1

    print("DIRECT RULE REGRESSION: PASS")
    print(f"- checked rules: {len(rules)}")
    print(f"- forbidden foreign fixtures: {len(FORBIDDEN_DOMAINS)}")
    print("- broad root DOMAIN-SUFFIX rules: none")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
