---
name: vendor-review
description: Review a vendor, subprocessor, or AI provider's data protection terms and practices, with a clause-by-clause DPA gap analysis against GDPR Article 28, US state service provider terms, FERPA and student privacy terms, and transfer rules, plus an AI module for models, agents, and AI features (training on customer data, retention, outputs, model changes, agent permissions, EU AI Act roles, AIUC-1 certification). Records the review as a vendor review record with findings, risks, a recommendation, and a draft request list for the vendor. Use it whenever someone wants to onboard, renew, or reassess a vendor, review a DPA, subprocessor notice, or security questionnaire for privacy, or check an AI vendor or an AI feature turned on in an existing tool, even without saying "vendor review." Not for the company's own processing (dpia), RoPA entries (ropa), internal AI use-case intake (ai-intake), or a transfer impact assessment or transfer screen (tia).
compatibility: Requires the gov command from this repository (skills/install.sh installs it), with Python 3.10+, PyYAML, jsonschema, and Jinja2.
---

# Vendor review

This skill reviews a third party that will process personal data for the company, or supply AI that touches it, and records the review as one YAML record (`vr`). `gov render` writes the review and, from the record's `requests`, the draft request list for the vendor. Never write or edit either `.md` file.

**Rate what the documents say, not what the vendor's sales team says.** A trust center page, a questionnaire answer, or a sales email is evidence of a claim, not a contract term. The review proposes; the approvers in `approvals.md` decide, and nothing goes to the vendor until the privacy lead approves it.

## Files

| File | Read it when |
|---|---|
| [`../_shared/references/dpa-checklist.md`](../_shared/references/dpa-checklist.md) | Steps 3-4: the items each depth covers, and the red flags |
| [`references/intake.md`](references/intake.md) | Step 2: what to collect, by round |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md), [`us-state-privacy.md`](../_shared/references/us-state-privacy.md), [`ferpa.md`](../_shared/references/ferpa.md) | Roles, processor terms, transfers, state service provider terms, student data |
| [`../_shared/references/aiuc-1.md`](../_shared/references/aiuc-1.md), [`eu-ai-act.md`](../_shared/references/eu-ai-act.md) | The AI module, in vendor benchmark mode |
| [`../_shared/references/risk-method.md`](../_shared/references/risk-method.md) and [`../_shared/approvals.md`](../_shared/approvals.md) | Steps 4 and 6 |

## Workflow

### 1. Check the tool and what already exists

Run `gov --version`; if it fails, stop and tell the user to run `skills/install.sh`. Look under `compliance/vendors/` for an earlier review of this vendor: if one exists, this is a renewal, reassessment, or notice (below), not a new review. Check `compliance/registers/ropa/` for the activities that use the vendor, so the review covers the actual uses.

### 2. Scope it and get the documents

Pin down which services and features are in scope and for what; a CRM with an AI assistant switched on is two things. Set the depth from the facts, and say why:

- **Light:** no personal data beyond business contacts, nothing sensitive, no AI on personal data, no restricted transfers. Checklist sections 1-2 and item 7.1.
- **Standard:** ordinary personal data of customers, users, or employees. Sections 1-4 and 7.
- **Deep:** special category, children's, student, or US-sensitive data; large scale; AI on personal data or agents that act; an unsettled transfer; or a vendor critical to the product. Standard, plus the AI module and evidence for every control the rating depends on.

A Light review that finds a red flag becomes Standard. Student data adds section 5; AI that touches personal data adds section 6.

Ask in Round 1 for the documents themselves (DPA, MSA or terms, AI terms, subprocessor list, security report) and the facts that decide depth and roles, including whether processing or an AI feature has already started. If it has, containment comes first: what the vendor already holds, scored, or trained on.

### 3. Answer the review

Answer it fully, then check each item against `dpa-checklist.md` and add what you missed. Points answers often miss:

