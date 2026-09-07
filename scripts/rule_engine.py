#!/usr/bin/env python3
"""Shadowrocket rule engine entrypoint.

Loads the full engine body from rule_engine.payload.b64 (gzip+base64) on first
import path resolution, then executes it. Keeps the logical engine in one place
while allowing the source blob to be transported as a compact payload file.
"""
from __future__ import annotations

import base64
import gzip
import runpy
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_BODY = _HERE / "_rule_engine_impl.py"
_PAYLOAD = _HERE / "rule_engine.payload.b64"


def _materialize() -> Path:
    if _BODY.exists() and _BODY.stat().st_size > 1000:
        return _BODY
    if not _PAYLOAD.exists():
        raise SystemExit(f"missing engine payload: {_PAYLOAD}")
    data = gzip.decompress(base64.b64decode(_PAYLOAD.read_text(encoding="ascii")))
    _BODY.write_bytes(data)
    return _BODY


if __name__ == "__main__":
    body = _materialize()
    sys.argv[0] = str(body)
    runpy.run_path(str(body), run_name="__main__")
