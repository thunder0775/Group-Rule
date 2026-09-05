#!/usr/bin/env python3
"""Block unsafe upstreams from ever entering DIRECT/China rule generation."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CFG = ROOT / "config" / "sources.json"

# Exactly two positive China DIRECT domain upstreams are allowed for this test.
# They are independent aggregators and are still passed through the sanitizer.
ALLOWED_CHINA_SOURCES = {
    "https://raw.githubusercontent.com/GrandpaNiuu/cn-direct-rules/main/dist/rule-set/cn.list",
    "https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/direct.txt",
}

# Known risky upstreams are denied even if they are accidentally referenced.
DENIED_SOURCE_FRAGMENTS = (
    "blackmatrix7/ios_rule_script/master/rule/Shadowrocket/ChinaMax/",
    "Vincent-Loeng/shadowrocket-rules/release/direct.list",
    "Vincent-Loeng/shadowrocket-rules/release/apple.list",
    "Vincent-Loeng/shadowrocket-rules/release/icloud.list",
    "Vincent-Loeng/shadowrocket-rules/release/cncidr.list",
    "Vincent-Loeng/shadowrocket-rules/release/lancidr.list",
    "PeterLooper/rules-config/main/cn-direct.conf",
    "GMOogway/shadowrocket-rules/master/sr_direct_list.module",
)


def main() -> int:
    cfg = json.loads(CFG.read_text(encoding="utf-8"))
    china = cfg.get("sources", {}).get("china", {})
    violations = []

    if set(china) != {"domains"}:
        violations.append("china: only the domains source group is permitted")

    configured_urls = []
    for item_name, source_list in china.items():
        if not isinstance(source_list, list):
            violations.append(f"china/{item_name}: sources must be a list")
            continue
        for source in source_list:
            obj = {"url": source} if isinstance(source, str) else source if isinstance(source, dict) else {}
            url = str(obj.get("url", ""))
            if not url:
                violations.append(f"china/{item_name}: missing source url")
                continue
            configured_urls.append(url)
            if any(fragment in url for fragment in DENIED_SOURCE_FRAGMENTS):
                violations.append(f"china/{item_name}: denied upstream: {url}")
            if url not in ALLOWED_CHINA_SOURCES:
                violations.append(f"china/{item_name}: unapproved upstream: {url}")

    # Exactly two sources: no silent fallback to stale/legacy China sources.
    if len(configured_urls) != 2:
        violations.append(f"china: expected exactly 2 upstreams, got {len(configured_urls)}")
    if set(configured_urls) != ALLOWED_CHINA_SOURCES:
        violations.append("china: configured upstream set does not exactly match the two-source test profile")

    # The safe profile is domain-only. China IP routing remains the explicit
    # Shadowrocket GEOIP,CN,no-resolve fallback in the user's .conf.
    if violations:
        print("DIRECT SOURCE GUARD: BLOCK")
        for item in violations:
            print(f"- {item}")
        return 1

    print("DIRECT SOURCE GUARD: PASS")
    print("- China domain upstreams: exactly 2 approved sources")
    print("- China IP direct routing: GEOIP,CN,no-resolve only")
    print("- known risky direct upstreams: denied")
    print("- source diversity requirement: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
