"""Document IDs: formats, parsing, and allocation from the counter file."""
from __future__ import annotations

import fcntl
import os
import re
from contextlib import contextmanager
from functools import lru_cache
from pathlib import Path

from gov import yamlio
from gov.paths import PACKAGE, counters_file

ID_RE = re.compile(r"\b([A-Z]{2,4})-(?:(\d{4})-)?(\d{3,4})\b")


class IdError(Exception):
    pass


@lru_cache(maxsize=None)
def prefixes() -> dict:
    return yamlio.load(PACKAGE / "rules" / "ids.yaml")["prefixes"]


def managed_types() -> dict:
    """Record types gov manages, keyed by type: {prefix, folder}."""
    return {
        spec["type"]: {"prefix": prefix, "folder": spec["folder"]}
        for prefix, spec in prefixes().items()
        if spec.get("type")
    }


def format_id(prefix: str, number: int, year: str | None = None) -> str:
    spec = _spec(prefix)
    seq = str(number).zfill(spec["digits"])
    return f"{prefix}-{year}-{seq}" if spec["yearly"] else f"{prefix}-{seq}"


def parse_id(text: str):
    """Return (prefix, year, number) for a well-formed ID, or None."""
    m = ID_RE.fullmatch(text)
    if not m or m.group(1) not in prefixes():
        return None
    prefix, year, seq = m.groups()
    spec = prefixes()[prefix]
    if bool(year) != spec["yearly"] or len(seq) != spec["digits"]:
        return None
    return prefix, year, int(seq)


def find_ids(text: str) -> list:
    """Every well-formed ID mentioned in a string."""
    return [m.group(0) for m in ID_RE.finditer(text) if parse_id(m.group(0))]


def counter_key(prefix: str, year: str | None) -> str:
    return f"{prefix}-{year}" if year else prefix


def read_counters(root: Path) -> dict:
    path = counters_file(root)
    if not path.exists():
        return {}
    data = yamlio.load(path) or {}
    return data.get("counters", {})


def next_id(root: Path, prefix: str, year: str | None = None) -> str:
    """Reserve and return the next ID. Numbers are never reused."""
    spec = _spec(prefix)
    if spec["yearly"] and not (year and re.fullmatch(r"\d{4}", year)):
        raise IdError(f"{prefix} IDs carry a year. Pass --year YYYY.")
    if not spec["yearly"] and year:
        raise IdError(f"{prefix} IDs don't carry a year.")
    path = counters_file(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    with _locked(path.with_suffix(".lock")):
        counters = read_counters(root)
        key = counter_key(prefix, year)
        number = counters.get(key, 0) + 1
        counters[key] = number
        tmp = path.with_suffix(".tmp")
        tmp.write_text(
            "# Last ID issued per prefix. Written by `gov next-id`; don't edit by hand.\n"
            + yamlio.dumps({"counters": dict(sorted(counters.items()))}),
            encoding="utf-8",
        )
        os.replace(tmp, path)
    return format_id(prefix, number, year)


def _spec(prefix: str) -> dict:
    try:
        return prefixes()[prefix]
    except KeyError:
        raise IdError(f"Unknown prefix {prefix}. Known: {', '.join(prefixes())}") from None


@contextmanager
def _locked(lock_path: Path):
    with open(lock_path, "w") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)
