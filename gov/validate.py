"""Record validation: schemas, word limits, IDs, cross-references, gates, and style."""
from __future__ import annotations

import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

from jsonschema import Draft202012Validator, ValidationError, validators
from jsonschema.exceptions import best_match

from gov import ids, profile, references, yamlio
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


def validate_tree(root: Path, as_of: str | None = None) -> list:
    """Validate every record under the output root, plus tree-wide checks. as_of (YYYY-MM-DD) dates the reference
    review check; without it, each record is checked as of its own last review or preparation date."""
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
        problems.extend(validate_record(root, rec, as_of))
    problems.extend(_tree_checks(root, records))
    problems.extend(_evidence_ids(root, records))
    problems.extend(_profile_checks(root, records))
    problems.extend(Problem(str(references.INDEX), "error", m) for m in references.index_problems(root))
    return sorted(set(problems))


def validate_record(root: Path, rec: Record, as_of: str | None = None) -> list:
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
    if rec.data.get("type") == "rdy":
        problems.extend(_readiness(root, where, rec.data))
    if rec.data.get("type") == "ctl":
        problems.extend(_objectives(root, where, rec.data))
    problems.extend(_gates(where, rec.data))
    problems.extend(_law_citations(where, rec.data))
    problems.extend(_issue_ids(where, rec.data))
    problems.extend(_required(root, where, rec.data))
    for n, r in enumerate(rec.data.get("finding_responses", [])):
        if "claude" in r["by"].lower():
            problems.append(Problem(where, "error", f"finding_responses/{n}: only a person answers a finding; remove this, and report the finding instead"))
    answered = {r["pointer"] for r in rec.data.get("finding_responses", []) if "claude" not in r["by"].lower()}
    problems.extend(
        Problem(where, "finding", f"{pointer}: {message}")
        for pointer, message in FINDINGS[rec.type](rec.data) + references.findings(root, rec.data, as_of)
        if pointer not in answered
    )
    problems.extend(_style(where, rec.data))
    return problems


def _profile_checks(root: Path, records: list) -> list:
    """Scope fields left as TODO in the company profile: a warning while records are drafts, an error on approval."""
    todo = profile.scope_todos(root)
    if not todo or not records:
        return []
    fields = ", ".join(todo)
    problems = [Problem(_rel(root, rec.path), "error", f"approved while the company profile's scope fields are TODO ({fields}); fill them in and re-check the regimes")
                for rec in records if isinstance(rec.data, dict) and rec.data.get("status") in APPROVED]
    if not problems:
        problems.append(Problem("skills/_shared/company-profile.md", "warning", f"scope fields are TODO ({fields}); records can't be approved until they're filled in"))
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


AI_ACT_REQUIRED = {
    "aip": {
        "outside-scope": ["art4"],
        "non-high-risk": ["art6-4", "art49-2"],
        "high-risk": ["art9", "art10", "art11", "art12", "art13", "art14", "art15", "art17", "art43", "art47-49", "art72", "art73"],
    },
    "aid": {"deployer": ["art4", "art26-1", "art26-2", "art26-4", "art26-5", "art26-6", "art26-7", "art26-9", "art26-11", "art50", "art86"]},
}


def _objectives(root: Path, where: str, data: dict) -> list:
    """Each objective must be one of the common control objectives in crosswalk.md."""
    from gov import crosswalk
    known = crosswalk.objectives(root)
    if not known:
        return [Problem(where, "error", f"objectives: can't read the control objectives from {crosswalk.REFERENCE}")]
    return [Problem(where, "error", f"objectives/{n}: {o['cco']} isn't an objective in {crosswalk.REFERENCE.name}")
            for n, o in enumerate(data["objectives"]) if o["cco"] not in known]


