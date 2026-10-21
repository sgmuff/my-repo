"""Company profile fields that set a record's scope. A fresh clone ships them as TODO; drafting can go ahead, but a record
can't be approved against an unfilled footprint."""
from __future__ import annotations

from pathlib import Path

from gov.paths import MARKER

# Line prefixes in company-profile.md whose value decides which regimes and authorities apply.
SCOPE_FIELDS = (
    "Legal entity name",
    "Sector",
    "EU establishment",
    "Lead supervisory authority",
    "US comprehensive state privacy laws",
)


def scope_todos(root: Path) -> list:
    path = root / MARKER
    if not path.is_file():
        return list(SCOPE_FIELDS)
    todo = []
    for line in path.read_text(encoding="utf-8").splitlines():
        text = line.strip().lstrip("-").strip()
        for field in SCOPE_FIELDS:
            if text.startswith(field) and text.rstrip(".").endswith("TODO"):
                todo.append(field)
    return todo
