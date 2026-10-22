---
title: Privacy and AI governance suite plan
status: Draft
author: SteveM
date: 2026-10-17
---

# Privacy and AI governance suite plan: required assessments and a deterministic pipeline

## Summary

The plan makes three changes:

1. **Cover every required assessment.** Add `lia`, `tia`, `ai-act-provider`, and `ai-act-deployer`, and a catalog of which assessment each law requires, who owes it, and what triggers it.
2. **Make assessments short and fixed.** Each contains only what its law requires and a regulator checks, in one format per type.
3. **Move bookkeeping into code.** A tool, `gov`, owns IDs, routing, required assessments, validation, and rendering. The model extracts facts and writes short prose fields.

With the same inputs, the suite produces the same records, IDs, deadlines, required assessments, step order, and documents. Only the wording of prose fields varies.

## Background

The suite has 14 skills, shared references, and nine workflow scripts. Records go under `compliance/`, which doesn't exist yet, so nothing needs migrating.

**Coverage gaps.** Templates ask whether an LIA or TIA is "on file," but no skill writes one. Nothing covers the AI Act's provider duties or the deployer duties in Art. 26.

**Nondeterminism.**

1. The triage skill builds each plan from a prose list.
2. The model assigns IDs by counting files (`conventions.md` section 9).
3. Three copies of a hand-rolled parser drop YAML lists and misread nested values.
4. `gov metrics` scrapes Markdown tables, so a format change breaks it silently.
5. No schema or cross-reference check exists. The model checks its own work.

The date scripts already work the right way: the model supplies facts, and code computes the answer.

## Goals and non-goals

**Goals:**

- Every required assessment has a catalog entry, a skill, and a record type.
- The same facts always produce the same results.
- Every record validates, and every cross-reference resolves.
- No activity passes In review while it owes an assessment.
- Every assessment of a type has the same format, and every section cites a requirement.

**Non-goals:**

- **Automated legal judgment.** Rules propose, a person confirms, and coded results stay Provisional.
- **Third-party work.** The suite prepares for notified bodies and independent auditors but doesn't replace them.
- **Claude Desktop.** It keeps no edits, so it can't hold registers or counters.

## Required assessments

### Catalog

`gov/rules/assessments.yaml` lists each assessment once. The skills read it through `gov`, so one edit changes the answer everywhere.

| Assessment | Law | Owed by | Trigger | Skill | Status |
|---|---|---|---|---|---|
| DPIA | GDPR and UK GDPR Art. 35; FADP Art. 22 | Controller | Likely high risk | `dpia` | Exists |
| Prior consultation | GDPR Art. 36; FADP Art. 23 | Controller | High residual risk | `dpia` | Exists |
| State data protection assessment | US state laws | Controller | Targeted ads, sale, profiling, sensitive data, known minors | `dpia` | Exists; add minors |
| CPPA risk assessment | 11 CCR § 7150 | Business | `us-state-privacy.md` section 6 | `dpia` | Exists |
| LIA | GDPR and UK GDPR Art. 6(1)(f), 5(2) | Controller | Legitimate interests as lawful basis | `lia` | New |
| Compatibility assessment | GDPR and UK GDPR Art. 6(4) | Controller | Reuse for a new purpose | `lia` | New |
| TIA | 2021 SCCs Clause 14; EDPB Recs. 01/2020 | Exporter | Transfer under SCCs or BCRs | `tia` | New |
| UK transfer risk assessment | UK GDPR Art. 46; DUAA test once commenced | Exporter | Transfer under IDTA or Addendum | `tia` | New |
| Swiss transfer assessment | FADP Art. 16 | Exporter | Transfer under Swiss SCCs | `tia` | New |
| Security risk assessment | GDPR Art. 32 | Controller, processor | Any processing | `controls-and-evidence` | New |
| CCPA cybersecurity audit prep | CCPA regulations | Business | Significant security risk; first due 2028–2030 | `controls-and-evidence` | New |
| COPPA security program assessment | 16 CFR Part 312 (2025) | Operator | Users under 13 | `controls-and-evidence` | New |
| Student data security and privacy plan | NY Educ. Law § 2-d | Contractor | New York school contract | `controls-and-evidence` | New |
| Prohibited practice screening | AI Act Art. 5 | Provider, deployer | Any AI system | `ai-intake` | Exists |
| Provider role check | AI Act Art. 25 | Deployer | Rebrand, substantial change, new high-risk use | `ai-intake` | New |
| Non-high-risk documentation | AI Act Art. 6(4) | Provider | Annex III system claimed not high-risk | `ai-act-provider` | New |
| Risk management system | AI Act Art. 9 | Provider | High-risk system | `ai-act-provider` | New |
| Data governance | AI Act Art. 10 | Provider | High-risk system | `ai-act-provider` | New |
| Conformity assessment readiness | AI Act Art. 43, Annex IV | Provider | High-risk system | `ai-act-provider` | New |
| Post-market monitoring plan | AI Act Art. 72 | Provider | High-risk system | `ai-act-provider` | New |
| Deployer duties check | AI Act Art. 26 | Deployer | High-risk system | `ai-act-deployer` | New |
| FRIA | AI Act Art. 27 | Certain deployers | Art. 27(1) deployer types | `ai-impact-assessment` | Exists |
| AI impact assessment | AIUC-1, NIST AI RMF, ISO/IEC 42001 | Company policy | Tier High or Elevated | `ai-impact-assessment` | Exists |
| Bias audit prep | NYC Local Law 144 | Employer | Hiring tool used in NYC | `ai-impact-assessment` | Partial |

