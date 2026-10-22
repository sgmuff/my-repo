from gov import security, yamlio
from gov.render import render_tree
from gov.skeleton import new_record
from gov.validate import validate_tree


def found(root, level):
    return [p.message for p in validate_tree(root) if p.level == level]


def assessment(root, kind, change=lambda d: None):
    path = new_record(root, "sra", kind, f"{kind} assessment", "2026-10-22", "Claude")
    data = yamlio.load(path)
    data["kind"] = kind
    change(data)
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    return path


def row(element, status="gap", controls=(), evidence=()):
    return {"element": element, "applicability": "applies", "reason": "Fixture", "controls": list(controls), "evidence": list(evidence), "status": status}


def test_every_kind_has_cited_elements():
    for kind, spec in security.kinds().items():
        assert spec["elements"] and spec["method"], kind
        assert all(e["cite"] and e["label"] for e in spec["elements"]), kind
    assert len(security.elements("ccpa-audit-prep")) == 19 and len(security.elements("nis2")) == 10


def test_missing_and_unknown_elements(root):
    assessment(root, "nis2", lambda d: d.update(elements=[row("21-2-a"), row("21-2-z")]))
    assert any("21-2-z isn't an element for nis2" in m for m in found(root, "error"))
    assert any("nis2 requires these, which the record doesn't list: 21-2-b" in m for m in found(root, "finding"))


def test_adequate_needs_every_element_met_with_controls_and_evidence(root):
    def adequate(d):
        d["elements"] = [row(e, "met") for e in security.elements("glba")]
        d["decision"] = {"value": "adequate", "status": "Provisional", "reason": "Fixture"}
    assessment(root, "glba", adequate)
    findings = found(root, "finding")
    assert any("b1-i is marked met with no control" in m for m in findings)
    assert any("b1-i is marked met with no evidence cited" in m for m in findings)


def test_coppa_is_annual_and_renders_with_citations(root):
    path = assessment(root, "coppa-security", lambda d: d.update(next_review="2027-12-31", elements=[row("b1")]))
    assert any("at least annually" in m for m in found(root, "finding"))
    assert found(root, "error") == []
    render_tree(root)
    text = path.with_suffix(".md").read_text()
    assert "| 16 CFR § 312.8(b)(1) | Employees designated to coordinate the program | Applies | Gap |" in text
    assert "SRA-2026-001" in (path.parent / "index.md").read_text()
