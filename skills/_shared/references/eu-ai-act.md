# EU AI Act

| Field | Value |
|---|---|
| Covers | Regulation (EU) 2024/1689 (the AI Act), as amended by Regulation (EU) 2026/1744 (the Digital Omnibus on AI) |
| Version covered | AI Act as amended, in force from July 27, 2026 |
| Sources | EUR-Lex (eur-lex.europa.eu/eli/reg/2024/1689/oj); artificialintelligenceact.eu summary of Regulation (EU) 2026/1744 (retrieved 2026-10-16); Orrick, Cooley, and Jones Walker summaries (July 2026) |
| Last verified | 2026-10-16 |
| Verification scope | Amended dates and the main Omnibus changes checked against the sources above. The Official Journal publication date (reported as July 24, 2026) and the new wording of Art. 4 come from secondary sources. Article content otherwise reflects the 2024 text. |
| Review interval | Quarterly. Implementing acts, guidelines, harmonized standards, and codes of practice continue to appear. |
| Volatile points | §2 dates (confirm on EUR-Lex); §3 Art. 4 wording; Commission guidelines on high-risk classification and Art. 50 |

## Contents

1. Scope
2. Timeline, as amended
3. Roles
4. Risk categories
5. High-risk: Annex III areas
6. Provider obligations for high-risk systems
7. Deployer obligations and the FRIA
8. Transparency (Art. 50)
9. General-purpose AI models
10. Penalties

---

## 1. Scope

The Act applies to (Art. 2(1)):

- Providers placing AI systems or general-purpose AI models on the EU market or putting them into service in the EU, wherever the provider is established
- Deployers established or located in the EU
- Providers and deployers outside the EU, where the system's output is used in the EU

An **AI system** is a machine-based system designed to operate with varying levels of autonomy, that may adapt after deployment, and that infers from its input how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments (Art. 3(1)). Commission guidelines on the definition (February 2025) help with edge cases. Rule-based software that only executes rules defined by people is generally outside the definition.

Exclusions include military and national security uses, scientific research and development before market placement, and purely personal non-professional use (Art. 2(3)–(10)).

---

## 2. Timeline, as amended

| Date | What applies |
|---|---|
| August 1, 2024 | Entry into force |
| February 2, 2025 | Chapters I and II: definitions, AI literacy (Art. 4), and prohibited practices (Art. 5) |
| August 2, 2025 | General-purpose AI model obligations (Chapter V), governance, notified bodies, and penalties |
| July 27, 2026 | Regulation (EU) 2026/1744 enters into force |
| August 2, 2026 | General application, including the Art. 50 transparency duties |
| December 2, 2026 | New prohibitions on AI generating non-consensual intimate material or child sexual abuse material (Art. 5(1)(ba)–(bb)). Machine-readable marking (Art. 50(2)) for generative systems placed on the market before August 2, 2026 (Art. 111(4)). |
| August 2, 2027 | GPAI models placed on the market before August 2, 2025 must comply (Art. 111(3)) |
| **December 2, 2027** | **High-risk obligations for Annex III systems** (Art. 6(2); Chapter III, Sections 1–3), including deployer duties (Art. 26) and the FRIA (Art. 27). Moved from August 2, 2026 by the Omnibus. |
| August 2, 2028 | High-risk obligations for Annex I systems (safety components of regulated products, Art. 6(1)) |
| August 2, 2030 | High-risk systems used by public authorities and already on the market (Art. 111(2)) |

> **Verify:** Before telling a customer, an executive, or a regulator that a high-risk obligation applies on a date, confirm the date on EUR-Lex and record when you checked.

---

## 3. Roles

| Role | Definition | Notes |
|---|---|---|
| Provider | Develops an AI system or GPAI model, or has one developed, and places it on the market or puts it into service under its own name or trademark (Art. 3(3)) | Carries most high-risk obligations |
| Deployer | Uses an AI system under its authority, except for personal non-professional use (Art. 3(4)) | Art. 26 duties; FRIA for some (Art. 27) |
| Authorized representative | EU-based, mandated by a non-EU provider (Art. 3(5)) | Required before a non-EU provider places a high-risk system on the market (Art. 22) |
| Importer | EU-based, places a third-country provider's system on the market (Art. 3(6)) | Art. 23 |
| Distributor | Makes a system available in the supply chain, other than provider or importer (Art. 3(7)) | Art. 24 |
| Product manufacturer | Places a high-risk AI system on the market with its product under its own name | Treated as the provider (Art. 25(3)) |

