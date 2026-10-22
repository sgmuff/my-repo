# Conventions

Every skill in the privacy and AI governance suite follows these rules. Each SKILL.md covers its own workflow and links here for everything shared, so changing a rule here changes it everywhere.

## Contents

1. Who reads the output
2. Writing style
3. Citations
4. Currency: verify flags and reference freshness
5. Roles: ask each run
6. Intake
7. Human review points
8. Where deliverables go
9. IDs and document control
10. Connected tools
11. Handing back

---

## 1. Who reads the output

The deliverables support compliance decisions. Auditors, customers, regulators, and leadership may read them, often months later and without the conversation that produced them. Each document has to stand on its own: what was decided, on what facts, under which rule, by whom, and when.

Write for a privacy professional first, and make the executive summary readable by an executive or engineer who reads nothing else.

## 2. Writing style

All prose follows the user's `writing-style` skill. Load it before drafting.

The essentials hold even if the style skill can't be loaded:

- **American English:** spelling, punctuation inside quotation marks, and month-first dates ("October 16, 2026" in prose, `2026-10-16` in tables, filenames, and metadata).
- **Concise, plain, and active:** "The SRE lead deletes archives after 90 days," not "Archives should be deleted." Active voice puts an owner on each control.
- **One idea per paragraph,** opening with the conclusion, so a skimmer gets the verdict from first sentences.
- **No AI filler** ("robust," "seamless," "leverage," "it's worth noting," "navigate the landscape") and no vague qualifiers ("very," "quite," "somewhat").
- **A position, not a hedge, with its status.** "May," "could," and "possibly" belong in risk scenarios, not in conclusions. Each assessment ends on "Adequate," "Gap: …," or "Not met: …," with the reason. Each legal determination also carries a status (section 7), so a provisional position is never mistaken for a settled one. Being clear about what is unknown is not hedging.

Adaptations for compliance documents:

- **Terms of art stay.** Use legal terms exactly as the law uses them: controller, processor, service provider, data subject, consumer, deployer, provider, supervisory authority, legitimate interests, special category data, education records. Plain English never replaces a defined term, because changing the term changes the meaning. Define each on first use in the executive summary.
- **Quoted law keeps its spelling.** Quote legal text exactly, including British spelling ("organisational measures").
- **Portable Markdown only.** Use headings, tables, lists, bold, plain blockquotes, links, and fenced code blocks. Mermaid diagrams are allowed for data flows; they render on GitHub and Confluence. Don't use Obsidian callouts (`> [!note]`), `==highlights==`, `[[wikilinks]]`, inline `#tags`, or emoji.
- **Labeled blockquotes for flags.** Write flags as a blockquote that opens with a bold label:
  - `> **Verify:** …` for a point that depends on law or guidance that may have changed (section 4)
  - `> **Decision needed:** …` for a determination that needs a person (section 7)
  - `> **Blocker:** …` for a condition that stops launch or sign-off
  - `> **Assumption:** …` for a fact the user didn't confirm
- **Bold sparingly.** Bold the overall rating and the decision requested. Nothing else needs it.

## 3. Citations

Every conclusion cites the specific provision it rests on. A conclusion with no citation can't be checked, and an auditor will treat it as opinion.

Use these forms:

| Source | Form | Example |
|---|---|---|
| EU GDPR | Art. n(p)(x) | GDPR Art. 35(3)(a) |
| UK GDPR | UK GDPR Art. n | UK GDPR Art. 22A |
| Swiss FADP | FADP Art. n | FADP Art. 22 |
| EU AI Act | AI Act Art. n, or Annex III point | AI Act Art. 26(9); AI Act Annex III, point 4(a) |
| US state statute | Short name and section | VCDPA § 59.1-580; Cal. Civ. Code § 1798.185 |
| California regulations | CCPA Regs. § n | CCPA Regs. § 7150 |
| FERPA | 34 CFR § 99.n | 34 CFR § 99.31(a)(1)(i)(B) |
| NIST Privacy Framework | Subcategory ID | NIST PF ID.IM-P1 |
| NIST AI RMF | Function and subcategory | NIST AI RMF MAP 5.1 |
| ISO/IEC 42001 | Clause or Annex A control | ISO/IEC 42001 cl. 6.1.4; A.5.2 |
| AIUC-1 | Requirement or control ID, with the version | AIUC-1 E004 (Oct 15, 2026 release) |
| Regulator guidance | Issuer, title, date | EDPB Guidelines 9/2022 on personal data breach notification, v2.0 (Mar 28, 2023) |

