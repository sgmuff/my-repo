---
name: dsr-response
description: Handle a data subject or consumer privacy request end to end. Classify the request (access, deletion, correction, portability, opt-out, limit, objection, appeal), work out which laws apply and whether the company answers or forwards it as a processor, calculate every deadline, set proportionate identity verification, find the data, apply exceptions, and draft the acknowledgment, verification request, extension notice, and response for a person to send. Covers GDPR, UK GDPR, Swiss FADP, US state privacy laws including CCPA, FERPA, and COPPA. Use it whenever someone forwards a privacy request from a customer, user, employee, parent, or authorized agent, or asks about a DSAR, "right to be forgotten," "delete my data," "do not sell," opt-out, request deadline, or appeal, even if they don't call it a DSR. Not for breaches (incident-assessment), privacy notice changes (notice-and-policy), or documenting processing (ropa).
---

# Data subject request response

This skill handles one request at a time, from the moment it arrives to the drafted reply. Deadlines start running when the request is received, so the skill's first job is to find the clock and protect it.

The skill classifies the request, applies the law, calculates the dates, and drafts. It doesn't send anything, verify anyone's identity itself, delete data, or decide to refuse a request. A person does each of those (`approvals.md`). Every message to the requester is a draft that the privacy lead approves.

## Files

| File | Read it when |
|---|---|
| [`../_shared/conventions.md`](../_shared/conventions.md) | At the start of every run |
| [`../_shared/company-profile.md`](../_shared/company-profile.md) | At the start, for the controller identity and the regimes in scope |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Steps 6 and 8 |
| [`../_shared/references/dsr-matrix.md`](../_shared/references/dsr-matrix.md) | Steps 2–7: which law applies, request types, deadlines, verification, exceptions, response content |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md) | Territorial scope (§1a), rights (§5), automated decisions (§6) |
| [`../_shared/references/us-state-privacy.md`](../_shared/references/us-state-privacy.md) | State applicability (§2) and exemptions (§10) |
| [`../_shared/references/ferpa.md`](../_shared/references/ferpa.md) | Requests about student data, and COPPA |
| [`scripts/deadlines.py`](scripts/deadlines.py) | Step 3: compute every deadline |
| [`assets/dsr-case-template.md`](assets/dsr-case-template.md) | Step 8: the case file |
| [`assets/response-letters.md`](assets/response-letters.md) | Step 8: draft messages to the requester |

## Workflow

### 1. Capture the request and check for urgency

Record exactly what was received: the channel, the date and time received, the requester's words (quoted), and any attachments. Check `<output root>/dsr/` for earlier requests from the same person. Repeat requests affect fees and "manifestly excessive" judgments, and an open request may already have a clock running.

If the request mentions a breach, a regulator, a lawsuit, or a complaint already filed, say so at once and bring in the privacy lead. If it mentions a breach, also point to `incident-assessment` (or, until that skill exists, to counsel).

### 2. Classify and decide who answers

Using `dsr-matrix.md`, §1–2:

- **Request types:** a single message often contains several, such as "send me my data and then delete it." List each one.
- **Company role for this person's data:** controller or business (the company answers), processor or service provider (forward to the customer under the DPA), or FERPA school official (forward to the institution). If the company is a processor, refer the request promptly to the controller and **assist** it as the DPA and GDPR Art. 28(3)(e) require. The deliverable is the referral and the help, not a substantive answer, and the person isn't simply sent away. If the company is a school official, the district is the likely lead for FERPA, but that doesn't replace the company's own obligations. Check separately whether the company processes the data for any purpose of its own, which brings direct duties (COPPA operator duties stay with the operator even under school authorization; state student privacy laws reach vendors directly). Check how the account came to exist: an account the company provisions for a customer or district differs from one a person or parent created directly, and a direct account usually makes the company the controller (and, for children under 13, the COPPA operator who answers the parent).
- **Applicable laws:** by territorial scope, residency, thresholds, and exemptions, each marked Provisional where facts are missing (`conventions.md`, §7). Employee, applicant, and B2B data need each state's exemption checked, not assumed.
- **Requester:** the person, a parent or guardian, or an authorized agent.

### 3. Calculate the deadlines

Run `python3 scripts/deadlines.py <received date> <regimes…>` with every regime that may apply. Record each date in the case file's deadline table, and put the earliest substantive deadline at the top of the case file and the reply. Check public holidays by hand.

