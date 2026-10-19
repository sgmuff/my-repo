# GLBA Safeguards Rule

| Field | Value |
|---|---|
| Covers | The FTC Safeguards Rule (16 CFR Part 314) under the Gramm-Leach-Bliley Act, and its application to higher education institutions and their service providers |
| Version covered | The rule as amended in 2021 (most provisions effective June 9, 2023) and 2023 (breach notification to the FTC, effective May 13, 2024) |
| Sources | ecfr.gov (16 CFR Part 314); FTC business guidance on the Safeguards Rule; Department of Education Federal Student Aid electronic announcements on GLBA |
| Last verified | 2026-10-18, against secondary sources (law-firm, regulator-guide, and tracker summaries); primary texts not yet read line by line. **Needs counsel review before live use.** |
| Review interval | Every six months |
| Volatile points | §4 (Department of Education audit and enforcement practice for institutions) |

## Contents

1. When the rule reaches the company
2. The written risk assessment (§ 314.4(b))
3. The rest of the information security program
4. Higher education

---

## 1. When the rule reaches the company

The Safeguards Rule binds **financial institutions** under FTC jurisdiction, which include colleges and universities that take part in federal student aid programs. A company that receives customer information from such an institution is a **service provider**: the institution must oversee it and require safeguards by contract (§ 314.4(f)). So the duty usually reaches the company through its customer contracts, and the company should be ready to show a risk assessment and safeguards that meet the rule.

"Customer information" means nonpublic personal information about a customer of the institution, such as student aid and loan records.

## 2. The written risk assessment (§ 314.4(b))

The assessment must be written and include:

1. Criteria for evaluating and categorizing identified security risks or threats
2. Criteria for assessing the confidentiality, integrity, and availability of information systems and customer information, including the adequacy of existing controls
3. How each identified risk will be mitigated or accepted, and how the program will address it

Repeat it periodically to reexamine reasonably foreseeable internal and external risks. Institutions that maintain information on fewer than 5,000 consumers still assess risk, but needn't put it in writing; § 314.6 also relieves them of the written incident response plan, the annual board report, and continuous monitoring or the testing schedule. MFA, encryption, and the FTC notice still apply. *Verify* the § 314.6 text, and whether the exemption reaches a service provider's own program.

## 3. The rest of the information security program

- A **qualified individual** oversees the program (§ 314.4(a))
- Safeguards including access controls, data inventory, **encryption** in transit and at rest, **multi-factor authentication**, secure development, disposal within two years of last use unless needed, change management, and monitoring of authorized users (§ 314.4(c))
- Regular testing: continuous monitoring, or annual penetration testing and vulnerability assessments every six months (§ 314.4(d))
- Staff training, service provider oversight, an incident response plan, and an annual written report to the board (§ 314.4(e)–(i))
- **Notification to the FTC** within 30 days of discovering the unauthorized acquisition of unencrypted customer information of at least 500 consumers, through the FTC's online form (§ 314.4(j), effective May 13, 2024). It doesn't require notice to individuals; state breach laws may. Route to `incident-assessment`. *Verify* how this notice applies to Title IV institutions alongside Department of Education reporting.

## 4. Higher education

The Department of Education expects Title IV institutions to comply, and checks through audits under its program participation agreements. *Volatile:* check current Federal Student Aid guidance, including any requirement to report suspected breaches to the Department. A vendor contract with a college will often carry these terms; review them in `vendor-review` when the company is the vendor.
