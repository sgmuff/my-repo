---
name: incident-assessment
description: Assess a security or privacy incident for notification duties, fast. Start the notification clocks (GDPR's 72 hours, US state deadlines, contractual and regulator deadlines), decide whether it's a personal data breach and who must be told (supervisory authorities, attorneys general, individuals, customers as controllers, districts, credit bureaus, insurers), and draft every notice for counsel and the privacy lead to approve. Covers GDPR, UK GDPR, Swiss FADP, all US state breach laws, FERPA and student privacy contracts, and AI serious incidents under the EU AI Act. Use it whenever someone reports a breach, data leak, misdirected email or file, lost or stolen device, ransomware, unauthorized access, a vendor's security incident, an AI agent exposing data, or asks "do we have to notify," even if they don't call it a breach. Not for routine privacy requests (dsr-response) or vendor contract reviews (vendor-review).
---

# Incident assessment

This skill works the notification side of an incident: who must be told, by when, and what they must be told. Security incident response (containment, forensics, recovery) belongs to the security team. This skill runs alongside it, and its first job is to start the clocks.

The decision to notify, or not, is a legal determination. The skill prepares the analysis and the drafts. Counsel and the privacy lead decide, and a person sends every notice (`approvals.md`). **Before first live use, counsel must review `us-breach-notification.md` and record the review in its header.** Until then, say so at the top of every incident record.

## Files

| File | Read it when |
|---|---|
| [`../_shared/conventions.md`](../_shared/conventions.md) | At the start, once the clock is running |
| [`../_shared/company-profile.md`](../_shared/company-profile.md) | At the start, for counsel, the lead supervisory authority, and insurers |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 7 |
| [`scripts/incident_clock.py`](scripts/incident_clock.py) | Step 1, and whenever facts change |
| [`references/risk-factors.md`](references/risk-factors.md) | Steps 3–5: the GDPR and US analyses, contracts, AI incidents |
| [`../_shared/references/us-breach-notification.md`](../_shared/references/us-breach-notification.md) | Steps 4–6: each state's rules, notice content, federal and sector laws to flag |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md) | §9 breach duties, §1a territorial scope |
| [`../_shared/references/ferpa.md`](../_shared/references/ferpa.md) | Student data |
| [`../_shared/references/eu-ai-act.md`](../_shared/references/eu-ai-act.md) | AI serious incidents |
| [`assets/incident-record-template.md`](assets/incident-record-template.md) | Step 7 |
| [`assets/notice-drafts.md`](assets/notice-drafts.md) | Step 6 |
| [`../_shared/scripts/build_register_index.py`](../_shared/scripts/build_register_index.py) | Step 7, to rebuild the incident register |

## Workflow

### 1. Start the clock, now

Before anything else, record:

- **When the company became aware**, with the time zone and the reasoning ("Security confirmed exfiltration of the customer table at 14:20 ET")
- **When the incident started**, if known
- Whether it's **ongoing**

Run `python3 scripts/incident_clock.py --aware <timestamp> --tz <zone> --regimes <…> --states <…>` with every regime and state that could apply. Where facts are missing, include the plausible ones and work to the earliest deadline. Put the earliest deadline at the top of the record and of the reply. Re-run it whenever facts change. Deadlines are actions, never calendar events.

**Every date is a working deadline until the awareness time is confirmed.** Write it as "working deadline: <date and time>, assuming awareness at <time>; confirm the awareness timestamp now." Each recipient is a separate decision with its own deadline. The authority, individuals, each state, each controller or district, and the insurer don't share one date. A statutory deadline is an outer limit, not a target: notify as soon as the facts and approvals allow. Set internal milestones before it: a decision review the day before, then filing with time to spare.

Then, in the first reply (short, within minutes):

- The earliest deadline, and what it's for
- Bring in **counsel** now. In the US, communications may need to run through counsel to preserve privilege. Ask counsel how to mark drafts and notes.
- Check the **cyber insurance** policy's notice conditions now, since late notice can void coverage
- Preserve evidence. Don't delete logs or systems the security team needs.
- Don't speculate about cause or blame in writing, and **don't send any unreviewed external notice**. Escalate the notification decisions to counsel and the privacy lead immediately, so there's time to meet every deadline. Don't let this be read as a reason to delay a required notice: districts and controllers often need initial notice before the investigation ends.
- Name **one incident commander** who owns the timeline and escalations, with security, counsel, the privacy lead, and communications in their own roles
- **Technical containment runs in parallel**, owned by security: isolate affected systems and accounts, revoke sessions and credentials, check privileged accounts, identity systems, backups, and connections to customer or district systems, and confirm what remains exposed. Preserving evidence never delays containment. Record what was done and how it was verified.
- **Contact with attackers** (ransomware) is coordinated by counsel and the incident responders. No one negotiates, promises payment, or sends information on their own.

### 2. Gather the facts

In a short Round 1 (under about 12 questions, with an "Evidence requested" group), ask what decides the duties:

- What happened, to which systems, and whether data was **acquired** or only **accessed**, encrypted (with the key safe?), deleted, altered, or made unavailable
- Which data elements, and for how many people, **by state and country of residence**
- The company's **role** for each data set: controller or owner; processor, service provider, or maintainer; school official
- Who the recipient or attacker is, and whether data was published or a ransom demanded
- Whether a vendor caused it, and what the vendor has said in writing
- Whether law enforcement is involved, or has asked for a delay
- Contracts with deadlines: customer DPAs, district agreements, insurance, card brands

Facts in an incident change fast. Keep the fact register (`conventions.md`, §6) current, with the time each fact was learned and its source.

Ask for the evidence that establishes the facts: the original message ID and headers, mail and access audit events, the time the incident was reported internally, the actual columns or fields of the exposed data (by controlled inspection, not by circulating the file), counts by country and state **including people whose residence is unknown**, and what containment has been completed and independently verified. Keep evidence copies restricted, integrity-protected, and logged. Don't make extra copies of the exposed data, and don't download or redistribute leak-site samples beyond what forensics needs.

### 3. Decide whether it's a personal data breach, and the company's role

Use `references/risk-factors.md`. Mark each conclusion Provisional (`conventions.md`, §7).

- **Processor, service provider, or maintainer:** the main duty is to notify each affected **controller or owner** without undue delay, and within any contractual hours, with the facts they need (GDPR Art. 33(2); state maintainer duties). Draft those notices first. The controllers decide on regulators and individuals. Offer them help.
- **School official:** notify each institution under its agreement (New York: within 7 days under Ed Law 2-d). The institutions notify parents and students.
- **Controller or owner:** continue to steps 4 and 5.

### 4. Assess notification under each regime

For **GDPR, UK GDPR, and FADP**, apply the questions and factors in `references/risk-factors.md`: authority notice unless unlikely to result in a risk; individuals if likely high risk; exceptions. Record each factor and the conclusion.

For **each US state** where affected people live, apply §1 of `us-breach-notification.md`: covered data, breach definition, safe harbors, risk-of-harm (only where allowed), deadlines, regulator, and credit bureaus. Until the actual fields, the counts by state, each state's definition and exceptions, and any contractual or sector duties are checked, the US position is **"undetermined pending review."** That applies in both directions: "these fields aren't covered anywhere" and "full card numbers mean every state requires notice" are both too categorical. Name the facts that would reopen the analysis.

Assess **individual notice (GDPR Art. 34)** as its own determination, separate from authority notice. A recipient's deletion confirmation is evidence, but it neither proves nor rules out risk: also weigh whether the data was opened, copied, or forwarded, what the mail system shows independently, and the residual risk after containment.

**The authority route is counsel's call.** Record the analysis (main establishment, whether the one-stop shop applies to this processing, representative, affected countries) and counsel's written conclusion. Don't assume a filing destination from where affected people live.

For **AI incidents**, check AI Act Art. 73 (providers of high-risk systems, applying from December 2, 2027 for Annex III) and the company's AIUC-1 failure plans.

**Flag federal and sector laws** from `us-breach-notification.md`, §4 when the facts point to them (SEC, FTC, NYDFS, HIPAA, and others). They're outside the suite's scope, so route them to counsel.

### 5. Build the notification matrix

One row per recipient: regime, required? (Provisional), threshold met?, deadline (from the script or the contract), content rules, method, owner, and status. Recipients include supervisory authorities, attorneys general and other state agencies, individuals, controllers or customers, institutions, credit bureaus, insurers, card brands, and law enforcement. Label each deadline statutory or contractual.

### 6. Draft the notices

Use `assets/notice-drafts.md`. Draft only what the matrix requires. Each draft:

- Starts with "DRAFT: not sent," and carries whatever privilege marking counsel directs
- States facts known at the time, without speculation, blame, or admissions
- Meets the recipient's content rules: GDPR Art. 33(3) for authorities, Art. 34(2) for individuals; each state's requirements, including California's format and Massachusetts's restrictions
- Uses the regulator's own form where one exists. The draft supplies the content to paste in.

### 7. Write the record and route the decisions

Fill in `assets/incident-record-template.md`. Save it to `<output root>/incidents/YYYY/YYYY-MM-DD-<incident-id>.md`, ID `INC-YYYY-NNN`, with the drafts beside it as `…-notices.md`. Rebuild the register with `python3 ../_shared/scripts/build_register_index.py <output root>/incidents/YYYY incident`. Art. 33(5) requires documenting every breach, notified or not.

Route the decisions (`approvals.md`): whether to notify each recipient (counsel and the privacy lead), the content of each notice (privacy lead, with counsel for regulators), and any credit monitoring offer. Record each in the **decision log**: the conclusion, who decided, when, the evidence relied on, and the rationale. A prepared draft is contingency planning, not evidence that notice is required.

Track each sent notice by delivery, not drafting: when it went, by what method, to whom, and whether delivery was confirmed. A recipient's silence doesn't stop the clock.

Reply in about 150 words: the earliest deadline and what it's for, the decisions needed now, the Round 1 questions, and the record path. In an incident, the reply leads with time.

## As the incident develops

Re-run the clock when facts change: new data types, more people, new states, confirmation of exfiltration. Update the matrix and drafts. Use phased notification to authorities where facts are still emerging (GDPR Art. 33(4)). After closure, record lessons learned and the follow-ons: a DPIA rescreen, a vendor reassessment, RoPA updates, notice changes, and AIUC-1 failure-plan updates.