def _evidence_ids(root: Path, records: list) -> list:
    """Evidence IDs live in control records: each issued by gov next-id, listed once, and every reference to one resolves."""
    problems, defined = [], {}
    counters = ids.read_counters(root)
    for rec in records:
        if rec.type != "ctl" or not isinstance(rec.data.get("evidence"), list):
            continue
        where = _rel(root, rec.path)
        for e in rec.data["evidence"]:
            ev = e.get("id", "")
            if ev in defined:
                problems.append(Problem(where, "error", f"evidence {ev} is also listed in {defined[ev]}; list each item once and cite it elsewhere"))
                continue
            defined[ev] = where
            parsed = ids.parse_id(ev)
            if parsed and parsed[2] > counters.get(ids.counter_key("EV", None), 0):
                problems.append(Problem(where, "error", f"{ev} is above the counter; allocate evidence IDs with `gov next-id EV`"))
    if not any(rec.type == "ctl" for rec in records):
        return problems
    for rec in records:
        refs = set(re.findall(r"\bEV-\d{4}\b", _all_text(rec.data)))
        own = {e.get("id") for e in rec.data.get("evidence", [])} if rec.type == "ctl" else set()
        problems += [Problem(_rel(root, rec.path), "error", f"refers to {ev}, which no control record lists")
                     for ev in sorted(refs - own - set(defined))]
    return problems


def _readiness(root: Path, where: str, data: dict) -> list:
    """An AIUC-1 Statement of Applicability against the requirements in aiuc-1.md for the agent's capabilities."""
    from gov import aiuc
    reqs = aiuc.requirements(root)
    if not reqs:
        return [Problem(where, "error", f"soa: can't read the AIUC-1 requirements from {aiuc.REFERENCE}")]
    listed = [s["requirement"] for s in data["soa"]]
    problems = [Problem(where, "error", f"soa: {i} isn't a requirement in the release in {aiuc.REFERENCE.name}; it may have been retired") for i in listed if i not in reqs]
    problems += [Problem(where, "error", f"soa: list {i} once") for i in sorted(set(listed)) if listed.count(i) > 1]
    missing = [i for i in aiuc.triggered(reqs, data["capabilities"]) if i not in listed]
    if missing:
        problems.append(Problem(where, "finding", f"soa: these mandatory requirements apply to the agent's capabilities and need a row: {', '.join(missing)}"))
    caps = set(data["capabilities"]) | {"Universal"}
    for n, s in enumerate(data["soa"]):
        r = reqs.get(s["requirement"])
        if r and s["applicability"] == "excluded" and r["status"] == "Mandatory" and caps & set(r["tags"]):
            problems.append(Problem(where, "finding", f"soa/{n}: {s['requirement']} is mandatory and tagged {', '.join(r['tags'])}, which the agent has; exclude it only if the agent genuinely lacks the capability, never to reduce effort"))
        if r and s["applicability"] == "undecided" and r["status"] == "Mandatory" and caps & set(r["tags"]):
            problems.append(Problem(where, "error", f"soa/{n}: {s['requirement']} is mandatory for this agent, so it's in scope; undecided is only for optional requirements"))
    return problems


