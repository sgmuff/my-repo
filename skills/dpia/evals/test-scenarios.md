# DPIA test scenarios

Use these to check that the `dpia` skill triggers on the right requests, stays quiet on its neighbors' requests, and produces a sound deliverable. The trigger lists are also in `trigger-evals.json` for the skill-creator's description optimizer. The full-run cases are in `evals.json`.

## Should trigger

| # | Request | Why it belongs here |
|---|---|---|
| 1 | "We're adding FullStory session replay to the student dashboard for spring semester. Do we need a DPIA? Most users are 13–17 at our partner districts." | Screening question about a new processing activity, with children and education records |
| 2 | "Can you write up the privacy assessment for the churn-prediction model CS wants to run on product usage data? Launch is February." | Asks for a DPIA without naming it; profiling |
| 3 | "Legal says Colorado needs a data protection assessment because we're turning on targeted ads for the free tier. Draft it." | State assessment, which the DPIA covers through its crosswalk |
| 4 | "rescreen DPIA-2026-004. Support Copilot is moving from OpenAI to a self-hosted Llama and we're adding Japan as a region" | Update to an existing DPIA after a material change |
| 5 | "Is keystroke monitoring for the SOC team high-risk processing under Art 35? HR wants it live next month." | Art. 35 screening; employee monitoring |
| 6 | "need a PIA for the new referral program: users upload their contacts and we email invites" | PIA by another name; third-party data subjects |
| 7 | "We're going to sell de-identified usage aggregates to a research partner. Do we need a CPPA risk assessment?" | California risk assessment trigger (sale) |
| 8 | "Our EU university customers keep asking for DPIA input on the proctoring add-on. Put together what they need from us." | Processor assistance pack (Art. 28(3)(f)) |
| 9 | "Product wants to fingerprint devices to stop account sharing. Run the screening." | Screening; tracking technology |

## Should not trigger (near misses)

| # | Request | Where it belongs |
|---|---|---|
| 1 | "Review Acme Analytics' DPA and tell me what's missing against Article 28." | `vendor-review` |
| 2 | "Add the new webinar registration flow to our RoPA." | `ropa` |
| 3 | "Run an AI impact assessment on the essay-grading model: fairness, human oversight, the works." | `ai-impact-assessment` |
| 4 | "A California user asked us to delete their data. What's our deadline and what do we send back?" | `dsr-response` |
| 5 | "A laptop with unencrypted student exports was stolen last night. Do we have to notify anyone?" | `incident-assessment` |
| 6 | "Update our privacy notice to cover the new in-app chat feature." | `notice-and-policy` |
| 7 | "Map our privacy program to the NIST Privacy Framework and show the gaps." | `program-assessment` |
| 8 | "Which US state privacy laws take effect in 2027, and what changes for us?" | `regulatory-change` |
| 9 | "We need a FRIA for the credit-scoring model a bank customer is deploying." | `ai-impact-assessment` |

## What a good run looks like

Every run, whatever the scenario:

- Reads `conventions.md` and the company profile first. Asks for profile gaps once per session, in Round 2.
- **Is evidence-led.** Keeps a fact register (Confirmed, Stated by requester, Unverified assumption, or TBC), and labels every legal determination and role Confirmed, Provisional, or Open. Nothing a skill drafts is Confirmed until a person signs off.
- **Proposes roles per operation** from the facts, as working assumptions. Doesn't treat a contract as deciding a role, and doesn't pre-fill AI Act provider status from "built on a vendor model."
- Checks **territorial scope** before concluding the GDPR doesn't apply.
- Treats EDPB criteria as **indicators with supporting facts**, and writes the outcome as a judgment ("a DPIA is warranted, Provisional").
- Runs **profiling and Art. 22 as separate analyses**, testing significance against real consequences. Treats reversibility as a safeguard.
- Classifies AI **by documented function, not labels.** Assesses possible prohibitions now. Analyzes each Art. 50 paragraph separately.
- Sends a short **Round 1** of blocker questions that asks for evidence (DPA, configuration, test results), and puts the rest in Round 2.
- Rates **inherent, current residual, and target residual** risk. Says "Residual risk: not yet confirmed" until controls are verified. Doesn't rule out prior consultation on an unverified target.
- States the **launch gate**: "Not authorized by this draft." Records the **stage** (Screening complete, Draft complete, Ready for sign-off) separately from the status.
- Keeps **facts, controls, and decisions** as three separate lists, gives each control a status (implemented and evidenced, implemented but unverified, planned, or absent), and lists verify flags in a **verification register**.
- If processing has already started, asks **containment** questions first.
- Gives every action a dependency, an acceptance criterion, and evidence; sequences dates so blockers and legality-affecting verifications fall before launch; turns each verify flag into an action.
- Records review dates as actions. **Never creates or offers calendar events.**
- Answers "does the law apply?" and "does this activity trigger it?" separately for each regime.
- Saves to `compliance/assessments/dpia/YYYY-MM-DD-<slug>.md` with the metadata block, status Draft, and the reference files used.
- Replies in **about 150 words**: path, status block, decisions needed, Round 1 questions, and a count of verify flags.

Scenario-specific expectations are in `evals.json`. The Support Copilot calibration case is in `../examples/example-run.md`.
