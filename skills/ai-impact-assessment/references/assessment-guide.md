# AI impact assessment guide

What each section of the AI impact assessment (AIIA) covers, the evidence that supports it, and where it maps. Sections follow AIUC-1's domains, with Safety, Reliability, and Accountability as the core. Data & Privacy and Security are covered briefly, with links to the DPIA and the security team, because those documents own them.

Every section ends on a position with a status (`conventions.md`, §7), and the evidence it rests on. A section without evidence says so, and its conclusion is Provisional or Open.

## 1. Intended purpose and context

**Covers:** the intended purpose in the provider's terms and the company's; the deployment context; who uses it; who it affects; the decisions it informs or makes; reasonably foreseeable misuse.
**Evidence:** product documentation, instructions for use (AI Act Art. 13), the intake entry, sample outputs.
**Maps to:** NIST AI RMF MAP 1.1, 3.3; ISO/IEC 42001 A.9.4; AI Act Arts. 9, 13.

## 2. Fairness and non-discrimination (AIUC-1 Safety)

**Covers:** whether outcomes or error rates differ across groups, and whether those differences are justified.
**How:**
- Define the groups that matter in context (protected characteristics, and proxies such as language, disability-related behavior, device quality, or connectivity).
- Choose metrics that fit the decision. For selection decisions: selection rate ratios (the US "four-fifths" guideline is a screening heuristic, not a legal safe harbor). For error-prone classifiers: false positive and false negative rates by group. For scores: calibration by group.
- Say where group data comes from. Collecting special category data to test for bias needs a lawful route: GDPR Art. 9, or the AI Act's new Art. 4a for providers of high-risk systems, under strict conditions (`eu-ai-act.md`, §6). Synthetic or proxy testing has limits; state them.
- Record sample sizes, test conditions, and confidence intervals where available.
- Say what each figure measures: which stage of the process, what "pass" means, the threshold and model version, and whether the test population represents the real one. Check consistency across roles, locations, and time.
- A disparity is a warning signal, not proof of unlawful discrimination. An untested group is an evidence gap, not a finding. Label both accordingly.
- Predictive accuracy against past decisions (for example, "hired or not") measures agreement with those decisions, not validity for the job. Ask for validity evidence.
**Evidence:** test reports; the provider's bias evaluations; the company's own tests in its context.
**Maps to:** AIUC-1 C003, C010; NIST AI RMF MEASURE 2.11; AI Act Arts. 10(2)(f)–(g), 15; ISO/IEC 42001 A.5.4, A.7.4.

## 3. Transparency and explainability (AIUC-1 Accountability)

**Covers:** who is told that AI is involved, what they're told, and when; whether a person affected by a decision can get a meaningful explanation.
**How:** check each AI Act Art. 50 paragraph separately; GDPR Arts. 13(2)(f), 14(2)(g), and 15(1)(h) for automated decisions; AI Act Art. 86 for Annex III decisions; Art. 26(11) notice to people subject to high-risk decisions; Art. 26(7) notice to workers.
**Evidence:** UI screenshots, notice text, model cards, explanation samples.
**Maps to:** AIUC-1 E016, E017; NIST AI RMF MEASURE 2.8, 2.9; ISO/IEC 42001 A.8.2.

## 4. Human oversight (AIUC-1 Safety and Accountability)

**Covers:** who oversees the system, with what authority, information, and training; whether oversight is meaningful or nominal.
**How:**
- What the reviewer sees: the original evidence, or only the AI's output
- Whether the reviewer must record an independent reason before acting on an output
- Override and disagreement rates (a reviewer who never disagrees is a warning sign of automation bias)
- Whether the reviewer can stop the system (AI Act Art. 14(4)(e))
- Remedies for affected people: challenge, human review before an adverse finding, and an alternative process
**Evidence:** workflow documentation, reviewer training, override statistics, the appeal process.
**Art. 22 stays Provisional until these are confirmed:** whether low-scoring people are rejected in practice or only sorted; whether a reviewer looks at the underlying material (the application, the footage), not only the score; whether the reviewer can and does override it; and who decides the purposes and means. A reviewer clicking "approve" on a predetermined outcome isn't meaningful intervention.
**Maps to:** AIUC-1 C007, C009; NIST AI RMF GOVERN 3.2, MAP 3.5; AI Act Arts. 14, 26(2); GDPR Art. 22(3).

## 5. Data provenance and quality (AIUC-1 Data & Privacy)

**Covers:** where training, fine-tuning, evaluation, and retrieval data came from; licenses and consents; representativeness; known gaps; whether customer data is used for training.
**Evidence:** datasheets, license terms, data lineage records, vendor training terms.
**Maps to:** AIUC-1 A001, E006, E017; NIST AI RMF MAP 2.3; AI Act Art. 10; ISO/IEC 42001 A.7.2–A.7.6. Privacy risks to individuals go to the DPIA. Link it.

