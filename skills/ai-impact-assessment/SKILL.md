---
name: ai-impact-assessment
description: Assess an AI system or agent's impact on people, groups, and society, covering fairness, transparency, human oversight, data provenance, model limitations, reliability, safety, and accountability, aligned to AIUC-1's Safety, Reliability, and Accountability domains, NIST AI RMF, ISO/IEC 42001, and the EU AI Act. Also produces Article 27 fundamental rights impact assessments (FRIAs) and FRIA input packs for customers. Records each as a gov record, separate from the DPIA, with evidence-backed findings, computed risk ratings, and approval routing. Use it whenever someone needs an AI impact, algorithmic impact, or AI risk assessment, a bias or fairness review, a human oversight review, a FRIA, or a pre-launch AI review, or when ai-intake tiers a system High or Elevated, even if they don't name the assessment. Not for AI intake and tiering (ai-intake), personal data risks to individuals (dpia), or AI vendor contracts (vendor-review).
compatibility: Requires the gov command from this repository (skills/install.sh installs it), with Python 3.10+, PyYAML, jsonschema, and Jinja2.
---

# AI impact assessment

This skill assesses what an AI system does to the people it touches and whether the safeguards work, and records it as an `aiia` record: kind `aiia` for the assessment, `fria` for an AI Act Art. 27 assessment the company owes as deployer, or `fria-input-pack` for customers' own FRIAs. Each is its own record, separate from the DPIA; they link, but don't merge. Never write or edit a record's `.md` file; `gov` writes it.

**Evidence decides, not labels.** "Suspicious behavior" or "engagement score" doesn't say what a model infers; ask for the inputs, outputs, and how they're used. Where evidence is missing, the finding says so and stays Provisional. The approvers in `approvals.md` decide.

## Files

| File | Read it when |
|---|---|
| [`references/assessment-guide.md`](references/assessment-guide.md) | Steps 2-4: what each domain covers, its evidence, its mappings, and the FRIA |
| [`../_shared/references/risk-method.md`](../_shared/references/risk-method.md) | Step 3: the AI risk catalog (§2a) and the three ratings |
| [`../_shared/references/eu-ai-act.md`](../_shared/references/eu-ai-act.md) | Steps 1-3: classification, roles, deployer duties, the FRIA |
| [`../_shared/references/aiuc-1.md`](../_shared/references/aiuc-1.md), [`nist-ai-rmf.md`](../_shared/references/nist-ai-rmf.md), [`iso-42001.md`](../_shared/references/iso-42001.md) | Step 3: the citations for each domain |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 5 |

## Workflow

### 1. Check the tool, the intake, and the scope

Run `gov --version`; if it fails, stop and tell the user to run `skills/install.sh`. Find the system's inventory entry under `compliance/registers/ai-inventory/`, and any DPIA, vendor review, or earlier assessment. Without an inventory entry, run `ai-intake` first if the user can answer its questions; otherwise record the tier as TBC with an action to run it. If the system is live, ask what it has already done; containment comes first.

Set the scope: the system, the uses assessed, and the deployment context. Re-check any Art. 5 prohibition against the documented function now, since prohibitions already apply. Decide whether a FRIA is in play: the company as a deployer that owes one under Art. 27(1), or as a provider whose customers may owe one (an input pack).

### 2. Get the evidence

Ask in Round 1, usually under 12 questions, for what the domains need most: evaluation and bias test results, sample outputs, the oversight workflow and override statistics, the provider's instructions for use, training data documentation, failure plans, and logs. `references/assessment-guide.md` lists the evidence per domain. A vendor's claim is `stated-by-vendor` until the document arrives.

### 3. Answer the assessment

Answer it fully, then check each domain against `references/assessment-guide.md` and add what you missed. Points answers often miss:

- **Severity counts reach, reversibility, and autonomy**, and harms to groups and society as well as individuals.
- **Personal data risks to individuals belong in the DPIA**; link it rather than duplicating them.
- **Tier 1 assesses all nine domains**; Tier 2 marks a domain not-applicable only with the reason.
- **A FRIA follows Art. 27(1)(a)-(f)** and draws its risks of harm from the assessment's risk rows. Whether a deployer owes one turns on its status (a public body, a private entity providing public services, or a deployer of an Annex III point 5(b) or 5(c) system); for an input pack, that's the deployer's determination, not the company's.

### 4. Record it

Run `gov new aiia --slug <slug> --title "<system and use>" --date <today>`, set `kind`, and fill in the record from your answer: each domain's position, evidence, and citations (AIUC-1 ID with release, AI Act article, NIST AI RMF subcategory, ISO/IEC 42001 control); risks with likelihood and severity at three points, which `gov` rates; and the fact register. For a FRIA or input pack, start a second record, set `domains: []`, fill in `fria`, cite the assessment's risks as `AIIA-YYYY-NNN/R3` rather than copying them, and link the two records both ways (`related.aiia` in the FRIA, `related.fria` in the assessment). Each call stays Provisional; a point that doesn't fit a field goes in `analysis` (400 words at most).

### 5. Validate, render, and reply

Run `gov validate`, fix errors, and resolve findings by changing the record; a finding that names a real gap stays open with an action. Don't add a `finding_responses` entry yourself. Run `gov render`, then add the record to the inventory entry's `related` field. A FRIA notification to the market surveillance authority and an input pack for customers are external communications: drafts the privacy lead approves.

Reply in plain English: the outcome and any prohibition concern first, then what has to happen before launch, grouped as legal requirements, risks, and internal policy, who approves, and the Round 1 evidence still outstanding, five questions at most. Close with one line naming the records and their paths. The AIUC-1 quarterly testing duties are recurring actions, never calendar events.

## Reassessment

Reassess when the model, data, use, autonomy, or affected population changes; after an incident; when a new AIUC-1 release changes an applicable requirement; and at least every 12 months for Tier 1 systems. Update the record: closed actions with evidence move measures to verified, and add a version history row.
