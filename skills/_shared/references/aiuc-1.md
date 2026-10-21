# AIUC-1

| Field | Value |
|---|---|
| Covers | AIUC-1, the AI agent standard published by the Artificial Intelligence Underwriting Company (AIUC) |
| Version covered | **October 15, 2026 release** (the Q4 2026 update). AIUC labels releases by date, not by number. |
| Next scheduled release | January 15, 2027 |
| Sources | standard.aiuc-1.com: requirement pages for domains A–F, changelog, certification, re-certification, and auditor scoping pages, and crosswalks to the EU AI Act, ISO/IEC 42001, and NIST AI RMF. All retrieved 2026-10-16. |
| Last verified | 2026-10-16 |
| Review interval | **Quarterly**, within two weeks of each release (January 15, April 15, July 15, October 15) |
| Volatile points | The whole file. Requirements are added, renamed, and retired each quarter. |
| Reuse terms | © AIUC, all rights reserved. AIUC's terms of use (standard.aiuc-1.com/legal/terms, checked 2026-10-21) grant a personal, noncommercial licence to use the site and bar copying, distributing, or creating derivative works from its content. This file holds IDs, titles, status, tags, and AIUC's published mappings, not requirement text. |

Every deliverable that cites AIUC-1 names the release it used, for example "AIUC-1 E004 (Oct 15, 2026 release)."

## Contents

1. Versioning and release cycle
2. Two ways the suite uses AIUC-1
3. How the standard works
4. Requirements by domain
5. Crosswalk to the EU AI Act, NIST AI RMF, and ISO/IEC 42001
6. October 15, 2026 changes and retired requirements
7. Recurring testing and certification calendar

---

## 1. Versioning and release cycle

AIUC-1 is updated every quarter, with releases on January 15, April 15, July 15, and October 15. The changelog at standard.aiuc-1.com/changelog lists each release's new, revised, and retired requirements.

Audits run against the latest release. A previous release can still be selected for up to 30 days after a new one appears, so an organization can prepare against a fixed version. The version is fixed at audit kickoff and stays constant through fieldwork and the report.

**When a new release appears:** run the `regulatory-change` skill (Wave 5) or update this file by hand. Diff the requirement list, update the tables in §4 and §5, record retired IDs in §6, and flag any open readiness assessment or vendor review that cited a changed requirement.

---

## 2. Two ways the suite uses AIUC-1

| Mode | When | What the skill does |
|---|---|---|
| **Certification readiness** | The company builds or deploys its own AI agent and wants AIUC-1 certification, or wants to operate as if certified | Maps the company's controls to each in-scope requirement, tracks evidence, schedules the quarterly testing, and prepares for the auditor |
| **Vendor benchmark** | The company is buying or embedding a third party's AI agent or model | Uses the requirements as the yardstick for the vendor review: asks whether the vendor is certified, for which product and release, and covers the gaps with questions and contract terms |

Pick the mode from the facts when it is obvious: a vendor review is a benchmark, and work on the company's own agent is readiness. Ask only when it isn't clear (`conventions.md`, §5).

---

## 3. How the standard works

- **Six domains:** A. Data & Privacy, B. Security, C. Safety, D. Reliability, E. Accountability, F. Society.
- **Requirements and controls.** Each requirement is **Mandatory** or **Optional**. Each has *core* controls, which an organization implements to pass, and *supplemental* controls, which it may opt into. Control IDs extend the requirement ID (for example, A009.1).
- **Capability tags** say which agents a requirement applies to: Universal, External-facing, Automation, Code-generation, Text-generation, Voice-generation, Image-generation. A mandatory requirement can be excluded only when the agent genuinely lacks the tagged capability, with a one- or two-sentence justification. Never exclude a requirement to reduce effort.
- **Statement of Applicability.** The client proposes and the auditor signs off the list of requirements and controls in scope, the exclusions, and the opt-ins. The audit report covers exactly that list.
- **Evidence categories:** legal policies, operational practices, technical implementation, and third-party evaluations. The evidence templates are at standard.aiuc-1.com/evidence.
- **Certification:** led by an AIUC-accredited auditor, typically four to eight weeks. Phases: scoping and kickoff (1–2 weeks), evidence collection (3–5 weeks), technical evaluations (3–5 weeks), and the audit report (1–3 weeks).
- **Maintaining certification:** certification lasts one year. Agents are red-teamed every quarter during that year, and a re-certification audit starts about two months before expiry.
- **Two different providers.** The **accredited auditor** reviews evidence and controls and supports the certification audit. The **technical evaluations** (the third-party testing requirements) are run by AIUC, per the current certification and re-certification guidance ("AIUC re-runs technical evaluations"). Plan and budget them separately, and confirm the arrangement with AIUC. *Verify* against the current guidance, since the arrangement could change between releases.
- **Developer and deployer responsibilities.** AIUC's scoping guidance distinguishes developers from deployers. Where an agent relies on a third-party model, record for each requirement whether the company, the model provider, or both are responsible.
- **Scope is usually a product, not a company.** A certificate covers specific agents. In a vendor review, check that the product being bought is in scope, which release was audited, and the report date.

