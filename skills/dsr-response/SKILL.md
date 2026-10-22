---
name: dsr-response
description: Handle a data subject or consumer privacy request end to end and record it as a gov case. Classify the request (access, deletion, correction, portability, opt-out, limit, objection, appeal), work out which laws apply and whether the company answers or forwards it as a processor, compute every deadline, set proportionate identity verification, find the data, apply exceptions, and draft the acknowledgment, verification request, extension notice, and response for a person to send. Covers GDPR, UK GDPR, Swiss FADP, US state privacy laws including CCPA, FERPA, and COPPA. Use it whenever someone forwards a privacy request from a customer, user, employee, parent, or authorized agent, or asks about a DSAR, "right to be forgotten," "delete my data," "do not sell," opt-out, request deadline, or appeal, even if they don't call it a DSR. Not for breaches (incident-assessment), privacy notice changes (notice-and-policy), or documenting processing (ropa).
compatibility: Requires the gov command from this repository (skills/install.sh installs it), with Python 3.10+, PyYAML, jsonschema, and Jinja2.
---

# Data subject request response

This skill handles one request at a time and records it as a `dsr` case. Deadlines run from receipt, so its first job is to find the clock and protect it. Never write or edit a record's `.md` file; `gov` writes it.

The skill classifies, applies the law, and drafts. It doesn't send anything, verify anyone, delete data, or decide to refuse. A person does each of those (`approvals.md`), and `gov validate` rejects a record that says Claude did.

## Files

| File | Read it when |
|---|---|
| [`../_shared/references/dsr-matrix.md`](../_shared/references/dsr-matrix.md) | Steps 2-4: which law applies, deadlines, verification, exceptions, response content |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md) | Territorial scope (§1a), rights (§5), automated decisions (§6) |
| [`../_shared/references/us-state-privacy.md`](../_shared/references/us-state-privacy.md) | State applicability (§2) and exemptions (§10) |
| [`../_shared/references/ferpa.md`](../_shared/references/ferpa.md) | Student data, and COPPA |
| [`assets/response-letters.md`](assets/response-letters.md) | Step 4: the message drafts |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 5 |

## Workflow

### 1. Check the tool, earlier requests, and urgency

Run `gov --version`; if it fails, stop and tell the user to run `skills/install.sh`. Read `compliance/dsr/index.md` for earlier requests from the same person: repeats affect fees and "manifestly excessive" judgments, and an open request may already have a clock running. If the request mentions a breach, a regulator, a lawsuit, or a complaint already filed, say so first and bring in the privacy lead; a breach also goes to `incident-assessment`.

### 2. Answer the request

Answer it fully, then check it against `dsr-matrix.md` and add what you missed. Points answers often miss:

- **One message often holds several requests**, such as "send me my data and then delete it." List each.
- **Who answers depends on how the account came to exist.** An account the company provisions for a customer or district makes it a processor or school official: refer the request to the controller or institution at once, and help as the DPA and GDPR Art. 28(3)(e) require, rather than sending the person away. An account a person or parent created directly usually makes the company the controller (and, for children under 13, the COPPA operator). Check whether the company also uses the data for its own purposes, which brings direct duties.
- **Employee, applicant, and B2B data** need each state's exemption checked, not assumed.
- **Until the requester is verified, confirm nothing**, not even that an account exists. Start verification from what the company already holds; don't ask for ID documents by default, or verify opt-outs beyond what's needed to apply them. An agent needs the person's signed permission.
- **Run access and deletion in parallel.** Preserve a controlled copy for the access response while the deletion review (Art. 17 exceptions, legal holds) runs. Pause purge jobs only as far as needed, check for upstream feeds that would recreate the data, and remember that deletion and correction reach processors.
- **Under FERPA, parents can inspect and seek amendment, but there's no general right to delete accurate records.** Deletion may still follow from COPPA, a state student privacy law, or the contract.
- **A hold has a scope and an end.** "Delete nothing until told otherwise" isn't a hold.
- **Never send government ID or account numbers, passwords, or biometrics in a California response** (CCPA Regs. § 7024(d)), and redact other people's data (GDPR Art. 15(4)).

### 3. Record it

Run `gov new dsr --slug <request-types> --title "<request types>, <requester kind>" --date <today>`, then set `received.date` to the date the request reached the company's inbox or channel, in the company's time zone, even if nobody read it until later. Keep the person's name, contact details, and any child's details out of the record and the drafts: use `requester_ref` for the ticket or inbox reference, and placeholders in drafts. Fill in the record from your answer: the request in the requester's words (without quotation marks), one `roles` row per account or data set with its role, `regimes` with each regime a known fact points to until residency and role are settled (gov computes the deadlines and works to the earliest; a regime the facts rule out is a Provisional false row in `laws`), any deadline in the customer's or district's agreement in `contract_deadlines`, the laws as Provisional calls, the verification method, where the data is (with RoPA IDs, or `none` for a gap), the processors that must act, any preservation hold with its scope and end, and one position per request and account. An exception, refusal, partial refusal, or fee is a Provisional position with an open question for the privacy lead.

### 4. Draft the messages

Add only the messages this request needs now to `messages`, usually the acknowledgment and a verification request, or the referral for a processor case, each from `assets/response-letters.md`, in plain language without internal notes or system names. State the deadline, and for any refusal the reasons and how to appeal or complain. An extension notice gives the reasons and the new date and goes out before the first deadline. Offer to save the drafts as email drafts if an email tool is connected; never send them.

### 5. Validate, render, and reply

Run `gov validate`, fix errors, and resolve findings by changing the record; a finding that names a real gap stays open with an action. Don't add a `finding_responses` entry yourself. Run `gov render`, which writes the case, the drafts under `compliance/dsr/drafts/`, and the index. If Jira or ServiceNow is connected and the company tracks requests there, offer to update the ticket.

Reply in plain English: the earliest deadline first, then the request types, who answers, the laws (with statuses), the next message to send (a draft awaiting approval), the decisions needed, and up to five questions. If the company profile lacks the contact details the messages need, ask for them. Close with one line naming the case and its path.

## Keeping the record

When a person sends a message, they record `approved_by`, `sent`, and `sent_by`. Set `extended_deadline` only once an extension notice went out in time, `responded` when the response goes out, and `closed` when the case closes; leadership reports time requests from `received` to `responded`. The rendered case shows the retention date (24 months after closing, CCPA Regs. § 7101); delete identity documents collected only for verification at closing. Record gaps the request reveals in `follow_ons`: a system missing from the RoPA, a processor that can't delete, a notice that doesn't describe a use.
