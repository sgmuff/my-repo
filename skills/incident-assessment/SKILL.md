---
name: incident-assessment
description: Assess a security or privacy incident for notification duties, fast. Start the notification clocks (GDPR's 72 hours, US state deadlines, contractual and regulator deadlines), decide whether it's a personal data breach and who must be told (supervisory authorities, attorneys general, individuals, customers as controllers, districts, credit bureaus, insurers), and draft every notice for counsel and the privacy lead to approve. Covers GDPR, UK GDPR, Swiss FADP, all US state breach laws, FERPA and student privacy contracts, and AI serious incidents under the EU AI Act. Use it whenever someone reports a breach, data leak, misdirected email or file, lost or stolen device, ransomware, unauthorized access, a vendor's security incident, an AI agent exposing data, or asks "do we have to notify," even if they don't call it a breach. Not for routine privacy requests (dsr-response) or vendor contract reviews (vendor-review).
compatibility: Requires the gov command from this repository (skills/install.sh installs it), with Python 3.10+, PyYAML, jsonschema, and Jinja2.
---

# Incident assessment

This skill works the notification side of an incident: who must be told, by when, and what. Containment, forensics, and recovery belong to the security team; this skill runs alongside, and its first job is to start the clocks. It records everything in one `inc` record. `gov render` computes the statutory clocks from the record's awareness time and writes the record and the notice drafts. Never write or edit either `.md` file.

**The decision to notify is a legal determination.** The skill analyzes and drafts; counsel and the privacy lead decide, and a person sends every notice (`approvals.md`). Only a person's decision goes in the decision log. Until counsel has fully reviewed `us-breach-notification.md`, the rendered record says so at the top.

## Files

| File | Read it when |
|---|---|
| [`references/risk-factors.md`](references/risk-factors.md) | Steps 3-4: the GDPR and US analyses, contracts, AI incidents |
| [`../_shared/references/us-breach-notification.md`](../_shared/references/us-breach-notification.md) | Steps 4-5: each state's rules, notice content, federal and sector laws to flag |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md), [`ferpa.md`](../_shared/references/ferpa.md), [`eu-ai-act.md`](../_shared/references/eu-ai-act.md) | §9 breach duties and §1a scope; student data; AI serious incidents |
| [`assets/notice-drafts.md`](assets/notice-drafts.md) | Step 5: the content rules and model wording for each kind of notice |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 6 |

## Workflow

### 1. Start the clock, now

Run `gov --version`; if it fails, stop and tell the user to run `skills/install.sh`, and meanwhile give the 72-hour and state deadlines by hand. Run `gov new inc --slug <slug> --title "<what happened>" --date <today>` and record at once: when the company became aware, with the zone and the reasoning ("security confirmed exfiltration at 14:20 ET"); when it started, if known; whether it's ongoing; and every regime and state that could apply. Where facts are missing, include the plausible ones and work to the earliest deadline; if nobody knows when the error was noticed, use the earliest possible time and say so in the reasoning. `gov clock --aware <time> --tz <zone> --regimes ... --states ...` shows the same clocks before the record exists.

Every date is a working deadline until the incident commander confirms the awareness time. Each recipient is its own decision with its own deadline, and a statutory deadline is an outer limit, not a target.

In a live incident, the first reply goes within minutes, before the record is complete; when there's only one reply, lead with it. It's short: the earliest deadline and what it's for; bring in counsel now (privilege may need communications to run through counsel); check the cyber insurance notice conditions, since late notice can void cover; preserve evidence; don't speculate in writing or send any unreviewed notice, but don't let that delay a required one; name one incident commander; containment runs in parallel, owned by security; and no one contacts an attacker except through counsel and the responders.

### 2. Get the facts

Ask in a short Round 1 (under about 12 questions, with an "Evidence requested" group) for what decides the duties: acquired or only accessed; encrypted with the key safe; the actual fields, by controlled inspection, not by circulating the file; counts by country and state, including people whose residence is unknown; the company's role for each data set; the recipient or attacker; any vendor involvement and what the vendor has said in writing; law enforcement; and contracts with deadlines (customer DPAs, district agreements, insurance, card brands). Facts change fast: record each in `facts` with when it was learned. Don't copy the exposed data or download leak-site samples beyond what forensics needs.

### 3. Answer the assessment

Answer it fully, then check against `references/risk-factors.md` and `us-breach-notification.md`, and add what you missed. Points answers often miss:

- **Role decides who notifies whom.** A processor or maintainer notifies each controller or owner first, within any contractual hours; a school official notifies each institution under its agreement (New York: 7 days under Ed Law 2-d).
- **Authority and individual notice are separate determinations** (GDPR Arts. 33 and 34). A recipient's deletion confirmation is evidence, not proof of no risk.
- **The authority route is counsel's call.** Don't assume a filing destination from where the people live.
- **The US position stays undetermined** until the fields, counts by state, each state's definition and exceptions, and contracts are checked. "Not covered anywhere" and "every state requires notice" are both too categorical.
- **Flag federal and sector laws** (SEC, FTC, NYDFS, HIPAA) for counsel; for AI incidents, AI Act Art. 73 and any AIUC-1 failure plans.

### 4. Record it

Fill in the record from your answer: the data sets, with every role the company holds for each (a school official is often a maintainer too), acquisition, and encryption; the breach call; one `matrix` row per recipient (authorities, attorneys general, individuals, controllers, institutions, credit bureaus, insurers, card brands, law enforcement), each with its basis, its deadline from the clock or the contract, and its status. Give every contractual or same-day deadline a `due` (a date, a date and time, or `immediately`) so it counts toward the earliest deadline; and security's containment measures. Each call stays Provisional; a point that doesn't fit a field goes in `analysis` (400 words at most).

### 5. Draft the notices

Draft only what the matrix requires, as `notices` entries, following `assets/notice-drafts.md`: facts known at the time, without speculation, blame, or admissions; each recipient's content rules (GDPR Art. 33(3) and 34(2), California's format, Massachusetts's restrictions); and the regulator's own form where one exists. `gov render` writes them with "DRAFT: not sent."

### 6. Validate, render, and reply

Run `gov validate`, fix errors, and resolve findings by changing the record; a finding that names a real gap stays open with an action. Run `gov render`. Route the decisions (`approvals.md`): whether to notify each recipient, each notice's content, and any credit monitoring offer. When a person decides, record it in `decisions` with the time, who, the evidence, and the rationale; when a notice goes, record it in the row's `sent`. A recipient's silence doesn't stop the clock. Art. 33(5) requires documenting every breach, notified or not.

The reply leads with time: the earliest deadline and what it's for, the decisions needed now and from whom, and the Round 1 questions. Close with one line naming the record and its path.

## As the incident develops

Update the record when facts change (new data types, more people, new states, confirmed exfiltration): the clocks re-render from it. Use phased reporting to authorities where facts are still emerging (GDPR Art. 33(4)). At closure, fill in `closure` with the root cause from security and the follow-ons: a DPIA rescreen, a vendor reassessment, RoPA updates, notice changes, and AIUC-1 failure-plan updates.