Verify the COPPA program's risk assessment and frequency before building; `ferpa.md` flags the provision. Art. 32 names no assessment, but its "appropriate to the risk" test implies one, which the entry records.

**Conditional entries** stay off until a fact in `company-profile.md` turns them on. None has a reference file yet.

| Assessment | Law | Turned on when the company |
|---|---|---|
| Security risk analysis | HIPAA, 45 CFR § 164.308(a)(1) | Is a covered entity or business associate |
| Written risk assessment | GLBA Safeguards Rule, 16 CFR § 314.4(b) | Serves financial institutions, such as colleges in federal student aid |
| Cybersecurity risk management | NIS2 Art. 21 | Is an essential or important entity |
| Privacy impact assessments | Quebec Law 25 | Processes data of people in Quebec |
| GPAI duties | AI Act Art. 53, 55 | Trains or markets general-purpose models |

**Left out:** laws with no assessment duty, such as Colorado SB 26-189, which dropped the Colorado AI Act's impact assessments. `regulatory-change` proposes catalog edits when laws change.

A catalog entry:

```yaml
- id: tia
  citation: "2021 SCCs Clause 14; EDPB Recommendations 01/2020"
  owed_by: data-exporter
  triggers: {all: {restricted_transfer: yes, transfer_mechanism: [sccs, bcrs]}}
  applies_from: 2021-06-27
  produced_by: tia
  required_content:
    - {key: transfer_map, cite: "Recs. 01/2020 step 1"}
    - {key: mechanism, cite: "step 2"}
    - {key: destination_law, cite: "step 3"}
    - {key: supplementary_measures, cite: "step 4"}
    - {key: procedural_steps, cite: "step 5"}
    - {key: reassessment, cite: "step 6"}
  word_budget: 800
```

### What an activity owes

`gov required <record> --as-of <date>` evaluates the catalog and writes the result into the record:

```yaml
required_assessments:
  - {assessment: dpia, status: on-file, record: DPIA-2026-004}
  - {assessment: lia, status: owed, reason: "lawful_basis = legitimate_interests (P2)"}
  - {assessment: tia, status: tbc, open_fact: transfer_mechanism}
```

Statuses are `owed`, `on-file`, `tbc`, `not-applicable`, and `not-yet-applicable`, each with a reason. `gov validate` blocks In review while anything is `owed` or `tbc`. Only a person can mark an entry not applicable, and the approval record names them.

### New and extended skills

| Skill | Writes | Hands off to |
|---|---|---|
| `lia` | LIA (purpose, necessity, balance; UK recognized interests) and Art. 6(4) compatibility assessments | `dpia` for Art. 9 conditions |
| `tia` | TIAs in the six EDPB steps, with UK and Swiss variants; a verify flag on every finding about a country's law | `vendor-review` and `dpia` link to it |
| `ai-act-provider` | Provider files for Art. 6(4), 9, 10, 43, and 72 | `ai-impact-assessment` for fairness and FRIAs |
| `ai-act-deployer` | The deployer's Art. 26 duties, and evidence of the provider's compliance | `ai-impact-assessment` for fairness and FRIAs |
| `controls-and-evidence` | Adds the four security entries | |
| `ai-intake` | Adds the Art. 25 provider role check | |

