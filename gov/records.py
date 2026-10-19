"""Finding, loading, and describing records."""
from __future__ import annotations

import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from gov import yamlio
from gov.ids import managed_types
from gov.paths import PACKAGE, output_root

SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass
class Record:
    path: Path
    data: dict

    @property
    def id(self) -> str:
        return str(self.data.get("id", ""))

    @property
    def type(self) -> str:
        return str(self.data.get("type", ""))

    @property
    def markdown_path(self) -> Path:
        return self.path.with_suffix(".md")


@lru_cache(maxsize=None)
def schema(record_type: str) -> dict:
    path = PACKAGE / "schemas" / f"{record_type}.schema.yaml"
    if not path.exists():
        raise KeyError(record_type)
    return yamlio.load(path)


def record_files(root: Path) -> list:
    """Every record YAML file under the managed folders, sorted."""
    base = output_root(root)
    files = []
    for spec in managed_types().values():
        folder = base / spec["folder"]
        if folder.is_dir():
            files.extend(p for p in folder.glob("*.yaml"))
    return sorted(files)


def load(path: Path) -> Record:
    return Record(path=path, data=yamlio.load(path) or {})


def slug_from_filename(path: Path, record_id: str):
    stem = path.stem
    prefix = f"{record_id}-"
    if not stem.startswith(prefix):
        return None
    slug = stem[len(prefix):]
    return slug if SLUG_RE.match(slug) else None