**Becoming a provider (Art. 25(1)).** A distributor, importer, deployer, or other third party becomes the provider of a high-risk system if it (a) puts its name or trademark on it, (b) makes a substantial modification so it stays high-risk, or (c) changes the intended purpose of a non-high-risk system, including a GPAI system, so that it becomes high-risk.

**Roles are fact-dependent, so treat them as Provisional until the facts are in** (`conventions.md`, §7). Building on a third-party model doesn't by itself make the company a provider. Ask:

- Did the company develop the AI system, or have it developed? Or is it switching on a feature a vendor built and sells under the vendor's name? The second is usually deployment only.
- Does the company place the system on the market or put it into service under its own name or trademark? An agent the company builds on a vendor model and offers to customers as its own product points to provider. An internal tool built in-house and put into service for the company's own use can also make it the provider, as well as the deployer.
- Did the company substantially modify, rebrand, or repurpose a vendor's system (Art. 25(1))?

Record the answers in the fact register and propose the role from them. Don't pre-fill "provider and deployer" as settled.

**AI literacy (Art. 4).** The original text required providers and deployers to ensure a sufficient level of AI literacy among staff. Regulation (EU) 2026/1744 replaced it with a duty to take measures to support AI literacy, with no guarantee of a specific individual level. *Volatile:* quote the amended text from EUR-Lex before citing it.

---

## 4. Risk categories

**Classify by function, not by labels.** Classification turns on the system's intended purpose and what it actually does: its inputs, what it detects or infers, and how its outputs are used. A product name, a UI label, or marketing copy doesn't settle it either way. Renaming a "suspicious behavior" flag doesn't change a model that infers intent from faces. Ask for technical documentation that shows the inputs, the outputs, what each output means, and what the user interface tells the person acting on it.

**The categories run on different clocks.** Prohibitions have applied since February 2, 2025, and transparency duties since August 2, 2026. The later high-risk dates don't postpone either one. Assess a possible prohibition now, independently of the high-risk classification.

### Prohibited practices (Art. 5)

Stop and escalate at once. No mitigation makes these acceptable, and a human reviewer doesn't make a prohibited function permissible. A prohibited function has to be removed or disabled before use.

- (a) Subliminal, manipulative, or deceptive techniques that materially distort behavior and cause significant harm
- (b) Exploiting vulnerabilities due to age, disability, or social or economic situation
- (c) Social scoring leading to detrimental or disproportionate treatment
- (d) Predicting the risk of a person committing a crime based solely on profiling or personality traits
- (e) Untargeted scraping of facial images from the internet or CCTV to build facial recognition databases
- (f) Emotion recognition in the workplace or in education, except for medical or safety reasons
- (g) Biometric categorization inferring race, political opinions, trade union membership, religious or philosophical beliefs, sex life, or sexual orientation
- (h) Real-time remote biometric identification in public spaces for law enforcement, with narrow exceptions
- From December 2, 2026: AI systems that generate or manipulate non-consensual intimate material of identifiable people, or child sexual abuse material (Art. 5(1)(ba)–(bb), added by Regulation (EU) 2026/1744)

Commission guidelines on prohibited practices (February 2025) give examples. Text-based sentiment analysis is not emotion recognition under (f), because emotion recognition relies on biometric data.

For (f), separate **detecting an observable event** (a second face in frame, a phone, gaze leaving the screen) from **inferring an emotion or intention** (anxiety, dishonesty, intent to cheat) from biometric data. The first isn't emotion recognition; the second is, and it is banned in education and the workplace except for medical or safety reasons. Physical states such as pain or fatigue are treated differently under the guidelines. Decide on documented functionality, and record the evidence.

### High-risk (Art. 6)