The privacy lead approves LIA and TIA outcomes. Provider files need the privacy lead and product owner; deployer files need the privacy lead and business owner, and a declaration of conformity needs the provider's authorized signatory.

## Assessment format

Current templates read like books: the blank DPIA runs 1,629 words over 12 sections. Every extra page slows a regulator's answer to four questions: what was assessed, what risks were found, what was done, and who decided. It also adds statements the company must stand behind.

**Rules for every assessment:**

1. **Every section cites a requirement.** A section with none goes.
2. **The decision comes first:** outcome, residual risk, conditions, launch blockers, and approver.
3. **Tables over prose,** one line per row.
4. **Cite the law; don't restate it.**
5. **Show gaps plainly,** each with an owner, and never claim compliance the record can't show.

**Rules that fix the format per type:**

1. **The model never writes Markdown.** It fills in the YAML record, and `gov render` builds the document from the type's template.
2. **Every section always appears.** A section that doesn't apply prints "Not applicable: <reason>."
3. **Columns and row order are fixed.**
4. **Set phrases come from fixed value lists,** such as `rating: Low | Medium | High`.
5. **Prose fields have word limits,** such as 40 words for a risk rationale.

`gov render --check` fails CI on any hand edit. A golden test per type catches format changes, which happen only through a reviewed `format_version` that re-renders every record of the type. Registers, actions, and version history live in the record and print as a generated appendix.

**Concision checks.** AI drafts run long, so code holds the line:

- `gov validate` rejects a prose field over its limit and warns when a document passes its word budget.
- It flags filler from the `writing-style` banned list and sentences that restate a cited article.
- Skill evals assert that every document is within budget.

**Example: the DPIA.**

| Section | Requirement | Form |
|---|---|---|
| Header | GDPR Art. 5(2), 24 | ID, activity, owner, status, approver, review date |
| Decision | Art. 35(7)(d), 36(1) | Five lines |
| Processing | Art. 35(7)(a) | One table |
| Necessity and proportionality | Art. 35(7)(b) | One table: principle, position, basis, gap |
| Risks and measures | Art. 35(7)(c)–(d) | One table: risk, likelihood, severity, measure, owner, residual |
| Consultation | Art. 35(2), 35(9) | Two or three lines |
| Other regimes | Triggered catalog rows | Only their extra elements |
| Sign-off and review | Art. 35(11) | One table |
| Appendix | Accountability | Facts, verify flags, actions |

**Scope.** All catalog assessments, plus the vendor review, screening record, incident assessment, and readiness report. Registers and memos follow the writing rules but keep their own shape. `conventions.md` changes to match.

## Pipeline

### Layout

```
gov/                        Python package
  schemas/                  JSON Schema per record type
  rules/                    assessments.yaml, routing.yaml
  templates/                Jinja2, one per type
tests/                      unit and golden tests
skills/                     the skills
compliance/
  .gov/counters.yaml        last ID per prefix
  registers/ropa/           ROPA-0042-gradebook-sync.yaml and .md, index.md
  assessments/              dpia/, lia/, tia/, ai-act/, ...
pyproject.toml              PyYAML, jsonschema, Jinja2
.claude-plugin/plugin.json  ships the suite as one plugin
```

Each record is one YAML file. Fields the model can't confirm hold `TBC` with a `source`. Generated Markdown sits beside its source with a do-not-edit header.

### Commands

| Command | Does |
|---|---|
| `gov next-id <prefix>` | Reserves the next ID; never reuses one |
| `gov new <type>` | Writes a skeleton with a one-line hint per field |
| `gov required <record>` | Lists owed assessments |
| `gov route <facts.yaml>` | Prints the ordered plan |
| `gov screen <record>` | Reports matched screening criteria, marked Provisional |
| `gov validate [path]` | Checks schemas, references, IDs, owed assessments, limits |
| `gov render [path]` | Builds Markdown; `--check` fails on drift |
| `gov index`, `gov metrics` | Replace `build_register_index.py` and `program_metrics.py` |
| `gov deadlines`, `gov clock` | The existing date scripts, moved in |

