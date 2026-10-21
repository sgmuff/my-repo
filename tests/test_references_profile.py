"""Overdue reference files, and scope fields left as TODO in the company profile."""
from pathlib import Path

from conftest import REPO

from gov import references, yamlio
from gov.profile import scope_todos
from gov.render import render_tree
from gov.validate import validate_tree

LIA = Path("compliance/assessments/lia/LIA-2026-001-lead-scoring.yaml")


def found(root, level, as_of=None):
    return [p.message for p in validate_tree(root, as_of) if p.level == level]


def edit(root, change):
    path = root / LIA
    data = yamlio.load(path)
    change(data)
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    return path


def test_the_index_gives_each_files_dates(root):
    gdpr = references.index(root)["gdpr.md"]
    assert gdpr == {"verified": "2026-10-16", "review_by": "2027-01-16"}


def test_a_current_reference_raises_nothing(assess_root):
    assert not any("gdpr.md" in m for m in found(assess_root, "finding"))


def test_an_overdue_reference_is_a_finding_and_renders(assess_root):
    path = edit(assess_root, lambda d: d.update(last_reviewed="2027-02-01"))
    assert any("gdpr.md was due for review by 2027-01-16, before 2027-02-01" in m for m in found(assess_root, "finding"))
    assert render_tree(assess_root).problems == []
    assert "gdpr.md was due for review by 2027-01-16" in path.with_suffix(".md").read_text()


def test_as_of_checks_every_record_on_one_date(assess_root):
    assert any("due for review by 2027-01-16, before 2027-03-01" in m for m in found(assess_root, "finding", "2027-03-01"))


def test_a_reference_re_verified_since_the_record_is_a_finding(assess_root):
    edit(assess_root, lambda d: d.update(references=[{"file": "gdpr.md", "version": "EU GDPR as of 2026-07-01", "verified": "2026-07-01"}]))
    assert any("gdpr.md has been re-verified since this record cited it" in m for m in found(assess_root, "finding"))


def test_a_person_can_answer_the_finding(assess_root):
    def answered(d):
        d["last_reviewed"] = "2027-02-01"
        d["finding_responses"] = [{"pointer": "references/gdpr.md", "response": "Re-checked Art. 6(1)(f) on EUR-Lex; unchanged", "by": "Privacy lead"}]
    edit(assess_root, answered)
    assert not any("gdpr.md was due" in m for m in found(assess_root, "finding"))


def test_the_shipped_profile_leaves_scope_fields_as_todo():
    assert scope_todos(REPO) == ["Legal entity name", "Sector", "EU establishment", "Lead supervisory authority", "US comprehensive state privacy laws"]


def test_an_unfilled_profile_warns_on_drafts_and_blocks_approval(assess_root):
    (assess_root / "skills/_shared/company-profile.md").write_text((REPO / "skills/_shared/company-profile.md").read_text())
    assert any("scope fields are TODO" in m for m in found(assess_root, "warning"))
    assert not any("approved while" in m for m in found(assess_root, "error"))
    edit(assess_root, lambda d: d.update(status="Approved"))
    assert any("approved while the company profile's scope fields are TODO" in m for m in found(assess_root, "error"))
