---
name: ai-impact-assessment
description: Assess an AI system or agent's impact on people, groups, and society, covering fairness, transparency, human oversight, data provenance, model limitations, reliability, safety, and accountability, aligned to AIUC-1's Safety, Reliability, and Accountability domains, NIST AI RMF, ISO/IEC 42001, and the EU AI Act. Also produces Article 27 fundamental rights impact assessments (FRIAs) and FRIA input packs for customers. The draft is separate from the DPIA, with evidence-backed findings, three-level risk ratings, and approval routing. Use it whenever someone needs an AI impact, algorithmic impact, or AI risk assessment, a bias or fairness review, a human oversight review, a FRIA, or a pre-launch AI review, or when ai-intake tiers a system High or Elevated, even if they don't name the assessment. Not for AI intake and tiering (ai-intake), personal data risks to individuals (dpia), or AI vendor contracts (vendor-review).
---

# AI impact assessment

This skill assesses what an AI system does to the people it touches, and whether the safeguards around it work. It produces an AI impact assessment (AIIA), a separate document from the DPIA. The two cross-reference each other, but don't merge. Where a FRIA is required, the skill produces that too, as its own document.

The assessment rests on evidence: evaluation results, oversight records, documentation, and configurations. Where evidence is missing, the finding says so and stays Provisional. The skill rates risk and drafts conclusions. The approvers in `approvals.md` decide.

## Files

| File | Read it when |
|---|---|
| [`../_shared/conventions.md`](../_shared/conventions.md) | At the start of every run |
| [`../_shared/company-profile.md`](../_shared/company-profile.md) | At the start |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 7 |
| [`references/assessment-guide.md`](references/assessment-guide.md) | Steps 3–5: what each section covers, its evidence, and its mappings; FRIA |
| [`../_shared/references/risk-method.md`](../_shared/references/risk-method.md) | Step 5: the AI risk catalog (§2a), three ratings, control statuses |
| [`../_shared/references/eu-ai-act.md`](../_shared/references/eu-ai-act.md) | Steps 2 and 6: classification, roles, deployer duties, FRIA |
| [`../_shared/references/aiuc-1.md`](../_shared/references/aiuc-1.md) | Steps 3–4: requirements and testing cadence |
| [`../_shared/references/nist-ai-rmf.md`](../_shared/references/nist-ai-rmf.md) | Mapping, and the Generative AI Profile risks |
| [`../_shared/references/iso-42001.md`](../_shared/references/iso-42001.md) | Mapping to cl. 6.1.4 and A.5 |
| [`assets/aiia-template.md`](assets/aiia-template.md) | Step 6 |
| [`assets/fria-template.md`](assets/fria-template.md) | Step 6, when a FRIA or FRIA input pack is needed |

## Workflow

### 1. Load context and the intake

Read `conventions.md` and `company-profile.md`. Find the system's inventory entry under `<output root>/registers/ai-inventory/`, plus any DPIA, vendor review, or earlier AIIA. If there is no inventory entry, run the `ai-intake` steps first (or ask the user to). The assessment needs the tier, the classification, and the facts.

If the system is already live, say so, and ask what it has already done. Containment comes before the assessment (`conventions.md`, §6).

### 2. Confirm scope and roles

Set the scope: the system, the use or uses being assessed, and the deployment context. Confirm the EU AI Act roles and classification from the intake, marked Provisional, and re-check any prohibition against the documented function now (`eu-ai-act.md`, §4). Decide which sections the tier requires: Tier 1 gets every section; Tier 2 gets the sections its factors call for, with the reasons recorded.

Decide whether a FRIA is in play (`eu-ai-act.md`, §7): is the company a deployer that owes one (decided case by case), or a provider whose customers may owe one (then a FRIA input pack)?

### 3. Gather the evidence

Round 1 (short, usually under 12 questions, with an "Evidence requested" group) asks for what the sections need most: evaluation and bias test results, sample outputs, oversight workflow and override statistics, the provider's instructions for use, training data documentation, failure plans, and logs. `references/assessment-guide.md` lists the evidence for each section.

Record each item in the fact register with its status. A vendor's claim is "Stated by vendor" until the document arrives.

### 4. Assess each section

Work through `references/assessment-guide.md`, sections 1–10. For each:

- State what the evidence shows, with citations to the documents and to the provisions or requirements that apply (AIUC-1 ID and release, AI Act article, NIST AI RMF subcategory, ISO/IEC 42001 control)
- Give each finding a status: Confirmed finding, Unverified concern, or Recommended control
- End on Adequate, Gap, or Not met, with the status of that conclusion

Be specific about function. A label ("suspicious behavior," "engagement score") is not evidence of what a model infers. Ask for inputs, outputs, and how they're used.

### 5. Rate the risks

Use the AI risk catalog (`risk-method.md`, §2a) and the register template, with inherent, current residual, and target residual ratings and control statuses. Add reach, reversibility, and autonomy to severity, and rate harms to groups and society as well as to individuals. Personal data risks to individuals belong in the DPIA; link them rather than duplicating them.

### 6. Write the documents

Fill in `assets/aiia-template.md`. Save it to `<output root>/assessments/ai-impact/YYYY-MM-DD-<slug>.md`, ID `AIIA-YYYY-NNN`. Open the executive summary with the status block, including **"Launch decision: Not authorized by this draft"** (`conventions.md`, §7).

If a FRIA is needed, fill in `assets/fria-template.md` and save it beside the AIIA as `…-fria.md` (or `…-fria-input-pack.md` for customers). A FRIA notification to the market surveillance authority and a FRIA input pack for customers are both external communications: drafts that the privacy lead approves.

Every action has a dependency, an acceptance criterion, and evidence. The AIUC-1 quarterly testing duties, for readiness mode, go in the action plan as recurring actions. Never put them on a calendar.

### 7. Route and hand back

Route sign-off by the current residual rating (`approvals.md`), with the business owner and system owner. Update the inventory entry's `related` field with the AIIA ID, and rebuild the index.

Reply in about 150 words: the document paths, the status block in two lines, any prohibition concern, the decisions needed, the Round 1 evidence still outstanding, and the count of verify flags.

## Reassessment

Reassess when the model, data, use, autonomy, or affected population changes; after an incident; when a new AIUC-1 release changes an applicable requirement; and at least every 12 months for Tier 1 systems. Carry forward what still holds, re-rate the risks (closed actions with evidence move into the current rating), and add a version history row.
