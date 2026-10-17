# DSR response test scenarios

The trigger lists are also in `trigger-evals.json`. The full-run cases are in `evals.json`.

## Should trigger

| # | Request | Why it belongs here |
|---|---|---|
| 1 | "Got this email Tuesday from a user in Berlin: 'Under Article 15 I want all the data you have on me and then delete my account.' What do we do?" | Access plus deletion under GDPR |
| 2 | "A California customer used our webform to say Do Not Sell My Info. Anything we need to do?" | CCPA opt-out, 15 business days |
| 3 | "An authorized agent company sent deletion requests for 40 people. Do we have to honor these?" | Authorized agent verification |
| 4 | "A parent wants to see everything our reading app has on their 9-year-old." | COPPA and FERPA; likely forward to the district |
| 5 | "Former employee in Ireland asked for all emails mentioning her." | Employee DSAR; proportionate search; third-party redaction |
| 6 | "We denied a Virginia deletion request last month and they're appealing. What's our deadline?" | State appeal |
| 7 | "Customer of a customer emailed us asking us to delete their data from our platform." | Processor forwarding |

## Should not trigger (near misses)

| # | Request | Where it belongs |
|---|---|---|
| 1 | "Write a DSAR procedure for the support team." | `notice-and-policy` or a policy task, not one request |
| 2 | "We accidentally emailed one customer's export to another customer." | `incident-assessment` |
| 3 | "Update the privacy notice to explain how to make a request." | `notice-and-policy` |
| 4 | "Add our DSR tool to the RoPA." | `ropa` |
| 5 | "Review our DSR vendor's DPA." | `vendor-review` |

## What a good run looks like

- Captures the received date and the requester's words. Checks for earlier requests.
- Classifies each request type, decides who answers (controller answers; processor forwards; school official forwards), and marks laws Provisional where residency or scope is unknown.
- Runs `scripts/deadlines.py`, puts the **earliest deadline** at the top, and works to the shortest plausible deadline when residency is unknown. No calendar events.
- Proposes proportionate verification: existing account or email first, no ID documents by default, none for opt-outs beyond what's needed.
- Lists where the data is from the RoPA, with search owners, and the processors that must act.
- Drafts only the messages needed now, each starting "DRAFT: not sent," in plain language.
- Routes any refusal, partial refusal, fee, or extension to the privacy lead as a decision.
- Saves the case file under `dsr/YYYY/`, and replies in about 150 words with the earliest deadline.
