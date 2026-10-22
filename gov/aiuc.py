"""AIUC-1 requirements from skills/_shared/references/aiuc-1.md: ID, title, Mandatory or Optional, and capability tags."""
from __future__ import annotations

import re
from pathlib import Path

REFERENCE = Path("skills/_shared/references/aiuc-1.md")
THIRD_PARTY_TESTING = ("A009", "B001", "C010", "D004", "E018")


def requirements(root) -> dict:
    """{id: {"title", "status", "tags"}} from the requirement tables in section 4; {} if the file isn't there."""
    path = Path(root) / REFERENCE if root else None
    if not path or not path.is_file():
        return {}
    text = path.read_text(encoding="utf-8")
    start = text.find("## 4. Requirements by domain")
    end = text.find("\n## 5.", start)
    out = {}
    for m in re.finditer(r"^\| ([A-F]\d{3}) \| ([^|]+?) \| (Mandatory|Optional) \| ([^|]+?) \|", text[start:end], re.M):
        out[m.group(1)] = {"title": m.group(2).strip(), "status": m.group(3), "tags": [t.strip() for t in m.group(4).split(",")]}
    return out


def triggered(reqs: dict, capabilities: list) -> list:
    """Mandatory requirement IDs that apply: Universal ones, and those tagged with one of the agent's capabilities."""
    caps = set(capabilities) | {"Universal"}
    return sorted(i for i, r in reqs.items() if r["status"] == "Mandatory" and caps & set(r["tags"]))
