"""`gov new`: a record skeleton with a fresh ID and a hint on every field."""
from __future__ import annotations

import calendar
import datetime
import json
import re
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from gov import ids
from gov.paths import PACKAGE, output_root
from gov.records import SLUG_RE


class SkeletonError(Exception):
    pass


def add_months(date_text: str, months: int) -> str:
    d = datetime.date.fromisoformat(date_text)
    month = d.month - 1 + months
    year, month = d.year + month // 12, month % 12 + 1
    day = min(d.day, calendar.monthrange(year, month)[1])
    return datetime.date(year, month, day).isoformat()


def new_record(root: Path, record_type: str, slug: str, title: str, date: str, prepared_by: str, kind: str | None = None) -> Path:
    types = ids.managed_types()
    if record_type not in types:
        raise SkeletonError(f"Unknown record type {record_type}. Known: {', '.join(sorted(types))}")
    if not SLUG_RE.match(slug) or len(slug) > 40:
        raise SkeletonError("The slug must be short, lowercase, and hyphenated, such as support-copilot.")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        raise SkeletonError("Pass --date as YYYY-MM-DD.")
    spec = types[record_type]
    folder = output_root(root) / spec["folder"]
    existing = sorted(folder.glob(f"*-{slug}.yaml")) if folder.is_dir() else []
    if existing:
        raise SkeletonError(f"A record with slug {slug} already exists: {existing[0].name}. Update it instead.")

    prefix = spec["prefix"]
    year = date[:4] if ids.prefixes()[prefix]["yearly"] else None
    record_id = ids.next_id(root, prefix, year)
    env = Environment(loader=FileSystemLoader(str(PACKAGE / "skeletons")), undefined=StrictUndefined, keep_trailing_newline=True)
    env.filters["tojson"] = lambda v: json.dumps(v, ensure_ascii=False)
    text = env.get_template(f"{record_type}.yaml.j2").render(
        id=record_id, title=title, date=date, next_review=add_months(date, 12), prepared_by=prepared_by
    )
    if kind:
        from gov.records import schema
        allowed = schema(record_type)["properties"]["kind"].get("enum", [])
        if kind not in allowed:
            raise SkeletonError(f"Unknown kind {kind} for {record_type}. Known: {', '.join(allowed)}")
        text = re.sub(r"^kind: \S+", f"kind: {kind}", text, count=1, flags=re.M)
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{record_id}-{slug}.yaml"
    path.write_text(text, encoding="utf-8")
    return path