def _structure(where: str, data: dict) -> list:
    if data.get("type") == "inc":
        from gov.derive import clock_rows
        problems = []
        _, _, error = clock_rows(data)
        if error:
            problems.append(Problem(where, "error", f"awareness: {error}"))
        problems += [Problem(where, "error", f"decisions/{n}: only a person decides; remove this, and route the decision instead")
                     for n, d in enumerate(data["decisions"]) if "claude" in str(d["by"]).lower()]
        return problems
    if data.get("type") == "aiia":
        problems = []
        domains = [g["domain"] for g in data["domains"]]
        if data["kind"] == "aiia":
            wanted = ["fairness", "transparency", "human-oversight", "data-provenance", "reliability", "safety", "security", "accountability", "society"]
            if sorted(domains) != sorted(wanted):
                problems.append(Problem(where, "error", "domains: an AI impact assessment has one row for each of the nine domains; mark a domain not-applicable with the reason"))
            if data["fria"]["applicable"]:
                problems.append(Problem(where, "error", "fria: set applicable: false for kind aiia, and record a FRIA as its own aiia record of kind fria"))
        else:
            if domains:
                problems.append(Problem(where, "error", "domains: a FRIA or input pack records Art. 27 content in fria, not domains; set domains: []"))
            needed = ["deployer_status", "processes", "period", "people", "rights_risks", "oversight", "remedies", "dpia_overlap", "notification"]
            missing = [k for k in needed if k not in data["fria"]]
            if not data["fria"]["applicable"] or missing:
                problems.append(Problem(where, "error", f"fria: set applicable: true and fill in {', '.join(missing) or 'every field'}"))
        return problems
    if data.get("type") == "vr":
        from gov.vendor_items import SECTIONS, required_clauses
        have = [c["item"] for c in data["clauses"]]
        problems = [Problem(where, "error", f"clauses: list item {i} once") for i in sorted(set(have)) if have.count(i) > 1]
        missing = [i for i in required_clauses(data) if i not in have]
        if missing:
            problems.append(Problem(where, "error", f"clauses: a {data['depth']['value']} review covers dpa-checklist.md items {', '.join(missing)}"))
        ai_have = [c["item"] for c in data["ai"]["items"]]
        if data["ai"]["applicable"] and data["kind"] != "notice" and sorted(ai_have) != sorted(SECTIONS["6"]):
            gap = [i for i in SECTIONS["6"] if i not in ai_have]
            problems.append(Problem(where, "error", f"ai/items: list each section 6 item once{' (missing ' + ', '.join(gap) + ')' if gap else ''}"))
        if not data["ai"]["applicable"] and ai_have:
            problems.append(Problem(where, "error", "ai/items: set applicable: true, or remove the items"))
        return problems
    if data.get("type") == "scr":
        numbers = sorted(c["criterion"] for c in data["criteria"])
        return [] if numbers == list(range(1, 10)) else [Problem(where, "error", "criteria: list each EDPB criterion 1 to 9 exactly once")]
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
    if data.get("type") in AI_ACT_REQUIRED:
        wanted = AI_ACT_REQUIRED[data["type"]][data["kind"]]
        present = {o["article"] for o in data["obligations"]}
        missing = [a for a in wanted if a not in present]
        return [Problem(where, "error", f"obligations: a {data['kind']} record must list {', '.join(missing)}; mark any that don't apply not-applicable with the reason as evidence")] if missing else []
    if data.get("type") != "ropa":
        return []
    rtype = data["record_type"]["value"]
    applicable = data["processor_record"].get("applicable")
    if rtype in ("processor", "both") and not applicable:
        return [Problem(where, "error", "processor_record: record type includes processor, so fill in the Art. 30(2) record")]
    if rtype == "controller" and applicable:
        return [Problem(where, "error", "processor_record: a controller record can't carry an Art. 30(2) record; change the record type to both")]
    return []


PROVISION = re.compile(r"(?:\b(?:Art\.|Arts\.|Article|s\.|ss\.|Section|Clause|Reg\.|Regulation|Rule|Part|Sch\.|Schedule|CFR|U\.S\.C\.)|§§?)\s*\d", re.I)


def _issue_ids(where: str, data: dict) -> list:
    """Context tags and issue IDs must come from gov/rules/issues.yaml."""
    from gov import issues
    rules = issues.rules()
    problems = [Problem(where, "error", f"context: unknown tag {tag}; use {', '.join(rules['context_tags'])}")
                for tag in data.get("context", []) if tag not in rules["context_tags"]]
    problems += [Problem(where, "error", f"issues: unknown issue {i}; see gov/rules/issues.yaml")
                 for i in issues.unknown(data)]
    return problems


def _law_citations(where: str, data: dict) -> list:
    """A launch block that rests on law must name the provision that requires it."""
    return [
        Problem(where, "error", f"{a['id']}: block_reason law needs scope naming the provision that requires this action, such as \"GDPR Art. 14\"; if none does, use risk or policy")
        for a in data.get("actions", [])
        if a["launch_blocking"] and a.get("block_reason") == "law" and not PROVISION.search(a.get("scope", ""))
    ]


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
