"""Common control objectives from skills/_shared/references/crosswalk.md, with each framework's mapped requirements."""
from __future__ import annotations

import re
from pathlib import Path

REFERENCE = Path("skills/_shared/references/crosswalk.md")
FRAMEWORKS = ("NIST PF", "AIUC-1", "NIST AI RMF", "ISO/IEC 42001", "GDPR", "EU AI Act", "US states", "FERPA")


def objectives(root) -> dict:
    """{CCO-nn: {"objective", "frameworks": {framework: text}}} from the objective tables; {} if the file isn't there."""
    path = Path(root) / REFERENCE if root else None
    if not path or not path.is_file():
        return {}
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\| (CCO-\d{2}) \| (.+) \|\s*$", line)
        if not m:
            continue
        cells = [c.strip() for c in m.group(2).split(" | ")]
        if len(cells) != 1 + len(FRAMEWORKS):
            continue
        out[m.group(1)] = {"objective": cells[0],
                           "frameworks": {f: c for f, c in zip(FRAMEWORKS, cells[1:]) if c not in ("—", "-", "")}}
    return out
