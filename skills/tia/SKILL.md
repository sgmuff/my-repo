---
name: tia
description: Write a transfer impact assessment (TIA) for personal data leaving the EEA, UK, or Switzerland under SCCs or BCRs, a UK transfer risk assessment under the IDTA or UK Addendum, or a Swiss transfer assessment, in the six EDPB steps, and screen first whether one is needed at all. Use it whenever someone sends or lets someone access data from outside Europe, asks "is it OK to send data to the US after Schrems II," mentions transfer risk, SCCs, or a vendor's support team abroad, or `gov required` or triage lists a TIA or transfer screening, even if they don't say "TIA." Not for reviewing a vendor's whole contract (vendor-review), checking a TIA a vendor sent as part of its review (vendor-review), or the DPIA (dpia).
compatibility: Requires the gov command from this repository (skills/install.sh installs it), with Python 3.9+, PyYAML, jsonschema, and Jinja2.
---

# Transfer impact assessments

This skill decides whether a transfer needs an assessment, and writes it in the six steps of EDPB Recommendations 01/2020. The output is one YAML record per transfer flow, rendered to Markdown in a fixed format.

**You fill in the record; `gov` writes the document.** Every TIA renders the same steps in the same order, so a regulator can read any of them the same way. Never write or edit the `.md` file.

**Foreign law is volatile, and the record must say so.** Each finding about the destination's law cites a source and carries a verify flag. Step 3 asks what can reach *this* importer and *this* data, not what a country's law says in general.

## Files

| File | Read it when |
|---|---|
| [`references/steps.md`](references/steps.md) | Always: when a TIA is needed, the six steps, and US points to check |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md) | Section 11 for mechanisms, adequacy, and the DPF |
| [`../_shared/conventions.md`](../_shared/conventions.md) | At the start of every run |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 6 |

## Workflow

### 1. Check the tool and screen the transfer

Run `gov --version`; if it fails, stop and tell the user to run `skills/install.sh`.

Screen before assessing. A restricted transfer exists when a regime applies and data is stored in, or accessed from, a country without adequacy. Where the data subjects live doesn't settle it. If an adequacy decision covers the destination, or a DPF certification covers this importer's exact entity and this data, no TIA is needed: say so, with the source and date you checked, and stop. A vendor's US headquarters is a reason to screen, not a finding.

### 2. Start the record

One record per flow: one exporter, one importer, one tool. Run `gov new tia --slug <short-slug> --title "<importer and flow>" --date <today>`, and set `kind`: `eu-tia` (SCCs or BCRs), `uk-tra` (IDTA or UK Addendum), or `ch-tia` (Swiss SCCs).

### 3. Work through the six steps

Follow `references/steps.md`:

1. **The transfer:** data, people, purpose, stored or remote access, and onward transfers.
2. **The tool:** the SCC module, and the date you checked adequacy and the DPF list.
3. **The destination's law and practice:** each law that could reach this importer, whether it can, and the importer's own evidence, such as transparency reports. Cite a source for each, and add a verify flag.
4. **Supplementary measures:** technical, contractual, or organizational, each with whether it works against what step 3 found. Only technical measures stop access the law compels.
5. **Procedural steps:** whether the tool is signed, and what's left.
6. **Reassessment:** the triggers for looking again.

The decision stays `open` while step 3 is open. If nothing makes the protection essentially equivalent, propose `suspend`.

### 4. Ask for the gaps

Round 1 asks only what blocks approval, five at most, in the order that changes the decision: what the importer's staff can actually see, which measures can reduce that, the importer's legal and service profile, where the data is stored and accessed from with its sub-processors, and its record of government access requests. Ask the vendor review for these where one exists.

### 5. Validate, render, and link

Before validating: mark an action `block_reason: law` only when a provision requires that action, and cite it; gathering facts, verifying a point, or getting counsel's view is `risk` or `policy`, even when the question behind it is legal; a DPIA is `law` only once screening finds likely high risk or a national Art. 35(4) list names the processing, so until then the action is the screening; a RoPA entry and vendor terms beyond Art. 28 are `policy`; give each verify flag its own resolution; and when no RoPA entry exists, add an action to create one rather than leaving it as a question. Run `gov validate`, fix errors, and resolve findings by changing the record. Report any you can't resolve in your reply; don't add a `finding_responses` entry yourself, because only a person decides a finding doesn't apply. Validation checks structure and consistency, not legal correctness. Run `gov render`. Then add `{assessment: tia, status: on-file, record: <TIA ID>}` (or `uk-transfer-risk-assessment`, `swiss-transfer-assessment`) to the RoPA entry's `assessments`, and rerun `gov validate` and `gov render`.

### 6. Hand back

The privacy lead decides the transfer mechanism and supplementary measures (`approvals.md`). Reply in 150 words at most, plus the Round 1 questions: the record's path and ID, whether a TIA was needed, the decision and why it's open or proposed, what blocks launch, and the decisions needed.

Open with a one-line answer the requester can act on, such as "No TIA needed if the certification covers this entity" or "Not yet: step 3 needs the vendor's facts", and any safer design, such as keeping sensitive tickets in the EEA. The record holds the full reasoning; the reply is the decision-oriented summary of it. Take counts of tests, questions, and findings from the rendered record, not your own tally.
