---
name: controls-and-evidence
description: Maintain the company's control library and evidence index, mapped through a common crosswalk to the NIST Privacy Framework, AIUC-1, NIST AI RMF, ISO/IEC 42001, GDPR, the EU AI Act, state laws, and FERPA, so one control tested once satisfies several frameworks. Runs AIUC-1 certification readiness (Statement of Applicability, control and evidence mapping, quarterly third-party testing), prepares audit evidence packs, and builds the schedule of recurring tests and reviews. Use it whenever someone wants to map a control to frameworks, build a control library or crosswalk, find evidence for an audit or customer questionnaire, prepare for AIUC-1 or ISO/IEC 42001 certification, ask which controls cover a requirement, or track recurring testing. Not for program-wide maturity scoring (program-assessment), one processing activity (dpia), or vendors (vendor-review).
compatibility: Requires the gov command from this repository (skills/install.sh installs it), with Python 3.10+, PyYAML, jsonschema, and Jinja2.
---

# Controls and evidence

This skill keeps the evidence side of the program in order. It records what the company actually does (controls), how it proves it (evidence), which framework requirements each control satisfies (through the crosswalk), and when each control must be tested again.

It drafts mappings, Statements of Applicability, evidence packs, and gap lists. It doesn't decide whether a control is effective. Control owners supply evidence, a reviewer judges it, and the privacy lead approves what goes to an auditor or customer (`approvals.md`). **A control is only as good as its evidence:** a policy that says something happens isn't evidence that it does.

## Files

| File | Read it when |
|---|---|
| [`../_shared/conventions.md`](../_shared/conventions.md) | At the start of every run |
| [`../_shared/company-profile.md`](../_shared/company-profile.md) | At the start, for the frameworks in scope and the security baseline |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Before anything goes to an auditor or customer |
| [`../_shared/references/crosswalk.md`](../_shared/references/crosswalk.md) | Always: the common control objectives (CCO-01 to CCO-32) and their framework mappings |
| [`../_shared/references/aiuc-1.md`](../_shared/references/aiuc-1.md) | AIUC-1 readiness: requirements, capability tags, certification, testing cadence |
| [`../_shared/references/iso-42001.md`](../_shared/references/iso-42001.md) | ISO/IEC 42001 readiness |
| [`../_shared/references/risk-method.md`](../_shared/references/risk-method.md) | Control statuses (§1) |
| [`assets/readiness-report-template.md`](assets/readiness-report-template.md) | ISO/IEC 42001 readiness or an audit evidence pack (AIUC-1 readiness is a `gov` record) |
| [`../_shared/scripts/make_checklist.py`](../_shared/scripts/make_checklist.py) | Generating a blank Statement of Applicability |
| `gov schedule` | After changing any test or review date |

## What the skill does

Pick the mode from the request:

| Mode | Request sounds like | Output |
|---|---|---|
| **Map a control** | "Which frameworks does our MFA control cover?" | Updated control entry |
| **Build or refresh the library** | "Build our control library from the SOC 2 report and policies" | Control entries, index, gap list |
| **Find evidence** | "What evidence do we have for Art. 32 / AIUC-1 E015?" | Evidence list by requirement, with gaps |
| **Certification readiness** | "Get us ready for AIUC-1 on the support agent" | Readiness report with Statement of Applicability |
| **Security assessment** | "Do our GLBA risk assessment," "Are we ready for the CCPA cybersecurity audit?" | `sra` record mapped to the library |
| **Audit or questionnaire pack** | "An auditor asked for evidence on access reviews" | Evidence pack, marked as an external draft |
| **Schedule** | "What tests are due this quarter?" | Rebuilt `schedule.md` |

## Workflow

### 1. Load context and the library

Run `gov --version`; if it fails, stop and tell the user to run `skills/install.sh`. Read `conventions.md`, the company profile, and `compliance/registers/controls/index.md` if it exists. Read the crosswalk. Check `aiuc-1.md` for the current release, since a new quarterly release changes requirements.

### 2. Record controls as what the company does

A control entry describes a specific practice, with an owner, a frequency, and the systems in scope: "The IT lead reviews Okta admin roles quarterly and removes access no longer needed." "We take security seriously" isn't a control.

Record each control as a `ctl` record: `gov new ctl --slug <slug> --title "<control>" --date <today>`. Fill in:

- The **objectives** it supports (CCO IDs from the crosswalk), with a line on how and any framework requirement it satisfies only partly. Its framework coverage then renders from `crosswalk.md`.
- **Design and operating status** (`risk-method.md`, §1): `evidenced` only when an evidence item shows the control operating.
- **Evidence:** each item with an ID from `gov next-id EV`, listed in one control and cited by ID elsewhere; its type, whether it shows design or operation, a link (never a copy of confidential material), the period it covers, and when it goes stale.
- **Testing:** each test with its method, scope, tester, result, and exceptions; `last_tested` (or `never`) and the `next_test` date its frequency requires.

