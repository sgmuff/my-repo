# Screening

Screen every regime in scope and record a result for each. The screening table goes into the document whatever the outcome.

## Contents

0. Territorial scope first
1. EU GDPR: Article 35(3), the EDPB criteria, and national lists
2. UK GDPR: the ICO's list
3. Swiss FADP: Articles 22 and 23
4. EU AI Act: role, prohibited practices, high-risk systems, transparency, and follow-on assessments
4a. US states and FERPA
5. Exemptions and reuse of an existing DPIA
6. Recording the result

---

## 0. Territorial scope first

Before screening under any regime, record whether it applies to the company at all, and on what facts. For GDPR, use `../../_shared/references/gdpr.md`, §1a: establishment, targeting, and monitoring. The location of the data subjects alone doesn't settle it. If the facts are missing, the result is Open, and the missing facts go in Round 1.

---

## 1. EU GDPR

### Article 35(3): a DPIA is always required for

- (a) a systematic and extensive evaluation of personal aspects, based on automated processing including profiling, on which decisions with legal or similarly significant effects are based
- (b) large-scale processing of special category data (Article 9) or criminal offense data (Article 10)
- (c) systematic monitoring of a publicly accessible area on a large scale

### The EDPB high-risk criteria

These come from the WP29 guidelines (WP248 rev.01), which the EDPB endorsed. They are **indicators** of likely high risk, not independent legal triggers. For each one, record Present, Not present, or Unclear, with the specific facts that support it (by fact ID) and whether those facts are confirmed. Describe the actual operation precisely. An operational prediction about a ticket isn't the same as scoring a person. Adding ticket data to a contact profile isn't necessarily "combining datasets." Communications content or an LLM alone doesn't make a DPIA mandatory.

| # | Criterion | SaaS examples that meet it |
|---|---|---|
| 1 | Evaluation or scoring, including profiling and prediction | Lead scoring, user risk scores, productivity analytics, churn prediction about individuals |
| 2 | Automated decisions with legal or similarly significant effect | Automatic account suspension, fraud blocks, automated hiring screens, credit or pricing decisions |
| 3 | Systematic monitoring | Employee monitoring, session replay, location tracking, keystroke or screen capture, call recording |
| 4 | Sensitive or highly personal data | Article 9 or 10 data, plus communications content, location, financial data, and private documents |
| 5 | Large scale | Weigh the number of people, the volume of data, the range of data items, the duration, and the geographic reach |
| 6 | Matching or combining datasets | Enriching CRM records with third-party data, or joining product data across products or sources in ways users wouldn't expect |
| 7 | Vulnerable data subjects | Children, employees (because of the power imbalance), patients, the elderly, and asylum seekers |
| 8 | Innovative use of technology | Generative AI or LLM features, biometrics, emotion detection, and new tracking techniques |
| 9 | Processing that blocks a right, service, or contract | Gatekeeping access to a service based on a score or check |

**How to conclude.** The EDPB's guidance is that processing meeting two or more criteria will, in most cases, need a DPIA. One criterion can be enough when it's severe, such as children's data combined with profiling, or biometrics, and two can fall short in context. The criteria inform the Art. 35(1) question; they don't answer it. Write the conclusion as a judgment about likely high risk, name the criteria and facts that drive it, and say which facts are still unverified:

> The available design information indicates a DPIA is warranted under Art. 35(1). Scoring of contacts (criterion 1, F3 confirmed) and free-text communications that may contain special category data (criterion 4, F6 stated by requester) point to likely high risk. Provisional until F6 is confirmed.

"No answer could change the outcome" is too strong to write unless every supporting fact is confirmed. "No answer is likely to remove the need for a DPIA" is a fair working assumption when the drivers are well supported.

### National lists under Article 35(4) and (5)

Each EU supervisory authority publishes a list of processing types that require a DPIA, and some also publish lists of types that don't. Check the list of the lead supervisory authority in the company profile. Where the processing targets one member state, check that state's list too. Common additions beyond the EDPB criteria include:

- Large-scale employee monitoring
- Large-scale location data
- Biometrics for identification
- Processing children's data for marketing or profiling
- Combining data from several sources

If you can't confirm the current text of a national list, say so in the record instead of guessing.

*Volatile:* the EU Digital Omnibus proposal would replace national lists with EU-wide lists prepared by the EDPB (`../../_shared/references/gdpr.md`, §1). Until it is adopted and applies, national lists stand.

---

## 2. UK GDPR

The ICO requires a DPIA for anything on its list of processing likely to result in high risk, even with no other criterion met:

- Innovative technology, when combined with an EDPB criterion
- Denial of service: decisions about access to a product, service, opportunity, or benefit based on automated decision-making or special category data
- Large-scale profiling
- Biometric data
- Genetic data
- Data matching across sources
- Invisible processing: personal data obtained from a third party, where giving a privacy notice would be impossible or take disproportionate effort
- Tracking of online or offline location or behavior
- Targeting children or other vulnerable people, including any online service likely to be accessed by children (the Age Appropriate Design Code requires a DPIA)
- Risk of physical harm

UK transfers rely on the IDTA, the UK Addendum to the EU SCCs, or the UK Extension to the EU-US DPF (the "data bridge"). The Data (Use and Access) Act 2025 amended parts of UK GDPR, including automated decision-making, recognized legitimate interests, and the transfer test. Check the current ICO guidance on any point that turns on those changes.

---

## 3. Swiss FADP (in force since September 1, 2023)

