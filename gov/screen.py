"""`gov screen`: the DPIA screening indicators a RoPA record's facts suggest. Every row is Provisional. The screen
counts suggested criteria but never concludes; WP248 says two or more will need a DPIA "in most cases", not always."""
from __future__ import annotations

from functools import lru_cache

from gov import yamlio
from gov.paths import PACKAGE


@lru_cache(maxsize=None)
def rules() -> dict:
    return yamlio.load(PACKAGE / "rules" / "screening.yaml")


def _open(call) -> bool:
    return isinstance(call, dict) and call.get("value") in (True, "TBC")


def _show(value) -> str:
    return {True: "true", False: "false"}.get(value, str(value))


def _hits(test, data: dict) -> list:
    """Where the test matches, as short evidence strings."""
    if test == "vulnerable_subject":
        return [f"data_subjects: {s['category']} (vulnerable {_show(s['vulnerable']['value'])})"
                for s in data.get("data_subjects", []) if _open(s.get("vulnerable"))]
    if test == "ai_used":
        return [f"ai_used: {_show(data['ai_used'])}"] if data.get("ai_used") in (True, "TBC") else []
    if "us_flag" in test:
        name = test["us_flag"]
        call = (data.get("us_flags") or {}).get(name)
        return [f"us_flags.{name}: {_show(call['value'])}"] if _open(call) else []
    if "data_flag" in test:
        wanted = set(test["data_flag"])
        return [f"data_categories: {c['category']} ({f['flag']})"
                for c in data.get("data_categories", []) if isinstance(c.get("flags"), list)
                for f in c["flags"] if f["flag"] in wanted]
    raise ValueError(f"unknown screening test {test!r}")


def screen(data: dict) -> dict:
    rows = []
    for c in rules()["criteria"]:
        if "raised_by" not in c:
            rows.append({"criterion": c["id"], "label": c["label"], "result": "ask", "evidence": []})
            continue
        evidence = [e for test in c["raised_by"] for e in _hits(test, data)]
        rows.append({"criterion": c["id"], "label": c["label"], "result": "suggested" if evidence else "not-suggested", "evidence": evidence})
    return {"record": data.get("id"), "status": "Provisional", "source": rules()["source"],
            "suggested": sum(r["result"] == "suggested" for r in rows), "ask": sum(r["result"] == "ask" for r in rows), "criteria": rows}


def to_markdown(result: dict) -> str:
    lines = [f"# DPIA screening indicators for {result['record']} (Provisional)", "",
             f"Source: {result['source']}. The facts suggest {result['suggested']} of 9 criteria; {result['ask']} can't be read "
             "from the RoPA and need asking. Two or more criteria will need a DPIA in most cases, not always: the screening "
             "record decides.", "", "| # | Criterion | Result | Raised by |", "|---|---|---|---|"]
    labels = {"suggested": "Suggested", "not-suggested": "Not suggested", "ask": "Ask"}
    for r in result["criteria"]:
        lines.append(f"| {r['criterion']} | {r['label']} | {labels[r['result']]} | {'; '.join(r['evidence']) or '-'} |")
    return "\n".join(lines) + "\n"
