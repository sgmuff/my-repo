---
name: vendor-review
description: Review a vendor, subprocessor, or AI provider's data protection terms and practices, with a clause-by-clause DPA gap analysis against GDPR Article 28, US state service provider terms, FERPA and student privacy terms, and transfer rules, plus an AI module for models, agents, and AI features (training on customer data, retention, outputs, model changes, agent permissions, EU AI Act roles, AIUC-1 certification). Produces a draft review with findings, risks, a recommendation, and a draft request list for the vendor. Use it whenever someone wants to onboard, renew, or reassess a vendor, review a DPA, subprocessor notice, or security questionnaire for privacy, or check an AI vendor or an AI feature turned on in an existing tool, even without saying "vendor review." Not for the company's own processing (dpia), RoPA entries (ropa), or internal AI use-case intake (ai-intake).
---

# Vendor review

This skill reviews a third party that will process personal data for the company, or supply AI that touches it. One run produces one Markdown review per vendor, plus a draft request list the privacy lead can send to the vendor after approval.

The review supports a decision a person makes: whether to sign, renew, or keep using the vendor, and on what conditions. The skill reads the documents, compares them to the checklist, rates the findings, and drafts. It takes a position on each point, cites the clause and the law behind it, labels how settled the position is, and leaves the approval decision and anything sent to the vendor to the approvers in `approvals.md`. **Rate what the documents say, not what the vendor's sales team says.**

## Files

| File | Read it when |
|---|---|
| [`../_shared/conventions.md`](../_shared/conventions.md) | At the start of every run: style, citations, verify flags, intake rounds, fact register, determination status, output layout |
| [`../_shared/company-profile.md`](../_shared/company-profile.md) | At the start of every run, for the standard DPA, transfer mechanisms, and security baseline |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 9, to route the decision |
| [`references/intake.md`](references/intake.md) | Step 3: what to collect, tagged by round |
| [`../_shared/references/dpa-checklist.md`](../_shared/references/dpa-checklist.md) | Steps 4–6: the clause-by-clause checklist and red flags |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md) | Roles (§2), processor terms (§8), transfers (§11) |
| [`../_shared/references/us-state-privacy.md`](../_shared/references/us-state-privacy.md) | State processor and service provider terms (§4) |
| [`../_shared/references/ferpa.md`](../_shared/references/ferpa.md) | When the vendor will touch student data |
| [`../_shared/references/aiuc-1.md`](../_shared/references/aiuc-1.md) | Step 5, the AI module, in vendor benchmark mode |
| [`../_shared/references/eu-ai-act.md`](../_shared/references/eu-ai-act.md) | Step 5, for AI Act roles and deployer duties |
| [`../_shared/references/risk-method.md`](../_shared/references/risk-method.md) | Step 7: three ratings, control statuses |
| [`assets/vendor-review-template.md`](assets/vendor-review-template.md) | Step 8: the review |
| [`assets/vendor-request-template.md`](assets/vendor-request-template.md) | Step 8: the draft request list for the vendor |

## Workflow

### 1. Load context and check for an existing review

Read `conventions.md` and `company-profile.md`. Look under `<output root>/vendors/<vendor-slug>/` for earlier reviews. If one exists, this is a renewal or reassessment: read it, carry forward what still holds, and focus on what changed (new services, new AI features, new subprocessors, a new DPA version, an expired report). Also check `<output root>/registers/ropa/` and `<output root>/assessments/` for activities that use this vendor, so the review covers the actual uses.

Start the fact register (`conventions.md`, §6). For a vendor review, it records which documents were provided, their versions and dates, and what the requester has said without evidence.

### 2. Scope the review and set its depth

Pin down which services, products, and features the company uses or plans to use, and for what. One vendor can need several reviews' worth of analysis: a CRM with an AI assistant switched on is two things.

Set the review depth from the facts, and say why:

