#!/usr/bin/env python3
"""Monitor configured upstream rule sources and request a rebuild after stable changes."""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
CFG = ROOT / "config" / "sources.json"
REPORT = ROOT / "reports" / "latest.json"
TIMEOUT = 30
MAX_BYTES = 10 * 1024 * 1024
WORKERS = 12
CONFIRM_SECONDS = 600


def load_sources() -> list[str]:
    data = json.loads(CFG.read_text(encoding="utf-8"))
    urls: list[str] = []
    for category in data.get("sources", {}).values():
        for entries in category.values():
            for item in entries:
                url = item.get("url")
                if url and url not in urls:
                    urls.append(url)
    return urls


def load_previous() -> dict[str, str]:
    if not REPORT.exists():
        return {}
    try:
        data = json.loads(REPORT.read_text(encoding="utf-8"))
    except Exception:
        return {}

    result: dict[str, str] = {}
    for section in data.get("status", {}).values():
        for source in section.get("sources", []):
            url = source.get("url")
            sha256 = source.get("sha256")
            if url and sha256:
                result[url] = sha256
    return result


def fetch_hash(url: str) -> tuple[str, str | None, str | None]:
    request = Request(
        url,
        headers={
            "User-Agent": "Group-Rule-Upstream-Monitor/1.0",
            "Accept-Encoding": "identity",
        },
    )
    try:
        with urlopen(request, timeout=TIMEOUT) as response:
            digest = hashlib.sha256()
            total = 0
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                total += len(chunk)
                if total > MAX_BYTES:
                    return url, None, f"response exceeds {MAX_BYTES} bytes"
                digest.update(chunk)
            return url, digest.hexdigest(), None
    except HTTPError as exc:
        return url, None, f"HTTP {exc.code}"
    except (URLError, TimeoutError, OSError) as exc:
        return url, None, str(exc)


def fetch_all(urls: list[str]) -> tuple[dict[str, str], dict[str, str]]:
    hashes: dict[str, str] = {}
    errors: dict[str, str] = {}
    with ThreadPoolExecutor(max_workers=WORKERS) as pool:
        futures = [pool.submit(fetch_hash, url) for url in urls]
        for future in as_completed(futures):
            url, digest, error = future.result()
            if digest:
                hashes[url] = digest
            elif error:
                errors[url] = error
    return hashes, errors


def main() -> int:
    urls = load_sources()
    previous = load_previous()

    if not urls:
        print("No upstream sources configured.")
        return 0

    if not previous:
        print("No previous source hashes found; requesting a full rebuild.")
        return 2

    current, errors = fetch_all(urls)
    changed = [url for url in urls if url not in previous or current.get(url) != previous.get(url)]

    print(f"Checked {len(urls)} sources; successful={len(current)}, errors={len(errors)}")
    if errors:
        for url, error in sorted(errors.items()):
            print(f"WARN {url}: {error}")

    if not changed:
        print("No upstream content changes detected.")
        return 0

    print(f"Detected {len(changed)} changed source(s). Waiting {CONFIRM_SECONDS}s for stability...")
    first = {url: current.get(url) for url in changed}
    time.sleep(CONFIRM_SECONDS)
    second, second_errors = fetch_all(changed)

    unstable = [url for url in changed if second.get(url) != first.get(url)]
    if unstable:
        print("Upstream is still changing; defer rebuild to the next monitor cycle:")
        for url in unstable:
            print(f"  - {url}")
        return 0

    if any(url not in second for url in changed):
        print("A changed source could not be revalidated; defer rebuild.")
        for url, error in sorted(second_errors.items()):
            print(f"WARN {url}: {error}")
        return 0

    print("All changed sources are stable. Triggering rule rebuild.")
    return 2


if __name__ == "__main__":
    sys.exit(main())
