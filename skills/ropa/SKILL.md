---
name: ropa
description: Create, update, or bulk-build record of processing activities (RoPA) entries from intake answers, interviews, or system documentation such as PRDs, architecture docs, data dictionaries, schemas, and vendor lists, covering GDPR Article 30 controller and processor records, Swiss FADP Article 12, and the data inventory duties in US state laws, and keep the register's index current. Use it whenever someone wants to document, map, or inventory what personal data a system, team, or process handles, add or update a processing activity, build a data map, answer "what data do we hold and why," or prepare RoPA records for an audit or regulator request, even if they don't say "RoPA." Not for deciding whether an activity is high risk or needs a DPIA (dpia), reviewing a vendor's contract (vendor-review), or inventorying AI systems and agents (ai-intake).
compatibility: Requires the gov command from this repository (skills/install.sh installs it), with Python 3.10+, PyYAML, jsonschema, and Jinja2.
---

# Record of processing activities

This skill turns what people know, and what documents show, into RoPA entries that hold up to an auditor: one YAML record per processing activity, rendered to Markdown, plus a generated index.

**You fill in the record; `gov` writes the document.** Every entry renders from the same template, so an auditor reads the same sections in the same order every time. `gov validate` catches missing fields, broken references, and legal inconsistencies before anyone sees them. A hand-written Markdown entry fails CI and breaks that consistency, so never write or edit the `.md` files.

**Facts, positions, and decisions stay apart.** A fact carries its source. A legal position is a *call*: a value, Provisional or Confirmed, and a one-line reason. Only an approver confirms a call, so every call you write is Provisional. The record is reused by reports and other skills, so an assumption written as a fact here spreads further than one buried in prose.

## Files

| File | Read it when |
|---|---|
| [`../_shared/conventions.md`](../_shared/conventions.md) | At the start of every run |
| [`../_shared/company-profile.md`](../_shared/company-profile.md) | At the start of every run, for the company's identity, DPO, security baseline, and standard transfer mechanisms |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 7 |
| [`references/fields.md`](references/fields.md) | Steps 2 to 4: what fills each field, and the provision behind it |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md) | Art. 30 contents (§7), roles (§2), lawful bases (§3), transfers (§11) |
| [`../_shared/references/us-state-privacy.md`](../_shared/references/us-state-privacy.md) | State flags: sale, sharing, targeted advertising, sensitive data |
| [`../_shared/references/ferpa.md`](../_shared/references/ferpa.md) | When the activity uses student data |

## Workflow

### 1. Check the tool and find existing entries

Run `gov --version`. If it fails, stop and tell the user to run `skills/install.sh`. Don't fall back to writing Markdown.

Read `compliance/registers/ropa/index.md`, if it exists, and look for an entry covering the same activity. Match on purpose and system, not only on name.

- **Existing entry:** edit its YAML. Change only the affected fields, raise `version`, add a `version_history` row, and set `status` to Draft.
- **Overlapping entries:** say so, and propose merging them.
- **New entry:** run `gov new ropa --slug <short-slug> --title "<Activity name>" --date <today, YYYY-MM-DD>`. It reserves the next ID and writes a skeleton with a hint on every field. Never pick an ID yourself.

**One entry per processing activity:** a purpose, or closely related purposes, on a defined set of data. Use separate entries when the company entity, purposes, lawful bases, recipients, or transfers differ materially between countries.

### 2. Settle the record type first

Roles follow the facts, purpose by purpose (`gdpr.md`, §2). For each purpose, set `decided_by`: the company, a customer, jointly, or TBC.

- **Processor** (customers decide every purpose): fill in `processor_record`. Describe the customers' purposes, but set each `lawful_basis` to `controller-to-confirm`. The customer chooses its basis, and the record must not imply that the company chose it.
- **Controller:** propose a lawful basis per purpose, and an `art9_condition` where special category data serves it. Where the GDPR doesn't apply, such as a US-only activity with no EU establishment involved, use `not-applicable` with that reason, and record the US duties in flags, questions, and actions instead.
- **Both,** or a processor that also uses the data for its own ends (such as training a model): the company is a controller for those purposes (Art. 28(10)). Record the entry as `both`, or create a second entry for the company's own purposes and link the two in `related.linked_entries`.

### 3. Record what the sources show, and nothing more

Read everything provided: intake answers, PRDs, architecture docs, data dictionaries, schemas, vendor lists, privacy notices, and earlier assessments. Give every item a `source`.

