#!/usr/bin/env python3
"""Shadowrocket rule engine entrypoint.

Keeps scripts/ lean: materializes the full engine body from a known-good
historical commit (gzip+base64 payload parts) into a local cache file, then
executes it. policy_consistency.py stays as a normal source module.
"""
from __future__ import annotations

import base64
import gzip
import runpy
import sys
import urllib.request
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_BODY = _HERE / "_rule_engine_impl.py"
# Last commit that still contained complete part0+part1+part2 payloads.
_COMMIT = "4b789c3e14c896dcd17027e48e87735e63551dfb"
_BASE = f"https://raw.githubusercontent.com/thunder0775/Group-Rule/{_COMMIT}/scripts"


def _materialize() -> Path:
    if _BODY.exists() and _BODY.stat().st_size > 1000:
        return _BODY
    parts: list[str] = []
    for i in range(3):
        url = f"{_BASE}/rule_engine.payload.part{i}"
        with urllib.request.urlopen(url, timeout=30) as resp:
            parts.append(resp.read().decode("ascii").strip())
    data = gzip.decompress(base64.b64decode("".join(parts)))
    _BODY.write_bytes(data)
    return _BODY


if __name__ == "__main__":
    body = _materialize()
    sys.argv[0] = str(body)
    runpy.run_path(str(body), run_name="__main__")
