#!/usr/bin/env python3
"""Block unsafe upstreams from ever entering DIRECT/China rule generation."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CFG = ROOT / "config" / "sources.json"

# These upstreams are intentionally never accepted for China/DIRECT generation.
# They are broad, derived, or have documented false-positive/coverage risks.
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
            if any(fragment in url for fragment in DENIED_SOURCE_FRAGMENTS):
                violations.append(f"china/{item_name}: denied upstream: {url}")

    # Conservative policy: China/DIRECT sources are opt-in only through this guard.
    # An empty source set is the safe default; any future source must be audited and
    # explicitly added to this allow model before it can reach generated DIRECT rules.
    if any(isinstance(v, list) and v for v in china.values()):
        violations.append("china: non-empty upstream source set requires explicit security review")

    if violations:
        print("DIRECT SOURCE GUARD: BLOCK")
        for item in violations:
            print(f"- {item}")
        return 1

    print("DIRECT SOURCE GUARD: PASS")
    print("- china upstream sources: empty (conservative mode)")
    print("- known risky direct upstreams: denied")
    return 0


if __name__ == "__main__":
    sys.exit(main())