Commands read only files and arguments, never the clock, and list every problem before exiting nonzero.

### Routing

`routing.yaml` holds four things, and `gov route` turns a facts file into a plan and a decision register:

- **Facts,** each with its question. A child fact, such as `ai_act_role`, waits for its parent, `ai_involved`.
- **Steps,** in priority order, each with its trigger, its basis (law, internal policy, or a risk indicator), and its decision owner. `start_after` marks real data dependencies only; `finalize_after` lets a step such as the RoPA start now and settle later. DPIA screening runs for all new processing, as policy; a full DPIA is a screening outcome.
- **Checks:** legal decisions with no workflow of their own, such as Art. 14 notice for indirect collection, the Art. 21 right to object to direct marketing, cookie consent, recording consent, biometrics, and COPPA.
- **Next questions:** the three open facts that settle the most conditional steps and checks.

```yaml
steps:
  - {id: dpia-screening, skill: dpia, when: {new_processing: true}, basis: "Policy: screen all new processing"}
  - {id: transfer-screening, skill: tia, when: {cross_border_access: true}, start_after: [vendor-review]}
  - {id: ropa, skill: ropa, when: {new_processing: true}, finalize_after: [dpia-screening, vendor-review]}
checks:
  - {id: indirect-notice, when: {indirect_collection: true}, owner: Privacy lead and counsel}
```

Each step is required or conditional, starts now or after named steps, and shows when it has no skill yet. Every required step and check enters the decision register, which blocks launch until each decision is recorded. A step with no skill stays in the register, and its owner does the work by hand. The triage skill adds, below the plan, legal issues the table can't see, in a labeled section; it never edits the plan. The catalog says what is owed; the routing table says in what order.

### Stages

Intake writes `facts.yaml`, then route, required assessments, screen, draft, validate, and approve each write a file. A stage won't start without its input. Moving past In review needs a recorded approval and no owed assessments.

### Skills

*Target, not the shipped shape.* The plan proposed four steps per SKILL.md: gather facts, run `gov new`, fill in the record, and run `gov`. The record-based skills shipped with five, answer first (answer, check against the references, record, validate and render, reply), because the holdouts showed the record alone doesn't improve the analysis. Each also:

- **Says why the record comes first.** A hand-written document fails CI and breaks the shared format.
- **Declares `gov`** in a `compatibility` field, and stops with install steps if it's missing.
- **Keeps its description near 100 words.** Today's run up to 155, and the suite grows to 17 skills.

## Testing

**Code.** Unit tests, plus golden tests that pair facts with the expected route, required assessments, IDs, deadlines, and rendered document. Each catalog entry gets one fixture that triggers it and one that doesn't. CI runs `pytest`, `gov validate`, and `gov render --check`.

**Skills.** Every skill change goes through the skill-creator loop: snapshot, run old and new on the same prompts, grade, review in the eval viewer, iterate. Today's evals are thin: one to three prompts per skill, no assertions, and none at all for `privacy-governance` or `writing-style`. Each skill grows to three or more prompts, one of them messy. Most assertions become script checks:

- `gov validate` passes, and every required element is present.
- Documents stay within budget.
- Two runs give the same route, required assessments, and IDs.
- No Markdown exists without a YAML record.

The human reviewer judges the rest, such as whether a rating is sound.

**Triggering.** Each new or changed skill gets about 20 trigger prompts, half of them near-misses, followed by a description optimizer run. Descriptions use the words people type, such as "balancing test" and "Schrems II," not only "LIA" and "TIA." Likely collisions:

| Prompt | Goes to | Not to |
|---|---|---|
| "Do we need a DPIA, or is a legitimate interests check enough?" | `dpia`, then `lia` | `lia` alone |
| "The vendor sent their transfer assessment. Can you check it?" | `vendor-review` | `tia` |
| "We're sending tickets to a US contractor. Is that OK after Schrems II?" | `tia` | `vendor-review` |
| "Is our chatbot high-risk under the AI Act?" | `ai-intake` | `ai-act-deployer` |
| "We're the provider of a high-risk system. What do we need before launch?" | `ai-act-provider` | `ai-intake` |