Cite the narrowest provision that supports the point. "GDPR Art. 28(3)(h)" beats "GDPR Art. 28."

Every deliverable lists the reference files it relied on, with each file's version and last-verified date, in its document control section. That ties the conclusions to a known state of the law.

## 4. Currency: verify flags and reference freshness

Laws, regulations, and standards change. The suite handles this in three ways.

**Reference files carry their own dates.** Each file in `references/` opens with YAML front matter giving the version covered, the sources, the date last verified, when it's due for review, whether its sources are primary or secondary, and counsel's review. Before relying on a file, check its last-verified date against the interval. If the file is overdue, say so in the deliverable's document control section, and flag each conclusion that depends on it. For a `gov` record, list the file in `references` with its version and its `last_verified` date from the file's front matter (or a later date only if you re-checked the points you rely on against primary sources): `gov validate` raises a finding when a cited file is past its `review_by` date, has been re-verified since the record cited it, or is marked in its front matter as pending or only partly reviewed by counsel (a file whose review is `not-recorded` raises nothing). A skill's own reference files can be cited too; `gov` checks only the shared ones, and only a person can answer that finding.

**Volatile points are marked in the reference files.** A point marked *Volatile* in a reference file is one known to be changing: a pending amendment, a delayed effective date, a contested adequacy decision. A conclusion that rests on a volatile point gets a verify flag.

**Sources have an order of trust.**

1. The current reference file, if not overdue
2. A primary source fetched in this session (the statute, regulation, official journal, regulator site, or standard body site), cited with the date fetched
3. Anything else, including the model's own knowledge

A conclusion that rests on the third tier always gets a verify flag. Never present model knowledge as settled law.

A verify flag names the exact thing to check, the source to check it in, who checks it, and by when:

> **Verify:** The Annex III high-risk obligations apply from December 2, 2027 under Regulation (EU) 2026/1744. Check: EUR-Lex consolidated text. Owner: privacy lead *(proposed)*. By: before the pack goes to customers.

Every verify flag also goes in the deliverable's **verification register**, and becomes a row in the action plan, so it is tracked like any other action. A list of citations to check is not a completed legal review, and a flagged citation is not a confirmed defect.

| # | Claim being checked | Why it matters | Source to check | Owner | Blocks launch? | Action |
|---|---|---|---|---|---|---|
| V1 | Annex III obligations apply from 2027-12-02 | Decides which provider duties are due before the pack is released | EUR-Lex consolidated AI Act | Privacy lead *(proposed)* | No | A12 |

**Anything that could change the legality of the processing, or the controls required before launch, must be verified before launch.** Never schedule it for after. If a reference file's review date falls before the launch date and the deliverable relies on it, add an action to re-check it before launch.

When you can search the web, check a volatile point before flagging it, and record what you found and when. A flag is still needed if the source was secondary.

## 5. Roles: ask each run

Roles decide who owes which duty, and they change from one activity to the next. Don't store them in the company profile and don't assume them. On each run:

1. Read the facts.
2. Propose the role or roles, with one line of reasoning each.
3. Ask the user to confirm in the same message as the other intake questions. If the facts make a role obvious, state it as an assumption and move on, so the user can correct it without being asked.

| Regime | Roles to choose from | Deciding question |
|---|---|---|
| GDPR, UK GDPR, FADP | Controller, joint controller, processor, sub-processor | Who decides the purposes and essential means? (GDPR Art. 4(7)–(8), Art. 26) |
| US state laws | Controller or business; processor, service provider, or contractor; third party | Does the company process for its own purposes, or on behalf of another under contract? |
| FERPA | Educational agency or institution; "school official" vendor; other recipient of PII from education records | Does the company receive education records, and under which exception? (34 CFR § 99.31) |
| EU AI Act | Provider, deployer, importer, distributor, authorized representative, product manufacturer | Who develops the system or places it on the market under their name, and who uses it under their authority? (AI Act Art. 3(3)–(8), Art. 25) |
| AIUC-1 | Certification readiness for the company's own agent, or benchmark for a third party's agent | Is the company preparing its own product for audit, or judging someone else's? |