| Depth | When | What it covers |
|---|---|---|
| **Light** | No personal data, or only business contact data, with no special category, children's, student, or sensitive data, no AI on personal data, and no restricted transfers | Checklist §1–2 and §7.1, and the red flags |
| **Standard** | Personal data of customers, users, or employees at ordinary sensitivity | The full checklist, except §5–6 where they don't apply |
| **Deep** | Special category, children's, student, or US-sensitive data; large scale; AI on personal data or agents that act; restricted transfers without a settled mechanism; or the vendor is critical to the product | The full checklist, the AI module, and the transfer analysis, with evidence requested for each control the rating depends on |

Depth decides the work, not the standard. A Light review that finds a red flag becomes Standard.

Then **propose roles per operation**, marked Provisional (`gdpr.md`, §2): processor, sub-processor, service provider, contractor, third party, or controller for any own-purpose use. For AI, propose the vendor's and the company's EU AI Act roles (`eu-ai-act.md`, §3), and set AIUC-1 to **vendor benchmark** mode.

### 3. Gather documents and facts in two rounds

Use `references/intake.md`.

- **Round 1 (blockers):** the documents themselves (DPA, MSA or terms, AI terms, subprocessor list, security report) and the facts that decide depth and roles: what data, whose, for what, which features, and whether processing has already started. If it has, ask what the vendor already holds, and whether any feature, especially an AI feature, was turned on before review.
- **Round 2 (completion):** send it with the draft. Business owner and contract details, renewal dates, internal integration details, and the remaining checklist items the documents didn't answer.

Ask for documents, not summaries. A trust center page, a questionnaire answer, or a sales email is evidence of a claim, not a contract term. Record it as "Stated by vendor" in the fact register.

### 4. Run the DPA gap analysis

Work through `dpa-checklist.md` §1–4 and §7 (and §5 for student data). For each item, record:

