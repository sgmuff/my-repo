---
name: dpia
description: Screen and write a data protection impact assessment (DPIA) for a processing activity, from GDPR Article 35 screening to a draft with a fact register, risk register, action plan, and approval routing, folding in US state data protection assessments, CPPA risk assessments, and FERPA. Also produces processor assistance packs for customers' own DPIAs. Use it whenever someone asks whether a feature, product change, process, or data use needs a DPIA, PIA, privacy impact or risk assessment, or state data protection assessment, or asks for one to be written, updated, or rescreened, even without saying "DPIA." Triggers include Article 35 or 36, prior consultation, high-risk processing, customers asking for DPIA input, and Colorado, Virginia, or CPPA assessments. Not for vendor or DPA reviews (vendor-review), AI fairness or oversight assessments and FRIAs (ai-impact-assessment), RoPA entries (ropa), legitimate interests or compatibility assessments (lia), or transfer impact assessments (tia).
compatibility: Requires the gov command from this repository (skills/install.sh installs it), with Python 3.10+, PyYAML, jsonschema, and Jinja2.
---

# Data protection impact assessment

This skill answers whether a processing activity needs a DPIA, and if it does, assesses it. It records the answer as two YAML records, rendered to Markdown in a fixed format: a screening record (`scr`) for every activity screened, and a DPIA (`dpia`) when screening finds one warranted or recommended. A processor assistance pack for a customer's own DPIA stays a Markdown document.

**Answer first, then record.** The legal analysis is yours, as full and as careful as you would give without this skill. The records capture it; they don't shape it. Never write or edit a record's `.md` file; `gov` writes it.

**The assessment proposes; the approvers decide.** Take a position on each point, cite the provision, and say how settled it is. Determinations, risk acceptance, and launch belong to the approvers in `approvals.md`. A document that resolves legal questions confidently while key facts are unknown isn't defensible, however good its analysis.

## Files

| File | Read it when |
|---|---|
| [`references/screening.md`](references/screening.md) | Step 3: territorial scope, Art. 35(3), the EDPB criteria, national lists, UK, Swiss, US state, FERPA, and AI Act screening |
| [`references/intake.md`](references/intake.md) | Step 2: the questions, tagged Round 1 (blockers) and Round 2 (completion) |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md) | Steps 3 and 4: scope, roles, lawful bases, Art. 9, Art. 22, transfers, prior consultation (§10) |
| [`../_shared/references/risk-method.md`](../_shared/references/risk-method.md) | Step 4: the matrix, the three ratings, the catalog, and mitigations |
| [`../_shared/references/us-state-privacy.md`](../_shared/references/us-state-privacy.md), [`ferpa.md`](../_shared/references/ferpa.md), [`eu-ai-act.md`](../_shared/references/eu-ai-act.md) | Step 4, for the other regimes the activity touches |
| [`references/assistance-pack.md`](references/assistance-pack.md) and [`assets/dpia-template.md`](assets/dpia-template.md) | Only when the company is the processor |
| [`../_shared/conventions.md`](../_shared/conventions.md) and [`../_shared/approvals.md`](../_shared/approvals.md) | Steps 5 and 7 |

## Workflow

### 1. Check the tool, the roles, and what already exists

Run `gov --version`; if it fails, stop and tell the user to run `skills/install.sh`. Look under `compliance/assessments/dpia/` and `compliance/registers/ropa/` for an existing screening, DPIA, or RoPA entry for the activity; if one exists, this is an update (below).

Propose the roles operation by operation, from the facts, not the contract (`gdpr.md`, §2), each Provisional:

- **Controller or joint controller:** the company owns the screening and the DPIA.
- **Processor:** the customer owns the DPIA. Produce an assistance pack under Art. 28(3)(f) with `references/assistance-pack.md` and `assets/dpia-template.md`, and no `scr` or `dpia` record.
- **Both:** assess the controller operations; give the processor operations their own assistance pack, or leave them out of scope and say so.
- **FERPA school official:** the institution stays responsible under FERPA. Assess the company's own processing, and record the exception and its limits (`ferpa.md`, §3-4).

A related operation where the company is controller, such as training its own model on customer data, is a separate workstream. Name it, and add an action to assess it.

**If processing has already started,** including a pilot on real data, deal with what exists first: what was captured, where it went, and containment (pause capture, restrict access, delete, keep data out of model pipelines). A future launch gate doesn't address data already collected.

### 2. Get the facts that decide it

If a RoPA entry exists, run `gov screen <RoPA record>` for the criteria its facts suggest; it never concludes. Ask the Round 1 questions in `references/intake.md` that could change the screening outcome, a legal determination, or launch, as one short numbered list. Ask for evidence, not only answers: the DPA, the retention and training settings, the subprocessor list. If the user can't answer, carry on with `TBC`; never invent a fact, vendor setting, retention period, or control.