AIUC-1 says itself that a certificate can't guarantee security, safety, or reliability, any more than a SOC 2 report can. Treat it as strong evidence, not proof.

---

## 4. Requirements by domain

AIUC-1 is © AIUC, all rights reserved, and its terms of use bar copying or redistributing its content. This file lists only what a cross-reference needs: each requirement's ID, title, status, and capability tags ("Applies to"), from the October 15, 2026 release. For what a requirement asks and its controls, read its page on standard.aiuc-1.com (linked under each domain). Don't paste AIUC's requirement text into this file or into deliverables kept in the repository; cite the ID and release instead.

### A. Data & Privacy

Requirement text: https://standard.aiuc-1.com/data-and-privacy

| ID | Requirement | Status | Applies to |
|---|---|---|---|
| A001 | Establish input data policy | Mandatory | Universal |

| A002 | Establish output data policy | Mandatory | Universal |

| A003 | Limit AI agent data access | Mandatory | Universal |

| A004 | Protect IP & trade secrets | Mandatory | Universal |

| A005 | Prevent cross-customer data exposure | Mandatory | Universal |

| A006 | Prevent PII leakage | Mandatory | Universal |

| A007 | Prevent IP violations | Mandatory | External-facing |

| A008 | Prevent leakage of credentials and secrets | Mandatory | Code-generation |

| A009 | Third-party testing for data & privacy risk | Mandatory | Universal |

### B. Security

Requirement text: https://standard.aiuc-1.com/security

| ID | Requirement | Status | Applies to |
|---|---|---|---|
| B001 | Third-party testing for security risk | Mandatory | Universal |

| B002 | Detect adversarial input | Optional | Universal |

| B003 | Manage public release of technical details | Optional | Universal |

| B004 | Prevent AI endpoint scraping | Mandatory | Universal |

| B005 | Implement real-time input filtering | Optional | Text-generation, Voice-generation, Image-generation |

| B006 | Prevent unauthorized AI agent actions | Mandatory | Automation |

| B007 | Enforce user access privileges to AI systems | Mandatory | Universal |

| B008 | Protect AI system deployment environment | Mandatory | Universal |

| B009 | Limit output over-exposure | Mandatory | Text-generation, Voice-generation, Image-generation |

| B010 | Promote secure patterns in generated code | Mandatory | Code-generation |

### C. Safety

Requirement text: https://standard.aiuc-1.com/safety

| ID | Requirement | Status | Applies to |
|---|---|---|---|
| C001 | Define AI risk taxonomy | Mandatory | Universal |

| C002 | Conduct pre-deployment testing | Mandatory | Universal |

| C003 | Prevent harmful outputs | Mandatory | Text-generation, Voice-generation, Image-generation |

| C004 | Prevent out-of-scope outputs | Mandatory | Text-generation, Voice-generation |

| C005 | Prevent agent-specific high risk outputs | Mandatory | Universal |

| C006 | Prevent output vulnerabilities | Mandatory | Code-generation, Text-generation, Voice-generation |

| C007 | Flag high risk outputs for human review | Optional | Universal |

| C008 | Monitor AI risk categories | Optional | Universal |

| C009 | Enable real-time feedback and intervention | Optional | Universal |

| C010 | Third-party testing for safety risk | Mandatory | Universal |

### D. Reliability

Requirement text: https://standard.aiuc-1.com/reliability

| ID | Requirement | Status | Applies to |
|---|---|---|---|
| D001 | Prevent hallucinated outputs | Mandatory | Text-generation, Voice-generation, Code-generation |

| D003 | Restrict unsafe tool calls | Mandatory | Automation |

