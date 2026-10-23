import re

import yaml

from gov.render import render_tree
from gov.skeleton import new_record
from gov.ids import managed_types


def test_rendered_front_matter_is_valid_yaml_whatever_the_title(root):
    for t in managed_types():
        new_record(root, t, f"fm-{t}", "GDPR Art. 32: support # tools, 'quoted'", "2026-10-22", "Claude")
    assert render_tree(root).problems == []
    for md in (root / "compliance").rglob("*.md"):
        m = re.match(r"---\n(.*?)\n---", md.read_text(), re.S)
        if m:
            data = yaml.safe_load(m.group(1))
            if "title" in data and md.name != "index.md" and data.get("type") in managed_types():
                assert data["title"] == "GDPR Art. 32: support # tools, 'quoted'", md.name