## Delivery

### First slice

- [x] `gov` with `next-id`, `new`, `validate`, `render`, and `index`
- [x] RoPA schema and templates
- [x] `routing.yaml` and `gov route`, with golden tests
- [x] `ropa` and `privacy-governance` rewritten to call `gov`, with `compatibility` fields
- [x] `conventions.md` sections 8 and 9 updated
- [x] `plugin.json`, `install.sh` installing `gov`, and CI
- [x] Evals with assertions for both skills
- [x] Old against new compared in the eval viewer, over three reviewed rounds
- [x] Iteration 2 from review feedback: RoPA schema v2 (record-type-aware, calls with status and reason, actions, blocking questions, legal consistency findings) and router v2 (step states, decision register, legal checks, next questions)
- [x] Iteration 3: router facts and checks for school context, vendor own use, scraped sources, and session replay; one ranked question list; computed launch status, retention by store, and contract findings in the RoPA
- [x] RoPA removed from `build_register_index.py`, which still serves the AI inventory, incident, and control registers until phase 5

Done when the RoPA evals produce valid YAML, two triage runs print the same plan, the new skills match or beat the old on every eval, and CI passes.

### Phase 1: catalog, `lia`, and `tia`

- [x] Catalog in `assessments.yaml` and `gov required`, with RoPA findings for owed assessments
- [x] LIA and TIA schemas, skeletons, templates, and findings
- [x] `lia` and `tia` skills; `vendor-review` and `dpia` point to them
- [x] Reference files for the five conditional regimes, verified against secondary sources and approved by counsel on 2026-10-19
- [x] Evals against no skill, iterations 1 and 2 reviewed
- [x] Fixes from the iteration 2 review: each LIA test's result in the status line, validation findings rendered in every record, narrower `law` blocks, and the UK data protection test in force since February 5, 2026
- [x] Iteration 3 evals reviewed: `lia` 96% and `tia` 98% against 55% and 61% without the skill
- [x] Fixes from the iteration 3 review: launch blockers grouped by reason, required notices as `law`, a trail for negative transfer screens, and live transfers flagged first
- [x] Iteration 4 evals reviewed: `lia` 94% and `tia` 98% against 57% without the skill
- [x] Fixes from the iteration 4 review: `gov validate` rejects a law block without a cited provision; replies attribute counts to `gov`, group blockers by reason, and set no unsourced dates
- [x] Iteration 5 evals reviewed with records visible: `lia` 100% and `tia` 98% against 57% and 58% without the skill
- [x] Fixes from the iteration 5 review: a method line per assessment kind, `gov` findings for dropped notice, Art. 9, and transfer-tool duties, CLOUD Act and DPF onward-transfer corrections, and proportionate TIAs
- [x] Iteration 6 evals, with the mixed DPF and SCC eval
- [x] Counsel answer keys for the seven evals, and a blind comparison against them: the skills reach the expected outcome in all seven with no material errors, but trail on breadth (mean 73 against 77)
- [x] Breadth fixes: issue rules in `gov/rules/issues.yaml` raised by context tags, kind, regime, and country; reasoning fields on each test; a transfer screen record (TSR) for negative screens 
- [x] Iteration 7, scored blind against the answer keys: skill 94 against 72 for the baseline, ahead in all seven
- [x] Holdout of eight new scenarios, scored blind: the skill trails, 76 against 84, though it makes no material errors and scores higher with a regulator (4.5 against 3.1). The development gain was largely fitted to its seven scenarios.
- [x] Changes from the holdout: a 400-word analysis section in every record, written before the fields; a provisional view always; a plain-English reply for the requester; `gov` fixes for the purpose test's "both" label and country adequacy screens
- [x] Second holdout, eight scenarios with counsel-approved keys: the skill trails, 83 against 91, with the same gap as the first
- [x] Answer-first restructure: Claude answers as it would without the skill, then records it. On the second holdout, 88 against 93 with no material errors and regulator usability 4.5 against 3.9. Single runs vary by up to 10 points, so small gaps aren't reliable.
- [x] Decision: `lia` and `tia` add the record and its checks, not better legal analysis; tuning them for legal quality stops here. Replies keep record details to one closing line.
- [x] Descriptions for `lia` and `tia` reviewed by hand against their 20-query trigger sets: exclusions added for notice wording, framework news, and general transfer questions. The automated optimizer (`claude -p`) hit the usage limit, so trigger rates aren't measured yet.
- [x] `phase-1` merged to main

