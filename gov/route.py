"""`gov route`: the triage plan and decision register for a set of deciding facts."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from gov import yamlio
from gov.paths import PACKAGE

TBC = "TBC"
NEXT_QUESTIONS = 3
GATES = {"law": "Law", "policy": "Policy", "risk": "Risk"}
CANDIDATES = 8


class RoutingError(Exception):
    pass


@lru_cache(maxsize=None)
def table() -> dict:
    data = yamlio.load(PACKAGE / "rules" / "routing.yaml")
    check_table(data)
    return data


def check_table(data: dict) -> None:
    facts = data["facts"]
    for key, spec in facts.items():
        if spec.get("parent") and spec["parent"] not in facts:
            raise RoutingError(f"fact {key} names unknown parent {spec['parent']}")
    seen = set()
    for step in data["steps"]:
        sid = step["id"]
        if sid in seen:
            raise RoutingError(f"step {sid} appears twice")
        for dep in step.get("start_after", []):
            if dep not in seen:
                raise RoutingError(f"step {sid} starts after {dep}, which must be listed earlier")
        if not (step.get("when") or step.get("when_any")):
            raise RoutingError(f"step {sid} has no trigger")
        if step.get("gate") not in GATES:
            raise RoutingError(f"step {sid} needs a gate: {', '.join(GATES)}")
        _check_conditions(sid, facts, step)
        for key in step.get("indicators", []):
            if key not in facts:
                raise RoutingError(f"step {sid} lists undeclared indicator {key}")
        seen.add(sid)
    for sid_ref in [d for s in data["steps"] for d in s.get("finalize_after", [])]:
        if sid_ref not in seen:
            raise RoutingError(f"finalize_after names unknown step {sid_ref}")
    for check in data.get("checks", []):
        if check.get("gate") not in GATES:
            raise RoutingError(f"check {check['id']} needs a gate: {', '.join(GATES)}")
        if not (check.get("when") or check.get("when_any") or check.get("when_open")):
            raise RoutingError(f"check {check['id']} has no trigger")
        if check.get("when_open") and check["when_open"] not in facts:
            raise RoutingError(f"check {check['id']} uses undeclared fact {check['when_open']}")
        _check_conditions(check["id"], facts, check)


def _check_conditions(name, facts, item) -> None:
    for key, want in {**item.get("when", {}), **item.get("when_any", {})}.items():
        if key not in facts:
            raise RoutingError(f"{name} uses undeclared fact {key}")
        for value in want if isinstance(want, list) else [want]:
            _check_value(key, facts[key], value, allow_tbc=False)


def resolve_facts(given: dict) -> dict:
    """Each declared fact's value and where it came from: given, assumed, or open."""
    declared = table()["facts"]
    unknown = sorted(set(given) - set(declared))
    if unknown:
        raise RoutingError(f"unknown facts: {', '.join(unknown)}. Known: {', '.join(declared)}")
    resolved = {}
    for key, spec in declared.items():
        if key in given:
            _check_value(key, spec, given[key], allow_tbc=True)
            value = given[key]
            origin = "open" if value == TBC else "given"
        elif "default" in spec:
            value, origin = spec["default"], "assumed"
        else:
            value, origin = TBC, "open"
        resolved[key] = {"value": value, "origin": origin}
    # A child fact can't hold when its parent is no: no AI means no AI profiling.
    for key, spec in declared.items():
        parent = spec.get("parent")
        if parent and resolved[parent]["value"] is False and key not in given:
            resolved[key] = {"value": False if spec["type"] == "boolean" else "none", "origin": "implied"}
    return resolved


