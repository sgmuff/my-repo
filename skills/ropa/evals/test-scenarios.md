# RoPA test scenarios

The trigger lists are also in `trigger-evals.json`. The full-run cases, with fixture documents in `files/`, are in `evals.json`.

## Should trigger

| # | Request | Why it belongs here |
|---|---|---|
| 1 | "Add HR onboarding to the RoPA. Workday, background checks through Checkr, staff in the US and Ireland." | New controller entry |
| 2 | "Here's the data dictionary for Gradebook Sync. Can you turn it into a RoPA entry?" | Entry from system documentation |
| 3 | "We switched payroll providers from Gusto to Rippling. Update the record." | Update to an existing entry |
| 4 | "Build out our RoPA from this list of 30 systems." | Bulk build |
| 5 | "The Irish DPC asked for our Article 30 records. What do we send?" | Art. 30(4) request |
| 6 | "what personal data does our marketing team actually hold and why? need it written down" | Data map, without saying RoPA |
| 7 | "We're a processor for our customers' data. Do we need processor records, and can you draft them?" | Art. 30(2) processor record |

## Should not trigger (near misses)

| # | Request | Where it belongs |
|---|---|---|
| 1 | "Do we need a DPIA for Gradebook Sync?" | `dpia` |
| 2 | "Review Checkr's DPA." | `vendor-review` |
| 3 | "List all the AI tools teams are using." | `ai-intake` |
| 4 | "Update our privacy notice to cover the new data we collect in onboarding." | `notice-and-policy` |
| 5 | "An employee asked for a copy of all their HR data." | `dsr-response` |
| 6 | "Map our controls to NIST Privacy Framework ID.IM." | `program-assessment` or `controls-and-evidence` |

## What a good run looks like

- Checks the index for an existing or overlapping entry, and decides the unit (activity, not system or field).
- Records a **source** for every field (Document, Stated by, Inferred, or TBC). Never infers purposes or lawful bases from a schema.
- Proposes record type, lawful bases, Art. 9 conditions, and transfer mechanisms as Provisional.
- Leaves required fields it can't confirm as TBC, especially retention, and doesn't invent them.
- Flags follow-ons in "Related assessments": DPIA screening, vendor reviews, AI intake, notice coverage.
- Fills US state and FERPA flags where relevant.
- Creates the entry with `gov new`, fills in the YAML record, and runs `gov validate` and `gov render`. Never writes the Markdown by hand.
- Routes facts to the business owner and legal positions to the privacy lead.
- Records the next review as an action, not a calendar event.
- Replies in about 150 words.