### Later phases

Each phase closes with skill evals, trigger evals, and a description optimizer run.

1. **Catalog, `lia`, and `tia`.** Point `vendor-review` and `dpia` at them. Add reference files for the five conditional regimes, so their entries can be switched on.
2. **`ai-act-provider` and `ai-act-deployer`,** and the Art. 25 check. Finish well before December 2, 2027. Built 2026-10-21, answer-first from the start: AIP and AID records with the required articles enforced, findings for profiling claimed as not high-risk, a deployer that has become the provider, "ready" with gaps, and an owed FRIA, plus AI Act issue rules. Counsel-approved answer keys (version 6) and blind holdout evals done 2026-10-21: 90.0 with the skill, 82.4 without, 5 wins of 8, no material errors with the skill (`docs/evals/ai-act-results.md`). Fixed after scoring: an `outside-scope` kind for provider files, and Art. 111(2) in the reference and issue rules. Still to do: the trigger-rate run. The Art. 25 check lives in the AID record; `ai-intake` still owns the catalog entry.
3. **Security entries** in `controls-and-evidence`. The first CCPA audit is due April 1, 2028 at the earliest.
4. **Existing assessments in the new format,** starting with the DPIA, plus `gov screen`.
5. **Remaining registers.**
6. ~~**Dates and metrics** moved into `gov`.~~ Done 2026-10-21: `gov clock`, `gov deadlines`, `gov schedule`, and `gov metrics` replace the four scripts. `schedule` and `metrics` take a required `--as-of`, since gov never reads the clock. `build_register_index.py` stays until phase 5 moves the remaining registers.
7. ~~**Reference files** with YAML front matter, so `regulatory-change` reads data.~~ Done 2026-10-22: every shared reference file carries front matter (dates, source quality, counsel review); `gov` checks it, fails closed on gaps, and generates the README index table.

## Decisions and assumptions

**Decided (2026-10-17):** Claude Code and CI only; PyYAML, jsonschema, and Jinja2 allowed; records in this repository; the first slice above.

**Decided (2026-10-18):** `lia` keeps its scope, covering LIAs and Art. 6(4) compatibility assessments. All five conditional entries apply: GPAI duties, the GLBA Safeguards Rule, HIPAA, NIS2, and Quebec Law 25. Each needs a reference file before its catalog entry is switched on.

**Assumed, open to change before the first slice:**

- **IDs come from a counter file** and are never reused.
- **Generated Markdown is committed** beside its source.
- **Word budgets warn rather than block,** starting at 1,500 words for a DPIA and tuned after real use.
- **The appendix stays in the document,** so a regulator gets one file.
- **`gov` sits at the repository root.**
- **The plan uses portable Markdown,** per `conventions.md`.
- **Colorado has no entry,** and `regulatory-change` watches the attorney general's ADMT rules.
- **Local Law 144 is partly covered,** since the law requires an independent auditor.
- **Counsel approved the legal content on 2026-10-19:** the `law` block rules, the UK, DPF, US, and India points in `steps.md`, the LIA test, `methods.yaml`, and the five conditional reference files. `us-breach-notification.md` is still unreviewed.
- **Counsel decided the DPIA design on 2026-10-22:** `gov screen` raises criteria only from the RoPA fields in `gov/rules/screening.yaml` and prints the rest as questions; it counts suggested criteria but never concludes (WP248: two or more "in most cases, not always"); Art. 35(4) lists go in a reference file per authority, starting with the lead authority, and a list not yet checked makes the row Unclear with a verify flag; screening keeps three outcomes (warranted, recommended, not indicated), explaining a non-GDPR high risk in `analysis`; issue rules for `scr` and `dpia` are drafted for counsel's approval; and an assistance pack's own residual risk is approved under `approvals.md`, separately from its release gate. Art. 36 is decided on its test, not on an internal High rating. The privacy lead kept the 1,500-word DPIA budget and left pre-record DPIAs as they are.

## Risks