## 6. Reliability and model limitations (AIUC-1 Reliability)

**Covers:** accuracy and robustness in the deployment context; hallucination rates; incorrect tool calls; known failure modes; inputs the system handles poorly; performance drift.
**How:** pre-deployment testing across risk categories; third-party testing at least every 3 months for AIUC-1 readiness; monitoring in production; a rollback plan.
**Evidence:** evaluation results with test sets and conditions; red-team reports; production monitoring metrics.
**Maps to:** AIUC-1 C002, D001, D003, D004, C008; NIST AI RMF MEASURE 2.3, 2.5; AI Act Art. 15.

## 7. Safety (AIUC-1 Safety)

**Covers:** harmful, out-of-scope, or high-risk outputs (medical, legal, financial, crisis advice); vulnerable users; the risk taxonomy for this system.
**Evidence:** the system's risk taxonomy, safeguard configuration, test results, incident history.
**Maps to:** AIUC-1 C001, C003–C006, C010; NIST AI RMF MEASURE 2.6.

## 8. Security (AIUC-1 Security)

**Covers, briefly:** prompt injection, unauthorized agent actions, output over-exposure, endpoint scraping. The security team owns the detailed review. Record their findings, or the request to them.
**Maps to:** AIUC-1 B001–B010; NIST AI RMF MEASURE 2.7.

## 9. Accountability (AIUC-1 Accountability)

**Covers:** named owners for the system and its changes; failure plans for security breaches, harmful outputs, and hallucinations; logging; incident reporting (AI Act Art. 73 for providers of high-risk systems); records retention.
**Evidence:** RACI, failure plans, log configuration, change approval records.
**Maps to:** AIUC-1 E001–E004, E008, E015; NIST AI RMF GOVERN 2.1, MANAGE 4.3; ISO/IEC 42001 5.3, A.3.2.

## 10. Society (AIUC-1 Society)

**Covers, where relevant:** misuse for cyberattacks or catastrophic harm; information integrity at scale; environmental impact if material.
**Maps to:** AIUC-1 F001, F002; NIST AI RMF MEASURE 2.12; ISO/IEC 42001 A.5.5.

## 11. Rating and conclusion

Label each launch blocker Legal (applies on the launch date) or Readiness (an internal control, or preparation for a later obligation such as Annex III duties from December 2, 2027), per `conventions.md`, §7. Express launch conditions as measurable gates. Don't treat a SOC 2, ISO, or AIUC-1 certificate as evidence of fairness or explainability.

Use the AI risk catalog (`risk-method.md`, §2a) and the three ratings (inherent, current residual, target residual), adding reach, reversibility, and autonomy to severity. Rate harms to groups and society as well as to individuals. The conclusion states the launch gate (`conventions.md`, §7).

**AIUC-1 for systems that aren't agents.** Cite an AIUC-1 requirement only where its capability tags fit the system (`aiuc-1.md`, §3). For a classic scoring or classification model, many Safety and Society requirements are tagged for generation or automation; mark them not applicable rather than citing them, and lean on NIST AI RMF and ISO/IEC 42001 for those domains.

## FRIA (AI Act Art. 27)

Record the FRIA determination with its reasoning: whether the deployer falls within Art. 27's categories, and why. Record separately whether a GDPR DPIA is required and who owns it, and any worker consultation duties. "No FRIA" never means "no impact assessment needed."

When a deployer must carry out a FRIA (`eu-ai-act.md`, §7), record it as its own `aiia` record of kind `fria`, linked from the assessment and the DPIA. Art. 27(1) requires (a) the deployer's processes in which the system is used, (b) the period and frequency of use, (c) the categories of people and groups likely to be affected, (d) the specific risks of harm to them, (e) the human oversight measures, and (f) the measures if risks materialize, including internal governance and complaint mechanisms. The deployer notifies the market surveillance authority using the AI Office's template (Art. 27(3)). Where a DPIA covers an element, the FRIA complements it (Art. 27(4)).

When the company is the **provider** and a customer is the deployer, produce a **FRIA input pack** instead (kind `fria-input-pack`): the facts the customer needs for (a)–(f), without deciding whether the customer owes a FRIA. That's the customer's determination.

## ISO/IEC 42005

ISO/IEC 42005 gives guidance on AI system impact assessments. *Verify* its publication status before citing it (`iso-42001.md`, §4). This guide covers what ISO/IEC 42001 cl. 6.1.4 and A.5.2–A.5.5 require an impact assessment to address.