- **Art. 6(1):** safety components of products covered by Annex I legislation that need third-party conformity assessment. As amended, AI used only for non-safety purposes, such as convenience or quality control, is not a safety component.
- **Art. 6(2):** systems in the Annex III areas (§5).
- **Art. 6(3) derogation:** an Annex III system is not high-risk if it poses no significant risk of harm to health, safety, or fundamental rights, because it (a) performs a narrow procedural task, (b) improves the result of a previously completed human activity, (c) detects decision-making patterns or deviations without replacing or influencing the human assessment without proper review, or (d) performs a preparatory task. **A system that profiles natural persons is always high-risk.**
- **Art. 6(4):** a provider relying on the derogation documents its assessment before placing the system on the market and registers it (Art. 49(2)).

### Transparency-risk systems

Systems covered by Art. 50 (§8), whatever their risk level.

### Minimal risk

Everything else. No specific obligations beyond AI literacy and voluntary codes of conduct.

### General-purpose AI models

A separate track (§9).

---

## 5. High-risk: Annex III areas

| Point | Area | Covered uses |
|---|---|---|
| 1 | Biometrics (where permitted by law) | (a) Remote biometric identification, excluding verification; (b) biometric categorization by sensitive or protected attributes; (c) emotion recognition |
| 2 | Critical infrastructure | Safety components in critical digital infrastructure, road traffic, and the supply of water, gas, heating, or electricity |
| 3 | **Education and vocational training** | (a) Determining access, admission, or assignment; (b) evaluating learning outcomes, including to steer the learning process; (c) assessing the appropriate level of education a person will receive or can access; (d) monitoring and detecting prohibited behavior during tests |
| 4 | **Employment and workers management** | (a) Recruitment or selection, including targeted job ads and analyzing, filtering, or evaluating applications; (b) decisions on terms of work, promotion, or termination, allocating tasks based on behavior or personal traits, and monitoring or evaluating performance and behavior |
| 5 | Access to essential private and public services | (a) Eligibility for public assistance benefits and services; (b) creditworthiness or credit scores, except fraud detection; (c) risk assessment and pricing for life and health insurance; (d) evaluating and classifying emergency calls and triage |
| 6 | Law enforcement | Several uses, where permitted by law |
| 7 | Migration, asylum, and border control | Several uses, where permitted by law |
| 8 | Administration of justice and democratic processes | Assisting judicial authorities; influencing elections or voting behavior |

Points 3 and 4 are the usual hits for an education or SaaS company. An AI feature that grades, ranks, proctors, or places students, or that screens, scores, or monitors workers, needs, at minimum, the derogation analysis in §4.

---

## 6. Provider obligations for high-risk systems

| Article | Obligation |
|---|---|
| Art. 9 | Risk management system across the life cycle, including testing and the effect on people under 18 and other vulnerable groups |
| Art. 10 | Data governance: training, validation, and test data that are relevant, sufficiently representative, and as free of errors and complete as possible; examination for bias |
| Art. 4a (new) | Exceptional basis to process special category data to detect and correct bias, under strict necessity, with safeguards, deletion, and records |
| Art. 11, Annex IV | Technical documentation (simplified for SMEs and small mid-caps) |
| Art. 12 | Automatic event logging |
| Art. 13 | Transparency and instructions for use to deployers |
| Art. 14 | Human oversight by design |
| Art. 15 | Accuracy, robustness, and cybersecurity |
| Art. 16–17 | Provider obligations; quality management system (simplified for SMEs and small mid-caps) |
| Art. 18–19 | Keep documentation 10 years; keep logs at least 6 months |
| Art. 20 | Corrective action and duty to inform |
| Art. 43, 47–49 | Conformity assessment, EU declaration of conformity, CE marking, registration in the EU database |
| Art. 72 | Post-market monitoring plan |
| Art. 73 | Serious incident reporting: within 15 days of awareness; 2 days for widespread infringements or serious disruption of critical infrastructure; 10 days for a death |

---

## 7. Deployer obligations and the FRIA

These apply to Annex III systems from December 2, 2027.

**Deployer duties (Art. 26):**

- (1) Use the system according to the provider's instructions
- (2) Assign human oversight to people with the competence, training, authority, and support to carry it out
- (4) Make sure input data under the deployer's control is relevant and sufficiently representative
- (5) Monitor operation; on risk, inform the provider and the market surveillance authority and suspend use; report serious incidents
- (6) Keep the logs under its control for at least 6 months
- (7) **Before using a high-risk system in the workplace, inform workers' representatives and the affected workers**
- (9) Use the provider's Art. 13 information to carry out a DPIA under GDPR Art. 35 where one is required
- (11) Inform natural persons that they are subject to a high-risk Annex III system that makes or assists decisions about them

