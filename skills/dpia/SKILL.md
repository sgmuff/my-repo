---
name: dpia
description: Screen and write a data protection impact assessment (DPIA) for a processing activity, from GDPR Article 35 screening to a draft with a fact register, risk register, action plan, and approval routing, folding in US state data protection assessments, CPPA risk assessments, and FERPA. Also produces processor assistance packs for customers' own DPIAs. Use it whenever someone asks whether a feature, product change, process, or data use needs a DPIA, PIA, privacy impact or risk assessment, or state data protection assessment, or asks for one to be written, updated, or rescreened, even without saying "DPIA." Triggers include Article 35 or 36, prior consultation, high-risk processing, customers asking for DPIA input, and Colorado, Virginia, or CPPA assessments. Not for vendor or DPA reviews (vendor-review), AI fairness or oversight assessments and FRIAs (ai-impact-assessment), or RoPA entries (ropa).
---

# Data protection impact assessment

This skill runs a repeatable DPIA. One run produces one Markdown file that serves as the paper trail: a full DPIA, a screening record that explains why one isn't needed, or a processor assistance pack for a customer.

The deliverable supports a decision a person makes. The skill gathers facts, screens, rates risk, and drafts. It takes a position on each point, cites the provision behind it, labels how settled that position is, and leaves determinations, risk acceptance, and launch to the approvers in `approvals.md`. **Be evidence-led, not conclusion-led.** A document that resolves legal questions confidently while key facts are unknown isn't defensible, however good its analysis.

## Files

Shared files (in `../_shared/`) apply to every skill in the suite. Read them at the step that needs them, not all up front.

| File | Read it when |
|---|---|
| [`../_shared/conventions.md`](../_shared/conventions.md) | At the start of every run: style, citations, verify flags, intake rounds, fact register, determination status, launch gate, output layout |
| [`../_shared/company-profile.md`](../_shared/company-profile.md) | At the start of every run |
| [`../_shared/approvals.md`](../_shared/approvals.md) | Step 8, to route sign-off |
| [`references/screening.md`](references/screening.md) | Step 2: GDPR, UK, Swiss, US state, FERPA, and AI Act screening |
| [`references/intake.md`](references/intake.md) | Step 3: the fact-finding checklist, tagged by round |
| [`references/assistance-pack.md`](references/assistance-pack.md) | When the company is a processor and the customer is the controller |
| [`../_shared/references/gdpr.md`](../_shared/references/gdpr.md) | Steps 2, 4, and 6: territorial scope, roles, lawful bases, Art. 22, transfers, prior consultation |
| [`../_shared/references/risk-method.md`](../_shared/references/risk-method.md) | Step 5: the matrix, the three ratings, the catalog, and mitigations |
| [`../_shared/references/us-state-privacy.md`](../_shared/references/us-state-privacy.md) | Step 7: state applicability, triggers, and the crosswalk |
| [`../_shared/references/ferpa.md`](../_shared/references/ferpa.md) | Steps 2 and 7, when student data is involved: FERPA, COPPA, and state student privacy laws |
| [`../_shared/references/eu-ai-act.md`](../_shared/references/eu-ai-act.md) | Steps 2 and 7, when the activity uses an AI system |
| [`../_shared/references/nist-privacy-framework.md`](../_shared/references/nist-privacy-framework.md) | Step 5, to tag risks with subcategory IDs |
| [`assets/dpia-template.md`](assets/dpia-template.md) | Step 8: the full DPIA or assistance pack |
| [`assets/screening-record-template.md`](assets/screening-record-template.md) | Step 8, when no full DPIA is required |
| [`examples/example-run.md`](examples/example-run.md) | When the user wants a test case, or you need a calibration example |

## Workflow

### 1. Load context, read the brief, and propose roles

Read `conventions.md` and `company-profile.md`. Check the "Review by" dates in `../_shared/references/README.md`, and note any file you'll rely on that is overdue or falls due before the activity launches.

Read everything the user supplied, and look under `<output root>/assessments/dpia/` and `<output root>/registers/ropa/` for an existing DPIA or RoPA entry for the same activity. If a DPIA exists, this is an update; see "Updating an existing DPIA" below.

**If processing has already started,** including a pilot or test on real data, deal with what exists before planning the launch. Record what was captured and where it went, and add immediate containment actions where needed (pause capture, restrict access, delete, or keep data out of model pipelines). A future launch gate doesn't address data already collected.

Start the **fact register** (`conventions.md`, §6): every fact the assessment relies on, with its status (Confirmed, Stated by requester, Unverified assumption, or TBC) and its evidence.

Then **propose the roles** for each processing operation, with the facts behind each, and mark them Provisional (`conventions.md`, §7). Roles follow the facts, not the contract (`gdpr.md`, §2). Assign them operation by operation:

- **Controller or joint controller:** the company owns the DPIA.
- **Processor:** the customer owns the DPIA. Produce a *processor assistance pack* under GDPR Art. 28(3)(f), following `references/assistance-pack.md`.
- **Both:** assess the controller operations. Note the processor operations and leave them out of scope, or give them their own assistance pack.
- **FERPA school official:** the institution remains responsible under FERPA. Assess the company's own processing, and record the exception and its limits (`ferpa.md`, §3–4).
- **AI system involved:** propose the EU AI Act role from the questions in `eu-ai-act.md`, §3. Building on a third-party model doesn't by itself make the company a provider.

A related operation where the company is controller, such as training its own model on customer data, is a separate workstream. Name it, add an action to assess it, and say how it affects this assessment.

### 2. Screen

Follow `references/screening.md`. Screening runs before full intake because it decides how much intake you need.

**Check territorial scope first.** Don't conclude that the GDPR doesn't apply from where the data subjects live (`gdpr.md`, §1a). If establishment facts are missing, the GDPR question is Open, and it goes in Round 1.

**Treat the screening criteria as indicators, not triggers.** The question under Art. 35(1) is whether the processing is likely to result in a high risk. For each EDPB criterion, record whether it is present, the specific facts that support that, and whether those facts are confirmed. Then reach the overall conclusion and say why. A criterion being present isn't the same as the overall conclusion.

Express the outcome with its status:

- **Warranted:** "The available design information indicates a DPIA is warranted under Art. 35 (Provisional; F2 and F5 unverified)." Proceed.
- **Recommended:** one indicator with aggravating factors, or the user wants a DPIA as good practice. Proceed, and say the DPIA is voluntary.
- **Not indicated:** write the screening record, but first check step 7. A state assessment may still be required.

Each outcome is the skill's position, followed by a `> **Decision needed:**` block for the privacy lead.

If the activity uses an AI system, screen it against the AI Act here, classifying by **function, not labels** (`eu-ai-act.md`, §4). Assess any possible prohibition now, independently of the high-risk dates, because prohibitions already apply. Record whether a separate AI impact assessment or FRIA is needed. Those are separate documents (`ai-impact-assessment` skill), linked from this one. If that skill isn't installed yet, add an action to produce one.

### 3. Gather the facts in two rounds

Use `references/intake.md`, whose questions are tagged Round 1 or Round 2.

- **Round 1 (blockers):** send first, alone, as one short numbered message. These are the facts that could change the screening outcome, a legal determination, or whether the activity can launch. Usually under 15 questions.
- **Round 2 (completion):** send with the draft. These cover company profile gaps (once per session), transfers, retention, security detail, consultation, and contributors.

**Ask for evidence, not only answers:** the DPA, the retention and training configuration, the subprocessor list, test results, the contract clause. Record what was provided in the fact register.

If the user can't answer, carry on with `TBC`. Never invent a fact, vendor setting, retention period, or control. Mark each TBC as a launch blocker or not, based on whether it could change legality or the required controls.

Flag these wherever they appear: special category data (with the biometric distinctions in `gdpr.md`, §3), criminal offense data, children's data and users under 13, student education records, transfers outside the EEA, UK, or Switzerland, and any model training on the data.

### 4. Assess necessity and proportionality

Use `gdpr.md`, §3–6. For each purpose:

- **Lawful basis** under Art. 6, plus an Art. 9 condition where needed. For legitimate interests, link the LIA (`lia` skill) by its ID, and summarize its outcome in a line; if none exists, recommend running `lia` rather than writing the test inline. For consent, check that it is freely given, specific, informed, unambiguous, and as easy to withdraw as to give.
- **Data minimization:** for each data element, why it's needed, and whether a less intrusive option exists. Name the elements to drop.
- **Purpose limitation:** list each secondary use, especially analytics, product improvement, model training, and staff performance evaluation, and whether it's compatible under Art. 6(4). Treat each one as a separate purpose that needs its own basis.
- **Transparency** (Arts. 13–14) and **data subject rights** (Arts. 15–22), including at processors and in backups, logs, and model weights.
- **Profiling and automated decisions:** run the two analyses in `gdpr.md`, §6 separately: is there profiling, and is there an Art. 22 decision? Test "similarly significant effects" against real consequences. Reversibility and notices are safeguards to record after the analysis, not exemptions.
- **Retention:** whether each period is justified by purpose, and how deletion is enforced. A vendor default isn't a justification.

End each point on "Adequate," "Gap: …," or "Not met: …," with the citation and the status.

### 5. Identify and score risks

Follow `risk-method.md` and use `../_shared/templates/risk-register.md`. Risks are risks *to individuals*. A typical feature has 5 to 12. Fewer than 4 usually means something was missed.

Score **three ratings** for each risk: inherent, current residual (verified controls only), and target residual (planned controls). A planned control never lowers the current rating. For each planned control, name the evidence that would verify it. Report the overall current and target ratings separately. Unless controls are already verified, the summary says **"Residual risk: not yet confirmed,"** gives the current rating, and gives the target as a forecast.

