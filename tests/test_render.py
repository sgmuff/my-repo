from conftest import FIXTURES, golden

from gov import derive, yamlio
from gov.render import render_tree
from gov.skeleton import add_months, new_record
from gov.validate import validate_tree

FOLDER = "compliance/registers/ropa"


def test_entry_and_index_golden(ropa_root):
    result = render_tree(ropa_root)
    assert result.problems == []
    golden(FIXTURES / "ropa" / "ROPA-0001-gradebook-sync.expected.md",
           (ropa_root / FOLDER / "ROPA-0001-gradebook-sync.md").read_text())
    golden(FIXTURES / "ropa" / "index.expected.md", (ropa_root / FOLDER / "index.md").read_text())


def test_render_is_deterministic(ropa_root):
    render_tree(ropa_root)
    first = (ropa_root / FOLDER / "ROPA-0001-gradebook-sync.md").read_text()
    assert render_tree(ropa_root).written == []
    assert (ropa_root / FOLDER / "ROPA-0001-gradebook-sync.md").read_text() == first


def test_check_catches_hand_edits(ropa_root):
    render_tree(ropa_root)
    md = ropa_root / FOLDER / "ROPA-0001-gradebook-sync.md"
    md.write_text(md.read_text() + "\nA note added by hand.\n")
    assert render_tree(ropa_root, check=True).stale == [f"{FOLDER}/ROPA-0001-gradebook-sync.md"]


def test_invalid_records_block_rendering(ropa_root):
    path = ropa_root / FOLDER / "ROPA-0001-gradebook-sync.yaml"
    data = yamlio.load(path)
    data["status"] = "Done"
    path.write_text(yamlio.dumps(data))
    result = render_tree(ropa_root)
    assert result.problems and result.written == []


def test_derived_values():
    data = yamlio.load(FIXTURES / "ropa" / "ROPA-0001-gradebook-sync.yaml")
    d = derive.ropa(data)
    assert d["special_category"] is True
    assert d["children_or_students"] is True
    assert d["restricted_transfers"] == "TBC"
    assert d["lawful_basis_status"] == "Open"
    assert d["required_tbc"] == 3
    assert d["missing"][0].startswith("Art. 30(1)(a)/(2)(a)")


def test_each_art30_element_counts_once():
    data = yamlio.load(FIXTURES / "ropa" / "ROPA-0001-gradebook-sync.yaml")
    data["retention"] = [dict(r, current_practice="TBC", proposed_policy="TBC") for r in data["retention"] * 4]
    assert derive.ropa(data)["required_tbc"] == 3  # processor record: retention isn't an Art. 30(2) element
    data["record_type"]["value"] = "both"
    assert derive.ropa(data)["required_tbc"] == 4


def test_new_skeleton_is_valid_and_renders(root):
    path = new_record(root, "ropa", "webinar-signup", "Webinar signup", "2026-10-18", "Claude")
    assert path.name == "ROPA-0001-webinar-signup.yaml"
    assert validate_tree(root) == []
    assert render_tree(root).problems == []
    assert yamlio.load(path)["next_review"] == "2027-10-18"


def test_new_refuses_a_duplicate_slug(root):
    new_record(root, "ropa", "webinar-signup", "Webinar signup", "2026-10-18", "Claude")
    try:
        new_record(root, "ropa", "webinar-signup", "Webinar signup", "2026-10-18", "Claude")
    except Exception as exc:
        assert "already exists" in str(exc)
    else:
        raise AssertionError("expected a refusal")


def test_add_months_clamps_the_day():
    assert add_months("2028-02-29", 12) == "2029-02-28"
    assert add_months("2026-10-31", 4) == "2027-02-28"


def test_front_matter_feeds_the_legacy_scripts(ropa_root):
    """compliance_schedule.py and program_metrics.py read flat front matter until phase 6."""
    import re
    render_tree(ropa_root)
    text = (ropa_root / FOLDER / "ROPA-0001-gradebook-sync.md").read_text()
    block = re.match(r"---\n(.*?)\n---", text, re.S).group(1)
    meta = dict(line.split(": ", 1) for line in block.splitlines())
    assert meta["type"] == "ropa" and meta["next_review"] == "2027-10-18" and meta["vendors"] == "[aws, error-monitoring-vendor]"


def test_tbc_with_an_explanation_still_counts():
    data = yamlio.load(FIXTURES / "ropa" / "ROPA-0001-gradebook-sync.yaml")
    data["security"]["baseline"] = "TBC (company profile baseline not yet filled in)"
    assert "Art. 30(1)(g)/(2)(d): security measures" in derive.ropa_missing(data)
    assert not derive.is_tbc("TBCx")


def test_vendor_slugs_fall_back_to_processor_names():
    data = yamlio.load(FIXTURES / "ropa" / "ROPA-0001-gradebook-sync.yaml")
    assert derive.vendor_slugs(data) == ["aws", "error-monitoring-vendor"]


def test_launch_status_lists_blockers(ropa_root):
    render_tree(ropa_root)
    text = (ropa_root / FOLDER / "ROPA-0001-gradebook-sync.md").read_text()
    assert "**Launch:** blocked by A1, A3." in text