| D004 | Third-party testing for reliability risk | Mandatory | Universal |

### E. Accountability

Requirement text: https://standard.aiuc-1.com/accountability

| ID | Requirement | Status | Applies to |
|---|---|---|---|
| E001 | AI failure plan for security breaches | Mandatory | Universal |

| E002 | AI failure plan for harmful outputs | Mandatory | External-facing |

| E003 | AI failure plan for hallucinations | Mandatory | External-facing |

| E004 | Assign accountability | Mandatory | Universal |

| E005 | Document data storage security | Mandatory | Universal |

| E006 | Conduct vendor and model due diligence | Mandatory | Universal |

| E008 | Review internal processes | Mandatory | Universal |

| E009 | Monitor third-party access | Mandatory | Universal |

| E010 | Establish AI acceptable use policy | Mandatory | Universal |

| E011 | Record processing locations | Mandatory | Universal |

| E012 | Document regulatory compliance | Mandatory | Universal |

| E013 | Implement quality management system | Optional | Universal |

| E015 | Log AI system activity | Mandatory | Universal |

| E016 | Implement AI disclosure mechanisms | Mandatory | Universal |

| E017 | Document system transparency policy | Optional | Universal |

| E018 | Third-party testing for accountability risk | Mandatory | Universal |

### F. Society

Requirement text: https://standard.aiuc-1.com/society

| ID | Requirement | Status | Applies to |
|---|---|---|---|
| F001 | Prevent AI cyber misuse | Mandatory | Text-generation, Automation, Voice-generation, Code-generation |

| F002 | Prevent catastrophic misuse | Mandatory | Text-generation, Voice-generation, Image-generation |

---

## 5. Crosswalk to the EU AI Act, NIST AI RMF, and ISO/IEC 42001

**Source.** The mappings come from AIUC's published crosswalks, inverted so that each AIUC-1 requirement lists the provisions it supports. AIUC's crosswalk pages still cite five requirements that the October 15, 2026 release retired. Those citations are reassigned to the successor requirements listed in §6.

**Proposed mappings.** Entries marked `*` are this suite's proposals for requirements that AIUC's crosswalks don't map yet. Confirm them before relying on them in an audit.

**Abbreviations.** NIST AI RMF functions: GV = GOVERN, MP = MAP, MS = MEASURE, MG = MANAGE. ISO/IEC 42001: plain numbers are management system clauses; "A." numbers are Annex A controls.

**Read the gaps too.** AIUC rates its own coverage of ISO/IEC 42001, and several clauses are partial or full gaps: 4.2 interested parties, 6.2 AI objectives, 7.3 awareness, 6.1.4 and A.5 impact assessment, A.6.1.2 and A.6.1.3 responsible development objectives and processes, and A.10.4 customers. AIUC-1 alone doesn't satisfy ISO/IEC 42001. See `iso-42001.md`.


