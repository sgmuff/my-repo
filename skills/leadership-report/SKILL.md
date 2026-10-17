---
name: leadership-report
description: Build the periodic privacy and AI governance report for the board, an audit or risk committee, or the executive team, drawn from the program's own registers, assessments, incidents, requests, vendor reviews, controls, and regulatory change memos. Produces a one-page summary with key risk indicators, top risks, changes since the last report, the regulatory horizon, and the decisions leadership needs to make, with every number traceable to a record. Use it whenever someone asks for a board update, a quarterly privacy or AI risk report, program metrics, a KRI dashboard, or a summary of where the program stands for executives, even if they don't say "leadership report." Not for scoring program maturity against a framework (program-assessment), for assessing one activity (dpia, ai-impact-assessment), or for audit evidence packs (controls-and-evidence).
---

# Leadership report

This skill turns the program's records into a short report leadership can act on. The numbers come from a script, so they can be traced and rebuilt. The judgment (which risks matter, what leadership should decide) is drafted for the privacy lead to own. The report describes risk and progress. It never states that the company is compliant, certified, or conforming, because those are determinations for counsel or an auditor (`conventions.md`, §7).

## Files

| File | Read it when |
|---|---|
| [`../_shared/conventions.md`](../_shared/conventions.md) | At the start of every run |
| [`../_shared/company-profile.md`](../_shared/company-profile.md) | Step 1, for business areas and regimes |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 6 |
| [`scripts/program_metrics.py`](scripts/program_metrics.py) | Step 2: counts everything from the records |
| [`../_shared/scripts/compliance_schedule.py`](../_shared/scripts/compliance_schedule.py) | Step 2: upcoming deadlines and reviews |
| [`references/kri-guide.md`](references/kri-guide.md) | Step 3: which KRIs to show, thresholds, and how to word risk for leadership |
| [`assets/leadership-report-template.md`](assets/leadership-report-template.md) | Step 5 |

## Workflow

### 1. Confirm the audience and period

Ask, unless the request says: who the report is for (board, audit or risk committee, executive team), the period it covers, and whether there's a previous report to compare against. The audience sets the depth. A board gets one page and decisions. An executive team can take an appendix with operational detail.

### 2. Count from the records

Run, from the suite folder:

```
python3 leadership-report/scripts/program_metrics.py <output root> --since <period start> --today <period end>
python3 _shared/scripts/compliance_schedule.py <output root>
```

`program_metrics.py` writes `reports/metrics-YYYY-MM-DD.md`, with each count followed by the files it came from. Use those numbers in the report. Don't recount by hand, and don't round in a way that changes the meaning (3 of 5 DSRs on time is not "most").

**Escalate urgent items now, not in the report.** If the records show a running clock that may have passed or is close (a breach notice deadline, a DSR past its statutory date, a launch blocker on a live system), tell the privacy lead (and counsel for incidents) in the reply at once, as a separate item. The report can follow; the escalation can't wait for it.

If the output root doesn't exist or is thin, say so. Build the report from what the user provides, label each number with its source (for example, "stated by the privacy lead, not in the registers"), and list the missing registers as a gap. A count of zero from an empty register is "not recorded," not "none."

### 3. Choose the indicators and the top risks

Use `references/kri-guide.md`. Show 6 to 8 KRIs with a value, the previous value, a direction, and a threshold. Give each a definition and a denominator ("2 of 5 DSRs due this period"), using the guide's definitions, so the numbers compare across quarters. Amber means off threshold with a named owner and a plan; with no owner or plan, it's red.

Keep separate measures separate:

- **DSRs:** statutory timeliness and internal targets. Lateness against a statutory deadline stays Provisional until the deadline is confirmed for the laws and request type; a missed internal target is still a service failure, reported as one.
- **Incidents:** security incidents, personal data breaches, and breaches notified to a regulator are three different counts.
- **Risks:** current residual risks in assessments, risks in proposals not yet approved (a vendor under review), and unresolved findings.

Then pick the top 3 to 5 risks:

- Start from open High current residual risks and High assessment ratings, then late statutory deadlines, launch blockers past due, and live high-tier AI systems without an assessment.
- Describe each in business terms: what could happen, to whom, what it would cost (regulatory, contractual, customer trust), and what's being done. Keep the risk ID and record so it can be traced.
- Say what's known and what isn't: whether a defect is still active, how many records it affects, whether a pilot touches real people (candidates, students) or only test data, the interim control, and who owns the fix. An evidence gap ("no bias testing") is a gap, not proof of harm, and a defect isn't a reportable breach unless the facts show it.
- Keep the ratings as recorded. If a rating looks wrong, flag it for the owner in the cover note; don't change it in the report.

### 4. Changes, horizon, and decisions

- **Changes since last report:** new and closed assessments, incidents, risk ratings that moved, controls verified, and actions closed. Compare with the previous report when there is one. A headline such as "risk went up" needs the counts behind it, previous and current. If the previous report's numbers can't be checked against records, say the trend can't be measured reliably yet, and note where the previous count looks wrong (an undercount is a measurement change, not a new failure).
- **Regulatory horizon:** open regulatory change memos and the effective dates in the reference files that fall in the next 12 months. Mark pending laws as pending.
- **Decisions needed:** write each as a resolution the audience can pass: the action, the options, a recommendation, the accountable owner, the date, and what happens if it's deferred. Typical decisions are risk acceptance above the privacy lead's authority (`approvals.md`), funding for a gap, containment or pause of a live system, and go or no-go on a high-risk launch. A funded assessment is the deliverable, not a promise of compliance or certification. If there's nothing to decide, say so.

### 5. Draft the report

Fill in `assets/leadership-report-template.md`. Keep the summary to one page: the headline, the KRIs, the top risks, and the decisions. Put the detail in the appendix, with links to the metrics file and the records. Save it to `<output root>/reports/YYYY-QN-<audience>.md`, ID `LR-YYYY-QN`.

Wording rules for this audience:

- No "compliant," "certified," "conforms," or "no risk." Say what was assessed, what was found, and what remains open. When asked for an assurance statement, offer wording the report itself supports. Don't write "each gap has an owner" if some don't. AIUC-1 certification covers named agents or systems, decided by an accredited auditor, so name the scope.
- Provisional determinations stay labeled Provisional.
- Incidents under privilege: give counts and status only, unless counsel has directed otherwise. Check the incident record's `privilege` field.
- No personal data about requesters, candidates, or affected individuals.

Before handing back, check the report against itself: the KRI counts in the summary match the table, the number of red and amber indicators is right, the period's case counts agree across sections, and each number matches the metrics file.

### 6. Route for review

The privacy lead reviews the draft, and counsel reviews any statement about legal exposure or incidents, before it goes to leadership (`approvals.md`). The report is internal. Don't send it or post it anywhere.

Reply in about 150 words: the headline, the KRIs that are off threshold, the top risks, the decisions requested, any data gaps, and the file paths.
