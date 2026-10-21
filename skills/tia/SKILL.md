---
name: tia
description: Answer whether a transfer of personal data needs safeguards, and record it as a transfer screen or a transfer impact assessment (TIA) for personal data leaving the EEA, UK, or Switzerland under SCCs or BCRs, a UK transfer risk assessment under the IDTA or UK Addendum, or a Swiss transfer assessment, in the six EDPB steps, and screen first whether one is needed at all. Use it whenever someone sends or lets someone access data from outside Europe, asks "is it OK to send data to the US after Schrems II," mentions transfer risk, SCCs, or a vendor's support team abroad, or `gov required` or triage lists a TIA or transfer screening, even if they don't say "TIA." Not for reviewing a vendor's whole contract (vendor-review), checking a TIA a vendor sent as part of its review (vendor-review), the DPIA (dpia), whether a transfer framework still stands (regulatory-change), or a general question about transfer law, such as which SCC module fits or which countries have adequacy, with no specific transfer to assess.
compatibility: Requires the gov command from this repository (skills/install.sh installs it), with Python 3.10+, PyYAML, jsonschema, and Jinja2.
---

# Transfer impact assessments

This skill answers a question about a transfer of personal data out of the EEA, the UK, or Switzerland, and records the answer: a transfer screen when no assessment is needed, or an assessment in the six EDPB steps when one is. Each record is one YAML file, rendered to Markdown in a fixed format.

**Answer first, then record.** The legal analysis is yours, as full and as careful as you would give without this skill. The record captures it; it doesn't shape it. Never write or edit the `.md` file; `gov` writes it.

**The assessment proposes; the privacy lead decides.** Give a provisional view on every answer, and never present a transfer as cleared, or a risk as rated, before the facts that decide it are known. Destination law is volatile: mark what you can't check against a source as a point to verify.

## Files

| File | Read it when |
|---|---|
| [`references/steps.md`](references/steps.md) | Step 2, to check your answer for gaps |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md) | Section 11 for mechanisms, adequacy, and the DPF |
| [`../_shared/conventions.md`](../_shared/conventions.md) | Step 3 |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 5 |

## Workflow

### 1. Check the tool

Run `gov --version`; if it fails, stop and tell the user to run `skills/install.sh`.

### 2. Answer the question

Answer the request as a careful privacy lawyer would, before you open any template: which flows are transfers and which aren't (remote access counts; where the people live doesn't settle it), the mechanism for each, whether an adequacy decision or a certification covers it, what the destination's law and practice mean for this importer and this data, which measures would actually work, what the interim position is if the transfer is already running, and your provisional view with the facts that would change it. Write it in whatever form fits the question. Then read `references/steps.md` and add anything your answer missed; don't cut what it already covers.

### 3. Record it

If your answer finds that adequacy or a certification covers a flow, record it as a screen: `gov new tsr --slug <short-slug> --title "<importer and flow>" --date <today>`. For a flow that needs an assessment, run `gov new tia` with the same arguments and set `kind`: `eu-tia` (SCCs or BCRs), `uk-tra` (IDTA or UK Addendum), or `ch-tia` (Swiss SCCs). One record per flow. Set `context` to every tag in `gov/rules/issues.yaml` that fits the facts.

Fill in the record from your answer. Put its reasoning in `analysis`, condensed to 400 words, and each step's findings in the step's fields, with what the request stated recorded as a stated source. Each call stays Provisional, and the decision stays `open` while step 3 is open; propose `suspend` where no measure makes the protection essentially equivalent. If a point doesn't fit a field, it goes in `analysis`; the record never changes your conclusion. Add a verify flag for each point to verify.

### 4. Validate and render

Before validating: mark an action `block_reason: law` only when a provision requires that action, and cite it in `scope` (`gov validate` rejects a law block without one). Gathering facts, verifying a point, or getting counsel's view is `risk` or `policy`. A DPIA is `law` only once screening finds likely high risk or a national Art. 35(4) list names the processing; a notice the law requires at collection (Art. 13 or 14) is `law`; a RoPA entry, a vendor review, and vendor terms beyond Art. 28 are `policy`. When no RoPA entry exists, add an action to create one. Run `gov validate`, fix errors, and resolve findings by changing the record. For each issue it raises, record in `issues` how your answer deals with it: `addressed` with the conclusion, `not-applicable` with why, or `open` with what's needed. If `gov` raises an issue your answer missed, deal with it in the answer too. Don't add a `finding_responses` entry yourself; only a person decides a finding doesn't apply. Validation checks structure and consistency, not legal correctness. Run `gov render`, then add the record to the RoPA entry's `assessments` if one exists, and rerun `gov validate` and `gov render`.

### 5. Reply

The privacy lead decides the transfer mechanism and supplementary measures (`approvals.md`). Send the answer from step 2, as you amended it, to the requester: in plain English, as long as the answer needs and no longer. Say what has to happen before launch in ordinary words, grouped as legal requirements, risks, and internal policy, and ask the questions, five at most, that would change the answer. Give a date only when the request, a contract, or the law sets it. Keep the record out of the reply: no record or action IDs, field names, or counts of findings and flags, apart from one closing line naming the record and its path, such as "Recorded as LIA-2026-004 in compliance/assessments/lia/." The record holds the rest for the privacy lead. If the transfer is already running, say so first, with the privacy lead's interim choice: continue under named measures while the assessment finishes, or suspend.
