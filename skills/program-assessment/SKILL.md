---
name: program-assessment
description: Assess the privacy program as a whole against the NIST Privacy Framework, with Target and Current Profiles across all 100 subcategories, an Implementation Tier, ranked gaps, and a quarter-by-quarter roadmap, using the suite's registers, assessments, and control library as evidence. Also runs NIST AI RMF maturity and ISO/IEC 42001 gap assessments. Use it whenever someone asks how mature the privacy or AI governance program is, or wants a NIST Privacy Framework profile, gap or maturity assessment, annual program review, or roadmap, or asks whether the program reasonably conforms to the framework for Tennessee's affirmative defense, even if they don't name the framework. Not for mapping controls or audit evidence (controls-and-evidence), assessing one activity (dpia, ai-impact-assessment), or the board summary (leadership-report).
---

# Program assessment

This skill takes a point-in-time view of the whole program: where it needs to be (Target Profile), where it is (Current Profile), how mature its risk management is (Tier), and what to do first (roadmap). It is evidence-led. Each rating links to the records that support it, and a rating built only on interviews says so.

The skill proposes ratings, priorities, and the roadmap. The privacy lead approves the assessment; leadership approves the roadmap's resourcing (`approvals.md`).

## Files

| File | Read it when |
|---|---|
| [`../_shared/conventions.md`](../_shared/conventions.md) | At the start of every run |
| [`../_shared/company-profile.md`](../_shared/company-profile.md) | At the start, for the regimes in scope |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 6 |
| [`references/rating-guide.md`](references/rating-guide.md) | Steps 2–5: Target selection, rating scale, Tier attributes, prioritization, roadmap |
| [`../_shared/references/nist-privacy-framework.md`](../_shared/references/nist-privacy-framework.md) | The Core and the category-to-law map |
| [`../_shared/references/nist-ai-rmf.md`](../_shared/references/nist-ai-rmf.md) | AI RMF variant |
| [`../_shared/references/iso-42001.md`](../_shared/references/iso-42001.md) | ISO/IEC 42001 variant |
| [`../_shared/references/crosswalk.md`](../_shared/references/crosswalk.md) | Linking subcategories to controls |
| [`../_shared/scripts/make_checklist.py`](../_shared/scripts/make_checklist.py) | Step 2: generate the blank profile table |
| [`assets/program-assessment-template.md`](assets/program-assessment-template.md) | Step 6 |

## Workflow

### 1. Scope and gather the evidence

Confirm the framework (NIST Privacy Framework by default; AI RMF or ISO/IEC 42001 if asked), the organizational scope (the whole company, or named entities and products), and the assessment date.

Collect the evidence before rating anything. Read the program's own records under the output root:

- `registers/ropa/` and `registers/ai-inventory/` (with their indexes and TBC counts)
- `registers/controls/` (the control library and evidence)
- `assessments/` (DPIAs, AI impact assessments, readiness reports)
- `vendors/`, `dsr/`, and `incidents/` (reviews, case files, incident records)
- `schedule.md` (overdue reviews and tests)

Then ask a short Round 1 for what the records don't show: policies, training records, governance minutes, and interviews with owners. Record each source.

### 2. Generate the profile table

Run `python3 ../_shared/scripts/make_checklist.py nist-pf profile` (or `ai-rmf` or `iso-42001`). Every subcategory then appears once, in the framework's own wording.

### 3. Set the Target Profile

Follow `references/rating-guide.md`, §1. For each subcategory, record whether it's in the Target Profile and why: law, risk, commitments, or benefit. Exclusions need a reason.

### 4. Rate the Current Profile and the Tier

Follow §2 and §3. Rate each Target Profile subcategory Achieved, Largely, Partly, Not achieved, or Not assessed, with linked evidence and a status. Rate the four Tier attributes, with evidence, and give the overall Tier with the attribute that holds it back.

Rate what the evidence shows. A policy shows design, not operation. Where the evidence is thin, say so, rate lower, and mark the rating Provisional, rather than giving the benefit of the doubt.

### 5. Rank the gaps and build the roadmap

Follow §4 and §5. Rank each gap on legal exposure, risk to individuals, dependency, and effort. Group them into a quarter-by-quarter roadmap with owners, acceptance criteria, and the evidence that will show each one closed. Label each item Legal or Readiness.

### 6. Write and route

Fill in `assets/program-assessment-template.md`. Save it to `<output root>/assessments/program/YYYY-MM-DD-<framework>-assessment.md`, ID `PRG-YYYY-NNN` from `gov next-id PRG --year <YYYY>`.

Route three separate approvals (`approvals.md`), and don't let one stand in for another: **assessment acceptance** (the privacy lead, with someone other than the preparer reviewing when the preparer is also the main evidence source), **legal validation** of applicability and interpretations (counsel), and **remediation approval** of priorities, resources, and dates (leadership). Approving an assessment never certifies that the company complies. The `leadership-report` skill, when built, summarizes it for the board.

Reply in about 150 words: the path, the Tier, the counts by rating, the top five gaps, the next quarter's roadmap items, and the decisions needed.

## Repeat assessments

Reassess annually, and after a major change such as a new jurisdiction, an acquisition, or a significant incident. Compare with the previous assessment: show rating changes by subcategory, and whether last year's roadmap items closed with evidence. When NIST finalizes Privacy Framework 1.1, map the old IDs to the new ones before comparing (`nist-privacy-framework.md`, §1).
