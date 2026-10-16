# Vendor review test scenarios

The trigger lists are also in `trigger-evals.json`. The full-run cases, with fixture documents in `files/`, are in `evals.json`.

## Should trigger

| # | Request | Why it belongs here |
|---|---|---|
| 1 | "Sales wants Lumen Notes for customer calls. Here's their DPA and AI terms. Can we sign?" | Vendor onboarding with an AI module |
| 2 | "Our helpdesk vendor just emailed that they're adding Quillwave AI in Singapore as a subprocessor. 30 days to object, notice came Oct 10." | Subprocessor notice with an objection window |
| 3 | "Is the Zoom AI Companion we turned on last month OK from a privacy standpoint?" | AI feature embedded in an existing tool, possibly turned on before review |
| 4 | "redline this DPA against Art 28 and tell me what's missing" | DPA gap analysis |
| 5 | "Annual reassessment for our payroll provider is due; their SOC 2 is attached" | Reassessment |
| 6 | "Does this edtech vendor's contract meet FERPA and NY Ed Law 2-d?" | Student data contract terms |
| 7 | "Procurement sent me a security questionnaire back from a CRM vendor. Anything privacy-wise I should push on?" | Questionnaire review for privacy |
| 8 | "Check whether OpenAI's enterprise terms let them train on our data and whether they're AIUC-1 certified" | AI provider review in benchmark mode |

## Should not trigger (near misses)

| # | Request | Where it belongs |
|---|---|---|
| 1 | "Do we need a DPIA for the new churn model?" | `dpia` |
| 2 | "Add Lumen to the RoPA as a recipient for sales calls." | `ropa` |
| 3 | "Our vendor had a breach that exposed our customers' emails. Do we have to notify?" | `incident-assessment` |
| 4 | "Write our own DPA template that we give to customers." | Not a vendor review; a contract drafting task for Legal |
| 5 | "Inventory every AI tool employees use and tier them by risk." | `ai-intake` |
| 6 | "Our customer sent us their vendor questionnaire to fill in about our product." | The company is the vendor here; a response task, not a review |
| 7 | "We're buying an AI note-taker that records student tutoring sessions. What do we need to do?" | `privacy-governance` first: spans vendor review, AI intake, DPIA, and RoPA |

## What a good run looks like

- Reads `conventions.md` and the company profile; checks for earlier reviews of the vendor and for activities that use it.
- Scopes services and features, sets the depth with a reason, and proposes roles per operation (Provisional), including a controller role for any own-purpose use.
- Sends a short Round 1 that asks for **documents**, and treats trust center pages and questionnaire answers as "Stated by vendor."
- Rates each checklist item Present, Partial, Missing, or Conflicts, with the clause reference and the legal basis, and reads the order of precedence first.
- For AI vendors: training, retention, outputs, agent actions, model changes, and AIUC-1 certification (product, release, date, exclusions), plus EU AI Act roles and the classification of the company's use by function.
- Verifies transfers for the right entity and framework scope (EU, UK, Swiss), or flags them.
- Rates risks to individuals with three ratings; keeps contractual and commercial findings separate for Legal and Procurement; treats unsigned terms as planned controls.
- Writes the review and a separate draft request list (metadata first, then "DRAFT: not sent").
- States "Onboarding decision: Not authorized by this draft," routes by the current rating, and recommends follow-ons (DPIA screening, RoPA, AI impact assessment) without running them.
- Puts objection deadlines and reassessment dates in the action plan, never on a calendar.
- Replies in about 150 words.
