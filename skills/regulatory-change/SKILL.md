---
name: regulatory-change
description: Turn a new or amended law, regulation, guidance, court decision, enforcement action, or standard release (such as a quarterly AIUC-1 update or a NIST Privacy Framework revision) into a sourced summary, an applicability call, an impact map across the program's reference files, controls, registers, and open deliverables, and proposed edits to the reference files that are never applied without approval. Also runs periodic sweeps of every reference file's volatile points and review dates. Use it whenever someone asks what a new law or guidance means for the company, whether something changed, to update the suite's reference files, to process an AIUC-1 release, or to check what's coming, even if they don't say "regulatory change." Not for applying the law to one activity (dpia, vendor-review, incident-assessment) or for program-wide maturity scoring (program-assessment).
---

# Regulatory change

This skill keeps the suite current. When the law or a standard changes, it confirms the change against the primary source, works out whether and how it affects the company, traces every place in the program the change touches, and proposes the edits. The reference files are the suite's memory of the law, so they change only with the privacy lead's approval (`approvals.md`).

## Files

| File | Read it when |
|---|---|
| [`../_shared/conventions.md`](../_shared/conventions.md) | At the start of every run |
| [`../_shared/company-profile.md`](../_shared/company-profile.md) | Step 3, for the regimes in scope |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 6 |
| [`../_shared/references/README.md`](../_shared/references/README.md) | Always: the reference index, review dates, and update steps |
| [`references/sources.md`](references/sources.md) | Step 2: primary sources by regime, and the review calendar |
| [`../_shared/references/crosswalk.md`](../_shared/references/crosswalk.md) | Step 4: which control objectives a change touches |
| [`scripts/aiuc_release_diff.py`](scripts/aiuc_release_diff.py) | AIUC-1 releases |
| [`scripts/find_citations.py`](scripts/find_citations.py) | Step 4: every reference, skill, and deliverable that cites the changed provision |
| [`assets/change-memo-template.md`](assets/change-memo-template.md) | Step 5 |

## Workflow

### 1. Pin down the change

Record what arrived: a bill, a final rule, guidance, a decision, an enforcement action, or a standard release. Note who raised it and when. Classify its stage, because the stage decides what to do:

| Stage | What to do |
|---|---|
| Proposed or pending (a bill, a draft rule, a consultation, a court case under appeal) | Note it in the reference file as *Volatile*, add a watch action, and change no conclusion yet |
| Political agreement (such as an EU trilogue deal) | Assess the agreed text and prepare proposed changes. Implement nothing; the text can still change |
| Adopted, not yet in force | Update the reference file with the entry-into-force and application dates, and plan readiness actions |
| In force | Update the reference file, and assess the impact on current practice now |
| Guidance | Say which kind: binding instrument, final guidance, voluntary code of practice, or draft for consultation. A voluntary code doesn't create the law's obligations, but can show how a regulator reads them |
| Enforcement or court decision | Note how it changes interpretation, cite it, and assess the impact |
| Unverified | Only secondary sources so far. Nothing changes until a primary source confirms it |

Where a law commences in stages (such as the UK DUAA), map each provision to its commencement instrument and date, including transitional provisions. Don't treat the whole act as one stage.

### 2. Confirm it against the primary source

Use `references/sources.md`. Search the web when available. Confirm the text, the effective dates, the citation, and the stage from the primary source. For each change, record the official source, the provision, the publication and effective dates, the date checked, and who checked it. Use secondary sources to find changes, never as the final authority. If only secondary sources are available, say so, mark the change Unverified, and mark every conclusion built on it Provisional with a verify flag.

When you do check a primary source during the run, write the result into the memo ("Checked on October 17, 2026: listed as Awaiting committee decision"), rather than leaving the check as a future action.

### 3. Summarize and decide applicability

Write what changed in plain terms: who it applies to, what it requires, and from when. When you restate the current rule, restate it fully, with its exceptions (GDPR Art. 33 notice is "without undue delay and, where feasible, within 72 hours," unless the breach is unlikely to result in a risk), and keep the duties of different parties apart (controller to authority, processor to controller, contract deadlines). Then answer separately (`conventions.md`, §7):