def route(root: Path, given: dict) -> dict:
    facts = resolve_facts(given or {})
    spec = table()
    included = {}
    for step in spec["steps"]:
        state, because, open_facts = _evaluate(step, facts)
        if state is not False:
            included[step["id"]] = (step, state, because, open_facts)

    order = [s["id"] for s in spec["steps"] if s["id"] in included and s.get("time_critical")]
    order += [s["id"] for s in spec["steps"] if s["id"] in included and not s.get("time_critical")]
    number = {sid: n for n, sid in enumerate(order, 1)}

    plan = []
    for sid in order:
        step, state, because, open_facts = included[sid]
        skill = step.get("skill")
        available = skill is None or (root / "skills" / skill / "SKILL.md").is_file()
        start_after = [number[d] for d in step.get("start_after", []) if d in included]
        plan.append({
            "n": number[sid],
            "step": sid,
            "label": step.get("label", sid),
            "skill": skill,
            "available": available,
            "time_critical": bool(step.get("time_critical")),
            "status": "required" if state is True else "conditional",
            "applies_if": _applies_if(step, open_facts),
            "start": "after " + ", ".join(map(str, start_after)) if start_after else "now",
            # Only required steps hold up finalizing; a conditional one may never run.
            "finalize_after": [number[d] for d in step.get("finalize_after", []) if d in included and included[d][1] is True],
            "gate": step["gate"],
            "because": because,
            "indicators": [k for k in step.get("indicators", []) if facts[k]["value"] is True],
            "basis": step["basis"],
            "open_facts": open_facts,
            "decision": step["decision"],
        })

    register = []
    for p in plan:
        register.append({
            "about": f"step {p['n']}",
            "decision": p["decision"]["text"],
            "owner": p["decision"]["owner"],
            "gate": p["gate"],
            "status": p["status"],
            "applies_if": p["applies_if"],
            "blocks_launch": True,
            "note": None if p["available"] else "No skill yet: the owner runs this step by hand, and launch waits until the result is recorded",
        })
    for check in spec.get("checks", []):
        state, _, open_facts = _evaluate(check, facts)
        if state is False:
            continue
        register.append({
            "about": check["id"],
            "decision": check["decision"],
            "owner": check["owner"],
            "gate": check["gate"],
            "status": "required" if state is True else "conditional",
            "applies_if": _applies_if(check, open_facts),
            "blocks_launch": True,
            "note": None,
        })

    return {
        "plan": plan,
        "decisions": register,
        "next_questions": _next_questions(plan, register, facts, NEXT_QUESTIONS),
        "question_candidates": _next_questions(plan, register, facts, CANDIDATES),
        "assumed": {k: v["value"] for k, v in facts.items() if v["origin"] == "assumed"},
        "not_built": sorted({p["skill"] for p in plan if not p["available"]}),
    }


def _evaluate(item: dict, facts: dict):
    """(True | False | None, matched facts, open facts). None means it depends on TBC facts."""
    if item.get("when_open"):
        key = item["when_open"]
        return (True, [f"{key} = TBC"], []) if facts[key]["value"] == TBC else (False, [], [])
    if item.get("when"):
        results = {k: _match(facts[k]["value"], w) for k, w in item["when"].items()}
        if any(r is False for r in results.values()):
            return False, [], []
        state = True if all(r is True for r in results.values()) else None
    else:
        results = {k: _match(facts[k]["value"], w) for k, w in item["when_any"].items()}
        if any(r is True for r in results.values()):
            state = True
        elif any(r is None for r in results.values()):
            state = None
        else:
            return False, [], []
    because = [f"{k} = {_show(facts[k]['value'])}" for k, r in results.items() if r is True]
    open_facts = [k for k, r in results.items() if r is None] if state is None else []
    return state, because, open_facts


def _applies_if(item: dict, open_facts: list):
    if not open_facts:
        return None
    conditions = {**item.get("when", {}), **item.get("when_any", {})}
    joiner = " and " if item.get("when") else " or "
    return joiner.join(f"{k} = {_show_want(conditions[k])}" for k in open_facts)


def _next_questions(plan: list, register: list, facts: dict, limit: int) -> list:
    """The open facts that settle the most conditional steps and checks, in table order on ties."""
    declared = table()["facts"]
    weight = {k: 0 for k in declared}
    bonus = {k: spec.get("priority", 0) for k, spec in declared.items()}
    for item in plan:
        for k in item["open_facts"]:
            weight[k] += 1
    for check in table().get("checks", []):
        _, _, open_facts = _evaluate(check, facts)
        for k in open_facts:
            weight[k] += 1
    for k, spec in declared.items():
        parent = spec.get("parent")
        if parent and facts[parent]["value"] is not True:
            if facts[parent]["value"] == TBC:
                weight[parent] += weight[k]
            weight[k] = 0
    ranked = [
        k for k in declared
        if facts[k]["origin"] == "open" and declared[k].get("ask", True) and weight[k] > 0
    ]
    ranked.sort(key=lambda k: -(weight[k] + bonus[k]))  # stable: table order breaks ties
    return [{"fact": k, "question": declared[k]["question"]} for k in ranked[:limit]]


