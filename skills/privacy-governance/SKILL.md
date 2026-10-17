---
name: privacy-governance
description: Triage privacy and AI governance requests that span several workflows, or that don't say which one they need, and plan the order to run them in. For example, a new AI tool that will touch customer or student data, a product launch with new vendors and data uses, an acquisition or new market, "where do I start," or "what do we need to do before we can use X." Produces a short triage plan that names the facts that decide the path, the skills to run in order, and the human decisions along the way. Use it when a request mixes vendor, assessment, records, AI, or policy work, or when it's unclear which privacy workflow applies. Skip it when the request clearly matches one skill, such as "review this DPA" (vendor-review), "do we need a DPIA for X" (dpia), or "add this to the RoPA" (ropa), and go straight to that skill.
---

# Privacy and AI governance triage

This skill is the front door for requests that don't fit one workflow. It works out what is being asked, which workflows apply, in what order, and what a person must decide along the way. Then it hands off. It produces no compliance deliverable of its own, only a plan.

Requests that clearly match one skill should go straight to that skill. Its description is written to catch them. Triage adds value when a request spans workflows ("we want to buy an AI note-taker that records customer calls") or names none ("legal says we need to look at the new analytics thing").

## Files

| File | Read it when |
|---|---|
| [`../_shared/conventions.md`](../_shared/conventions.md) | Always: roles, intake rounds, and determination status apply to triage too |
| [`../_shared/company-profile.md`](../_shared/company-profile.md) | Always, for the regimes in scope and the business areas |
| [`../_shared/approvals.md`](../_shared/approvals.md) | When naming the decisions in the plan |

## The suite

Check which skills are installed by looking for each folder's `SKILL.md` next to this one. Recommend only what exists. For a planned skill, say what it will do and what to do meanwhile.

| Skill | Covers | Wave |
|---|---|---|
| `dpia` | DPIA and state assessment screening and drafting for a processing activity; processor assistance packs | 0 (built) |
| `vendor-review` | Vendor, subprocessor, and AI provider reviews; DPA gap analysis; AI vendor module with AIUC-1 benchmark | 1 (built) |
| `ropa` | RoPA entries and the register index | 1 (built) |
| `dsr-response` | Data subject requests: law, deadline, verification, response draft | 2 (built) |
| `ai-intake` | AI system and agent inventory, including agents in purchased tools; risk tiering | 2 (built) |
| `ai-impact-assessment` | AI impact assessments, FRIAs, and FRIA input packs | 2 (built) |
| `incident-assessment` | Breach notification analysis, clocks, and draft notices | 3 (built; counsel review of the breach reference pending) |
| `controls-and-evidence` | Control library, crosswalk, evidence, AIUC-1 readiness, testing schedule | 4 (built) |
| `program-assessment` | NIST Privacy Framework (and AI RMF, ISO/IEC 42001) maturity assessment and roadmap | 4 (built) |
| `notice-and-policy` | Privacy notice review against practice; AI acceptable use policy | 5 (built) |
| `regulatory-change` | New law or guidance mapped to program changes and reference updates | 5 (built) |
| `leadership-report` | Board and leadership risk summary | 5 (built) |

**Time-critical requests don't wait for triage.** A suspected breach, a data subject request with a running deadline, a regulator inquiry, or a subprocessor notice with an objection window comes first, before anything else in the plan. A data subject request goes straight to `dsr-response`, and a suspected breach straight to `incident-assessment`, which starts the clocks before anything else.

## Workflow

### 1. Restate the request as activities

Break the request into the things that will actually happen to personal data: what is being bought, built, shared, or changed; for whom; with what data. Each becomes a candidate for one or more workflows. A vendor that provides an AI feature to process student data usually means a vendor review, an AI intake, a DPIA screening, and a RoPA update.

### 2. Find the facts that decide the path

List only the facts that change which workflows run or in what order. Ask them in one short numbered message, usually under eight questions. Typical deciding facts:

- Has processing already started, including a pilot or a feature turned on by default? If so, containment comes first.
- Which data and whose: special category, children's, student, employee, or customer content?
- Is a vendor involved, and is the company the controller or a processor for this activity?
- Is AI involved, and does it make or inform decisions about people?
- Which regions and states are the people in, and where are the company's establishments?
- Is there a hard date (a launch, a signature, a notice period)?

Propose answers you can infer, marked as assumptions, so the user only has to correct them.

### 3. Write the plan

Reply with the plan in chat. Don't save a file unless the user asks. Keep it to one screen:

```markdown
**Triage plan: <request in a few words>**

Deciding facts: <answered, assumed (A), or open (?)>

| Step | Skill | Why | Depends on | Human decision after this step |
|---|---|---|---|---|
| 1 | vendor-review | New processor of student data with an AI feature | — | Privacy lead: approve vendor with conditions? |
| 2 | dpia | Children's free text plus profiling → high-risk indicators | Step 1 findings on training and retention | Privacy lead: screening outcome; risk acceptance per rating |
| 3 | ropa | New activity and recipient | Steps 1–2 | Business owner confirms facts |

Not yet available: <planned skills this needs, and what to do meanwhile>
Time-critical: <any running deadline, or "none">
Launch gate: nothing in this plan authorizes processing until each step's approver signs off.
```

Order the steps by dependency: what other steps need the answers to goes first. The usual order is:

1. Containment of anything already running
2. Vendor review, because its findings feed the assessment
3. AI intake
4. DPIA, and the AI impact assessment as a separate document
5. RoPA update
6. Notice update

### 4. Hand off

Ask whether to start step 1. When the user agrees, follow that skill's `SKILL.md` from the beginning, and carry forward the facts already gathered, so the user isn't asked twice. After each step, point to the next one and the decision the user needs to make before moving on.

## Rules

- Triage proposes a path. It doesn't make legal determinations. "This likely needs a DPIA" goes to the `dpia` skill for screening, not into the plan as a conclusion.
- Don't run a planned skill's work ad hoc in triage. Say it's not built yet, and recommend the interim step: the privacy lead, counsel, or the relevant built skill.
- Never create calendar events. Deadlines go in the plan, and in the action plans of the skills that run.