- **Data elements come only from a source.** Don't add elements a system *could* collect, such as chat logs or bank fields the user didn't list. Ask about them in `open_questions` instead. A category the user states or plainly implies still gets a row: "they get the recording" means a recording category, with its elements TBC.
- **Link data to the purposes that use it,** as the source shows. Don't assign every category to every purpose; ask where the source is silent.
- **A schema shows data, not purposes or lawful bases.** Don't infer either from column names.
- **Flag each data category with care.** Each flag carries its status and a reason. Children's data and education records are not special category data. A flag like `ell_status` alone is not Art. 9 data; `iep_flag` may reveal disability, so flag it Provisional with that reason.
- **Leave a call TBC while an open question could change it.** Record `sensitive_data: false` only when nothing pending could make it true.
- **Screen transfers by flow,** not by where data subjects live: the regime, the exporter, the importer's country, and whether data is stored there or only accessed remotely. A US-hosted vendor is a fact to screen, not a conclusion.
- **Retention goes store by store:** one row for each place a copy lives, including each vendor's copy and backups. Keep what happens today, what the law requires, and the proposed policy apart. Never guess a period.

### 4. Turn risks into actions, and gaps into questions

- **`actions`:** anything that needs doing, not just documenting, such as cutting an unneeded field, redacting logs, or setting a retention limit. Give each an owner and closure evidence. Mark it launch-blocking when processing shouldn't start without it, and say why in `block_reason`: `law` (a processor with no signed contract, Art. 28), `policy` (our own rule), or `risk` (a risk someone must clear first, such as student data sent to an unreviewed vendor, or sensitive fields imported with no stated need). When it blocks only one flow or feature, name it in `scope`, so the rest can proceed. Give each verify flag its own resolution; don't close several with one action.
- **`open_questions`:** set `blocks` to `launch`, `approval`, `record` (an Art. 30 field stays TBC), or `none`.
- **Round 1:** ask only the questions that block launch or approval, five at most, in one message. The rest stay in the record for the owners.

Keep the entry proportionate. A routine activity, such as a webinar signup, gets a short entry and a few questions. Depth follows risk.

### 5. Flag follow-ons

Add to `follow_ons`, recommending without concluding: `dpia` when high-risk indicators appear (`dpia/references/screening.md`), `vendor-review` for each recipient without a current review, `ai-intake` when AI is used, `tia` when a flow may be a restricted transfer, and `notice-and-policy` when the notice doesn't cover the activity.

### 6. Answer the required assessments

Run `gov required <the entry's YAML file>`. It lists what the catalog (`gov/rules/assessments.yaml`) says this activity owes, from the entry's facts. For each one marked owed, add an `assessments` item: `on-file` with its record ID, or `planned`. Don't mark anything `not-applicable` yourself; only a person decides that, and the item names them. "May be owed" means an open fact decides it; ask that fact in Round 1 if it blocks approval.

### 7. Validate and render

Run `gov validate` and fix every error. Validation checks structure and consistency, not legal correctness, so report it as "`gov validate` found no structural errors" and never as approval. Then resolve each **finding** by changing the record. A finding you can't resolve goes in your reply for the privacy lead. Don't add a `finding_responses` entry yourself; only a person records why a finding doesn't apply. Rerun until no errors remain, then run `gov render`.

Text that contains a comma inside `{...}` must be in double quotes, or YAML splits it. `gov validate` points this out.

### 8. Route approval and hand back

The business owner confirms the facts, and the privacy lead confirms the calls and approves (`approvals.md`). Leave `signoff` empty; only a recorded approval fills it.

Reply in 150 words at most, plus the Round 1 questions. Cover only what the user acts on: the entry's path and ID, the record type, the actions that block launch, any unresolved findings, and the decisions needed, with a one-line pointer to the follow-ons. The rendered entry holds everything else, so don't restate its TBC list, purposes, or actions.

## Bulk builds

1. Propose the activity list and the system-to-activity mapping, and get it confirmed before drafting.
2. Create and fill every entry, then send one question list grouped by entry, blockers first.
3. Run `gov validate` and `gov render` once, at the end.

For a regulator request under Art. 30(4), produce the register as it stands, with TBC fields visible, and flag the request to the privacy lead at once. The response to the authority is an external communication.

## Keeping the register current

Each entry has a `next_review` date (default 12 months), tracked as an action, never a calendar event. A new vendor, purpose, data category, or region triggers an update.