| AIUC-1 | EU AI Act | NIST AI RMF | ISO/IEC 42001 |
|---|---|---|---|
| A001 Establish input data policy | Art. 11 | MS 2.10 | A.7.2, A.7.3 |
| A002 Establish output data policy | — | MP 4.1* | A.8.2* |
| A003 Limit AI agent data access | — | MP 2.1 | — |
| A004 Protect IP & trade secrets | Art. 72 | — | — |
| A005 Prevent cross-customer data exposure | — | MS 2.10 | — |
| A006 Prevent PII leakage | Art. 72 | MS 2.10 | — |
| A007 Prevent IP violations | — | GV 6.1, MP 4.1 | A.7.5 |
| A008 Prevent leakage of credentials and secrets | Art. 15* | MS 2.7* | — |
| A009 Third-party testing for data & privacy risk | — | MS 1.3*, MS 2.10* | A.6.2.4* |
| B001 Third-party testing for security risk | — | GV 4.3, MS 2.1, MS 2.6, MS 2.7 | — |
| B002 Detect adversarial input | Art. 15, Art. 72 | GV 1.5, MS 2.4, MS 2.7, MS 3.1 | — |
| B003 Manage public release of technical details | — | MS 2.7* | — |
| B004 Prevent AI endpoint scraping | Art. 15 | MS 2.7 | — |
| B005 Implement real-time input filtering | — | MS 2.7 | — |
| B006 Prevent unauthorized AI agent actions | — | MP 2.1 | — |
| B007 Enforce user access privileges to AI systems | Art. 15* | MS 2.7* | — |
| B008 Protect AI system deployment environment | Art. 15 | — | — |
| B009 Limit output over-exposure | — | MS 2.10 | — |
| B010 Promote secure patterns in generated code | Art. 15* | MS 2.7* | — |
| C001 Define AI risk taxonomy | Art. 9 | GV 1.3, GV 1.4, GV 4.2, GV 6.1, MG 1.2, MG 1.3, MG 1.4, MP 1.5, MP 5.1, MS 1.1, MS 2.10, MS 2.11, MS 3.1 | 4.1, 6.1.1, 6.1.2, 6.1.3, 6.1.4, 8.2, 8.3, 8.4, A.5.2, A.5.3, A.5.4, A.5.5 |
| C002 Conduct pre-deployment testing | Art. 9, Art. 27 | GV 4.3, MG 1.1, MP 4.2, MS 2.1, MS 2.3, MS 2.5, MS 4.3 | A.6.2.4, A.6.2.5 |
| C003 Prevent harmful outputs | Art. 9 | MS 2.11 | — |
| C004 Prevent out-of-scope outputs | Art. 72 | MP 2.2, MP 3.4 | — |
| C005 Prevent agent-specific high risk outputs | Art. 9 | MG 1.4 | — |
| C006 Prevent output vulnerabilities | Art. 72 | — | — |
| C007 Flag high risk outputs for human review | — | GV 3.2, MP 3.5 | A.6.1.2, A.9.2, A.9.3 |
| C008 Monitor AI risk categories | Art. 72 | GV 1.5, MG 3.1, MG 4.1, MS 2.4, MS 4.3 | 6.1.1, 6.1.2, 6.1.3, 8.2, 8.3, 9.1, A.5.4, A.6.2.6, A.9.2, A.9.4 |
| C009 Enable real-time feedback and intervention | Art. 14 | GV 3.2, MP 3.5, MS 3.3 | A.8.3 |
| C010 Third-party testing for safety risk | Art. 9 | GV 4.3, MG 2.2, MP 2.2, MS 1.3, MS 2.1, MS 2.6, MS 2.11, MS 4.1, MS 4.2 | A.6.2.4 |
| D001 Prevent hallucinated outputs | — | MS 2.5 | — |
| D003 Restrict unsafe tool calls | Art. 72 | GV 6.1 | — |
| D004 Third-party testing for reliability risk | — | GV 4.3, GV 6.1, MG 2.2, MS 1.3, MS 2.1, MS 2.5, MS 2.6, MS 4.1, MS 4.2 | A.6.2.4 |
| E001 AI failure plan for security breaches | Art. 20, Art. 73 | GV 4.3, MG 1.3, MG 4.3 | A.8.4, A.8.5 |
| E002 AI failure plan for harmful outputs | Art. 20, Art. 73 | GV 4.3, MG 1.3, MG 4.3 | A.8.4 |
| E003 AI failure plan for hallucinations | Art. 20, Art. 73 | GV 4.3, MG 1.3, MG 4.3 | A.8.4 |
| E004 Assign accountability | Art. 17, Art. 18 | GV 2.1, GV 2.3, MG 1.1, MP 3.5, MS 2.8, MS 4.3 | 5.1, 5.3, 6.3, 7.2, A.3.2, A.4.6, A.6.2.2, A.6.2.4, A.10.2 |
| E005 Document data storage security | — | MP 4.2 | — |
| E006 Conduct vendor and model due diligence | Art. 23, Art. 24 | MP 4.2 | A.10.3 |
| E008 Review internal processes | Art. 43 | GV 1.7, GV 5.1, GV 5.2, MG 4.2, MS 1.2, MS 2.13 | 6.3, 7.5.2, 9.2.1, 9.2.2, 9.3.1, 9.3.2, 9.3.3, A.2.3, A.2.4, A.3.3 |
| E009 Monitor third-party access | Art. 72 | GV 1.5, MG 4.1 | — |
| E010 Establish AI acceptable use policy | — | GV 1.2, MP 1.6, MP 3.3, MP 3.4, MS 2.4 | 4.1, 4.3, 5.2, A.2.2, A.2.4, A.9.2, A.9.3, A.9.4 |
| E011 Record processing locations | Art. 11 | GV 1.6 | A.7.5 |
| E012 Document regulatory compliance | Art. 16, Art. 18, Art. 21, Art. 22, Art. 25, Art. 26, Art. 43, Art. 44, Art. 47, Art. 48, Art. 49 | GV 1.1, GV 1.7, MP 1.1, MP 4.1 | 10.2, A.2.3, A.8.5 |
| E013 Implement quality management system | Art. 9, Art. 10, Art. 11, Art. 12, Art. 16, Art. 17, Art. 18, Art. 19, Art. 26, Art. 43, Art. 72, Art. 73 | GV 1.3, GV 1.4 | 4.4, 6.1.4, 7.1, 7.5.1, 8.1, 8.4, 9.1, 10.1, 10.2, A.4.2, A.5.2, A.5.3, A.5.4, A.6.2.3, A.6.2.7 |
| E015 Log AI system activity | Art. 12, Art. 19 | MS 2.4, MS 2.8 | A.6.2.8 |
| E016 Implement AI disclosure mechanisms | Art. 13, Art. 50 | MP 2.2, MP 3.4, MS 2.8 | A.8.2 |
| E017 Document system transparency policy | Art. 11 | GV 1.2, GV 1.6, MG 4.2, MG 4.3, MP 1.6, MP 5.2, MS 2.8, MS 2.9, MS 4.2, MS 4.3 | 4.3, 5.2, 7.4, A.2.2, A.2.4, A.4.2, A.4.3, A.4.4, A.4.5, A.6.2.3, A.6.2.7, A.8.2, A.8.5 |
| E018 Third-party testing for accountability risk | — | MS 1.3*, MS 2.8* | A.6.2.4* |
| F001 Prevent AI cyber misuse | — | MS 2.7 | A.5.5 |
| F002 Prevent catastrophic misuse | — | — | A.5.5 |

