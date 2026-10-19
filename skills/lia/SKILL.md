---
name: lia
description: Write a legitimate interests assessment (LIA), the GDPR three-part test of purpose, necessity, and balancing, or an Art. 6(4) compatibility assessment for reusing data for a new purpose, or record a UK recognized legitimate interest. Use it whenever someone wants to rely on legitimate interests, asks "can we use legitimate interests for X," needs a balancing test, wants to reuse customer or user data for something new such as analytics or model training, or `gov required` lists an LIA or compatibility assessment as owed, even if they don't say "LIA." Not for choosing among all lawful bases when legitimate interests isn't proposed (the RoPA and DPIA record those), the DPIA itself (dpia), or marketing consent rules alone (counsel).
compatibility: Requires the gov command from this repository (skills/install.sh installs it), with Python 3.9+, PyYAML, jsonschema, and Jinja2.
---

# Legitimate interests and compatibility assessments

This skill writes the assessment a controller needs before relying on legitimate interests, or before reusing data for a new purpose. The output is one YAML record, rendered to Markdown in a fixed format.

**You fill in the record; `gov` writes the document.** Every assessment renders the same sections in the same order, each citing what it satisfies, so a regulator can read any of them the same way. Never write or edit the `.md` file.

**The assessment proposes; the privacy lead decides.** Every test is a call with a value, Provisional, and a one-line reason. The decision stays `open` until the facts support it, and only the privacy lead confirms it.

## Files

| File | Read it when |
|---|---|
| [`references/test.md`](references/test.md) | Always: how to run each test |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md) | Section 3 for lawful bases, section 1 for UK changes |
| [`../_shared/conventions.md`](../_shared/conventions.md) | At the start of every run |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 6 |

## Workflow

### 1. Check the tool and the role

Run `gov --version`; if it fails, stop and tell the user to run `skills/install.sh`. Find the RoPA entry for the activity. If the company is a processor for the purpose, stop: the customer chooses its own basis. Say so, and offer to note it in the RoPA.

### 2. Pick the kind

- `lia`: legitimate interests under the three-part test
- `recognized-interest`: a UK Annex 1 purpose, which needs no balancing
- `compatibility`: a new purpose for data collected for another (Art. 6(4))

Run `gov new lia --slug <short-slug> --title "<what is assessed>" --date <today>`, set `kind`, and set the sections that don't fit the kind to `{applicable: false}`.

### 3. Fill in the tests

Follow `references/test.md`. Record what the sources show:

- **Purpose:** the specific interest, whose it is, and what the processing achieves for it.
- **Necessity:** why the processing is needed, the less intrusive options and why each was or wasn't chosen, and what data is left out.
- **Balancing:** whose data, any relationship, reasonable expectations, vulnerability, and each impact with its likelihood and severity. The outcome stays `open` while a fact that decides it is unknown.
- **Safeguards and objection:** how people object, and whether direct marketing makes the right absolute. Say plainly that processing stops on objection when it's marketing.

Ask for evidence that less intrusive options fall short, and give each impact its basis. Don't decide a test from the requester's confidence. "Marketing is sure prospects expect it" is a stated view, not evidence; ask what the people were told.

### 4. Ask for the gaps

Round 1 asks only the facts that block approval, five at most: usually how the data was obtained, what the people were told, and whether a less intrusive option would work.

### 5. Validate, render, and link

Before validating: mark an action `block_reason: law` only when a provision requires that action, and cite it in `scope` (`gov validate` rejects a law block without one); gathering facts, verifying a point, or getting counsel's view is `risk` or `policy`, even when the question behind it is legal; a DPIA is `law` only once screening finds likely high risk or a national Art. 35(4) list names the processing, so until then the action is the screening; a notice the law requires at collection (Art. 13 or 14) is `law`; a RoPA entry, a vendor review, and vendor terms beyond Art. 28 are `policy`; give each verify flag its own resolution; and when no RoPA entry exists, add an action to create one rather than leaving it as a question. Run `gov validate`, fix errors, and resolve findings by changing the record. Report any you can't resolve in your reply; don't add a `finding_responses` entry yourself, because only a person decides a finding doesn't apply. Validation checks structure and consistency, not legal correctness. Run `gov render`. Then add `{assessment: lia, status: on-file, record: <LIA ID>}` to the RoPA entry's `assessments`, and rerun `gov validate` and `gov render`.

### 6. Hand back

The privacy lead decides whether legitimate interests holds (`approvals.md`). Reply in 150 words at most in total, however many records, plus the Round 1 questions: the record's path and ID, the decision and why it's open or proposed, what blocks launch, and the decisions needed. Point to counsel for e-marketing consent rules, which neither legitimate interests nor compatibility settles. Use wording that fits the kind: a compatibility assessment isn't an LIA. For a new purpose, keep compatibility, the lawful basis, and marketing channel rules apart, and say which one blocks it.

Open with a one-line answer the requester can act on, such as "Not as proposed: logging all typed content fails necessity" or "Not yet: two facts decide it", and the less intrusive way to reach the same goal if there is one. The record holds the full reasoning; the reply is the decision-oriented summary of it. Take counts of tests, questions, and findings from the rendered record, not your own tally, and say they come from `gov`. Give launch blockers grouped by reason, as the record's Launch line does. Give a date only when the request, a contract, or the law sets it; the record's due dates are proposals. A provisional answer names the design or fact it rests on.