Two roles at once is common. A SaaS company is often a processor for customer data and a controller for its own product analytics, or a deployer of a vendor model and a provider of the agent built on top. Record each activity's role separately.

## 6. Intake

Each skill has an intake checklist. Run it the same way every time:

1. Read everything the user supplied, plus any linked documents you can reach: PRDs, tickets, contracts, questionnaires, architecture docs, earlier assessments, and the existing registers under the output root.
2. Fill in every field you can find or reasonably infer. Mark inferences as assumptions.
3. Ask about the remaining gaps in **two rounds**, each one numbered message grouped by heading, so the user can answer inline:
   - **Round 1: blockers and evidence requests.** Facts that could change the screening outcome, a legal determination, or whether the activity can launch at all, usually under 15 questions. List the documents you need in a separate "Evidence requested" group in the same message, so they aren't buried among the questions.
   - **Round 2: completion.** Everything else needed to finish the document: company profile gaps, transfer details, retention periods, security specifics, consultation, contributors. Send it with the draft, so it doesn't compete with the decisions that matter.
4. **Ask for evidence, not only answers.** Where a fact can be documented, ask for the document: the DPA, the retention or training configuration, the subprocessor list, the test results, the contract clause. Record what was provided.
5. If the user can't answer, record `TBC` and carry it into the fact register. Never invent a fact, vendor name, retention period, contract term, or control. A document that states assumptions as facts is worse than one with visible gaps, because an auditor or regulator reads it as a misstatement.

Always capture the **requesting business area** and the **system owner**. They are often different, and both appear in document control and in the approval routing.

Ask for missing company profile values once per session, in Round 2, not on every run.

### Fact register

Every assessment keeps a fact register, so a reader can see which conclusions rest on what:

| # | Fact | Status | Evidence or source | Owner | Needed by | Effect if unresolved |
|---|---|---|---|---|---|---|
| F1 | Vendor does not retain prompts | Unverified assumption | Vendor marketing page only | Procurement *(proposed)* | Before launch | R1 stays High; launch blocked |

Findings get a status of their own, so a reader can tell what was shown from what was suspected:

- **Confirmed finding:** supported by a supplied document, configuration, or test result, cited
- **Unverified concern:** a plausible risk that needs evidence
- **Recommended control:** a proposed mitigation, not proof that anything is wrong

Don't write "not compliant" or "violates" unless the legal requirement and the facts are both confirmed. Otherwise, describe the gap and its status.

Fact status is one of: **Confirmed** (with evidence), **Stated by requester** (no evidence yet), **Stated by vendor** (a vendor claim in a questionnaire, trust center, or email, not a contract term), **Unverified assumption**, or **TBC**. A conclusion that depends on anything other than a Confirmed fact is Provisional (section 7).

## 7. Human review points

The approval rules are in `approvals.md`. In every workflow:

- **Legal determinations** (whether a law applies, whether an assessment or notification is required, a lawful basis, a role, an AI Act classification) are drafted as a position with reasoning and citations, followed by a `> **Decision needed:**` block naming the approver.
- **Risk acceptance** is never implied. The skill rates risk. A person accepts it.
- **Anything external** (a notice to a regulator, a reply to a data subject, a letter to a vendor, a pack or report for a customer or auditor) is saved as a draft. Its metadata block comes first, then the line "DRAFT: not sent" as the first line of the body. The skill never sends it, even when an email or ticketing tool is connected.
- **Status** stays Draft until a person records approval.

### Determination status

Label every legal determination and every role with one of these statuses, in the text where it appears and in the summary:

| Status | Meaning | Wording |
|---|---|---|
| **Confirmed** | Rests only on Confirmed facts and a current reference, and an approver has signed off | "The company is the controller for support data (confirmed by <name>, <date>)." |
| **Provisional** | The skill's position, which depends on named facts or on law flagged for verification | "Provisional: the processing likely falls outside Art. 22, because closure doesn't affect refund or complaint rights (F7, unverified). If closure can affect either, reassess." |
| **Open** | The facts or the law aren't settled enough to take a position | "Open: Colorado applicability can't be decided until thresholds are confirmed (F3)." |

A draft prepared by a skill has no Confirmed determinations until a person signs off. Before that, the best a determination can be is Provisional.

Keep two questions apart, because they have different answers and different evidence:

1. **Does the law apply to the company?** (Territorial scope, thresholds, exemptions, role.)
2. **Does this activity trigger a specific obligation under it?** (An assessment, a notice, a consent requirement.)