| Risk | Mitigation |
|---|---|
| Readers treat coded outcomes as legal conclusions | Provisional status and a named confirmer |
| The catalog goes stale | Each entry cites a reference file, and `regulatory-change` sweeps both |
| The format has no place for an unusual finding | One bounded "Other findings" field per type |
| Lean assessments omit reasoning a regulator expects | The privacy lead's review judges whether each finding is explained |
| Schemas change | `schema_version` and migrations on read |
| The model writes Markdown by hand | SKILL.md explains why, an eval assertion, and CI |
| Skills collide | Near-miss trigger evals and the router |

## Open questions

1. ~~Retire or freeze the Desktop zips?~~ Retired: the zips are deleted.
2. Commit generated Markdown, or build it only for Confluence?
3. Should catalog changes need the privacy lead's approval? (Assumed yes.)
4. ~~Which conditional entries apply?~~ All five (2026-10-18).
5. ~~Keep compatibility assessments in `lia`?~~ Yes (2026-10-18).
6. Keep counsel's advice in a separate privileged memo that the assessment cites?

## Backlog (2026-10-21)

From an outside review of the repository (Lumo, via Proton), checked against the code before listing. Ordered by risk.

1. **Third-party content.** AIUC-1 is © AIUC, all rights reserved; its terms (standard.aiuc-1.com/legal/terms, checked
   2026-10-21) bar copying, distributing, or creating derivative works from its content. Done: `aiuc-1.md` §4 no longer
   quotes AIUC's requirement summaries (IDs, titles, status, and tags remain, with links to AIUC's pages), and
   `controls-and-evidence` reads requirement text from AIUC's site. Open for counsel:
   - Done 2026-10-22, on counsel's decision not to ask AIUC: git history was rewritten so no commit contains AIUC's
     quoted summaries, and main was force-pushed. Copies already cached or forked elsewhere aren't affected.
   - §5 of `aiuc-1.md` and the "AIUC coverage" column in `iso-42001.md` reproduce AIUC's published crosswalk mappings.
     These are closer to facts than to expression, but the terms reach all site content. Keep with attribution, or ask.
   - `regulatory-change` downloads AIUC's `llms.txt`, which AIUC publishes for machine reading. One fetch per release
     sits within normal use; note it if AIUC's terms change.