**Right to explanation (Art. 86):** a person subject to a decision based on an Annex III high-risk system's output, which has legal or similarly significant effects, can obtain a clear and meaningful explanation of the system's role and the main elements of the decision.

**Fundamental rights impact assessment (Art. 27).** Required before first use of an Annex III high-risk system (other than point 2) by deployers that are:

- Bodies governed by public law
- Private entities providing public services
- Deployers of credit-scoring systems (Annex III, point 5(b)) or life and health insurance pricing systems (point 5(c))

Content (Art. 27(1)): (a) the deployer's processes in which the system is used; (b) the period and frequency of use; (c) the categories of people and groups likely to be affected; (d) the specific risks of harm to them; (e) the human oversight measures; (f) the measures if risks materialize, including internal governance and complaint mechanisms. The deployer notifies the market surveillance authority of the results using the AI Office's template (Art. 27(3)). Where a DPIA already covers an element, the FRIA complements it (Art. 27(4)).

Decide FRIA duties deployer by deployer. Whether a university or other customer owes one depends on its legal status (public-law body, or private entity providing a public service), the system's use, the exclusion of Annex III point 2 systems, and whether it can rely on a previous FRIA or the provider's assessment for similar cases (Art. 27(2)). Don't tell every customer in a sector that it owes one.

Most private SaaS companies are not FRIA-obligated, but their public-sector or education customers may be. The `ai-impact-assessment` skill (Wave 2) will build FRIAs and FRIA input packs for customers.

---

## 8. Transparency (Art. 50)

Applies from August 2, 2026, with the grace period for Art. 50(2) noted in §2.

- **50(1), providers:** AI systems that interact directly with people are designed so that people are told they are interacting with AI, unless that is obvious.
- **50(2), providers:** generative systems mark outputs as artificially generated or manipulated, in a machine-readable format.
- **50(3), deployers:** tell people exposed to emotion recognition or biometric categorization.
- **50(4), deployers:** disclose deepfakes. Disclose AI-generated or manipulated text published to inform the public on matters of public interest, unless a person reviewed it and a person or organization holds editorial responsibility.

Information is given clearly, at the latest at the first interaction or exposure (Art. 50(5)).

Analyze each paragraph on its own facts. Don't settle Art. 50 with a single rationale such as "an agent reviews every reply." Separate:

- Whether people **interact directly** with the AI system (50(1)): a chatbot does; an agent-assist tool whose drafts a human edits and sends usually doesn't
- Whether the system **generates synthetic content** that must be marked (50(2)): a provider duty, which depends on who the provider is
- Whether a deployer **publishes** generated text on matters of public interest, or deepfakes (50(4)), and whether the editorial-responsibility exception applies
- Who holds each duty: provider or deployer, which depends on the roles in §3

Human review of output is a useful safeguard, but it doesn't settle every Art. 50 duty. The Commission can assess codes of practice on labeling synthetic content and adopt implementing acts if they fall short (Art. 50(7), as amended).

---

## 9. General-purpose AI models

Providers of GPAI models must keep technical documentation, give information to downstream providers, put in place a copyright policy, and publish a summary of training content (Art. 53). Models with systemic risk carry more duties (Art. 55). The GPAI Code of Practice (July 2025) is the usual route to show compliance. The AI Office has exclusive competence over AI systems built on a GPAI model by the same provider (Arts. 75–75d, as amended).

A company that only calls a vendor's model through an API is not a GPAI model provider. It may still be the provider of the AI *system* it builds.

---

## 10. Penalties (Art. 99)

| Breach | Maximum fine |
|---|---|
| Prohibited practices (Art. 5) | €35 million or 7% of worldwide annual turnover, whichever is higher |
| Most other obligations, including provider, deployer, and transparency duties | €15 million or 3% |
| Supplying incorrect, incomplete, or misleading information to authorities | €7.5 million or 1% |

For SMEs, including start-ups, and small mid-caps, the cap is the lower of the two amounts (Art. 99(6), (6a)).