### Roles are working assumptions until verified

A proposed role is a working assumption. The contract is evidence, but it doesn't decide the role. The facts about who determines purposes and means do. A vendor can be a processor for one operation and a controller for another it decides on itself.

### The launch gate

A draft never authorizes processing. Every assessment states its launch decision in these terms, in the executive summary:

> **Launch decision:** Not authorized by this draft. Production processing must not begin until the approver named in the sign-off section has reviewed the completed assessment, confirmed the legal determinations and roles, verified the launch-blocking actions with evidence, and recorded the residual-risk decision.

Once a person approves, the sign-off section records the authorization. The skill doesn't change the launch decision text on its own.

**Two kinds of blocker.** Label each launch-blocking action as one of:

- **Legal:** a requirement that already applies on the launch date
- **Readiness:** an internal control the risk analysis depends on, or preparation for an obligation that applies later (for example, Annex III duties from December 2, 2027)

Don't present a future obligation as one already in force. Readiness blockers can still block launch, because the risk analysis depends on them, but the document says which kind each one is.

**Launch gates are measurable.** Express the conditions for launch as gates with an owner, a threshold or test, and the evidence that closes each one. Completed paperwork isn't a gate. A certificate or report (SOC 2, ISO/IEC 27001 or 42001, AIUC-1) is evidence about the controls it covers, not proof that a system is fair, explainable, or lawful.

## 8. Where deliverables go

Deliverables are files in the repository, under the output root from the company profile (default `compliance/`). Keep this layout so other skills, and any publishing target the company profile names, can find things by path.

**Records managed by `gov`** are YAML files, and `gov render` writes their Markdown. Never write or edit those `.md` files by hand; edit the YAML and re-render. CI fails on a hand edit. `gov` manages the RoPA, DPIA screenings (`scr`), DPIAs (`dpia`), LIAs, TIAs, transfer screens (`tsr`), and AI Act provider and deployer files (`aip`, `aid`), vendor reviews (`vr`), AI impact assessments and FRIAs (`aiia`), incidents (`inc`), and AIUC-1 readiness reports (`rdy`); `gov/rules/ids.yaml` lists each type's folder. Other deliverables move to `gov` one type at a time; until then they stay Markdown written from their templates, in a folder `gov` doesn't manage.

```
compliance/
  approvals/approval-log.md
  assessments/
    dpia/              DPIA-YYYY-NNN-<slug>.yaml and .md, plus index.md (generated)
      screening/       SCR-YYYY-NNN-<slug>.yaml and .md, plus index.md (generated)
      assistance-packs/ PA-YYYY-NNN-<slug>.md   (processor assistance packs, Markdown)
    ai-impact/         AIIA-YYYY-NNN-<slug>.yaml and .md, plus index.md (generated): assessments, FRIAs, and input packs
    program/           YYYY-MM-DD-<framework>-assessment.md
    aiuc-readiness/    RDY-YYYY-NNN-<slug>.yaml and .md, plus index.md (generated)
  vendors/           VR-YYYY-NNN-<slug>.yaml and .md, plus index.md (generated)
    requests/        VR-YYYY-NNN-<slug>-requests.md (generated draft request lists)
  registers/
    ropa/              ROPA-NNNN-<slug>.yaml (record) and .md (generated), plus index.md (generated)
    ai-inventory/      <system-slug>.md, plus index.md
    risk-register.md
    controls/          CTL-NNNN-<slug>.md, plus index.md (control library and evidence)
  dsr/YYYY/            YYYY-MM-DD-<request-id>.md
  incidents/          INC-YYYY-NNN-<slug>.yaml and .md, plus index.md (generated)
    notices/          INC-YYYY-NNN-<slug>-notices.md (generated notice drafts)
  policies/            <policy-slug>.md, and YYYY-MM-DD-<notice-slug>-review.md
  regulatory-change/   YYYY-MM-DD-<slug>.md
  reports/             YYYY-QN-<audience>.md, and metrics-YYYY-MM-DD.md (generated)
  schedule.md          generated by gov schedule
  .gov/counters.yaml   last ID issued per prefix, written by `gov next-id`
```

Create folders as needed (`gov new` creates its own). Slugs are lowercase, hyphenated, and short ("support-copilot," not "support-copilot-llm-feature-dpia-v2").

