# Control crosswalk

| Field | Value |
|---|---|
| Covers | 32 common control objectives (CCO-01 to CCO-32), each mapped to the NIST Privacy Framework 1.0, AIUC-1 (Oct 15, 2026 release), NIST AI RMF 1.0, ISO/IEC 42001:2023 (public checklist), the EU GDPR, the EU AI Act as amended, US state privacy and breach laws, and FERPA |
| Version covered | Built 2026-10-16 from the reference files listed in each column |
| Sources | AIUC-1 ↔ AI Act, AI RMF, and ISO/IEC 42001 mappings come from AIUC's published crosswalks (`aiuc-1.md`, §5). Every other mapping, including all NIST Privacy Framework, GDPR, state, and FERPA links, is **this suite's proposal**, drawn from `nist-privacy-framework.md` §3 and the legal reference files. |
| Last verified | 2026-10-16 |
| Review interval | Quarterly, after each AIUC-1 release, and when any mapped framework changes |
| Volatile points | AIUC-1 columns (quarterly releases); NIST Privacy Framework IDs (1.1 will renumber them) |

A **control objective** is what a control has to achieve. A company **control** is the specific thing the company does to achieve it, such as "Okta enforces MFA for all workforce accounts." Map each company control to one or more objectives in the control library (`controls-and-evidence` skill). Its framework coverage then follows from this table, so one control, tested once, can satisfy several frameworks.

The mapping shows where frameworks **overlap**. It doesn't mean they're equivalent. A control that meets an objective may still need framework-specific evidence or wording to satisfy each one. Auditors decide what satisfies their framework.

## Contents

1. Privacy program and governance (CCO-01 to CCO-06)
2. Processing and individuals (CCO-07 to CCO-14)
3. Security and resilience (CCO-15 to CCO-20)
4. People and oversight (CCO-21 to CCO-23)
5. AI-specific (CCO-24 to CCO-32)

Abbreviations: NIST PF subcategory IDs as in `nist-privacy-framework.md`; AI RMF GV/MP/MS/MG = GOVERN/MAP/MEASURE/MANAGE; ISO numbers are clauses, "A." numbers are Annex A controls.

---

## 1. Privacy program and governance

| ID | Objective | NIST PF | AIUC-1 | NIST AI RMF | ISO/IEC 42001 | GDPR | EU AI Act | US states | FERPA |
|---|---|---|---|---|---|---|---|---|---|
| CCO-01 | Accountability: named owners for privacy and AI, with authority and reporting lines | GV.PO-P3, GV.PO-P4, GV.RM-P1, ID.BE-P1 to ID.BE-P3 | E004 | GV 2.1, GV 2.3 | 5.1, 5.3, A.3.2, A.10.2 | Arts. 5(2), 24, 37–39 | Arts. 17, 26(2) | Program duties; Tennessee NIST defense | § 99.7 (school official criteria) |
| CCO-02 | Policies: privacy policy, AI policy, acceptable use, reviewed on a schedule | GV.PO-P1, GV.MT-P2 | E010, E017 | GV 1.2 | 5.2, A.2.2, A.2.4 | Art. 24(2) | Art. 4 | — | — |
| CCO-03 | Legal and regulatory requirements identified and tracked | GV.PO-P5, GV.MT-P1 | E012 | GV 1.1, MP 1.1 | 4.1, 4.2, A.2.3 | Art. 24 | Arts. 16, 26 | All | Part 99 |
| CCO-04 | Risk method and appetite defined, applied, and reviewed | GV.RM-P1, GV.RM-P2, GV.RM-P3, ID.RA-P4, ID.RA-P5 | C001 | GV 1.3, GV 1.4, MP 1.5, MG 1.2–1.4 | 6.1.1–6.1.3, 8.2, 8.3 | Arts. 24, 32(2) | Art. 9 | Risk-based assessment duties | — |
| CCO-05 | Data and AI inventory: RoPA, data maps, AI system inventory | ID.IM-P1 to ID.IM-P8 | E011, E017 | GV 1.6 | A.4.2–A.4.5 | Art. 30 | Arts. 11, 49 | Minnesota data inventory | § 99.32 |
| CCO-06 | Privacy impact assessment of high-risk processing | ID.RA-P1 to ID.RA-P5, GV.MT-P1 | — | MP 5.1 | — | Arts. 35, 36 | Art. 26(9) | State data protection assessments; CCPA Regs. §§ 7150–7157 | — |

