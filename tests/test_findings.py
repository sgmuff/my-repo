from test_validate import ENTRY, edit, messages


def findings(root):
    return messages(root, "finding")


def test_fixture_has_no_findings(ropa_root):
    assert findings(ropa_root) == []


def test_company_purpose_in_a_processor_record(ropa_root):
    edit(ropa_root, lambda d: d["purposes"][1].update(decided_by="company"))
    assert any("Art. 28(10)" in m for m in findings(ropa_root))


def test_customer_purpose_with_a_chosen_basis(ropa_root):
    edit(ropa_root, lambda d: d["purposes"][0]["lawful_basis"].update(value="public-task"))
    assert any("use controller-to-confirm" in m for m in findings(ropa_root))


def test_special_category_without_art9_condition(ropa_root):
    edit(ropa_root, lambda d: d["purposes"][0]["art9_condition"].update(value="none"))
    assert any("no Art. 9 condition" in m for m in findings(ropa_root))


def test_inferred_elements(ropa_root):
    edit(ropa_root, lambda d: d["data_categories"][0].update(source={"kind": "inferred", "ref": "a guess"}))
    assert any("elements are inferred" in m for m in findings(ropa_root))


def test_no_transfers_but_a_us_recipient(ropa_root):
    edit(ropa_root, lambda d: d.update(transfers="none"))
    assert any("AWS store or access data outside" in m for m in findings(ropa_root))


def test_ai_without_intake(ropa_root):
    def drop(d):
        d["follow_ons"] = [f for f in d["follow_ons"] if f["skill"] != "ai-intake"]
    edit(ropa_root, drop)
    assert any("no AI inventory entry" in m for m in findings(ropa_root))


def test_indefinite_retention_without_action(ropa_root):
    edit(ropa_root, lambda d: d.update(actions=[]))
    assert any("kept indefinitely" in m for m in findings(ropa_root))


def test_false_flag_with_an_open_question(ropa_root):
    def change(d):
        d["open_questions"][2]["field"] = "us_flags/sale_or_sharing"
    edit(ropa_root, change)
    assert any("us_flags/sale_or_sharing: recorded as false" in m for m in findings(ropa_root))


def test_a_response_clears_a_finding(ropa_root):
    def change(d):
        d["transfers"] = "none"
        d["finding_responses"] = [{"pointer": "transfers", "response": "AWS region is Frankfurt; US support access screened in VR-2026-001", "by": "Pat Lee, privacy lead"}]
    edit(ropa_root, change)
    assert not any("AWS store or access" in m for m in findings(ropa_root))


def test_findings_never_fail_validation(ropa_root):
    edit(ropa_root, lambda d: d.update(transfers="none"))
    assert messages(ropa_root) == []


def test_processor_without_contract_or_blocker(ropa_root):
    edit(ropa_root, lambda d: d.update(actions=[a for a in d["actions"] if a["id"] != "A3"]))
    assert any("AWS: no reviewed contract on file" in m for m in findings(ropa_root))


def test_processor_copy_without_a_retention_row(ropa_root):
    edit(ropa_root, lambda d: d.update(retention=[r for r in d["retention"] if r["store"] != "Error monitoring vendor"]))
    assert any("Error monitoring vendor holds a copy" in m for m in findings(ropa_root))


def test_data_with_no_purpose(ropa_root):
    edit(ropa_root, lambda d: d["data_categories"][3].update(purposes=[]))
    assert any("Sync logs: no purpose uses this data" in m for m in findings(ropa_root))