Before creating a record, check whether one already exists for the same activity, vendor, or system. Update the existing record and add a version history row, rather than creating a duplicate.

## 9. IDs and document control

**Document IDs** use a prefix, the year, and a three-digit sequence: `DPIA-2026-004`, `SCR-2026-011`, `VR-2026-007`, `ROPA-0042`, `AIS-0013`, `AIIA-2026-002`, `DSR-2026-118`, `INC-2026-003`, `CTL-0021` (control), `EV-0140` (evidence item), `RDY-2026-001` (readiness report), `PA-2026-001` (program assessment), `NR-2026-001` (notice review), `POL-0003` (policy), `RC-2026-002` (regulatory change), `LIA-2026-001` (legitimate interests or compatibility), `TIA-2026-001` (transfer impact), `TSR-2026-001` (transfer screen), `AIP-2026-001` (AI Act provider file), `AID-2026-001` (AI Act deployer check), `LR-2026-Q3` (leadership report). Get the next number from `gov next-id <PREFIX>` (add `--year YYYY` for yearly prefixes), or let `gov new` allocate it. Never count files or pick a number yourself: `gov` keeps a counter, never reuses a number, and `gov validate` rejects an ID it didn't issue. Within a document, number risks `R1`, `R2`, actions `A1`, `A2`, and open questions `Q1`, `Q2`, and cross-reference them in both directions.

**Metadata.** A `gov` record holds its metadata as fields, and its rendered Markdown starts with a flat metadata block for older scripts. Every other deliverable starts with a YAML metadata block, which GitHub, Confluence importers, and scripts can all read:

```yaml
---
id: DPIA-2026-004
type: dpia            # dpia | screening | vendor-review | ropa | ai-intake | ...
title: Support Copilot
status: Draft         # see approvals.md
version: 0.1
requesting_business_area: Customer Support
system_owner: Support Platform (Jane Doe, Eng Manager)
prepared_by: Claude (privacy-governance suite), for <privacy lead>
date_prepared: 2026-10-16
next_review: 2027-10-16
roles: {gdpr: controller, us_state: controller, eu_ai_act: deployer}
regimes: [GDPR, UK GDPR, FADP, EU AI Act, CA, CO]
references:           # file, version covered, last verified
  - gdpr.md (EU GDPR as of 2026-10-16; DUAA staged), 2026-10-16
  - us-state-privacy.md (20 in force, 4 enacted), 2026-10-16
tickets: []           # Jira or ServiceNow keys for actions, once created
---
```

**Document control section.** Right after the title, a short table repeats the IDs, owners, roles, and related records in human-readable form, followed by a version history table. Templates include both, and `gov` templates render them from the record.

## 10. Connected tools

Ticketing (Jira, ServiceNow), document sources, and email can make a run faster, but every skill must work without them. `connectors.md` explains how to detect each one, what the skills may do with it, and the fallback. The short version:

- Read from any connected source freely.
- Create tickets only after the user confirms the list in this session.
- Draft emails, never send them.
- **Never connect to a calendar or create calendar events,** even when one is connected. Review dates and deadlines stay as action items.

## 11. Handing back

Before replying:

1. Reread the deliverable against the `writing-style` checklist ("Before handing back") and fix what it catches.
2. Check that every conclusion has a citation and a status, every action has an owner, due date, dependency, and acceptance criterion (owner and date marked *proposed* if the user didn't give them), every verify flag has a matching action, and every decision a person must make has a `Decision needed` block.
3. Check the action dates for sequencing: nothing is due before the thing it depends on, and every launch blocker and legality-affecting verification is due before launch.

Skills that answer first and record in `gov` (`dpia`, `lia`, `tia`, `ai-act-provider`, `ai-act-deployer`, `vendor-review`, `ai-impact-assessment`, `incident-assessment`) follow their own reply step instead: the full answer in plain English, with the record named only in one closing line and no counts of findings or flags. Every other skill replies in **no more than about 150 words**:

- The file path
- The outcome in one or two lines, with statuses (for example, "DPIA warranted (provisional); residual risk not yet confirmed, target Medium")
- The decisions needed, and from whom
- The Round 1 blocker questions, or a pointer to them if there are more than five
- A count of verify flags, with a pointer to the action plan

Lists of actions, CSV import blocks, and verify details belong in the document, not in the reply. Don't paste the document into chat.
