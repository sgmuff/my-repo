"""Record validation: schemas, word limits, IDs, cross-references, gates, and style."""
from __future__ import annotations

import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from jsonschema import Draft202012Validator, ValidationError, validators
from jsonschema.exceptions import best_match

from gov import ids, yamlio
from gov import required as req
from gov.findings import FINDINGS
from gov.paths import PACKAGE, output_root
from gov.records import Record, load, record_files, schema, slug_from_filename

APPROVED = {"Approved", "Approved with conditions"}


@dataclass(frozen=True, order=True)
class Problem:
    path: str
    level: str  # "error", "finding" (a legal consistency question for a person), or "warning" (style)
    message: str

    def __str__(self) -> str:
        return f"{self.path}: {self.level}: {self.message}"


def _max_words(validator, limit, instance, schema_):
    if isinstance(instance, str) and len(instance.split()) > limit:
        yield ValidationError(f"has {len(instance.split())} words; the limit is {limit}")


GovValidator = validators.extend(Draft202012Validator, {"x-max-words": _max_words})


@lru_cache(maxsize=None)
def _registry():
    """Every schema file by name, so a schema can reference common.schema.yaml#/$defs/..."""
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT202012

    resources = [
        (path.name, Resource.from_contents(yamlio.load(path), default_specification=DRAFT202012))
        for path in sorted((PACKAGE / "schemas").glob("*.schema.yaml"))
    ]
    return Registry().with_resources(resources)


@lru_cache(maxsize=None)
def _validator(record_type: str):
    return GovValidator(schema(record_type), registry=_registry())


@lru_cache(maxsize=None)
def _filler() -> list:
    phrases = yamlio.load(PACKAGE / "rules" / "style.yaml")["filler"]
    return [(p, re.compile(r"\b" + re.escape(p) + r"\b", re.IGNORECASE)) for p in phrases]


def validate_tree(root: Path) -> list:
    """Validate every record under the output root, plus tree-wide checks."""
    problems = []
    records = []
    for path in record_files(root):
        try:
            rec = load(path)
        except Exception as exc:  # malformed YAML
            hint = ""
            if "flow mapping" in str(exc):
                hint = " Inside {...}, text containing a comma, colon, question mark, or # must be in double quotes."
            problems.append(Problem(_rel(root, path), "error", f"can't parse YAML: {exc}{hint}"))
            continue
        records.append(rec)
        problems.extend(validate_record(root, rec))
    problems.extend(_tree_checks(root, records))
    return sorted(set(problems))


def validate_record(root: Path, rec: Record) -> list:
    where = _rel(root, rec.path)
    if not isinstance(rec.data, dict):
        return [Problem(where, "error", "the file must hold a mapping")]
    try:
        validator = _validator(rec.type)
    except KeyError:
        return [Problem(where, "error", f"unknown record type {rec.type!r}")]

    problems = [Problem(where, "error", _describe(err)) for err in validator.iter_errors(rec.data)]
    if problems:
        return problems  # later checks assume a schema-valid record

    spec = ids.managed_types()[rec.type]
    expected_folder = output_root(root) / spec["folder"]
    if rec.path.parent.resolve() != expected_folder.resolve():
        problems.append(Problem(where, "error", f"{rec.type} records belong in {spec['folder']}/"))
    if not slug_from_filename(rec.path, rec.id):
        problems.append(Problem(where, "error", f"file name must be {rec.id}-<slug>.yaml, with a lowercase hyphenated slug"))

    problems.extend(_local_ids(where, rec.data))
    problems.extend(_structure(where, rec.data))
    problems.extend(_gates(where, rec.data))
    problems.extend(_required(root, where, rec.data))
    for n, r in enumerate(rec.data.get("finding_responses", [])):
        if "claude" in r["by"].lower():
            problems.append(Problem(where, "error", f"finding_responses/{n}: only a person answers a finding; remove this, and report the finding instead"))
    answered = {r["pointer"] for r in rec.data.get("finding_responses", []) if "claude" not in r["by"].lower()}
    problems.extend(
        Problem(where, "finding", f"{pointer}: {message}")
        for pointer, message in FINDINGS[rec.type](rec.data)
        if pointer not in answered
    )
    problems.extend(_style(where, rec.data))
    return problems