- What the contract says, quoted briefly, with the document and clause reference
- The rating: **Present**, **Partial**, **Missing**, **Conflicts**, or **Not provided** (the document wasn't supplied; ask for it, and don't guess)
- The legal basis for the requirement (the checklist's citation)
- What fixes it: a contract change, a configuration, or a compensating control

Read the order of precedence between documents before rating anything (checklist 1.3). A strong DPA that an MSA or online AI terms override is a Conflicts finding.

Compare to the company's standard DPA where the profile gives one, and note each departure.

### 5. Run the AI module, if the vendor supplies AI

Use `dpa-checklist.md` §6, benchmarked to AIUC-1 (Oct 15, 2026 release; check `aiuc-1.md` for a newer one). Cover AI features embedded in products the company already buys, not only AI vendors.

- **Training, retention, outputs, isolation, agent actions, model changes, incidents, logging, and transparency:** rate each against the contract and configuration evidence, with the AIUC-1 requirement it corresponds to.
- **AIUC-1 certification:** if the vendor claims it, ask for the certificate and audit report. Record the product in scope, the release audited, the report date, the expiry, whether quarterly evaluations are current, and the exclusions. A certificate for a different product doesn't cover this one. If the vendor isn't certified, ask about the applicable mandatory requirements (checklist 6.12).
- **EU AI Act:** propose the roles, classify the company's intended use by function (`eu-ai-act.md`, §4–5), and list what the vendor must supply for the company's deployer duties. If the use could be high-risk or prohibited, say so and recommend an `ai-impact-assessment`. If that skill isn't installed yet, add an action to produce one.

### 6. Check transfers and security assurance

**Transfers** (checklist §3): for each restricted transfer, confirm the mechanism for the right vendor entity and destination. For the DPF, check the active listing and its scope (EU, UK Extension, Swiss) on dataprivacyframework.gov when you can browse, and record the date. Otherwise make it a verify flag. Confirm SCCs as a fallback. Where a transfer relies on SCCs, BCRs, the IDTA, or the UK Addendum, recommend the `tia` skill for that flow and link its ID once it exists. When the vendor supplies its own transfer assessment, review it here, against `tia/references/steps.md`; don't start a new TIA just to restate it.

**Security assurance** (checklist §7.1): record the report type, date, scope, and noted exceptions, and whether the scope covers the service in use. A deep security review belongs to the security team. Note what they should look at, and don't rate controls you haven't seen evidence for.

### 7. Rate risks

Use `risk-method.md` and `../_shared/templates/risk-register.md`, with three ratings (inherent, current residual, target residual) and control statuses. Rate **risks to individuals** in the register. Record contractual and operational risks to the company (unfavorable liability terms, lock-in, weak exit rights) in a separate findings column for Legal and Procurement, without mixing them into the privacy rating.

Unconfirmed contract terms are not controls. If the fix is "the vendor will sign our DPA," the current rating stays where it is until a signed version exists.

### 8. Write the review and the request list

Fill in `assets/vendor-review-template.md` and save it to `<output root>/vendors/<vendor-slug>/YYYY-MM-DD-review.md`, ID `VR-YYYY-NNN`. Set status to Draft.

The executive summary opens with the status block:

> **Review status:** Draft, not approved. Depth: <Light | Standard | Deep>.
> **Recommendation:** <Approve | Approve with conditions | Do not approve as proposed> (Provisional; depends on F…).
> **Residual risk:** <not yet confirmed | confirmed>. Current: <rating>. Target: <rating>, subject to A….
> **Onboarding decision:** Not authorized by this draft. Don't sign, renew, or turn on the service for personal data until the approver named in the sign-off section has recorded a decision, and the conditions marked as blockers are verified.
> **Follow-on assessments:** <DPIA screening, AI impact assessment, RoPA update, as needed>.

Then fill in `assets/vendor-request-template.md` with the documents still needed, the contract changes requested (with suggested wording where useful), and the configuration changes to confirm. Save it beside the review as `YYYY-MM-DD-vendor-requests.md`. It is an external communication: metadata first, then "DRAFT: not sent" as the first body line. The privacy lead approves it before anyone sends it.

Give each finding a status: Confirmed finding (documented), Unverified concern, or Recommended control (`conventions.md`, §6). List the approval conditions as verifiable release gates, each with the evidence that closes it. If the service is already in use, put containment first, including what was already recorded, scored, or used for training.

Cross-reference facts `F`, findings `G`, risks `R`, and actions `A` both ways. Every action has an owner, due date, dependency, and acceptance criterion; every verify flag is in the verification register and has an action (`conventions.md`, §4).

### 9. Route the decision and recommend follow-ons

Route sign-off by the current residual rating (`approvals.md`), with the requesting business area and the system owner. Recommend, but don't run, the follow-ons the findings call for:

- `dpia`, if the use the vendor supports shows high-risk indicators
- `ropa`, to add the vendor as a recipient or processor in each affected record
- `ai-impact-assessment`, if an AI use could be high-risk

If Jira or ServiceNow is connected, offer to create tickets for the actions after the user confirms the list. Otherwise put the CSV import block in the review's appendix. Never create calendar events. Renewal and reassessment dates are actions.

### 10. Hand back

Follow `conventions.md`, §11. Reply in about 150 words: the review path and the request list path, the status block in two lines, the decisions needed, the Round 1 requests still outstanding, and the count of verify flags.

## Reassessments and subprocessor notices

When a vendor sends a subprocessor change notice or new terms, don't redo the whole review. Read the notice, update the affected checklist items and risks, add a version history row, and say whether the change needs an objection within the notice period (checklist 3.1). Treat the objection deadline as an action with a due date, and put it first, with a decision date far enough ahead of it to send the objection.

- **Draft objection text** goes in the vendor request list's objection section (`assets/vendor-request-template.md`), marked as a draft. Write it as a conditional objection that the company can withdraw once the evidence arrives. That way, the company keeps its position if the deadline comes first.
- **Onward notice.** If the company is itself a processor for customers whose data reaches the vendor, check the company's own customer DPAs. The company may owe its customers notice of the new sub-processor, often with an earlier deadline than its own objection window. Add that as an action too.

When the facts touch a law the reference files don't cover, such as call recording, biometrics, consumer health data, or background checks, raise it from `dpa-checklist.md` §9 as a verify flag for Legal.

Reassess each vendor at least every 12 months, sooner for Deep reviews, AI vendors after a material model change, or AIUC-1-certified vendors whose certificate is about to expire.