### 6. Check for prior consultation

Follow `gdpr.md`, §10, using the **current** residual rating. If any current rating is High, flag prior consultation and list the further mitigations that could bring it down. If the High drops only in the target, don't rule consultation out. Write that consultation isn't required *if* the target is achieved and verified, and name the actions to revisit it after. Where the GDPR doesn't apply, say Art. 36 isn't the route, and name any other obligation that applies.

### 7. Map to other regimes

For each regime, answer separately whether the law applies to the company, and whether this activity triggers an obligation under it, with the provision and the status (`us-state-privacy.md`, §1 and §5):

- **US states:** `us-state-privacy.md`. Usual additions: a benefit-risk weighing; California's required fields, go or no-go statement, and contributors; Colorado's Rule 8.04 items.
- **Student data:** `ferpa.md`. Keep school privacy and consumer privacy analyses apart. Cover the FERPA exception and its factual conditions, COPPA (users under 13; school authorization only for the school's purpose), and the state student privacy laws for each customer's state.
- **EU AI Act:** `eu-ai-act.md`. Record the role, the classification by function, each Art. 50 paragraph separately, and a link to the separate AI impact assessment or FRIA.

Add these as labeled subsections. Each conclusion gets a citation and a status, and each verify flag gets a matching action (`conventions.md`, §3–4).

### 8. Write the document

Fill in `assets/dpia-template.md` (or the screening record template). Save to `<output root>/assessments/dpia/YYYY-MM-DD-<slug>.md`, using the ID scheme in `conventions.md`, §9.

The executive summary opens with this status block, adapted to the facts:

> **DPIA status:** Draft, not approved. Stage: <Screening complete | Draft complete | Ready for sign-off> (`approvals.md`).
> **Screening:** <outcome> (<status; the facts it depends on>).
> **Residual risk:** <not yet confirmed | confirmed>. Current: <rating>. Target: <rating>, subject to verification of <actions>.
> **Prior consultation:** <determination, with status>.
> **Launch decision:** Not authorized by this draft. Production processing must not begin until the approver named in §11 has reviewed the completed assessment, confirmed the legal determinations and roles, verified the launch-blocking actions with evidence, and recorded the residual-risk decision.
> **Other regimes:** <each with its status>.

Then the rest of the summary: what the processing is, the top conditions for going ahead, and the decisions needed, from whom.

Rules for the document:

- Number facts `F1`, risks `R1`, actions `A1`, and questions `Q1`, and cross-reference them both ways.
- Every action has an owner, a due date, a dependency, and an acceptance criterion. Sequence the dates: nothing is due before what it depends on, and every launch blocker and legality-affecting verification is due before launch. State the number of launch blockers in a sentence that matches the table.
- Every verify flag is listed in the verification register (claim, why it matters, source, owner, whether it blocks launch) and has a matching action.
- Keep three lists apart: facts to confirm (fact register), controls to put in place (launch-blocking actions), and decisions needing approval. A missing control is an action, not a TBC fact. Give each control its status: implemented and evidenced, implemented but unverified, planned, or absent.
- Review dates and deadlines are actions. Never create calendar events (`connectors.md`).
- Set status to Draft, and route sign-off by the current residual rating (`approvals.md`), always including the requesting business area and, if different, the system owner.

### 9. Offer follow-through

If Jira or ServiceNow is connected, offer to create one issue per action, launch blockers first, after the user confirms the list. Otherwise put the CSV import block in the document's appendix. Never create calendar events.

### 10. Hand back

Follow `conventions.md`, §11. Check the document against the `writing-style` checklist and the sequencing rule. Then reply in about 150 words or fewer: the path, the status-block outcome in two lines, the decisions needed, the Round 1 questions (or a pointer to them), and a count of verify flags. Everything else stays in the document.

## Writing style

`conventions.md`, §2 applies in full. Three points matter most in a DPIA:

- **Terms of art stay, and get defined.** Controller, processor, data subject, supervisory authority, legitimate interests, special category data, education records, profiling. Define each on first use in the executive summary.
- **Citations stay precise.** Write "Art. 35(3)(a)," not "the GDPR's DPIA rules."
- **Active voice puts an owner on each control.** "The SRE lead deletes archives after 90 days," not "Archives should be deleted."

## Updating an existing DPIA

If the user points to an existing DPIA because something changed (a new vendor, data category, region, model, or incident), read it and rescreen against the change. Update the affected sections and the fact register, re-rate the risks (closed actions with evidence move into the current rating), add a version history row, bump the version, and reset the status to Draft. GDPR Art. 35(11) requires this review whenever the risk changes, California requires an update within 45 days of a material change, and several other states require updates after material changes.

Also check the document's reference list against the current reference index. If a framework it cites has changed since approval, say what changed and whether any conclusion moves.
