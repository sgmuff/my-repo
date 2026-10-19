from gov import yamlio
from gov.validate import validate_tree

ENTRY = "compliance/registers/ropa/ROPA-0001-gradebook-sync.yaml"


def edit(root, change):
    path = root / ENTRY
    data = yamlio.load(path)
    change(data)
    path.write_text(yamlio.dumps(data), encoding="utf-8")


def messages(root, level="error"):
    return [p.message for p in validate_tree(root) if p.level == level]


def test_fixture_is_valid(ropa_root):
    assert validate_tree(ropa_root) == []


def test_word_limit(ropa_root):
    edit(ropa_root, lambda d: d.update(summary="word " * 61))
    assert any("summary: has 61 words; the limit is 60" in m for m in messages(ropa_root))


def test_enum(ropa_root):
    edit(ropa_root, lambda d: d["purposes"][0]["lawful_basis"].update(value="because"))
    assert any(m.startswith("purposes/0/lawful_basis") for m in messages(ropa_root))


def test_unknown_field(ropa_root):
    edit(ropa_root, lambda d: d.update(extra="x"))
    assert any("extra" in m for m in messages(ropa_root))


def test_source_needs_a_ref(ropa_root):
    edit(ropa_root, lambda d: d["purposes"][0].update(source={"kind": "document"}))
    assert any("ref" in m for m in messages(ropa_root))


def test_undefined_purpose(ropa_root):
    edit(ropa_root, lambda d: d["data_categories"][0].update(purposes=["P9"]))
    assert any("P9 isn't a defined purpose" in m for m in messages(ropa_root))


def test_file_name_must_match_id(ropa_root):
    (ropa_root / ENTRY).rename(ropa_root / "compliance/registers/ropa/gradebook.yaml")
    assert any("file name must be ROPA-0001-<slug>.yaml" in m for m in messages(ropa_root))


def test_id_above_counter(ropa_root):
    edit(ropa_root, lambda d: d.update(id="ROPA-0005"))
    (ropa_root / ENTRY).rename(ropa_root / "compliance/registers/ropa/ROPA-0005-gradebook-sync.yaml")
    assert any("above the counter" in m for m in messages(ropa_root))


def test_dangling_reference(ropa_root):
    edit(ropa_root, lambda d: d["related"].update(assessment="Merged into ROPA-0099"))
    assert any("refers to ROPA-0099" in m for m in messages(ropa_root))


def test_markdown_without_record(ropa_root):
    (ropa_root / "compliance/registers/ropa/ROPA-0002-orphan.md").write_text("# hand-written\n")
    assert any("Markdown with no YAML record" in m for m in messages(ropa_root))


def test_approval_needs_recorded_signoff(ropa_root):
    edit(ropa_root, lambda d: d.update(status="Approved"))
    assert any("has no recorded approval" in m for m in messages(ropa_root))


def test_approval_waits_for_blocking_questions_and_actions(ropa_root):
    def approve(d):
        d["status"] = "Approved"
        for row in d["signoff"]:
            row.update(name="Pat Lee", date="2026-10-20", outcome="approved")
    edit(ropa_root, approve)
    found = messages(ropa_root)
    assert any("Q1 still blocks approval" in m for m in found)
    assert any("launch-blocking action A1 is open" in m for m in found)


def test_processor_record_required_for_processor(ropa_root):
    edit(ropa_root, lambda d: d.update(processor_record={"applicable": False}))
    assert any("fill in the Art. 30(2) record" in m for m in messages(ropa_root))


def test_unquoted_comma_gets_a_hint(ropa_root):
    path = ropa_root / ENTRY
    text = path.read_text().replace('reason: "K-12 students, likely including children"', "reason: K-12 students, likely including children")
    path.write_text(text)
    assert any("put the value in double quotes" in m for m in messages(ropa_root))


def test_filler_is_a_warning(ropa_root):
    edit(ropa_root, lambda d: d.update(summary="A robust sync of rosters."))
    assert messages(ropa_root) == []
    assert any("filler phrase 'robust'" in m for m in messages(ropa_root, "warning"))


def test_blocking_action_needs_a_reason(ropa_root):
    edit(ropa_root, lambda d: d["actions"][0].pop("block_reason"))
    assert any("block_reason" in m for m in messages(ropa_root))