def _tree_checks(root: Path, records: list) -> list:
    problems = []
    by_id = {}
    for rec in records:
        if rec.id in by_id:
            problems.append(Problem(_rel(root, rec.path), "error", f"duplicate ID {rec.id}, also in {_rel(root, by_id[rec.id].path)}"))
        else:
            by_id[rec.id] = rec

    counters = ids.read_counters(root)
    managed_prefixes = {spec["prefix"] for spec in ids.managed_types().values()}
    for rec in records:
        where = _rel(root, rec.path)
        parsed = ids.parse_id(rec.id)
        if parsed:
            prefix, year, number = parsed
            if number > counters.get(ids.counter_key(prefix, year), 0):
                problems.append(Problem(where, "error", f"{rec.id} is above the counter; allocate IDs with `gov next-id`"))
        for ref in sorted(set(ids.find_ids(_all_text(rec.data)))):
            if ref == rec.id:
                continue
            if ids.parse_id(ref)[0] in managed_prefixes and ref not in by_id:
                problems.append(Problem(where, "error", f"refers to {ref}, which doesn't exist"))

    base = output_root(root)
    for spec in ids.managed_types().values():
        folder = base / spec["folder"]
        if not folder.is_dir():
            continue
        for md in sorted(folder.glob("*.md")):
            if md.name != "index.md" and not md.with_suffix(".yaml").exists():
                problems.append(Problem(_rel(root, md), "error", "Markdown with no YAML record; edit the record and run `gov render`"))
    return problems


def _local_ids(where: str, data: dict) -> list:
    problems = []
    for key in ("purposes", "actions", "open_questions", "verify"):
        seen = [item["id"] for item in data.get(key) or []]
        for dup in sorted({i for i in seen if seen.count(i) > 1}):
            problems.append(Problem(where, "error", f"{key}: {dup} is used more than once"))
    purpose_ids = {p["id"] for p in data.get("purposes", [])}
    for section in ("data_categories", "recipients"):
        items = data.get(section)
        if not isinstance(items, list):
            continue
        for n, item in enumerate(items):
            for ref in item.get("purposes", []):
                if ref not in purpose_ids:
                    problems.append(Problem(where, "error", f"{section}/{n}/purposes: {ref} isn't a defined purpose"))
    return problems


KIND_SECTIONS = {
    "lia": {"purpose_test", "necessity_test", "balancing"},
    "recognized-interest": {"recognized_interest"},
    "compatibility": {"compatibility"},
}
TIA_TOOLS = {"eu-tia": {"sccs", "bcrs"}, "uk-tra": {"uk-idta", "uk-addendum"}, "ch-tia": {"ch-sccs"}}


def _structure(where: str, data: dict) -> list:
    if data.get("type") == "lia":
        wanted = KIND_SECTIONS[data["kind"]]
        problems = []
        for section in ("purpose_test", "necessity_test", "balancing", "recognized_interest", "compatibility"):
            applicable = data[section].get("applicable")
            if (section in wanted) != applicable:
                state = "fill in" if section in wanted else "set applicable: false for"
                problems.append(Problem(where, "error", f"{section}: a {data['kind']} assessment must {state} this section"))
        if data["kind"] == "recognized-interest" and data["regimes"] != ["uk-gdpr"]:
            problems.append(Problem(where, "error", "regimes: recognized legitimate interests exist only under the UK GDPR"))
        return problems
    if data.get("type") == "tia":
        tool = data["mechanism"]["tool"]
        if tool != "TBC" and tool not in TIA_TOOLS[data["kind"]]:
            return [Problem(where, "error", f"mechanism/tool: {tool} doesn't fit a {data['kind']}; use {', '.join(sorted(TIA_TOOLS[data['kind']]))}")]
        return []
    if data.get("type") != "ropa":
        return []
    rtype = data["record_type"]["value"]
    applicable = data["processor_record"].get("applicable")
    if rtype in ("processor", "both") and not applicable:
        return [Problem(where, "error", "processor_record: record type includes processor, so fill in the Art. 30(2) record")]
    if rtype == "controller" and applicable:
        return [Problem(where, "error", "processor_record: a controller record can't carry an Art. 30(2) record; change the record type to both")]
    return []