Record the SOC 2 or ISO criteria a control is tested against in `criteria`, and give each report criterion its own evidence item, so the library answers a questionnaire by criterion. Take evidence IDs one at a time as you add items; an ID once issued is never reused. A planned control has `lifecycle: planned` and coverage `none-yet`, and evidence described but not yet supplied is `status: requested`. Run `gov validate --as-of <today>`, which flags evidence gone stale behind an evidenced control, and `gov render`, which rebuilds the library index. Save a gap list as `compliance/registers/control-gaps-YYYY-MM-DD.md`, outside the controls folder.

When building from documents (a SOC 2 report, policies, an ISO Statement of Applicability), propose the control list first and get it confirmed, then draft. If nobody can confirm it now, draft the entries as Draft and ask for confirmation in the reply. Record each control's source. A SOC 2 control description is evidence of design. Its test results are evidence of operation for the report period only.

### 3. Judge evidence honestly

For each evidence item, ask: does it show the control **operating**, for the **period** that matters, for the **systems** in scope? Record the answer.

- Freshness: evidence older than its test frequency is stale.
- Scope: a report that doesn't cover the system in question doesn't count for it.
- Kind: a policy shows design, while a record or a test shows operation.

A **planned** control is not a covered control, and a policy that describes intended behavior doesn't show the behavior is enforced. Map SOC 2 evidence explicitly, criterion by criterion, with the system, period, and exceptions. Don't carry SOC 2 coverage or SOC 2 exceptions over to AIUC-1 automatically.

Label each requirement's coverage: **Covered** (controls mapped, with current operating evidence), **Partly covered** (mapped, but evidence is partial, stale, or out of scope), **Not covered**, or **Not applicable** (with the reason). These are the skill's Provisional view until a reviewer agrees.

### 4. AIUC-1 certification readiness

When the company is preparing its own agent (readiness mode, `aiuc-1.md` §2):

1. **Scope the agent:** which product and agent, its capabilities, and the release to audit against (the latest, or the previous one within the 30-day grace period). Build the requirement inventory from `aiuc-1.md` for that release, never from memory, and read each requirement's text and controls on its AIUC page; don't copy AIUC's text into the deliverable (`aiuc-1.md`, §4). For each requirement, record the applicability rationale, the control activities and evidence required, whether testing must be third-party and how often, and who is responsible (company, model provider, or shared).
2. **Record it:** `gov new rdy --slug <agent> --title "<agent> AIUC-1 readiness" --date <today>`, with `capabilities` set to the agent's tags, `release` to the release you assessed against, and `target_release` to the audit's release once kickoff fixes it. Build the Statement of Applicability in `soa`, one row per requirement; `gov validate` lists any mandatory requirement the capabilities trigger that the SoA leaves out, and rejects IDs not in the release. Mark each requirement as applying or not by capability tag. A mandatory requirement is excluded only when the agent lacks the tagged capability, with a one- or two-sentence justification. Mark optional requirements `opted-in`, `excluded`, or `undecided` while the business hasn't decided. A requirement with no control at all gets `gap: missing` and an open action that names its ID.
3. **Map controls** to each applicable requirement and its core controls, through the crosswalk and the control library. Note supplemental controls opted into.
4. **Map evidence** by AIUC-1 category: legal policies, operational practices, technical implementation, and third-party evaluations.
5. **Gaps:** requirements Not covered or Partly covered, each with an action (owner, due date, acceptance criterion, and evidence that closes it).
6. **Testing schedule:** the third-party testing requirements (A009, B001, C010, D004, E018) at least every 3 months, internal reviews (E008), and annual re-certification. Each becomes a control with a `next_test` date; a test that has never run has `last_done: never`. `gov schedule` lists the record's dated actions and testing rows. Never put them on a calendar. Plan the **auditor** and the **technical evaluations** (run by AIUC under current guidance) as separate arrangements (`aiuc-1.md`, §3).
7. **Milestones are gates, not commitments.** Work back from the target, and keep the audit start separate from the certificate date. Each milestone (testing arrangements confirmed, critical gaps fixed, baseline tests done, evidence pack complete, audit start) has an entry condition. If critical findings are open when a gate arrives, escalate the schedule risk rather than proceeding.
8. **Optional requirements are a recorded business decision:** for each, opt in or out on the agent's actual risks and on what customers require, with the rationale and the decision-maker.

Production risks from §4a are actions that block audit start, and the reply says they need fixing now, not at the audit. Fill in the record's `testing` and `milestones`, run `gov validate`, resolve what it raises, and run `gov render`; the report lands in `compliance/assessments/aiuc-readiness/`. For ISO/IEC 42001 readiness, write it up with `assets/readiness-report-template.md` instead, saved as `compliance/assessments/iso-readiness/ISO-YYYY-NNN-<slug>.md`, with `make_checklist.py iso-42001 soa` and the caution that the checklist is a public paraphrase, not the standard (`iso-42001.md`).

