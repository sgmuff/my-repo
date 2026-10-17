---
name: ropa
description: Create, update, or bulk-build record of processing activities (RoPA) entries from intake answers, interviews, or system documentation such as PRDs, architecture docs, data dictionaries, schemas, and vendor lists, covering GDPR Article 30 controller and processor records, Swiss FADP Article 12, and the data inventory duties in US state laws, and keep the register's index current. Use it whenever someone wants to document, map, or inventory what personal data a system, team, or process handles, add or update a processing activity, build a data map, answer "what data do we hold and why," or prepare RoPA records for an audit or regulator request, even if they don't say "RoPA." Not for deciding whether an activity is high risk or needs a DPIA (dpia), reviewing a vendor's contract (vendor-review), or inventorying AI systems and agents (ai-intake).
---

# Record of processing activities

This skill turns what people know, and what documents show, into RoPA entries that hold up to an auditor: one Markdown file per processing activity, plus an index of the whole register.

A RoPA is mostly facts, but it carries a few legal positions, such as roles, lawful bases, and transfer mechanisms. The skill records the facts with their sources, proposes the legal positions as Provisional, and leaves confirmation to the privacy lead and the business owner (`approvals.md`). **A register entry is only as good as its sources.** Record where each field came from, so the next reviewer can tell a confirmed fact from an inference.

## Files

| File | Read it when |
|---|---|
| [`../_shared/conventions.md`](../_shared/conventions.md) | At the start of every run |
| [`../_shared/company-profile.md`](../_shared/company-profile.md) | At the start of every run, for the controller identity, DPO, and standard transfer mechanisms |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 7 |
| [`references/fields.md`](references/fields.md) | Steps 2–5: every field, what fills it, and the legal provision behind it |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md) | Art. 30 contents (§7), roles (§2), lawful bases (§3), transfers (§11) |
| [`../_shared/references/us-state-privacy.md`](../_shared/references/us-state-privacy.md) | State fields: sale, sharing, targeted advertising, sensitive data, the Minnesota inventory |
| [`../_shared/references/ferpa.md`](../_shared/references/ferpa.md) | When the activity uses student data |
| [`../_shared/references/nist-privacy-framework.md`](../_shared/references/nist-privacy-framework.md) | Step 5, to tag the entry (ID.IM-P1 to P8) |
| [`assets/ropa-entry-template.md`](assets/ropa-entry-template.md) | Step 5 |
| [`assets/ropa-index-template.md`](assets/ropa-index-template.md) | Step 6, if no index exists |
| [`../_shared/scripts/build_register_index.py`](../_shared/scripts/build_register_index.py) | Step 6, to rebuild the index from the entries |

## Workflow

### 1. Load context and find existing entries

Read `conventions.md` and `company-profile.md`. Read `<output root>/registers/ropa/index.md`, if it exists, and look for an entry covering the same activity. Match on purpose and system, not only on name. "Customer support" and "Helpdesk" may be the same activity.

- **Existing entry:** update it. Change only the affected fields, add a version history row, and reset its status to Draft.
- **Overlapping entries:** if two entries describe the same activity, say so, and propose merging them, rather than adding a third.
- **New entry:** continue.

**Decide the unit.** One entry per processing activity: a purpose, or a set of closely related purposes, carried out on a defined set of data. Not one per system (a CRM supports several activities) and not one per data field. When the source is a system inventory, map systems to activities first, and show the mapping.

**Split by jurisdiction when it matters.** If the controller entity, purposes, lawful bases, recipients, or transfer mechanisms differ materially between countries (for example, Irish and US employees), use separate entries, or make each difference explicit in one entry with a column per jurisdiction. Don't hide differences in one generic entry. Assign vendor roles per activity, not per vendor relationship.

### 2. Read the sources and fill what you can

Read everything provided: intake answers, PRDs, architecture and data-flow docs, data dictionaries, schemas, vendor lists, privacy notices, earlier DPIAs, and vendor reviews under `<output root>/vendors/`.

Fill each field in `references/fields.md`, and record its **source** in the entry's source column: Document (name it), Stated by (name the person), Inferred (say from what), or TBC.

What documents can and can't tell you:

- A schema or data dictionary shows **data elements**. It doesn't show **purposes** or **lawful bases**, so don't infer either from column names.
- A vendor list shows **recipients**. It doesn't show what each vendor receives. Check the vendor review, or ask.
- A privacy notice shows what the company **says**. Record the facts and note any gap. The `notice-and-policy` skill, once built, takes the gap further.

### 3. Propose roles and legal positions

Propose, and mark Provisional (`conventions.md`, §7):

- **Record type:** controller record (GDPR Art. 30(1)), processor record (Art. 30(2)), or both. Roles follow the facts, operation by operation (`gdpr.md`, §2). A processor record covers processing carried out on behalf of customers, usually one per service or customer category.
- **Lawful basis per purpose**, and the Art. 9 condition where special category data is processed. Art. 30 doesn't require the basis, but the record is where people look for it, and the privacy notice needs it.
- **Transfer mechanism** for each restricted transfer, checked against the company profile and the vendor review.
- **US state flags:** whether the activity involves sale, sharing for cross-context behavioral advertising, targeted advertising, sensitive data, or profiling (`us-state-privacy.md`, §3).
- **FERPA:** whether education records are involved, and the exception relied on (`ferpa.md`, §3–4).

### 4. Ask for the gaps

Ask in two rounds, as `conventions.md`, §6 describes:

- **Round 1, sent first and alone (usually under 12 questions):** the facts behind any proposed role, missing purposes, and anything that triggers a follow-on review (below). Pick only the questions that are actually open.
- **Round 2, sent with the draft entry:** the remaining required fields (retention, recipients, transfers, security) and the enrichment fields (systems, owners, review cadence). Put these in the entry's open questions section, not in the first message.

Ask for documents where they exist, such as the retention schedule, the vendor's subprocessor list, or the transfer mechanism. A field the user can't answer stays `TBC`. Never fill a required field with a plausible guess. A RoPA with invented retention periods misstates the company's practices to a regulator.

### 5. Write the entry

Fill in `assets/ropa-entry-template.md`. Save it to `<output root>/registers/ropa/<activity-slug>.md`, ID `ROPA-NNNN` (next number from the index). Tag it with NIST PF ID.IM-P subcategories. Set status to Draft.

**Flag follow-ons** in the entry's "Related assessments" section, and recommend, without running them:

- `dpia` **screening**, when the activity shows high-risk indicators (`dpia/references/screening.md`) or may trigger a state assessment, and no assessment is linked. The RoPA recommends screening; it doesn't conclude that a DPIA is required. The DPIA is a separate document, cross-referenced from the entry.
- `vendor-review`, for each processor or recipient with no review on file, or with a review older than 12 months
- `ai-intake`, when the activity uses AI or an AI feature
- A notice update, when the activity's purposes, recipients, or data aren't in the privacy notice

### 6. Rebuild the index

Run `python3 ../_shared/scripts/build_register_index.py <output root>/registers/ropa ropa` from this skill's folder. It reads every entry's metadata and rewrites `index.md`. Don't edit the index by hand; edit the entries and rebuild. If Python isn't available, update the index table by hand from `assets/ropa-index-template.md`, and say so.

### 7. Route approval and hand back

Route per `approvals.md`: the business owner confirms the facts, and the privacy lead confirms the legal positions and approves the entry. Fill in the entry's sign-off section with roles only.

Follow `conventions.md`, §11. Reply in about 150 words: the entry path and ID, whether it's new or updated, the count of TBC required fields, the follow-ons recommended, and the decisions needed.

## Bulk builds

When asked to build or refresh many entries at once, such as from a system inventory, a data map, or a regulator request:

1. Propose the activity list and the system-to-activity mapping first, and get it confirmed before drafting entries.
2. Draft all entries, then send **one** consolidated question list grouped by entry, with Round 1 items first.
3. Rebuild the index once, at the end.
4. Report the coverage in the reply: entries drafted, required fields still TBC, and follow-ons recommended.

For a regulator request under Art. 30(4), produce the register as it stands, with TBC fields visible. Flag the request to the privacy lead at once. The response to the authority is an external communication.

## Keeping the register current

Each entry has a next review date (default 12 months), recorded as an action, never a calendar event. A new vendor, purpose, data category, or region triggers an update. Other skills point here when their work changes an activity: a DPIA, a vendor review, or an incident.