Where residency or role is unknown, include the regimes it could be, and work to the earliest date until the question is settled. Label each date as statutory or an internal target. Forwarding to a controller or district is immediate once the right contact is known, not scheduled for days later. Deadlines are actions in the case file, never calendar events (`connectors.md`).

### 4. Set proportionate verification

Using `dsr-matrix.md`, §4, propose the verification method. Start with what the company already holds (an account login, the email on file) before asking for anything new. Don't ask for ID documents by default, and don't ask for verification of opt-out requests beyond what's needed to apply them. For an agent, ask for the person's signed permission.

The verification request is a draft message. A person checks the evidence and records that verification succeeded or failed.

**Until the requester is verified, don't confirm or deny that the company holds their data,** or that an account exists. The acknowledgment says the request was received and what happens next, and nothing more about the person.

### 5. Find the data

List where this person's data may be, starting from the RoPA (`<output root>/registers/ropa/`): each activity and system that holds data about this kind of person, and each processor that must act (deletion and correction reach processors). Turn the list into search tasks with owners. Systems the RoPA doesn't cover are a gap; note them for `ropa`.

The skill doesn't search systems itself unless a connected tool gives it read access and the user asks. Even then, record what was searched, and when.

### 6. Apply exceptions and decide what to disclose

Using `dsr-matrix.md`, §5–6, draft the position for each request type:

- What will be provided, deleted, corrected, or applied
- Any exception relied on, with the provision. Exceptions are legal determinations: mark them Provisional, and add a `Decision needed` block for the privacy lead.
- Redactions for other people's data (GDPR Art. 15(4)), and data that must never be sent in a California response (government ID and account numbers, passwords, biometrics; CCPA Regs. § 7024(d))
- What processors must do, and the instruction to send them

A refusal, partial refusal, or fee is never decided by the skill.

**Coordinate access and deletion; don't make one rigidly wait for the other.** When a person asks for a copy and deletion, preserve a controlled, secure copy for the access response, and run the deletion review (Art. 17 exceptions, legal holds, retention duties) in parallel, so both are done without undue delay. Pause automatic purge jobs only as far as needed to answer the access request, and record the scope of the pause. When deleting, check for upstream feeds that would recreate the data, such as a roster sync, a CRM import, or a customer integration, and ask the source to stop sending it.

**Treat access and erasure as separate workstreams**, each with its own legal basis, approver, and outcome. Under FERPA, parents can inspect and seek amendment, but FERPA gives no general right to delete accurate records. Deletion may still be required by COPPA, a state student privacy law, the contract, or the company's own retention commitments.

**Preservation holds have a scope and an end.** Hold what's needed to answer the request or a dispute, record why, and resolve the deletion question promptly. "Delete nothing until told otherwise" is not a hold policy.

### 7. Draft the messages

Use `assets/response-letters.md`. Draft only the messages this request needs now, usually the acknowledgment and a verification request, then the response once the data is gathered. Each draft:

- Opens with "DRAFT: not sent"
- Uses plain language the requester will understand, with no internal notes, risk ratings, or system names they don't need
- States the deadline that applies and, for any refusal, the reasons and how to appeal or complain
- For an extension, gives the reasons and the new date, and goes out before the original deadline

Offer to save the drafts as email drafts if an email tool is connected. Never send them.

### 8. Write the case file and hand back

Fill in `assets/dsr-case-template.md`. Save it to `<output root>/dsr/YYYY/YYYY-MM-DD-<request-id>.md`, where the date is the **received** date, ID `DSR-YYYY-NNN`. Save the message drafts beside it as `YYYY-MM-DD-<request-id>-drafts.md`, and link them from the case file's messages table. Set status to Draft (or "Forwarded" when the company is a processor). If Jira or ServiceNow is connected and the company tracks requests there, offer to create or update the ticket after the user confirms.

Reply in about 150 words: the case path, the request types, the laws (with statuses), the **earliest deadline**, the next message to send (a draft, awaiting approval), and any decision needed.

## Keeping the record

Keep the case file for at least 24 months after closing (CCPA Regs. § 7101), and keep only what's needed to show compliance. Delete identity documents collected only for verification once the request closes. When the request reveals a gap, such as a system missing from the RoPA, a processor that can't delete, or a notice that doesn't describe a use, record it as a follow-on for the relevant skill.
