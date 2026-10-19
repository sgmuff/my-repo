"""Where the repository, records, and package data live."""
from __future__ import annotations

import os
from pathlib import Path

PACKAGE = Path(__file__).resolve().parent
MARKER = Path("skills/_shared/company-profile.md")
OUTPUT_ROOT = "compliance"


class RootNotFound(Exception):
    pass


def find_root(start: str | os.PathLike | None = None) -> Path:
    """The repository root: GOV_ROOT if set, else the nearest parent holding the suite."""
    env = os.environ.get("GOV_ROOT")
    if env:
        return Path(env).resolve()
    here = Path(start or os.getcwd()).resolve()
    for candidate in [here, *here.parents]:
        if (candidate / MARKER).is_file():
            return candidate
    raise RootNotFound(f"No suite found above {here}. Run inside the repository or set GOV_ROOT.")


def output_root(root: Path) -> Path:
    return root / OUTPUT_ROOT


def counters_file(root: Path) -> Path:
    return output_root(root) / ".gov" / "counters.yaml"