2. ~~**Stale references don't block.**~~ Done 2026-10-21: `gov validate` raises a finding when a cited file is past its
   "Review by" date (as of the record's own date, or `--as-of`), or was re-verified after the record cited it; the finding
   renders in the record and only a person can answer it. Original note: `gov validate` doesn't check reference review dates. Make an overdue reference that
   a record cites a validation finding, and show a banner in the rendered document.
3. ~~**Missing company facts.**~~ Done 2026-10-21: scope fields left as `TODO` give a warning while records are drafts
   and an error on an approved record (`gov/profile.py`). Original note: `gov route` doesn't read `company-profile.md`; the skills read it and ask about each `TODO`
   they need. Add a `gov` check that fails when a field that sets scope (regimes, establishments) is still `TODO`.
4. ~~**`gov clock` has no unit tests.**~~ Done 2026-10-21: `tests/test_incident_clock.py` (12 cases). The tests
   found that hour-based clocks added wall-clock time, so a 72-hour deadline across the autumn DST change printed an
   hour late; the script now counts elapsed time, rejects a local time that doesn't exist, and flags one that happens
   twice. Still open: occurrence versus awareness is the user's input, not the script's, and isn't tested.
5. **Router judgment isn't graded.** Started 2026-10-21: six draft holdout scenarios in `docs/evals/router-scenarios.yaml`,
   waiting for counsel's keys. Original note: `privacy-governance` has assertion and trigger evals but no counsel-approved answer
   keys. Build a small keyed holdout for the issues the router adds beyond `gov route`.
6. ~~**README vocabulary.**~~ Done 2026-10-21. Original note: The skill list mixes "Wave" and "suite phase". Use one scheme, and say which skills are shipped.
7. ~~**Contributor path for reference files.**~~ Done 2026-10-21: "Contributing a reference update" in
   `skills/_shared/references/README.md`. Original note: Document the header format, the review-date procedure, and the test to run,
   so updating a reference file doesn't need knowledge of `assessments.yaml`.

## Remaining roadmap (agreed 2026-10-22)

Five milestones to finish the buildout. Each ends tested and pushed. Order: 1, 2, 3, 4, 5; milestones 2 and 4 need nothing
from counsel and can run while counsel reviews.

| # | Milestone | Work | Needs from counsel | Done when |
|---|---|---|---|---|
| 1 | Close out the DPIA (phase 4) | Verify the DPIA keys' `verify` points; draft issue rules for `scr` and `dpia`; run the DPIA and router holdouts blind and fix what they show | Router key review; DPIA key sign-off; approval of the issue rules | Both holdouts scored and recorded, as for the AI Act |
| 2 | ~~Reference files as data (phase 7)~~ Done 2026-10-22 | YAML front matter on every reference file (version, last verified, review by, source quality, counsel review); gov reads it and generates the README table; `regulatory-change` reads it | Nothing | The staleness and source-quality checks read front matter; the table parser is gone |
| 3 | ~~Remaining assessments as records~~ Done 2026-10-22: `vr`, `aiia` (with FRIAs), `inc`, and `rdy`, each with a development run | Record type, answer-first rewrite, development run, and fixes for `vendor-review`, `ai-impact-assessment` (with the FRIA), `incident-assessment`, and the AIUC-1 readiness report | The rest of `us-breach-notification.md` before live incident use; keys for any holdout | Every catalog assessment is a `gov` record |
| 4 | ~~Remaining registers (phase 5)~~ Done 2026-10-22: `ais` (with two development runs), `ctl` with evidence items and crosswalk coverage, and `dsr` with computed deadlines; `build_register_index.py` and `new_control.py` retired; `gov metrics` and `gov schedule` read records; the leadership-report fixtures are records | AI inventory, controls, incidents, and DSR cases as records; retire `build_register_index.py`; `gov metrics` reads records | Nothing | No script scrapes Markdown tables |
| 5 | Release | Trigger evals for every skill and description tuning; security entries in `controls-and-evidence` (phase 3); a 1.0 tag, a changelog, a check that the plugin install reaches `gov`, and an accurate README status | Removing the old claude.ai skill copies | Every skill triggers reliably; the README matches what ships |

Estimate: eight to nine working sessions, with elapsed time set mostly by counsel's reviews.

Gaps found in development runs, for a reference update: whether public school districts notify under the private-sector breach statutes or their own (NY State Technology Law § 208, Cal. Civ. Code § 1798.29), 8 NYCRR 121.10 district deadlines, and whether IEP or disability status is medical information, in `us-breach-notification.md` and `ferpa.md`; employment AI laws (NYC Local Law 144 bias audits, Illinois HB 3773, California's FEHA automated-decision rules, Colorado) and the federal anti-discrimination baseline have no reference file; `gov required` assigns LL144 audit preparation to `ai-impact-assessment` without guidance behind it. From the AI intake runs (2026-10-22): no COPPA reference file, though several files cite it; no US bot-disclosure or impersonation law (California B.O.T. Act, SB 243, FTC Act § 5 and the impersonation rule); `eu-ai-act.md` doesn't address a human persona the deployer configures under Art. 50(1), whether external guests in an employee's meeting fall within the Art. 5(1)(f) workplace prohibition, or whether "engagement" or "attention" is an emotion or intention; no national employment-monitoring law (BetrVG § 87(1) no. 6, the French Code du travail L1222-4 and L2312-38, BDSG § 26 after CJEU C-34/21); no US biometric, monitoring-notice, or recording-consent laws (BIPA, CUBI, NY Civil Rights Law § 52-c, all-party consent states); no EU consumer law for the Art. 22 "legal effect" of a support agent's refund or return answers; no children's design codes or age assurance; no guidance on authenticating agent actions such as password resets. `eu-ai-act.md` front matter says last verified 2026-10-16 while §4 records a check on 2026-10-21. The `ais` record type has no issue rules yet; drafting them (Art. 50, Art. 22, COPPA and minors, works councils, biometrics) needs counsel's approval like the others.

Open with counsel now: the router key review (`docs/evals/router-answer-keys.yaml`), the DPIA keys' `verify` points
(`docs/evals/dpia-answer-keys.yaml`), the `ai-public-transition` rule, and the rest of `us-breach-notification.md`.
