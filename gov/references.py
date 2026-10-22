"""Reference files a record cites, checked against the index's review dates. gov never reads the clock: a reference is
overdue when its review-by date is before the record's own date (last_reviewed, else date_prepared) or a given as-of.
The check fails closed: an index that can't be read, or a shared file missing from it, is an error, not silence."""
from __future__ import annotations

import re
from pathlib import Path

FOLDER = Path("skills/_shared/references")
INDEX = FOLDER / "README.md"
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")


def index(root: Path) -> dict:
    """{file: {"verified", "review_by", "secondary", "unreviewed"}} from the index table; dates are ISO strings.
    secondary: verified against secondary sources only. unreviewed: the row says it needs counsel review."""
    path = root / INDEX
    if not path.is_file():
        return {}
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 6 or not re.fullmatch(r"`[a-z0-9-]+\.md`", cells[0]):
            continue
        verified, review_by = DATE.search(cells[3]), DATE.search(cells[4])
        row = " ".join(cells).lower()
        out[cells[0].strip("`")] = {"verified": verified.group() if verified else None,
                                    "review_by": review_by.group() if review_by else None,
                                    "secondary": "secondary source" in row,
                                    "unreviewed": "needs counsel review" in row}
    return out


def index_problems(root: Path) -> list:
    """Messages for a shared references folder whose index doesn't account for every file, with both dates."""
    folder = root / FOLDER
    if not folder.is_dir():
        return []
    files = {p.name for p in folder.glob("*.md") if p.name != "README.md"}
    known = index(root)
    problems = [f"{name} isn't in the reference index ({INDEX}), so its review dates can't be checked" for name in sorted(files - set(known))]
    problems += [f"{name}: the index row has no {field.replace('_', ' ')} date" for name, row in sorted(known.items())
                 for field in ("verified", "review_by") if not row[field]]
    return problems


def record_date(data: dict) -> str:
    return str(data.get("last_reviewed") or data.get("date_prepared"))


def findings(root: Path, data: dict, as_of: str | None = None) -> list:
    """(pointer, message) for each cited shared reference that is overdue, updated since the record cited it, or not
    yet reviewed by counsel."""
    known, when, out = index(root), as_of or record_date(data), []
    for ref in data.get("references", []):
        name, entry = ref["file"], known.get(ref["file"])
        if entry is None:
            continue  # a skill's own reference file, or one index_problems already reports
        if entry["review_by"] and entry["review_by"] < when:
            out.append((f"references/{name}", f"{name} was due for review by {entry['review_by']}, before {when}; re-verify it and the conclusions that rely on it, or record why they still hold"))
        elif entry["verified"] and str(ref["verified"]) < entry["verified"]:
            out.append((f"references/{name}", f"{name} has been re-verified since this record cited it ({ref['verified']}, now {entry['verified']}); check the conclusions that rely on it"))
        if entry["unreviewed"]:
            out.append((f"references/{name}/review", f"{name} hasn't been reviewed by counsel; have counsel confirm the conclusions that rely on it before approval"))
    return out


def notes(root: Path | None, data: dict) -> dict:
    """{file: caveat} for the rendered reference list, so a reader sees how settled each source is."""
    if root is None:
        return {}
    known, out = index(root), {}
    for ref in data.get("references", []):
        entry = known.get(ref["file"])
        if not entry:
            continue
        caveats = []
        if entry["secondary"]:
            caveats.append("checked against secondary sources only")
        if entry["unreviewed"]:
            caveats.append("not yet reviewed by counsel")
        if caveats:
            out[ref["file"]] = "; ".join(caveats)
    return out