### 3. Answer the screening question

Answer it fully before you open a template, then check your answer against `references/screening.md` and add what you missed. Points answers often miss:

- Where the data subjects live doesn't settle whether the GDPR applies; check establishment and targeting first (`gdpr.md`, §1a).
- The EDPB criteria are indicators, not triggers: two or more need a DPIA in most cases, not always, and one severe criterion can be enough. Say which facts behind each are confirmed.
- Check the lead authority's Art. 35(4) list, not only the criteria. Until that list has been checked against its source, record the national-list row as `unclear` with a verify flag.
- Use the three outcomes as they are. Where no Art. 35 duty applies but the risk is high (a US-only activity, say), choose warranted or recommended and say why in `analysis`.
- A US state assessment can be owed when the GDPR outcome is "not indicated."
- For an AI system, screen Art. 5 prohibitions now, since they already apply, and name any separate AI impact assessment or FRIA (`ai-impact-assessment`).

Record it with `gov new scr --slug <slug> --title "<activity>" --date <today>`, filling in all nine criteria from your answer and the reasoning in `analysis` (400 words at most). List each fact the screening relies on in `facts` (F1, F2), with its status and source, and cite the fact IDs in the criteria. If the outcome is not indicated, go to step 5.

### 4. Answer the assessment

Answer it fully, then check against `gdpr.md` (§3-6, §10), `risk-method.md`, and the regime files, and add what you missed. The suite's rules on top of the law:

- **Linked records, not inline tests.** For legitimate interests, link the LIA or run `lia`; for transfers, link the TIA or transfer screen (TSR) from `tia`. If the linked record doesn't exist yet, add an open action to produce it.
- **Profiling and Art. 22 are two analyses.** Retention needs a purpose, not a vendor default. Rights reach backups, logs, and model weights.
- **Three levels per risk** (typically 5 to 12 risks): inherent; current, counting verified measures only; and target, adding the planned ones. A planned measure never lowers the current level. Name the evidence that would verify each planned measure.
- **Prior consultation is decided on Art. 36(1)'s test:** whether the DPIA shows a high risk that the controller's measures don't mitigate. A current High rating prompts that decision; it isn't the answer. If only the target falls below High, consultation can be ruled out only once the target is verified.
- **Other regimes separately:** whether the law applies to the company, then whether this activity triggers it.

Record it with `gov new dpia --slug <slug> --title "<activity>" --date <today>`, with `screening` set to the screening record's ID and the same fact register. Use `kind: us-assessment` when the GDPR doesn't apply and the record is a US state or CPPA assessment. Give likelihood and severity, never ratings: `gov` computes every rating and names the approver from the current one. Each call stays Provisional. A point that doesn't fit a field goes in `analysis`; the record never changes your conclusion. Add a verify flag for each point you can't check against a source.

### 5. Validate and render

Mark an action `block_reason: law` only when a provision requires that action before processing, and cite it in `scope`. Gathering facts, verifying a point, or getting counsel's view is `risk` or `policy`. Run `gov validate`, fix errors, and resolve findings by changing the record. A finding that names a real gap, such as no Art. 9 condition yet, stays open with a launch-blocking action; that's the record telling the truth, not a failure. For each issue it raises, if any, record in `issues` how your answer deals with it. If `gov` raises a point your answer missed, deal with it in the answer too. Don't add a `finding_responses` entry yourself; only a person decides a finding doesn't apply. Run `gov render`, add the records to the RoPA entry's `assessments` if one exists, and rerun both.

### 6. Offer follow-through

If Jira or ServiceNow is connected, offer to create one issue per action, launch blockers first, once the user confirms the list. Never create calendar events.

### 7. Reply

Send the answer from steps 3 and 4, as you amended it, to the requester: in plain English, as long as the answer needs and no longer. Lead with the outcome (whether a DPIA is needed, and if so the current and target residual risk and whether prior consultation applies), then what has to happen before launch, grouped as legal requirements, risks, and internal policy, and the questions, five at most, that would change the answer. Say who has to approve, from `approvals.md`. Keep the records out of the reply: no record or action IDs, field names, or counts of findings and flags, apart from one closing line naming the records and their paths.

## Updating an existing DPIA

When something changes (a new vendor, data category, region, model, or incident), rescreen against the change: update the `scr` record, then the `dpia` record's affected rows. Measures whose actions closed with evidence move to `verified`, which lowers the current level. Add a version history row, bump the version, and reset the status to Draft. GDPR Art. 35(11) requires a review whenever the risk changes; California requires an update within 45 days of a material change. `gov validate` flags any reference the DPIA cites that has been re-verified or fallen due since.

A DPIA from before the record format is a Markdown file in the same folder. Leave it as it is; when it next needs an update, write the update as new `scr` and `dpia` records and note the old file in `analysis`.