## 2. Processing and individuals

| ID | Objective | NIST PF | AIUC-1 | NIST AI RMF | ISO/IEC 42001 | GDPR | EU AI Act | US states | FERPA |
|---|---|---|---|---|---|---|---|---|---|
| CCO-07 | Lawful basis and consent recorded and managed | CT.PO-P1 | A001 | — | A.7.2 | Arts. 6, 7, 8, 9 | Art. 4a | Sensitive data consent; opt-outs | § 99.30 |
| CCO-08 | Transparency: notices that match practice | CM.PO-P1, CM.PO-P2, CM.AW-P1 | A001, A002, E016, E017 | MS 2.8, MS 2.9 | A.8.2, A.8.5 | Arts. 12–14 | Arts. 13, 26(11), 50 | Privacy notice duties | § 99.7 |
| CCO-09 | Individual rights handled on time | CT.PO-P3, CT.DM-P1 to CT.DM-P4, CM.AW-P5 | — | MS 3.3 | A.8.3 | Arts. 12, 15–22 | Art. 86 | Consumer rights and appeals | §§ 99.10, 99.20 |
| CCO-10 | Minimization and purpose limitation | CT.DP-P4, CT.DM-P10 | A003 | MP 2.1 | A.7.4 | Arts. 5(1)(b)–(c), 25 | Art. 10 | Maryland minimization; purpose limits | § 99.33 |
| CCO-11 | Retention and deletion enforced, including at vendors and in derived data | CT.DM-P5, PR.DS-P3 | A001, A002 | — | — | Arts. 5(1)(e), 17 | Arts. 18, 19 | Deletion duties | § 99.31(a)(6) |
| CCO-12 | De-identification and pseudonymization | CT.DP-P1 to CT.DP-P5 | — | MS 2.10 | — | Arts. 25, 32(1)(a), 89 | — | De-identified data definitions | § 99.31(b) |
| CCO-13 | Vendor and model due diligence, contracts, and monitoring | ID.DE-P1 to ID.DE-P5 | E006, E009 | GV 6.1, GV 6.2, MG 3.1, MG 3.2, MP 4.2 | A.10.2, A.10.3 | Art. 28 | Arts. 23–26 | Processor and service provider contracts | §§ 99.31, 99.33, 99.35 |
| CCO-14 | International transfers safeguarded | ID.IM-P7, ID.DE-P3 | E011 | — | — | Arts. 44–49 | — | — | — |

## 3. Security and resilience

| ID | Objective | NIST PF | AIUC-1 | NIST AI RMF | ISO/IEC 42001 | GDPR | EU AI Act | US states | FERPA |
|---|---|---|---|---|---|---|---|---|---|
| CCO-15 | Access control and least privilege, including agent permissions and customer isolation | PR.AC-P1 to PR.AC-P6 | A003, A005, B006, B007, D003 | MS 2.7, MP 2.1 | — | Art. 32(1)(b), 32(4) | Art. 15 | Reasonable security | § 99.31(a)(1)(ii) |
| CCO-16 | Encryption, data security, and secrets protection | PR.DS-P1, PR.DS-P2, PR.DS-P5 | A008, B008, E005 | MS 2.7 | — | Art. 32(1)(a) | Art. 15 | Reasonable security; breach law encryption safe harbors | — |
| CCO-17 | Secure development, maintenance, and change approval | PR.PO-P1, PR.PO-P2, CT.PO-P4, PR.MA-P1, PR.MA-P2 | E004, C002, B010 | MG 1.1, MS 2.3 | 6.3, A.6.2.2–A.6.2.5 | Art. 25 | Arts. 9, 17 | — | — |
| CCO-18 | Logging and monitoring | CT.DM-P8, GV.MT-P1 | E015, E009, C008, B002 | MS 2.4, MG 4.1, GV 1.5 | A.6.2.6, A.6.2.8 | Art. 32(1)(d) | Arts. 12, 19, 26(6), 72 | — | § 99.32 |
| CCO-19 | Incident response and breach notification | PR.PO-P7, PR.PO-P8, CM.AW-P7, CM.AW-P8, GV.MT-P5, GV.MT-P6 | E001, E002, E003 | GV 4.3, MG 1.3, MG 4.3 | A.8.4 | Arts. 33, 34 | Arts. 20, 73 | State breach laws (`us-breach-notification.md`) | NY Ed Law 2-d |
| CCO-20 | Backup, availability, and recovery | PR.PO-P3, PR.DS-P4, PR.PT-P4 | — | MG 2.4 | — | Art. 32(1)(b)–(c) | Art. 15(4) | Reasonable security | — |

