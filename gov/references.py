"""Reference files and their front matter. Each shared reference file opens with YAML front matter giving its dates,
source quality, and counsel review; gov reads that, checks it, and writes the index table in the folder's README.
gov never reads the clock: a reference is overdue when its review-by date is before the record's own date
(last_reviewed, else date_prepared) or a given as-of. The checks fail closed: a file whose front matter is missing or
incomplete is an error, not silence."""
from __future__ import annotations

import re
from pathlib import Path

from gov import yamlio

FOLDER = Path("skills/_shared/references")
INDEX = FOLDER / "README.md"
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
QUALITY = {"primary", "secondary", "mixed", "internal"}
COUNSEL = {"approved", "partial", "pending", "not-recorded"}
REQUIRED = ("title", "summary", "version_summary", "last_verified", "review_by", "index_interval", "source_quality", "counsel_review")
START, END = "<!-- gov:reference-index:start -->", "<!-- gov:reference-index:end -->"


def front_matter(path: Path):
    """The file's front matter as a mapping, or None if it has none."""
    m = re.match(r"---\n(.*?)\n---\n", path.read_text(encoding="utf-8"), re.S)
    if not m:
        return None
    data = yamlio.loads(m.group(1))
    return data if isinstance(data, dict) else None


def _files(root: Path) -> list:
    folder = root / FOLDER
    return sorted(p for p in folder.glob("*.md") if p.name != "README.md") if folder.is_dir() else []


def _problems_in(name: str, fm) -> list:
    if fm is None:
        return [f"{name}: no front matter, so its review dates can't be checked"]
    out = [f"{name}: front matter has no {key}" for key in REQUIRED if key not in fm]
    for key in ("last_verified", "review_by"):
        if key in fm and not DATE.match(str(fm[key])):
            out.append(f"{name}: {key} must be YYYY-MM-DD")
    if "source_quality" in fm and fm["source_quality"] not in QUALITY:
        out.append(f"{name}: source_quality must be one of {', '.join(sorted(QUALITY))}")
    counsel = fm.get("counsel_review")
    if "counsel_review" in fm and (not isinstance(counsel, dict) or counsel.get("status") not in COUNSEL):
        out.append(f"{name}: counsel_review.status must be one of {', '.join(sorted(COUNSEL))}")
    elif isinstance(counsel, dict) and counsel.get("status") in ("approved", "partial") and not counsel.get("date"):
        out.append(f"{name}: counsel_review needs the date of the review")
    return out


def index(root: Path) -> dict:
    """{file: {"verified", "review_by", "secondary", "unreviewed", "partial", "scope", "front"}} for each file with
    complete front matter. secondary: some sources are secondary. unreviewed: counsel review pending. partial: counsel
    reviewed part of the file, as scope says."""
    out = {}
    for path in _files(root):
        fm = front_matter(path)
        if _problems_in(path.name, fm):
            continue
        counsel = fm["counsel_review"]
        out[path.name] = {"verified": str(fm["last_verified"]), "review_by": str(fm["review_by"]),
                          "secondary": fm["source_quality"] in ("secondary", "mixed"),
                          "unreviewed": counsel["status"] == "pending",
                          "partial": counsel["status"] == "partial", "scope": counsel.get("scope", ""), "front": fm}
    return out


def index_problems(root: Path) -> list:
    """Messages for shared reference files whose front matter is missing or incomplete."""
    return [m for path in _files(root) for m in _problems_in(path.name, front_matter(path))]


def index_table(root: Path) -> str:
    """The README's index table, generated from the front matter."""
    rows = ["| File | Covers | Version covered | Last verified | Review by | Interval | Sources | Counsel review |",
            "|---|---|---|---|---|---|---|---|"]
    for name, entry in index(root).items():
        fm = entry["front"]
        counsel = fm["counsel_review"]
        review = {"approved": f"Approved {counsel.get('date')}", "partial": f"Partial, {counsel.get('date')}",
                  "pending": "Pending", "not-recorded": "Not recorded"}[counsel["status"]]
        rows.append(f"| `{name}` | {fm['summary']} | {fm['version_summary']} | {fm['last_verified']} | {fm['review_by']} | "
                    f"{fm['index_interval']} | {fm['source_quality'].capitalize()} | {review} |")
    return "\n".join(rows)


def readme(root: Path):
    """The README with its index table regenerated, or None if the README has no generated block."""
    path = root / INDEX
    if not path.is_file():
        return None
    text = path.read_text(encoding="utf-8")
    if START not in text or END not in text:
        return None
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    return f"{head}{START}\n{index_table(root)}\n{END}{tail}"


def record_date(data: dict) -> str:
    return str(data.get("last_reviewed") or data.get("date_prepared"))


def findings(root: Path, data: dict, as_of: str | None = None) -> list:
    """(pointer, message) for each cited shared reference that is overdue, updated since the record cited it, or not
    fully reviewed by counsel."""
    known, when, out = index(root), as_of or record_date(data), []
    for ref in data.get("references", []):
        name, entry = ref["file"], known.get(ref["file"])
        if entry is None:
            continue  # a skill's own reference file, or one index_problems already reports
        if entry["review_by"] < when:
            out.append((f"references/{name}", f"{name} was due for review by {entry['review_by']}, before {when}; re-verify it and the conclusions that rely on it, or record why they still hold"))
        elif str(ref["verified"]) < entry["verified"]:
            out.append((f"references/{name}", f"{name} has been re-verified since this record cited it ({ref['verified']}, now {entry['verified']}); check the conclusions that rely on it"))
        if entry["unreviewed"]:
            out.append((f"references/{name}/review", f"{name} hasn't been reviewed by counsel; have counsel confirm the conclusions that rely on it before approval"))
        elif entry["partial"]:
            out.append((f"references/{name}/review", f"counsel has reviewed only part of {name} ({entry['scope']}); confirm the conclusions that rely on the rest before approval"))
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
        if entry["front"]["source_quality"] == "secondary":
            caveats.append("checked against secondary sources only")
        elif entry["front"]["source_quality"] == "mixed":
            caveats.append("partly checked against secondary sources")
        if entry["unreviewed"]:
            caveats.append("not yet reviewed by counsel")
        elif entry["partial"]:
            caveats.append("partly reviewed by counsel")
        if caveats:
            out[ref["file"]] = "; ".join(caveats)
    return out
