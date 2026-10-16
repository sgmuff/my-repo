# Approvals

This file says who approves what. It is deliberately short: one table of decisions, one rule for recording approval, and one log.

The skills prepare decisions. They never make them. Accountability for a legal determination, for accepting risk, or for anything that leaves the organization stays with a person, so every skill stops at the points below and asks.

## Decision table

"Privacy lead" and the other roles refer to the people named in `company-profile.md`. "Business owner" means the contact for the requesting business area, or for the system owner when someone else requested the review.

| Decision | Approver | Also informed or consulted | Notes |
|---|---|---|---|
| Legal determination: whether a DPIA, state assessment, notification, or FRIA is required; lawful basis; EU AI Act classification; whether a law applies | Privacy lead | Legal counsel when the privacy lead asks, or when the call is close | The skill gives a position and its reasoning. The privacy lead confirms or changes it. |
| Accepting residual risk rated Low | Privacy lead | Business owner (informed) | |
| Accepting residual risk rated Medium | Privacy lead **and** business owner | Security contact if the risk is a security risk | The business owner accepts the risk for their area. The privacy lead confirms the rating. |
| Accepting residual risk rated High | Executive risk approver | Privacy lead, business owner, DPO | Under GDPR, a High residual risk also triggers prior consultation (`references/gdpr.md`, §10). |
| Anything sent outside the organization: regulators, data subjects, customers, vendors, auditors, the public | Privacy lead | Legal counsel for regulators and litigation risk | The skill drafts. A person sends. |
| Publishing an assessment (Confluence or elsewhere) | Privacy lead | Business owner | |
| RoPA entry: facts | Business owner | System owner | Confirms the description is accurate |
| RoPA entry: record type, lawful bases, transfer mechanisms, and approval | Privacy lead | | |
| Vendor onboarding or renewal | Approver for the vendor review's current residual rating (rows above) | Legal or Procurement for contract and commercial findings | A request list to the vendor is an external communication |
| Changing a reference file in `_shared/references/` | Privacy lead | | `regulatory-change` proposes edits; it never applies them unasked. |

If a business area has no named contact, the skill records "TBC" and adds it to the open questions. It does not block on it.

**Which rating picks the approver.** Route by the **current** residual rating, the one based on verified controls (`references/risk-method.md`, §1). An approver may accept a target rating instead, but the approval must name the actions that have to close, with evidence, before launch.

**Who does what.** The roles stay separate even when one person holds several: the skill prepares; the DPO or counsel advises; the approver in the table accepts the risk; and the launch is authorized only when the sign-off section records that acceptance and the launch blockers are verified. A draft never authorizes processing (`conventions.md`, §7).

## Recording an approval

Approval is recorded in two places, both by the skill when the approver tells it to:

1. **The deliverable's sign-off table.** Name, role, date, decision, and conditions.
2. **The approval log**, `<output root>/approvals/approval-log.md`. One row per decision, using `templates/approval-record.md`.

Low friction matters more than ceremony. An approver can approve in the session ("approve DPIA-2026-004 with conditions A1 to A3") or by any channel the company already uses. The skill records who approved, the date, the channel, and what was approved. It never records an approval it didn't receive, and it never changes a document's status to Approved on its own judgment.

When the approval arrives by a channel the skill can't see, such as a meeting, the person recording it says so, and the log notes "recorded by <name> on behalf of <approver>."

## Assessment stages

An assessment passes through four stages. Never collapse them into a single "complete." Record the current stage in the status block and the metadata (`stage:`):

| Stage | Means |
|---|---|
| **Screening complete** | Enough evidence to decide whether an assessment is warranted |
| **Draft complete** | Processing and risks documented, with unresolved facts identified |
| **Ready for sign-off** | The evidence, safeguards, legal determinations, and consultation decisions needed for approval are in place |
| **Authorized to launch** | Approval recorded, and every pre-launch condition verified with evidence |

Every assessment also keeps three lists apart, because they have different owners:

1. **Facts to confirm** (the fact register)
2. **Controls to put in place** before launch (launch-blocking actions)
3. **Decisions needing approval** (the `Decision needed` blocks)

A missing control is an action, not a TBC fact.

## Who decides what

- **Privacy lead or legal counsel:** whether a law applies, whether an obligation is triggered, roles, lawful bases, and consultation duties.
- **Business owner:** the facts about the activity, and the business decision to go ahead (such as California's "whether the business will start the processing"), made on the privacy determination.
- **Control owners:** evidence that their controls work.
- **Executive:** attestations the law assigns to an executive, and acceptance of High residual risk where the law permits it.

## Status lifecycle

Every deliverable carries one of these statuses in its document control section:

- **Draft:** prepared by a skill or a person, and not yet reviewed
- **In review:** sent to the approvers
- **Approved:** every required approval recorded
- **Approved with conditions:** approved, with open actions that are conditions of approval
- **Rejected:** the approver declined. Record the reason.
- **Superseded:** replaced by a newer version, which the document links to

A skill can move a document from Draft to In review when it hands the document over for approval. Only a recorded approval moves it further.
