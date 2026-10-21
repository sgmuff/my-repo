"""Reference files a record cites, checked against the index's review dates. gov never reads the clock: a reference is
overdue when its review-by date is before the record's own date (last_reviewed, else date_prepared) or a given as-of."""
from __future__ import annotations

import re
from pathlib import Path

INDEX = Path("skills/_shared/references/README.md")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def index(root: Path) -> dict:
    """{file: {"verified": date, "review_by": date}} from the index table; dates are ISO strings."""
    path = root / INDEX
    if not path.is_file():
        return {}
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6 or not re.fullmatch(r"`[a-z0-9-]+\.md`", cells[0]):
            continue
        verified, review_by = DATE.search(cells[3]), DATE.search(cells[4])
        out[cells[0].strip("`")] = {"verified": verified.group() if verified else None,
                                    "review_by": review_by.group() if review_by else None}
    return out


def record_date(data: dict) -> str:
    return str(data.get("last_reviewed") or data.get("date_prepared"))


def findings(root: Path, data: dict, as_of: str | None = None) -> list:
    """(pointer, message) for each cited reference that is overdue or has been updated since the record cited it."""
    known, when, out = index(root), as_of or record_date(data), []
    for ref in data.get("references", []):
        name, entry = ref["file"], known.get(ref["file"])
        if entry is None:
            continue  # a skill's own reference file; it isn't in the shared index
        if entry["review_by"] and entry["review_by"] < when:
            out.append((f"references/{name}", f"{name} was due for review by {entry['review_by']}, before {when}; re-verify it and the conclusions that rely on it, or record why they still hold"))
        elif entry["verified"] and str(ref["verified"]) < entry["verified"]:
            out.append((f"references/{name}", f"{name} has been re-verified since this record cited it ({ref['verified']}, now {entry['verified']}); check the conclusions that rely on it"))
    return out
