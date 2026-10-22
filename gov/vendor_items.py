"""The dpa-checklist.md items each vendor review depth must cover, and their requirement text for rendering."""
import re
from pathlib import Path

CHECKLIST = Path("skills/_shared/references/dpa-checklist.md")
SECTIONS = {
    "1": ["1.1", "1.2", "1.3", "1.4"],
    "2": [f"2.{i}" for i in range(1, 12)],
    "3": [f"3.{i}" for i in range(1, 8)],
    "4": [f"4.{i}" for i in range(1, 5)],
    "5": [f"5.{i}" for i in range(1, 6)],
    "6": ["6.1", "6.2", "6.3", "6.3a"] + [f"6.{i}" for i in range(4, 13)],
    "7": [f"7.{i}" for i in range(1, 7)],
}
DEPTH = {"light": SECTIONS["1"] + SECTIONS["2"] + ["7.1"],
         "standard": SECTIONS["1"] + SECTIONS["2"] + SECTIONS["3"] + SECTIONS["4"] + SECTIONS["7"]}
DEPTH["deep"] = DEPTH["standard"]


def required_clauses(data: dict) -> list:
    wanted = list(DEPTH[data["depth"]["value"]])
    if "school-data" in data.get("context", []) or "children" in data.get("context", []):
        wanted += SECTIONS["5"]
    return wanted


def item_text(root) -> dict:
    """{item: the requirement's first sentence, trimmed} from the checklist tables; {} if the file isn't there."""
    path = Path(root) / CHECKLIST if root else None
    if not path or not path.is_file():
        return {}
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\| (\d\.\d+a?) \| (.+?) \|", line)
        if m:
            text = re.sub(r"\*\*|`", "", m.group(2))
            first = re.split(r"(?<=[.:;])\s", text, maxsplit=1)[0].rstrip(".:;")
            words = first.split()
            out[m.group(1)] = " ".join(words[:14]) + ("…" if len(words) > 14 else "")
    return out
