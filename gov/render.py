"""Markdown rendering from records. The model never writes these files."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined

from gov import derive, ids
from gov.paths import PACKAGE, output_root
from gov.records import load, record_files
from gov.validate import Problem, _rel, validate_tree

LABELS = {
    "controller": "Controller",
    "processor": "Processor",
    "both": "Controller and processor",
    "consent": "Consent (Art. 6(1)(a))",
    "contract": "Contract (Art. 6(1)(b))",
    "legal-obligation": "Legal obligation (Art. 6(1)(c))",
    "vital-interests": "Vital interests (Art. 6(1)(d))",
    "public-task": "Public task (Art. 6(1)(e))",
    "legitimate-interests": "Legitimate interests (Art. 6(1)(f))",
    "not-applicable": "Not applicable",
    "internal": "Internal",
    "authority": "Authority",
    "adequacy": "Adequacy decision",
    "eu-us-dpf": "EU-US Data Privacy Framework",
    "sccs": "SCCs",
    "uk-idta": "UK IDTA",
    "uk-addendum": "UK Addendum",
    "bcrs": "BCRs",
    "art49-derogation": "Art. 49 derogation",
    "covered": "Covered",
    "gap": "Gap",
    "approved": "Approved",
    "approved-with-conditions": "Approved with conditions",
    "rejected": "Rejected",
    "recommended": "Recommended",
    "none": "None",
    "special-category": "Special category",
    "criminal": "Criminal",
    "biometric": "Biometric",
    "us-sensitive": "US-sensitive",
    "education-record": "Education record",
    "children": "Children",
    "government-id": "Government ID",
    "financial": "Financial",
    "company": "Company",
    "customer": "Customer",
    "joint": "Joint",
    "controller-to-confirm": "Controller to confirm",
    "sub-processor": "Sub-processor",
    "eu-gdpr": "EU GDPR",
    "uk-gdpr": "UK GDPR",
    "ch-fadp": "Swiss FADP",
    "stored": "Stored",
    "remote-access": "Remote access",
    "uk-extension": "UK Extension to the DPF",
    "swiss-us-dpf": "Swiss-US DPF",
    "launch": "Launch",
    "law": "law",
    "policy": "policy",
    "risk": "risk",
    "approval": "Approval",
    "record": "Record",
    "open": "Open",
    "done": "Done",
}
SOURCE_KINDS = {"document": "Document", "stated": "Stated by", "inferred": "Inferred", "tbc": "TBC"}


def cell(value) -> str:
    if value is None:
        return "—"
    return str(value).replace("|", "\\|").replace("\n", " ").strip()


def yn(value) -> str:
    if isinstance(value, bool):
        return "Yes" if value else "No"
    return cell(value)


def label(value) -> str:
    if value is None:
        return "—"
    return LABELS.get(value, cell(value))


def src(source: dict) -> str:
    kind = SOURCE_KINDS[source["kind"]]
    return f"{kind}: {cell(source['ref'])}" if source.get("ref") else kind


def join_or_tbc(value) -> str:
    return "TBC" if value == "TBC" else ", ".join(cell(v) for v in value)


def flags(value) -> str:
    if value == "TBC":
        return "TBC"
    if not value:
        return "None"
    return "; ".join(f"{label(f['flag'])} ({f['status']}: {cell(f['reason'])})" for f in value)


def call(position: dict) -> str:
    """A position with its status and reason: "Contract (Art. 6(1)(b)). Provisional: reason"."""
    value = position["value"]
    shown = yn(value) if isinstance(value, bool) else label(value)
    if value == "TBC":
        return f"TBC: {cell(position['reason'])}"
    return f"{shown}. {position['status']}: {cell(position['reason'])}"


@lru_cache(maxsize=None)
def _env() -> Environment:
    env = Environment(
        loader=FileSystemLoader(str(PACKAGE / "templates")),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
        autoescape=False,
    )
    env.filters.update(cell=cell, yn=yn, label=label, src=src, join_or_tbc=join_or_tbc, flags=flags, call=call)
    return env


def render_record(rec) -> str:
    template = _env().get_template(f"{rec.type}.md.j2")
    vendors = derive.vendor_slugs(rec.data) if rec.type == "ropa" else []
    text = template.render(r=rec.data, d=derive.DERIVE[rec.type](rec.data), source_file=rec.path.name, vendors=vendors)
    return _tidy(text)


def render_index(record_type: str, records: list) -> str:
    rows = [
        {"r": rec.data, "d": derive.DERIVE[record_type](rec.data), "file": rec.markdown_path.name}
        for rec in sorted(records, key=lambda r: r.id)
    ]
    template = _env().get_template(f"{record_type}-index.md.j2")
    text = template.render(
        rows=rows,
        approved=sum(1 for row in rows if row["r"]["status"].startswith("Approved")),
        tbc=sum(row["d"]["required_tbc"] for row in rows),
    )
    return _tidy(text)


@dataclass
class RenderResult:
    written: list
    stale: list
    problems: list


def render_tree(root: Path, check: bool = False) -> RenderResult:
    """Render every record and index. With check, write nothing and report drift."""
    problems = [p for p in validate_tree(root) if p.level == "error"]
    if problems:
        return RenderResult([], [], problems)

    outputs = {}
    by_type = {}
    for path in record_files(root):
        rec = load(path)
        outputs[rec.markdown_path] = render_record(rec)
        by_type.setdefault(rec.type, []).append(rec)
    for record_type, spec in ids.managed_types().items():
        folder = output_root(root) / spec["folder"]
        if folder.is_dir() or by_type.get(record_type):
            outputs[folder / "index.md"] = render_index(record_type, by_type.get(record_type, []))

    written, stale = [], []
    for path, text in sorted(outputs.items()):
        current = path.read_text(encoding="utf-8") if path.exists() else None
        if current == text:
            continue
        if check:
            stale.append(_rel(root, path))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
            written.append(_rel(root, path))
    return RenderResult(written, stale, [])


def _tidy(text: str) -> str:
    """Collapse runs of blank lines left by conditional blocks."""
    lines, blank = [], False
    for line in text.splitlines():
        if not line.strip():
            if not blank and lines:
                lines.append("")
            blank = True
        else:
            lines.append(line.rstrip())
            blank = False
    while lines and not lines[-1]:
        lines.pop()
    return "\n".join(lines) + "\n"


__all__ = ["render_record", "render_index", "render_tree", "RenderResult", "Problem"]
