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
# Categories that map to proxy policies in typical Shadowrocket confs.
# Used for reject pollution cleanup and parent/child policy-split audit — no domain allowlists.
PROXY_CATEGORIES = ("ai", "streaming", "social", "developer", "service", "global")