- **Article 22:** a DPIA is required when processing may lead to a high risk to the personality or fundamental rights of the data subject. High risk arises in particular from the use of new technologies, or from the nature, scope, circumstances, or purpose of the processing. The two named cases are extensive processing of sensitive data and systematic monitoring of extensive public areas.
- Under Swiss law, sensitive data includes genetic and biometric data and data on religious, philosophical, political, or trade union views. It also covers health, intimate life, and racial or ethnic origin, along with administrative or criminal proceedings and social assistance measures.
- **Exemption:** a private controller doesn't need a DPIA if the processing is required by law, or if it uses a certified system, product, or service, or follows a code of conduct that meets the conditions in Article 22(5).
- **Article 23, prior consultation:** if residual risk stays high, consult the FDPIC before processing. A private controller can skip this if it consulted its data protection advisor, the Swiss equivalent of a DPO. Record that consultation.
- Swiss transfers rely on the Swiss-US DPF, or on EU SCCs with Swiss adaptations.

---

## 4. EU AI Act

Screen whenever the activity involves an AI system, meaning anything that uses ML or LLM models to produce outputs that affect people. The detail is in `../../_shared/references/eu-ai-act.md`. In the DPIA, record only what screening needs:

1. **Role:** provider, deployer, or both, proposed from the facts in `eu-ai-act.md`, §3, and marked Provisional. Building on a vendor model doesn't by itself make the company a provider. Developing the system and offering it under the company's name usually does.
2. **Prohibited practices (Art. 5):** these have applied since February 2, 2025, whatever the high-risk dates. Stop and escalate at once if any applies (`eu-ai-act.md`, §4). No mitigation, human reviewer, or relabeling makes them acceptable. For Art. 5(1)(f), separate detecting observable events from inferring emotion or intent, based on documented inputs and outputs. Text-based sentiment analysis is not emotion recognition, because emotion recognition relies on biometric data.
3. **High-risk (Art. 6 and Annex III):** classify by documented function, not by labels or product names (`eu-ai-act.md`, §4). Check the Annex III areas (`eu-ai-act.md`, §5). For an education or SaaS company, the usual hits are point 3 (admission, grading, placement, and proctoring) and point 4 (recruitment, task allocation, and monitoring or evaluating workers). If you rely on the Art. 6(3) derogation, record why, and remember that a system that profiles people is always high-risk.
4. **Transparency (Art. 50):** applies from August 2, 2026. Record whether the system interacts with people, generates synthetic content, or uses emotion recognition or biometric categorization.
5. **Follow-on assessments:** the AI impact assessment and, where Art. 27 requires one, the FRIA are **separate documents** produced by the `ai-impact-assessment` skill. The DPIA links them. Where a DPIA already covers an element, the FRIA complements it (Art. 27(4)). Deployers of high-risk systems use the provider's information to carry out the DPIA (Art. 26(9)).

**Timing:** under Regulation (EU) 2026/1744, Annex III high-risk obligations, including deployer duties and the FRIA, apply from **December 2, 2027**, not August 2, 2026. State the date, and add a verify flag (`eu-ai-act.md`, §2).

---

## 4a. US states and FERPA

**US states.** Screen state assessment duties with `../../_shared/references/us-state-privacy.md`, §5 and §6. Record the result even when GDPR screening comes back "Not required."

**FERPA.** If the activity touches student data, record:

- Whether the data includes education records or PII from education records (`ferpa.md`, §2)
- The company's role and the exception relied on (`ferpa.md`, §3–4)
- Whether the use stays within that exception. For example, model training or product analytics on education records usually falls outside the school official exception unless the institution authorizes it.

FERPA has no DPIA requirement of its own. Its limits on use and redisclosure feed the risk register and the action plan.

---

## 5. Exemptions and reuse

- A DPIA can cover a set of similar processing operations (Article 35(1)). If an existing DPIA covers the same type of processing, reference it, and assess only the differences.
- Processing that already existed before May 2018 and hasn't changed may not need a new DPIA. Once the risk changes, review it.
- Processing on an Article 35(5) "no DPIA required" list, where the lead supervisory authority publishes one.

---

## 6. Recording the result

Put a table like this in both templates. Every row has a status (`conventions.md`, §7):

| Regime | Applies to the company? | Trigger checked | Result | Supporting facts | Status | Rationale |
|---|---|---|---|---|---|---|
| GDPR territorial scope | Art. 3(1), 3(2) | — | Applies (EU users) | F2 | Provisional | … |
| GDPR Art. 35(3) | — | (a), (b), (c) | Not present | F4, F7 | Provisional | No decision with legal effect identified; closure consequences unverified (F7) |
| EDPB criteria | — | 1–9 | 3 present (#3, #7, #8), 1 unclear (#5) | F3, F5, F6 | Provisional | … |
| National list (CNIL) | — | … | … | … | … | … |
| UK ICO list | UK GDPR Art. 3 | … | … | … | … | … |
| Swiss FADP Art. 22 | FADP Art. 3 | … | … | … | … | … |
| EU AI Act | Art. 2; role per `eu-ai-act.md` §3 | Art. 5 (now), Art. 6 and Annex III (by function), Art. 50 (each paragraph) | … | … | … | … |
| AI impact assessment or FRIA | — | Art. 27; company policy | Needed or Not needed | … | … | Link the separate assessment |
| US states | Per state, `us-state-privacy.md` §1 | §5–6 | … | … | … | … |
| FERPA, COPPA, state student privacy | `ferpa.md` §2–3, §10–11 | Exception relied on; users under 13 | … | … | … | … |

**Outcome:** Warranted, Recommended, or Not indicated, with its status and the facts it depends on. Leave "decided by" and the date for the privacy lead to confirm (`approvals.md`).
