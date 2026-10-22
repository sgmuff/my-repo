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


def test_the_index_reads_front_matter(root):
    known = references.index(root)
    assert (known["gdpr.md"]["verified"], known["gdpr.md"]["review_by"]) == ("2026-10-16", "2027-01-16")
    assert not known["gdpr.md"]["secondary"] and not known["gdpr.md"]["unreviewed"]
    assert known["hipaa.md"]["secondary"] and not known["hipaa.md"]["partial"]
    assert known["us-breach-notification.md"]["partial"]


def test_every_shared_file_has_complete_front_matter(root):
    files = {p.name for p in (root / references.FOLDER).glob("*.md") if p.name != "README.md"}
    assert set(references.index(root)) == files and len(files) >= 18
    assert references.index_problems(root) == []


def test_broken_front_matter_fails_closed(assess_root):
    gdpr = assess_root / references.FOLDER / "gdpr.md"
    text = gdpr.read_text()
    gdpr.write_text(text.replace("review_by: '2027-01-16'", "review_by: next January"))
    assert any("gdpr.md: review_by must be YYYY-MM-DD" in m for m in found(assess_root, "error"))
    gdpr.write_text(text.split("---\n", 2)[2])
    assert any("gdpr.md: no front matter" in m for m in found(assess_root, "error"))


def test_partial_counsel_review_is_a_finding_and_caveats_render(assess_root):
    path = edit(assess_root, lambda d: d.update(references=[
        {"file": "us-breach-notification.md", "version": "As of 2026-10-21", "verified": "2026-10-21"},
        {"file": "hipaa.md", "version": "Rules through 2013", "verified": "2026-10-18"}]))
    assert any("counsel has reviewed only part of us-breach-notification.md" in m for m in found(assess_root, "finding"))
    assert render_tree(assess_root).problems == []
    text = path.with_suffix(".md").read_text()
    assert "verified 2026-10-21 (partly checked against secondary sources; partly reviewed by counsel)" in text
    assert "verified 2026-10-18 (checked against secondary sources only)" in text


def test_the_readme_table_is_generated_and_checked(root):
    readme = root / references.INDEX
    render_tree(root)
    assert "| `gdpr.md` | EU GDPR, UK GDPR and DUAA, Swiss FADP |" in readme.read_text()
    readme.write_text(readme.read_text().replace("| `gdpr.md` | EU GDPR", "| `gdpr.md` | Edited by hand"))
    assert render_tree(root, check=True).stale == [str(references.INDEX)]


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
