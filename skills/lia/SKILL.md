---
name: lia
description: Write a legitimate interests assessment (LIA), the GDPR three-part test of purpose, necessity, and balancing, or an Art. 6(4) compatibility assessment for reusing data for a new purpose, or record a UK recognized legitimate interest. Use it whenever someone wants to rely on legitimate interests, asks "can we use legitimate interests for X," needs a balancing test, wants to reuse customer or user data for something new such as analytics or model training, or `gov required` lists an LIA or compatibility assessment as owed, even if they don't say "LIA." Not for choosing among all lawful bases when legitimate interests isn't proposed (the RoPA and DPIA record those), the DPIA itself (dpia), or marketing consent rules alone (counsel).
compatibility: Requires the gov command from this repository (skills/install.sh installs it), with Python 3.9+, PyYAML, jsonschema, and Jinja2.
---

# Legitimate interests and compatibility assessments

This skill answers a question about legitimate interests, or about reusing data for a new purpose, and records the answer as an assessment a regulator can read. The record is one YAML file, rendered to Markdown in a fixed format.

**Answer first, then record.** The legal analysis is yours, as full and as careful as you would give without this skill. The record captures it; it doesn't shape it. Never write or edit the `.md` file; `gov` writes it.

**The assessment proposes; the privacy lead decides.** Give a provisional view on every answer, and never present a test as passed, or the processing as approved, before the facts that decide it are known.

## Files

| File | Read it when |
|---|---|
| [`references/test.md`](references/test.md) | Step 2, to check your answer for gaps |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md) | Section 3 for lawful bases, section 1 for UK changes |
| [`../_shared/conventions.md`](../_shared/conventions.md) | Step 3 |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 5 |

## Workflow

### 1. Check the tool and the role

Run `gov --version`; if it fails, stop and tell the user to run `skills/install.sh`. If the company is a processor for the purpose, say so: the customer chooses its own basis, and no LIA is the company's to write.

### 2. Answer the question

Answer the request as a careful privacy lawyer would, before you open any template: what the right basis is, whether legitimate interests or compatibility can work, every regime and country the facts touch, the national and sector rules on top of the GDPR, the traps a quick answer misses, a less intrusive way to reach the goal, and your provisional view with the facts that would change it. Write it in whatever form fits the question. Then read `references/test.md` and add anything your answer missed; don't cut what it already covers. Mark each point you can't check against a source as one to verify.

### 3. Record it

Run `gov new lia --slug <short-slug> --title "<what is assessed>" --date <today>`, and set `kind`: `lia` for the three-part test, `recognized-interest` for a UK Annex 1 purpose, or `compatibility` for a new purpose under Art. 6(4). Set the sections that don't fit the kind to `{applicable: false}`. Set `context` to every tag in `gov/rules/issues.yaml` that fits the facts.

Fill in the record from your answer. Put its reasoning in `analysis`, condensed to 400 words, and each test's call, with its reason, in the test's fields. Each call stays Provisional, and a test stays `open` while a fact that decides it is unknown. If a point doesn't fit a field, it goes in `analysis`; the record never changes your conclusion. Add a verify flag for each point to verify.

### 4. Validate and render

Before validating: mark an action `block_reason: law` only when a provision requires that action, and cite it in `scope` (`gov validate` rejects a law block without one). Gathering facts, verifying a point, or getting counsel's view is `risk` or `policy`. A DPIA is `law` only once screening finds likely high risk or a national Art. 35(4) list names the processing; a notice the law requires at collection (Art. 13 or 14) is `law`; a RoPA entry, a vendor review, and vendor terms beyond Art. 28 are `policy`. When no RoPA entry exists, add an action to create one. Run `gov validate`, fix errors, and resolve findings by changing the record. For each issue it raises, record in `issues` how your answer deals with it: `addressed` with the conclusion, `not-applicable` with why, or `open` with what's needed. If `gov` raises an issue your answer missed, deal with it in the answer too. Don't add a `finding_responses` entry yourself; only a person decides a finding doesn't apply. Validation checks structure and consistency, not legal correctness. Run `gov render`, then add the record to the RoPA entry's `assessments` if one exists, and rerun `gov validate` and `gov render`.

### 5. Reply

The privacy lead decides whether legitimate interests holds (`approvals.md`). Send the answer from step 2, as you amended it, to the requester: in plain English, as long as the answer needs and no longer, without restating the record. Put what blocks launch in words, grouped as legal requirements, risks, and internal policy, and the open questions, five at most, that would change the answer. Give a date only when the request, a contract, or the law sets it. End with one line for the file: the record IDs and paths, and the counts from `gov` of open questions, findings, and verify flags. Point to counsel for e-marketing consent rules, which neither legitimate interests nor compatibility settles, and keep compatibility, the lawful basis, and channel rules apart when they differ.
