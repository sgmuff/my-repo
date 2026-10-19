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
4. `program_metrics.py` scrapes Markdown tables, so a format change breaks it silently.
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

Each SKILL.md shrinks to four steps: gather facts, run `gov new`, fill in the record, and run `gov`. Each also:

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
- [x] Reference files for the five conditional regimes, verified against secondary sources; counsel review pending
- [x] Evals against no skill, iterations 1 and 2 reviewed
- [x] Fixes from the iteration 2 review: each LIA test's result in the status line, validation findings rendered in every record, narrower `law` blocks, and the UK data protection test in force since February 5, 2026
- [x] Iteration 3 evals reviewed: `lia` 96% and `tia` 98% against 55% and 61% without the skill
- [x] Fixes from the iteration 3 review: launch blockers grouped by reason, required notices as `law`, a trail for negative transfer screens, and live transfers flagged first
- [x] Iteration 4 evals reviewed: `lia` 94% and `tia` 98% against 57% without the skill
- [x] Fixes from the iteration 4 review: `gov validate` rejects a law block without a cited provision; replies attribute counts to `gov`, group blockers by reason, and set no unsourced dates
- [ ] Iteration 5 evals, with the new assertions
- [ ] Description optimizer runs for `lia` and `tia`
- [x] `phase-1` merged to main

### Later phases

Each phase closes with skill evals, trigger evals, and a description optimizer run.

1. **Catalog, `lia`, and `tia`.** Point `vendor-review` and `dpia` at them. Add reference files for the five conditional regimes, so their entries can be switched on.
2. **`ai-act-provider` and `ai-act-deployer`,** and the Art. 25 check. Finish well before December 2, 2027.
3. **Security entries** in `controls-and-evidence`. The first CCPA audit is due April 1, 2028 at the earliest.
4. **Existing assessments in the new format,** starting with the DPIA, plus `gov screen`.
5. **Remaining registers.**
6. **Dates and metrics** moved into `gov`.
7. **Reference files** with YAML front matter, so `regulatory-change` reads data.

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
- **Some citations need verifying:** the Swiss transfer entry rests on general knowledge, and the five conditional reference files on secondary sources pending counsel review.

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