def _match(value, want):
    if value == TBC:
        return None
    return value in want if isinstance(want, list) else value == want


def _check_value(key: str, spec: dict, value, allow_tbc: bool) -> None:
    if allow_tbc and value == TBC:
        return
    if spec["type"] == "boolean" and not isinstance(value, bool):
        raise RoutingError(f"{key} must be yes, no, or TBC, not {value!r}")
    if spec["type"] == "enum" and value not in spec["values"]:
        raise RoutingError(f"{key} must be one of {', '.join(spec['values'])}, or TBC, not {value!r}")


def _show(value) -> str:
    return ("yes" if value else "no") if isinstance(value, bool) else str(value)


def _show_want(want) -> str:
    return " or ".join(_show(w) for w in want) if isinstance(want, list) else _show(want)


def questions_markdown(result: dict) -> str:
    """Open facts ranked by how much they settle, for the triage skill to choose from."""
    if not result["question_candidates"]:
        return "No open facts would change this plan.\n"
    lines = ["Open facts, most decisive first:", ""]
    lines += [f"{n}. `{q['fact']}`: {q['question']}" for n, q in enumerate(result["question_candidates"], 1)]
    return "\n".join(lines) + "\n"


def to_markdown(result: dict) -> str:
    lines = []
    if result["plan"]:
        lines += [
            "| # | Step | Skill | Status | Starts | Triggered by | Finalize after |",
            "|---|---|---|---|---|---|---|",
        ]
        for p in result["plan"]:
            skill = f"`{p['skill']}`" if p["skill"] else "Human action"
            if not p["available"]:
                skill += " (no skill yet)"
            status = "Required" if p["status"] == "required" else f"If {p['applies_if']}"
            if p["time_critical"]:
                status += ", time-critical"
            trigger = "; ".join(p["because"]) or "—"
            if p["indicators"]:
                trigger += "; indicators: " + ", ".join(p["indicators"])
            final = ", ".join(map(str, p["finalize_after"])) or "—"
            lines.append(f"| {p['n']} | {p['label']} | {skill} | {status} | {p['start'].capitalize()} | {trigger} | {final} |")
        lines += ["", "**Why each step runs:**", ""]
        lines += [f"{p['n']}. {GATES[p['gate']]}: {p['basis']}" for p in result["plan"]]
    else:
        lines.append("No workflow is triggered by these facts.")

    required = [d for d in result["decisions"] if d["status"] == "required"]
    # Conditional steps already show their condition in the plan table; list only checks here.
    conditional = [d for d in result["decisions"] if d["status"] == "conditional" and not d["about"].startswith("step ")]
    lines += ["", "**Decision register.** Each blocks launch until recorded. Law: the law requires it where it applies. Policy: our own rule. Risk: a risk the owner must clear.", ""]
    if required:
        lines += ["| About | Decision | Owner | Gate | Note |", "|---|---|---|---|---|"]
        lines += [f"| {d['about']} | {d['decision']} | {d['owner']} | {GATES[d['gate']]} | {d['note'] or '—'} |" for d in required]
    else:
        lines.append("None yet.")
    if conditional:
        lines += ["", "**Legal checks that apply if a fact turns out yes:**", ""]
        lines += [f"- {d['about']} ({d['owner']}, {GATES[d['gate']].lower()}): if {d['applies_if']}" for d in conditional]
    if result["assumed"]:
        lines += ["", "**Assumed:** " + ", ".join(f"{k} = {_show(v)}" for k, v in result["assumed"].items()) + ". Say so if any is wrong."]
    lines += ["", "**Launch gate:** nothing in this plan authorizes processing. Launch waits for every required decision above."]
    return "\n".join(lines) + "\n"