AIUC-1 certification is issued by AIUC through accredited auditors. The skill prepares for the audit. It doesn't certify, and it doesn't claim that the company meets the standard.

### 4a. Agent safety checks that can't wait for certification

Some gaps are production risks now. When an agent can read customer data or take actions, check these first, and treat a failure as a security issue owned by Engineering and Security, not as a certification task:

- **Authorization of tool calls.** The user's identity comes from trusted application context, and the server checks authorization on every call. An identifier the model supplies can't override it. Negative tests cover guessed IDs, manipulated arguments, prompt injection (direct and through retrieved content), and repeated calls. Acceptance criterion: no response or tool call retrieves another customer's data, even when asked with a valid identifier belonging to someone else.
- **Action limits as business rules.** Define each limit precisely (per transaction, per order, per customer, per period), and test that the backend enforces it atomically against splitting, repetition, concurrent conversations, retries, and duplicates. The model's claim that an action is allowed is not authorization (AIUC-1 B006, D003).
- **Evaluations as release gates.** For each risk area: a representative test set, pass and fail thresholds, regression tests for past failures, a review process for failures, a rule that blocks release below thresholds, and re-evaluation after any change to the model, prompts, tools, permissions, or retrieval sources. Measure outcomes (authorization failures, unauthorized actions, leakage, successful injections), not only that tests ran. Retrieval grounding reduces hallucination, but brings its own risks, such as injected instructions and stale content.
- **Logs.** Check what the agent's logs contain (prompts, responses, identifiers, order details, credentials), who can read them, and for how long. Minimize and redact before ingestion where possible (AIUC-1 E015; GDPR Art. 5(1)(c)).
- **Disclosure.** Record the decision on telling users they're talking to AI: whether people in the EU use the agent, the company's AI Act role, and whether AI involvement is obvious in context (Art. 50(1)). Assess other jurisdictions separately. "Hi, I'm Ava, an AI assistant" is a simple fix if the duty applies (AIUC-1 E016).

### 4b. Security assessments the law requires

When `gov required` or the request names one, record it as an `sra` record: `gov new sra --kind <kind> --slug <scope> --title "<law>: <scope>" --date <today>`, where the kind is `gdpr-art32`, `ccpa-audit-prep`, `coppa-security`, `hipaa`, `glba`, or `nis2`. `gov/rules/security.yaml` lists each kind's elements with their citations, and `gov validate` names any the record leaves out. For each element, record whether it applies, how the company meets it, the library controls and evidence behind it, and its status; rate the risks with the shared matrix. Read the regime's reference file first (`hipaa.md`, `glba.md`, `nis2.md`, `us-state-privacy.md` §6, `ferpa.md` for COPPA), including its scope test: a company outside the regime doesn't owe the assessment.

- **CCPA:** the record prepares for the annual audit; the audit itself needs a qualified, objective, independent auditor, who decides which components apply (11 CCR §§ 7122-7123). First reports are due April 1, 2028, 2029, or 2030 by revenue.
- **COPPA and GLBA:** COPPA requires the risk assessment and the program's evaluation at least annually, GLBA a periodic reassessment; set `next_review` to match. A program already overdue goes in the reply first, with the compliance date that passed.
- **An element is met or partial only through controls that operate:** a planned control, or evidence gone stale, doesn't carry it, and `gov validate` says so.
- **NIS2:** national transposition decides the details; management bodies approve the measures (Art. 20).

### 5. Audit and questionnaire packs

When an auditor, customer, or regulator asks for evidence:

- List each request, the controls and evidence that answer it, and any gap. Link evidence; don't attach confidential material without the privacy lead's approval.
- Answer what was asked, accurately, and no more. Where evidence is partial, say so. Never overstate coverage.
- The pack is an external communication: metadata first, then "DRAFT: not sent." The privacy lead approves it.

### 6. Rebuild the schedule and hand back

Run `gov schedule <output root> --as-of <today>` to rebuild `schedule.md` from every deliverable's review, test, and deadline dates. Overdue items go in the reply.

Reply in plain English: the answer to the question asked first (often where the company is weak), then what changed, the coverage summary, the top gaps, overdue tests, the decisions needed, and up to five questions. If the company profile's security baseline is TODO, offer to save the facts you were given there. Close with one line naming the index and its path.

## Keeping the library current

A new AIUC-1 release, a framework change, or a new law can change what a control must cover. Then update `crosswalk.md` (with the privacy lead's approval, `approvals.md`), and flag the controls whose mapped requirements changed. Retire controls that no longer operate, keep their history, and never delete evidence that an audit relied on.
