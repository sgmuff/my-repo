# Risk method

| Field | Value |
|---|---|
| Covers | The suite's shared scoring method, risk catalog, and mitigation library |
| Basis | ICO-style 3x3 matrix; GDPR Recitals 75–76 and Art. 35(7)(c); NIST PF ID.RA-P; NIST AI RMF MAP 5.1 |
| Last verified | 2026-10-16 |
| Review interval | Annual, or when the company's risk appetite changes |
| Owner | Privacy lead |

Every skill that rates risk uses this method, so a Medium in a DPIA means the same as a Medium in a vendor review or an AI impact assessment. Section 2 holds the privacy risk catalog. The AI risk catalog arrives with the `ai-impact-assessment` skill.

## Contents

1. Scoring: the 3x3 matrix
2. Privacy risk catalog
3. Mitigation library
4. Risk appetite and who accepts what

---

## 1. Scoring

Risks are risks **to people**: their rights, freedoms, and interests. Risks to the company count only through their effect on people. A vendor review also records contractual and operational risks to the company, but it rates them in a separate column and doesn't mix them into the privacy rating.

### Three ratings, not two

Score each risk three times. The difference between the last two is the most important thing in the register.

| Rating | What it counts | When it's known |
|---|---|---|
| **Inherent** | The processing as designed, before safeguards | At screening |
| **Current residual** | Only the safeguards that are **in place and verified with evidence** today | Now. If no safeguard is verified yet, it equals the inherent rating. |
| **Target residual** | The planned safeguards, assuming each works as intended | A forecast, never a finding |

Give every control one of four statuses: **implemented and evidenced**, **implemented but unverified**, **planned**, or **absent**. A planned bias test is not evidence of fairness, and a contractual promise is not proof of a working deletion process.

A planned control lowers the target rating, never the current one. Closing an action doesn't lower risk by itself, either. Re-rate only after the evidence shows the control works. A control moves into the current rating only when its action is Done with evidence that it works (a configuration screenshot, a signed DPA clause, a test result), not when it is proposed or a policy is written.

Write it this way in the register and in the summary:

> **Residual risk: not yet confirmed.** Current residual: High (no controls verified). Target residual: Medium, subject to verification of A1–A4. Reassess each risk after those actions close.

**Prior consultation and other escalations follow the current rating, plus the target only once it is verified.** An unverified target of Medium is not a basis for ruling out GDPR Art. 36 consultation. Say that consultation is not required *if* the target is achieved and verified, and keep the question open until then.

### Splitting residual risk by who controls the safeguard

When the safeguards sit with different parties, rate them separately. The usual case is a processor assistance pack, where the company's controls and the customer's deployment choices both matter:

- **Vendor residual:** after the company's own verified controls
- **Deployment residual:** after the customer's policies, oversight, alternatives, and appeal routes, which only the customer can assess

Never assume a customer will implement a safeguard the company can't enforce. Name it as the customer's to assess.

### Likelihood that the harm happens

| Level | Meaning |
|---|---|
| **Remote** | Needs an unusual chain of events. No known occurrences in comparable processing. |
| **Possible** | Could plausibly happen. Has happened in comparable processing, or the controls depend on people following a process. |
| **Probable** | Expected to happen at some point, or built into the design (such as a default setting or a known gap). |

### Severity of the impact if it happens

| Level | Meaning |
|---|---|
| **Minimal** | Inconvenience or annoyance that people get past easily, such as receiving an unwanted email or having to re-enter data. |
| **Significant** | Serious consequences that people get past with some difficulty, such as financial loss, stress, discrimination on a limited scale, loss of control over sensitive data, or reputational embarrassment. |
| **Severe** | Significant or irreversible harm: physical harm, loss of a job, housing, or education, serious financial harm, long-term psychological harm, exposure of special category, children's, or student data, or discrimination at scale. |

Severity rises with the sensitivity of the data, with how vulnerable the people are, with how many people are affected, and with how hard the harm is to reverse. Mitigations mostly lower likelihood. Severity drops only when the mitigation changes what could be exposed, for example through minimization, pseudonymization, or shorter retention.

### Matrix

| Likelihood ↓ / Severity → | Minimal | Significant | Severe |
|---|---|---|---|
| **Probable** | Medium | High | High |
| **Possible** | Low | Medium | High |
| **Remote** | Low | Low | Medium |

**Overall residual risk** is the highest rating in the register, reported separately for current and target. Never average the ratings, because one High risk is not offset by ten Low ones.

**Target ratings name their conditions:** write `Target: Low, on verification of A3`. Approval of a target covers the plan, not the outcome. The risk is re-rated when the actions close.

**Record, for each risk:** who is harmed and how, likelihood and severity with a few words of justification, existing controls, planned controls (action IDs), the evidence that would verify them, the owner, and the three ratings. A score without a reason can't be defended to an auditor.

---

## 2. Privacy risk catalog

Start here, keep the risks that apply, and make each one specific to the activity. "Breach of data" is too vague. "Unauthorized access to meeting transcripts through a misconfigured sharing link exposes confidential discussions" is a risk you can score. A typical feature has 5 to 12 risks. Fewer than 4 usually means something was missed.