- **Order of precedence first** (item 1.3). A strong DPA that the MSA or online AI terms override is a `conflicts` finding.
- **Roles per operation, from the facts.** Any own-purpose use by the vendor, such as training, makes it a controller for that use.
- **Training is three questions** (item 6.1): foundation models, the vendor's product, and the company's own instance.
- **An AIUC-1 certificate covers one product and release.** Record the product, release, report date, and expiry.
- **Each transfer needs its mechanism for the right entity.** Link the TIA for SCCs, BCRs, the IDTA, or the UK Addendum, and the transfer screen for the DPF or adequacy.
- **A security report's scope must cover the service in use.** Don't rate controls you haven't seen evidence for.
- **Unsigned terms aren't controls.** "The vendor will sign our DPA" leaves the current rating where it is.

### 4. Record it

Run `gov new vr --slug <vendor-slug> --title "<vendor and service>" --date <today>`. Fill in the record from your answer:

- One `clauses` row per required item, rated `present`, `partial`, `missing`, `conflicts`, `not-provided` (the document wasn't supplied; ask, don't guess), or `not-applicable` with the reason as evidence. Quote briefly, with the document and clause.
- The AI module in `ai`, or `applicable: false`.
- Risks to individuals with likelihood and severity at three points (inherent, current with verified measures only, target); `gov` computes the ratings. Contract and commercial risks to the company go in `company_findings`, kept out of the privacy rating.
- A `requests` entry for each gap the vendor must close: documents, contract changes with suggested wording, configuration to confirm, and questions. One request can cover several items (`item: "2.1, 2.7"`). A gap the company closes itself, such as retrieving its own signed DPA, needs a fix and an action instead of a request.
- For an AIUC-1 certificate, record its product, release, report date, and expiry in `ai.aiuc_scope`; a certificate for another product leaves `aiuc_certified` false.
- The fact register in `facts`: a trust center page, questionnaire answer, or sales email is `stated-by-vendor`; what the requester says without evidence is `stated-by-requester`.

Each call stays Provisional. A point that doesn't fit a field goes in `analysis` (400 words at most); the record never changes your conclusion.

### 5. Validate and render

Run `gov validate`, fix errors, and resolve findings by changing the record. A finding that names a real gap stays open with an action. Don't add a `finding_responses` entry yourself. Run `gov render`, then add the review to each RoPA entry's `related` vendor reviews, or, if there's no entry yet, add an action to create one; rerun both. Recommend, but don't run, the follow-ons the findings call for: `dpia`, `ropa`, `tia`, and `ai-impact-assessment` for a possibly high-risk AI use.

### 6. Reply

Lead with the recommendation and what has to happen before signing or switching on the service, in plain English, grouped as legal requirements, risks, and internal policy. Say who approves, from `approvals.md`, and that the request list waits for the privacy lead. Ask the Round 1 questions still open, five at most. Close with one line naming the review and request list and their paths.

## Renewals, reassessments, and notices

For new terms or a subprocessor notice, set `kind` to `renewal`, `reassessment`, or `notice`. With an earlier review, update its record: only the affected items and risks, with a version history row. With none, start a new record; a `notice` needs only the section 3 items it changes, plus `objection_deadline`. The decision to object is an external communication the privacy lead approves; accepting the new subprocessor follows the residual rating (`approvals.md`). A notice's objection deadline is an action that comes first, with a decision date well ahead of it; put the draft objection, conditional and withdrawable once evidence arrives, in `requests` as `objection`. If the company is itself a processor for customers whose data reaches the vendor, its own customer DPAs may require earlier notice of the new sub-processor; add that as an action.

Reassess each vendor at least every 12 months, sooner for Deep reviews, after a material AI model change, or before an AIUC-1 certificate expires. When the facts touch a law the reference files don't cover, such as call recording, biometrics, or background checks, raise it from `dpa-checklist.md` section 9 as a verify flag for counsel.