A dash means AIUC publishes no mapping for that framework. It doesn't mean there is no overlap.

---

## 6. October 15, 2026 changes and retired requirements

**New requirements:** A009 Third-party testing for data & privacy risk; E018 Third-party testing for accountability risk.

**New supplemental controls:** C002.4 open-weight model change regression testing; E006.2 open-weight model source, integrity, and license verification; F001.3 cyber capability assessment for modified models.

**Renamed:** B001 (was adversarial robustness testing), C010 (was harmful outputs testing), D004 (was tool call testing) are now the third-party testing requirements for security, safety, and reliability risk. E006 is now "Conduct vendor and model due diligence."

**Other revisions:** E016.1 consolidates five disclosure controls into one. D003.4 moved from supplemental to core.

**Retired requirements, and where their content went:**

| Retired | Title | Successor | Retired in |
|---|---|---|---|
| C011 | Third-party testing for out-of-scope outputs | C010 | Q4 2026 (Oct 15, 2026) |
| C012 | Third-party testing for customer-defined risk | C010 | Q4 2026 (Oct 15, 2026) |
| D002 | Third-party testing for hallucinations | D004 | Q4 2026 (Oct 15, 2026) |
| E007 | Document system change approvals | E004 | Q1 2026 (Jan 15, 2026) |
| E014 | Share transparency reports | E017 | Q1 2026 (Jan 15, 2026) |

The changelog summary says five requirements were added and three retired, but its table shows two new IDs and five retired rows. The tables above follow the requirement pages, which are the most specific source.

**Earlier releases, for context:** July 15, 2026 added A008 (secrets leakage) and B010 (secure code patterns) for code-generating agents and revised A003. April 15, 2026 focused on MCP security, third-party risk, and agent identity and permissions. January 15, 2026 added detailed evidence requirements. The standard launched July 22, 2025.

---

## 7. Recurring testing and certification calendar

These recurring duties feed the testing schedule that the `controls-and-evidence` skill (Wave 4) maintains.

| Duty | Frequency | Requirement |
|---|---|---|
| Third-party testing for data and privacy risk | At least every 3 months | A009 |
| Third-party testing for security risk | At least every 3 months | B001 |
| Third-party testing for safety risk | At least every 3 months | C010 |
| Third-party testing for reliability risk | At least every 3 months | D004 |
| Third-party testing for accountability risk | At least every 3 months | E018 |
| Regular internal process reviews, with records and approvals | Regular (AIUC's ISO crosswalk describes them as quarterly) | E008 |
| Re-certification audit | Annually, starting about 2 months before expiry | Certification terms |
| Check for a new AIUC-1 release | Quarterly: Jan 15, Apr 15, Jul 15, Oct 15 | — |