- **Does it apply to the company?** Check thresholds, territorial scope, sector, and role. Provisional until counsel confirms where the call is close.
- **Which activities does it affect?** Search the registers: RoPA, AI inventory, vendors, controls.

### 4. Map the impact

Run `python3 scripts/find_citations.py "<provision or term>" ../_shared/references ../<skill folders> <output root>` to find every reference file section, skill instruction, and deliverable that cites what changed. Then list:

- **Reference files** and sections to edit
- **Crosswalk** objectives whose mappings change
- **Controls** whose mapped requirements change (`registers/controls/`)
- **Open deliverables** whose conclusions may move: DPIAs, AI impact assessments, vendor reviews, incident records, notices, policies, readiness reports. Each gets a reassessment action for its owner.
- **Skills** whose instructions need changing

For each change, say what kind of change it is: a new legal obligation, a change to an internal control, a reference file update only, or no change. Give it an owner, a due date, and the evidence that closes it. A count of "0 controls, 0 deliverables" means none need changing now, not that there's nothing to do. Say so when applicability or verification is still open.

For an **AIUC-1 release**, download the index (`curl -sL https://standard.aiuc-1.com/llms.txt`), run `python3 scripts/aiuc_release_diff.py <file>`, then read the changelog and the domain pages for control-level changes, status changes (core or supplemental), testing frequency, and capability tags. Keep the downloaded index with the memo as evidence. Run `find_citations.py` with the retired and renamed IDs (`--regex "C011|C012"`) across the skills and the output root, not only the reference file. Update `aiuc-1.md` (§1, §4–§7), the crosswalk, and the reference index, and flag readiness reports and controls that cite changed requirements. Where release notes disagree on a date, leave it open rather than picking one.

### 5. Write the change memo and propose edits

Fill in `assets/change-memo-template.md`. Save it to `<output root>/regulatory-change/YYYY-MM-DD-<slug>.md`. For each reference file edit, include the exact proposed text (current text, then replacement) in the memo. Don't edit the reference files yet.

Give each law, bill, or release its own change entry, so each can be approved, rejected, or held on its own. "About 22 bills" isn't a compliance record. List each bill with its number, status, effective date, and applicability. Put time-sensitive items (a comment deadline, a clock that starts soon) at the top, with the decision and its options: comment on named provisions, decline with a reason, or assess first.

### 6. Route, then apply on approval

Route to the privacy lead (`approvals.md`), with counsel for close applicability calls. The privacy lead approves each change entry on its own, not the memo as a batch. Verified changes can go ahead while unverified ones wait. When the privacy lead approves:

1. Apply the edits to the reference files.
2. Update each file's header (version, sources, last verified, volatile points) and `_shared/references/README.md`.
3. Add the reassessment actions to the affected deliverables' action plans, and rebuild `schedule.md`.
4. Suggest a commit message that says what changed and why. Don't commit unless the user asks.

Reply in about 150 words: what changed and its stage, applicability (with status), the number of reference sections, controls, and deliverables affected, the proposed edits awaiting approval, and any deadline.

## Sweeps

When asked what's changed, or on a quarterly review:

1. Read `_shared/references/README.md` and list files past or near their review date.
2. **Find candidates broadly first.** Scan each regime's tracker in `references/sources.md` (state legislation trackers, legislature sites for laws signed this session, EU procedure pages, regulator news pages) for anything enacted, commenced, or published since each file's last-verified date. A file's volatile points are a starting list, not the whole search: new laws won't be on it.
3. **Then verify** each candidate against its primary source (step 2 of the workflow), most consequential first: laws in force or taking effect soonest, then guidance, then pending items.
4. Check the release calendar: AIUC-1 quarterly releases, state legislative sessions, EU procedures.
5. Write one memo with a change entry for each change found (stage, sources, applicability, impact), the files confirmed unchanged with the date checked, and what wasn't checked and why. Proposed edits follow the same approval route.

A file's header being reviewed isn't the same as every claim in it being checked again. Record which sections were checked. A sweep that finds nothing still updates each checked file's last-verified date once the privacy lead approves.