def _gates(where: str, data: dict) -> list:
    status = data.get("status")
    if status not in APPROVED:
        return []
    problems = []
    for n, row in enumerate(data.get("signoff", [])):
        if not (row.get("name") and row.get("date") and row.get("outcome") in ("approved", "approved-with-conditions")):
            problems.append(Problem(where, "error", f"status is {status}, but signoff/{n} ({row.get('decision')}) has no recorded approval"))
    for q in data.get("open_questions", []):
        if q["blocks"] in ("launch", "approval"):
            problems.append(Problem(where, "error", f"status is {status}, but {q['id']} still blocks {q['blocks']}"))
    if status == "Approved":
        for a in data.get("actions", []):
            if a["launch_blocking"] and a["status"] == "open":
                problems.append(Problem(where, "error", f"status is Approved, but launch-blocking action {a['id']} is open; use Approved with conditions"))
    return problems


def _required(root: Path, where: str, data: dict) -> list:
    """Each assessment the catalog says this activity owes needs a response before review."""
    if data.get("type") != "ropa":
        return []
    problems = []
    known = {e["id"] for e in req.catalog()["entries"]}
    covered = set()
    for n, a in enumerate(data.get("assessments", [])):
        if a["assessment"] not in known:
            problems.append(Problem(where, "error", f"assessments/{n}: {a['assessment']} isn't in the catalog (gov/rules/assessments.yaml)"))
        if a["status"] == "on-file" and not ids.parse_id(a.get("record", "")):
            problems.append(Problem(where, "error", f"assessments/{n}: record must be a document ID, such as DPIA-2026-004"))
        covered.add(a["assessment"])
    in_review = data["status"] in {"In review"} | APPROVED
    for r in req.evaluate(req.facts_from_ropa(data), data["date_prepared"], root):
        if r["assessment"] in covered:
            continue
        if r["status"] == "owed":
            level = "error" if in_review else "finding"
            problems.append(Problem(where, level, f"assessments: owes {r['name']} ({r['citation']}); record it as on-file, planned, or not-applicable with who decided"))
        elif r["status"] == "tbc" and in_review:
            problems.append(Problem(where, "error", f"assessments: may owe {r['name']}; it {r['reason']}. Settle the facts or record a response before review"))
    return problems


def _style(where: str, data: dict) -> list:
    problems = []
    for pointer, text in _strings(data):
        for phrase, rx in _filler():
            if rx.search(text):
                problems.append(Problem(where, "warning", f"{pointer}: filler phrase {phrase!r}"))
    return problems


def _describe(err: ValidationError) -> str:
    if err.context:
        err = best_match(err.context)
    pointer = "/".join(str(p) for p in err.absolute_path) or "(record)"
    message = f"{pointer}: {err.message}"
    if err.validator == "additionalProperties" and isinstance(err.instance, dict) \
            and any(" " in str(k) or err.instance[k] is None for k in err.instance):
        message += ". A comma inside {...} splits the text; put the value in double quotes"
    return message


def _strings(data, pointer=""):
    if isinstance(data, str):
        yield pointer or "(record)", data
    elif isinstance(data, dict):
        for key, value in data.items():
            yield from _strings(value, f"{pointer}/{key}" if pointer else str(key))
    elif isinstance(data, list):
        for n, value in enumerate(data):
            yield from _strings(value, f"{pointer}/{n}")


def _all_text(data) -> str:
    return "\n".join(text for _, text in _strings(data))


def _rel(root: Path, path: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(path)
