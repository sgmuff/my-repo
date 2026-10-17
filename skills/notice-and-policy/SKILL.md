---
name: notice-and-policy
description: Review privacy notices and policies against what the company actually does, using the RoPA, AI inventory, vendor reviews, and assessments as the record of practice, and draft updates. Also drafts and maintains AI acceptable use policies, both the employee policy for staff using AI tools and the product policy for end users of the company's own AI agents (AIUC-1 E010). Covers website and app privacy notices, notices at collection, AI disclosures, employee notices, and internal privacy policies under GDPR, US state laws including CCPA, FERPA, COPPA, and the EU AI Act. Use it whenever someone asks whether a notice covers a practice, wants a privacy notice or policy reviewed, updated, or drafted, needs an AI acceptable use policy, or asks what to disclose about a new feature, even if they don't name the document. Not for one-off rights requests (dsr-response), processing records (ropa), or breach notices (incident-assessment).
---

# Notices and policies

This skill keeps what the company says in line with what it does. It compares notices and policies with the program's records of practice, finds mismatches in both directions, and drafts the changes. It also writes and maintains AI acceptable use policies.

A published notice is an external communication, and an internal policy binds people, so the skill drafts and a person approves (`approvals.md`). **The notice must follow the practice.** Where the practice is unknown, the finding is a question to answer, not wording to invent.

## Files

| File | Read it when |
|---|---|
| [`../_shared/conventions.md`](../_shared/conventions.md) | At the start of every run |
| [`../_shared/company-profile.md`](../_shared/company-profile.md) | At the start |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 6 |
| [`references/notice-requirements.md`](references/notice-requirements.md) | Notice reviews: required elements by regime, and the practice-comparison method |
| [`references/aup-guide.md`](references/aup-guide.md) | AI acceptable use policies: the two kinds, contents, and evidence |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md) | §4 transparency |
| [`../_shared/references/us-state-privacy.md`](../_shared/references/us-state-privacy.md) | §3 notice duties, §9 AI laws |
| [`../_shared/references/eu-ai-act.md`](../_shared/references/eu-ai-act.md) | §8 Art. 50 |
| [`../_shared/references/ferpa.md`](../_shared/references/ferpa.md) | Student data |
| [`../_shared/references/aiuc-1.md`](../_shared/references/aiuc-1.md) | E010, E016, E017 |
| [`assets/notice-review-template.md`](assets/notice-review-template.md) | Notice reviews |
| [`assets/ai-aup-template.md`](assets/ai-aup-template.md) | Employee AI use policy |
| [`assets/product-aup-template.md`](assets/product-aup-template.md) | Product acceptable use policy |

## Notice review

### 1. Gather the notice and the practice

Get the current notice text (the published version, with its date) and each place data is collected: forms, in-product notices, cookie banners, and AI interfaces. Then gather the record of practice from the output root:

- `registers/ropa/` for purposes, data, recipients, transfers, retention, and sale or sharing
- `registers/ai-inventory/` for AI features, decisions about people, and disclosures
- `vendors/` for recipients and own-purpose uses
- `assessments/` for DPIA and AI impact findings that require notice changes
- `dsr/` for how rights requests actually work

Where the records are thin, ask a short Round 1 for the missing facts, and request documents (configurations, data flow diagrams, tag manager exports for tracking), each with an owner and a date range. Mark which facts come from register entries and which from a technical check.

### 2. Compare both directions

Follow `references/notice-requirements.md`, §5. Build a table of findings:

- **Said but not done** (the most serious, since it can be deceptive): quote the statement, cite the practice record that contradicts it
- **Done but not said:** cite the practice record, and name the required element it falls under
- **Out of date** or **missing required elements**, by regime

Give each finding a status (Confirmed finding, Unverified concern, or Recommended control; `conventions.md`, §6) and the provision behind it. Keep bundled legal questions apart (§5, "Questions to keep separate"): a tag is not by itself a sale, and an announcement is not by itself consent. Put every gap in the gap tracker (§5), with evidence status, legal status, interim control, owner, and closure evidence.

### 3. Contain, then draft the changes

Work in this order: **contain** (decide interim controls for the riskiest practices, such as pausing a tag on pages children reach), **verify** the facts, have the privacy lead and counsel **decide** the legal questions, **draft**, then **validate** the live notice. Record each containment step as recommended, authorized, or implemented; the review doesn't pause anything itself.

Draft replacement text for each finding, in plain language the audience understands, keeping defined legal terms where the law requires them. Where the practice is wrong rather than the notice (a pixel that shares data the company promised not to share), the fix is to change the practice, flagged as an action for the business owner, not to rewrite the promise.

For new features, draft just-in-time notices (notice at collection, AI disclosure) as well as the full-notice changes, each mapped to the event that triggers it and an implementation owner.

Before handing back, check the draft against itself: retention periods, recipients, and promises about children's and student data must say the same thing everywhere. Mark as a **release gate** any statement that describes a mechanism not yet built and tested (an opt-out link, Global Privacy Control handling, consent withdrawal). It isn't published until the mechanism works. After publication, test the live website and app flows, confirm the notices appear where required, and keep the evidence.

## AI acceptable use policy

### 4. Pick the kind, and draft from the facts

Decide whether the request is for the **employee** AI use policy, the **product** acceptable use policy (AIUC-1 E010), or both (`references/aup-guide.md`). If it isn't obvious, ask.

Draft from the company's actual position: the approved tools in the AI inventory, the data classes the company uses, the contract terms vendors have accepted (no training on customer data), the intake process for new tools and agents, and the training available. Don't write rules the company can't follow or enforce. Note each one as an open decision instead.

For the employee policy, follow `references/aup-guide.md`: approve tools and their configurations, define the data classes precisely, keep monitoring as a separate decision, and keep the staff-facing policy free of internal analysis. List the approval gates that must close before the policy takes effect. Use the user's stated rules as given; if a stricter rule seems wiser, propose it as a decision rather than writing it in.

For the product policy, check that the detection, the in-product notices, and the enforcement it describes exist (E010.2–E010.4). If they don't, the policy is a draft with a gap list for `controls-and-evidence`.

## Both

### 5. Save the deliverable

- Notice review: `<output root>/policies/YYYY-MM-DD-<notice-slug>-review.md`, with the redline or replacement text in the same file, ID `NR-YYYY-NNN`
- Policy: `<output root>/policies/<policy-slug>.md`, with version history and `next_review` (at least every 12 months), ID `POL-NNNN`

A published notice draft is external: metadata first, then "DRAFT: not sent" in the body. Each draft lists the practice records it relies on, so the next review can check them again.

### 6. Route and hand back

Route per `approvals.md`: the privacy lead approves notice text and policies, with counsel for published notices; business owners confirm the practice facts and fix practices that don't match promises. Rebuild `schedule.md` with `../_shared/scripts/compliance_schedule.py` so the review date is tracked.

Reply in about 150 words: the path, the counts of findings by kind, the most serious finding, the decisions needed, and the Round 1 facts still missing.

## Keeping notices current

Every RoPA change, vendor review, DPIA, AI intake, or new law can change what a notice must say. Those skills flag notice coverage as a follow-on. Review the main privacy notice at least every 12 months, and whenever a flagged follow-on arrives.