| Category | Typical risks to individuals | NIST PF |
|---|---|---|
| Confidentiality | Unauthorized access by insiders, attackers, or vendor staff; over-broad internal access; accidental disclosure to the wrong recipient; access by public authorities in a third country | PR.AC-P, PR.DS-P |
| Integrity and accuracy | Inaccurate data, inferences, or AI outputs that lead to wrong decisions about a person; hallucinated content attributed to a real person | CT.DM-P, ID.RA-P2 |
| Availability | Loss of data that people rely on; being unable to get data back for an access or portability request | PR.DS-P4, PR.PO-P3 |
| Loss of control | Hidden processing; use beyond what people expected; function creep into new purposes; vendor reuse for its own purposes | CM.AW-P, ID.DE-P3 |
| Surveillance and chilling effects | Monitoring that changes behavior, especially in employment or education; a feeling of being watched | ID.RA-P1, CT.DP-P |
| Discrimination and unfairness | Biased scoring or profiling; disparate impact on protected groups; manipulation through dark patterns | ID.RA-P2, CT.DM-P10 |
| Automated decisions | Significant decisions with no meaningful human review; no way to contest them | CT.PO-P3, CM.AW-P8 |
| Rights | Difficulty exercising access, deletion, or objection, for example where data is embedded in model weights, backups, or vendor systems | CT.DM-P1 to P4, CM.AW-P5 |
| Over-collection and retention | Collecting more than needed; keeping data indefinitely; personal data in logs | CT.DM-P5, CT.DM-P8 |
| Re-identification | Pseudonymized or "anonymous" data linked back to individuals; combining datasets | CT.DP-P2, CT.DP-P3 |
| Children, students, and vulnerable people | Exposure to profiling or targeted advertising; age-inappropriate processing; redisclosure of education records; power imbalance with an employer or school | ID.RA-P1 |
| Transfers | Inadequate protection in the recipient country; no enforceable rights | ID.DE-P3, ID.IM-P7 |
| Downstream harm | Identity theft, fraud, phishing, financial loss, reputational damage, emotional distress | CM.AW-P7, CM.AW-P8 |

---

## 3. Mitigation library

A mitigation is real only if it is specific, has an owner and a due date, and someone can verify it. "Implement appropriate security" is not a mitigation. Give each one an acceptance criterion, such as "the reading-response field is masked in production, including drafts and deleted text, shown by a capture test," so "done" means verified.

**Test masking and redaction against every channel**, not only the visible field: keystrokes, pasted text, drafts and deleted text; identifiers in URLs, page titles, and event metadata; user-identification calls and custom variables; screenshots, DOM snapshots, and exports; attachments; and any vendor feature (including the vendor's own AI features) that can process captured data. Re-test after application changes. A configuration setting such as "private by default" is not evidence that a field is masked.

**Model performance claims need their evidence:** sample size, test conditions, false positive and false negative rates, results by language and relevant group, confidence intervals where available, and known limits. For a confidence threshold, record why it was chosen and how it performs on a representative test set. A model's confidence score isn't a calibrated probability unless it was tested as one.

**Pseudonymization isn't anonymization.** Hashing an identifier still leaves pseudonymous personal data, and it does nothing for the rest of a payload. Don't lower severity as if data were anonymous.

**Containment covers history.** When a control is missing today, such as payload capture in error monitoring or training switched on by default, the fix includes finding out what was already captured or used, and deleting or isolating it where possible. Changing a setting today doesn't establish what happened before.

A label is not a mitigation. Renaming "suspicious behavior" to a neutral event name doesn't change what a model does or reduce false positives. Change the function, or measure it.

| Lever | Examples |
|---|---|
| Don't collect | Drop data fields; make features opt-in; process on the device; keep only aggregates |
| Reduce exposure | Pseudonymization, tokenization, or redacting personal data before vendor calls; short retention with automatic deletion; field-level encryption |
| Restrict access | Role-based access, just-in-time privileged access, access reviews, customer-controlled sharing defaults set to private |
| Vendor controls | A DPA with a contractual ban on training on the data, zero-data-retention settings, a regional endpoint, audit rights, a subprocessor notice period |
| Transfers | A regional deployment in the EEA, an active DPF certification, SCCs with a TIA, encryption with keys held in the EEA |
| Transparency | In-product notices at the point of collection, privacy notice updates, visible indicators (such as "recording"), labels on AI output |
| Choice | Opt-out or opt-in controls; admin-level disable switches; consent capture with a log |
| Human oversight | Review before a decision takes effect; a contest or appeal route; a confidence threshold |
| Quality | Accuracy evaluation, bias testing, feedback loops, a correction workflow |
| Rights tooling | Deletion that reaches vendors and derived data; an export format; a documented process for requests |
| Assurance | Penetration testing, a vendor security review, monitoring and alerting, an incident runbook |

---

## 4. Risk appetite and who accepts what

The defaults below match `approvals.md`. Change them there, not here. The approver is chosen by the **current** residual rating at the time of approval. If the approver accepts on the strength of a target, the approval names the actions that must close first, and launch waits for them.

| Residual rating | Accepted by | Extra steps |
|---|---|---|
| Low | Privacy lead | None |
| Medium | Privacy lead and the business owner | Conditions tracked in the action plan |
| High | Executive risk approver | GDPR prior consultation (`gdpr.md`, §10). Processing doesn't start until the consultation ends or the risk drops to Medium. |

Accepting a risk doesn't make unlawful processing lawful. Where a risk stays High because a legal requirement isn't met, the answer is to change the processing, not to accept the risk.