## 4. People and oversight

| ID | Objective | NIST PF | AIUC-1 | NIST AI RMF | ISO/IEC 42001 | GDPR | EU AI Act | US states | FERPA |
|---|---|---|---|---|---|---|---|---|---|
| CCO-21 | Training, awareness, and AI literacy | GV.AT-P1 to GV.AT-P4 | — | GV 2.2 | 7.2, 7.3 | Art. 39(1)(b) | Art. 4 | — | § 99.31(a)(1)(ii) |
| CCO-22 | Internal review, audit, quality management, and continual improvement | GV.MT-P1 to GV.MT-P4 | E008, E013 | GV 1.5, MS 1.2, MS 2.13, MG 4.2 | 9.1–9.3, 10.1, 10.2 | Art. 24(1) | Art. 17 | Assessment review cadences | — |
| CCO-23 | Complaints and feedback handled | GV.MT-P7, CM.AW-P2 | C009 | GV 5.1, GV 5.2, MS 3.3 | A.3.3, A.8.3 | Art. 77 (and UK DUAA s. 103) | Art. 85 | Appeals | § 99.63 |

## 5. AI-specific

| ID | Objective | NIST PF | AIUC-1 | NIST AI RMF | ISO/IEC 42001 | GDPR | EU AI Act | US states | FERPA |
|---|---|---|---|---|---|---|---|---|---|
| CCO-24 | AI impact assessment and classification | ID.RA-P2 | C001, C002 | MP 1.1–5.2, MS 2.11 | 6.1.4, 8.4, A.5.2–A.5.5 | Art. 35 | Arts. 6, 9, 27 | CCPA ADMT; Colorado SB 26-189 | — |
| CCO-25 | AI data governance and provenance | CM.AW-P6 | A001, A007, E017 | MP 2.3 | A.7.2–A.7.6 | Arts. 5, 6, 9 | Arts. 4a, 10 | — | § 99.31(a)(1)(i)(B) |
| CCO-26 | AI safety guardrails: harmful, out-of-scope, and agent-specific high-risk outputs | — | C003, C004, C005, C006, F001, F002 | MS 2.6 | A.9.2 | — | Arts. 5, 9, 15 | — | — |
| CCO-27 | AI reliability: hallucinations and tool calls | — | D001, D003 | MS 2.5 | A.6.2.6 | Art. 5(1)(d) | Art. 15 | — | — |
| CCO-28 | AI security: adversarial input, filtering, endpoints, output exposure, and personal data leakage through outputs and logs | PR.DS-P5 | A006, B002, B003, B004, B005, B009 | MS 2.7 | — | Art. 32 | Art. 15 | — | — |
| CCO-29 | Human oversight, escalation, and the ability to contest | CT.PO-P3 | C007, C009 | GV 3.2, MP 3.5 | A.9.2, A.9.3 | Art. 22(3) | Arts. 14, 26(2), 86 | ADMT opt-out and appeal | — |
| CCO-30 | Independent and third-party testing | CT.DM-P9 | A009, B001, C010, D004, E018 | MS 1.3, MS 2.1, MS 4.1, MS 4.2 | A.6.2.4 | — | Art. 43 | NYC LL 144 bias audits | — |
| CCO-31 | Fairness and bias testing | ID.RA-P2, CT.DM-P10 | C003, C010 | MS 2.11 | A.5.4, A.7.4 | Arts. 5(1)(a), 9 | Arts. 4a, 10(2)(f)–(g) | Anti-discrimination; Illinois HB 3773; CCPA ADMT | — |
| CCO-32 | AI transparency to users: disclosure and labeling | CM.AW-P3 | E016 | MS 2.8 | A.8.2 | Arts. 13(2)(f), 14(2)(g) | Art. 50 | Utah AI disclosure | — |

Business data and IP protection (AIUC-1 A004, A007) map to CCO-16 and CCO-25.
