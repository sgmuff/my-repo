# Example run: Support Copilot

This is a calibration case. It was written for the earlier Markdown format: the substance checklist still applies, but the output is now an `scr` and a `dpia` record that `gov` renders, so ignore the document-format items. Paste the prompt below into a new session, then compare what the skill does against the checklist, and its output against the abbreviated reference output. The company and vendor names are made up.

## Test prompt

> Need a DPIA for a new feature. PRD summary: "Support Copilot" for our helpdesk. When a customer contacts support (email or in-app chat), we send the ticket thread, including attachments, to an LLM API to (1) summarize it for the agent, (2) draft a suggested reply that the agent edits before sending, (3) set priority, and (4) attach a churn-risk score (low/med/high) to the contact's profile so CSMs can step in. Tickets the model is 95%+ confident are resolved get auto-closed after 72 hours with no reply. About 40k tickets a year from roughly 25k people, mostly EU, UK, and US (incl. CA and CO), also some Swiss. LLM vendor is US-based and DPF-certified; we haven't confirmed its retention or training settings yet. Tickets kept 3 years. We're the controller for support data. Launch planned for January 15, 2027.

## What a good run does

- [ ] Reads `../_shared/conventions.md` and `../_shared/company-profile.md` first
- [ ] Proposes roles per operation and marks them Provisional: controller for support data (stated by the requester, so recorded as "Stated by requester" in the fact register); the vendor as processor, unless it uses data for its own purposes. For the AI Act, asks whether the company is building its own Copilot or turning on a helpdesk vendor's feature, rather than pre-filling "provider and deployer."
- [ ] Sends a short Round 1 (blockers only, under about 15 questions): vendor retention and training terms (asking for the DPA and configuration as evidence), what auto-close actually affects (refunds, complaints, security reports), whether the churn score is about people or accounts and who acts on it, attachments, children, and whether staff performance will be evaluated from Copilot data. Everything else goes in Round 2 with the draft.
- [ ] Treats EDPB criteria as indicators with supporting facts, and concludes "a DPIA is warranted (Provisional)," not "no answer can change the outcome"
- [ ] Runs two separate analyses: profiling (the churn score, Art. 4(4) and Art. 21) and Art. 22 (auto-close: solely automated, and whether effects are similarly significant given real consequences). Records reversibility as a safeguard, not an exemption.
- [ ] Classifies by function: not emotion recognition (text sentiment isn't biometric), not Annex III on current facts. Notes that using Copilot data to evaluate agents could engage Annex III point 4(b). Analyzes each Art. 50 paragraph separately.
- [ ] Answers "law applies?" and "activity triggers?" separately for California and Colorado, and marks applicability Open or Provisional rather than "not triggered"
- [ ] Rates three ratings per risk. Current residual equals inherent wherever no control is verified, so R2 (special category data in free text) is High now, and the overall current rating is High. Target is Medium. The summary says "Residual risk: not yet confirmed." (Rating R1 High instead of Medium is defensible if attachments can carry ID or health data. Either way, justify the score.)
- [ ] Doesn't rule out prior consultation on the unverified target
- [ ] States the launch gate: "Not authorized by this draft"
- [ ] Gives every action a dependency, an acceptance criterion, and evidence; sequences dates before January 15, 2027; makes each verify flag an action due before launch
- [ ] Records the post-launch review as an action, never a calendar event
- [ ] Saves `compliance/assessments/dpia/2026-10-16-support-copilot.md` with status Draft, the metadata block, and the reference files used
- [ ] Routes sign-off by the current rating: High now, so the executive risk approver, unless the approver accepts the Medium target with named conditions
- [ ] Replies in about 150 words: path, status block, decisions needed, Round 1 questions, verify flag count

## Abbreviated reference output

### Executive summary

> **DPIA status:** Draft, not approved.
> **Screening:** DPIA warranted under Art. 35(1) (Provisional; F3 and F6 unverified).
> **Residual risk:** not yet confirmed. Current: **High** (no controls verified). Target: **Medium**, subject to verification of A1–A4.
> **Prior consultation:** Not required if the target is achieved and verified. Revisit when A1 and A2 close. (Provisional)
> **Launch decision:** Not authorized by this draft. Production processing must not begin until the approver named in §11 has reviewed the completed assessment, confirmed the legal determinations and roles, verified the launch-blocking actions with evidence, and recorded the residual-risk decision.
> **Other regimes:** CA CPPA risk assessment: Open (F9). Colorado: Open (F10). EU AI Act: not high-risk on current facts (Provisional; F12).

Support Copilot sends support ticket threads to a US LLM vendor, which summarizes tickets, drafts replies, sets priority, scores churn risk for each contact, and auto-closes tickets it judges resolved. Scoring of contacts (criterion 1, F3 stated by requester) and free-text communications that may contain special category data (criterion 4, F6 unverified) indicate likely high risk.

Four conditions stand between this draft and launch: zero-retention and no-training terms with the vendor, verified in the DPA and the API configuration (A1); redaction of special category data and attachments, verified by a test set (A2); auto-close limited to tickets whose closure affects no refund, complaint, or security process, with notice and reopening (A3); and an opt-out from churn scoring, with a notice update (A4).

### Risk register (excerpt)

| ID | Risk | Inherent | Current residual | Planned controls | Evidence that verifies them | Target residual |
|---|---|---|---|---|---|---|
| R1 | The vendor keeps ticket content or trains on it, so customers' messages reach a third party's model | Possible × Significant = **Medium** | **Medium** (no terms verified) | A1 | Signed DPA clause; API configuration export | Remote × Significant = **Low** |
| R2 | Health or other special category data in tickets or screenshots goes to the vendor without an Art. 9 condition | Probable × Severe = **High** | **High** (no redaction in place) | A2, A5 | Redaction test results on a labeled sample, including attachments | Possible × Significant = **Medium** |
| R4 | Wrongful auto-close leaves a customer without support, or lets a refund or complaint lapse, with no human decision | Possible × Significant = **Medium** | **Medium** | A3 | Closure exclusion list in config; notice and reopen tested | Remote × Minimal = **Low** |

### Action plan (excerpt)

| ID | Action | Depends on | Acceptance criterion | Owner | Due | Launch blocker? |
|---|---|---|---|---|---|---|
| A1 | Get a DPA amendment with zero retention and no training; turn on the matching API settings | — | Signed clause on file; configuration export shows retention off | Procurement and Legal *(proposed)* | 2026-12-01 *(proposed)* | Yes |
| A2 | Redact special category patterns and strip attachments before the vendor call | A1 (vendor endpoint chosen) | Test set of 200 labeled tickets shows no special category terms sent | Eng lead, Support Platform *(proposed)* | 2026-12-15 *(proposed)* | Yes |
| A9 | Verify the EU-US DPF listing covers the vendor entity, plus the UK Extension and Swiss-US DPF | — | Listing screenshots dated within 30 days of launch | Privacy lead *(proposed)* | 2026-12-01 *(proposed)* | Yes |
