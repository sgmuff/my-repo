# RoPA fields

Each field, what fills it, whether the law requires it, and the provision. "Required" means required in a GDPR Art. 30 record. Fields marked "Recommended" aren't required by Art. 30, but other duties or the suite's other skills depend on them.

## Controller record (GDPR Art. 30(1); FADP Art. 12)

| Field | Required? | Provision | What fills it | Notes |
|---|---|---|---|---|
| Controller name and contact; joint controllers; representative; DPO | Required | Art. 30(1)(a) | Company profile | Joint controllers need an Art. 26 arrangement; link it |
| Purposes | Required | Art. 30(1)(b) | Intake, PRD | Specific. "Provide customer support by email and chat," not "Business operations." One row per purpose. |
| Lawful basis per purpose; Art. 9 condition | Recommended | Arts. 6, 9; needed for Arts. 13–14 notices | Proposed by the skill, Provisional | Never inferred from a schema |
| Categories of data subjects | Required | Art. 30(1)(c) | Intake, docs | Note children, students, employees, and other vulnerable groups |
| Categories of personal data | Required | Art. 30(1)(c) | Data dictionary, schema, intake | Flag special category (Art. 9), criminal (Art. 10), biometric (which kind), US-sensitive, and education records |
| Categories of recipients, including in third countries | Required | Art. 30(1)(d) | Vendor list, vendor reviews, intake | Internal teams, processors (link the vendor review), other controllers, authorities |
| Transfers to third countries, and safeguards for Art. 49(1) second-subparagraph transfers | Required | Art. 30(1)(e) | Vendor reviews, company profile | Mechanism per transfer, including remote access |
| Time limits for erasure | Required "where possible" | Art. 30(1)(f) | Retention schedule | Per record category (for example, payroll, right-to-work, background reports, and emergency contacts each differ), and separately for people who don't proceed (rejected applicants). Separate legally required periods from company policy. Period, trigger, and how deletion happens. Don't guess. |
| General description of security measures | Required "where possible" | Art. 30(1)(g) | Company profile baseline | Cite the baseline, and add activity-specific measures |
| Sources of the data | Recommended | Art. 14(2)(f) notice duty | Intake | Direct, observed, from customers, or from third parties |
| Systems and applications | Recommended | NIST PF ID.IM-P1, P7 | Architecture docs | Where the data lives and moves |
| Derived data and its downstream use | Recommended | Arts. 5(1)(b), 22; NIST PF ID.IM-P4 | Docs, intake | Scores, estimates, or inferences the activity produces, which systems of record they're written to, and what decisions they feed. A model output written into a gradebook or HR system needs its downstream use confirmed. |
| Third-party data subjects | Recommended | Art. 14 | Intake | People other than the main subjects, such as emergency contacts, references, or people named in content, and how they're told |
| Business owner and system owner | Recommended | Accountability, Art. 5(2) | Intake | |
| Related assessments | Recommended | Art. 35; state assessments | Assessment folders | DPIA, screening record, AI impact assessment, vendor reviews |

## Processor record (GDPR Art. 30(2))

| Field | Required? | Provision |
|---|---|---|
| Processor name and contact; each controller on whose behalf it acts; representatives; DPO | Required | Art. 30(2)(a) |
| Categories of processing carried out for each controller | Required | Art. 30(2)(b) |
| Transfers to third countries, and safeguards | Required | Art. 30(2)(c) |
| General description of security measures | Required "where possible" | Art. 30(2)(d) |

"Each controller" can be described by category, such as "customers on the Enterprise plan, under the standard DPA," with the customer list held elsewhere.

## US state and FERPA fields

| Field | Why | Provision |
|---|---|---|
| Sale, sharing for cross-context behavioral advertising, targeted advertising | Notice, opt-out, and assessment duties | `us-state-privacy.md` §3, §5 |
| Sensitive data processed (state definitions) | Consent and assessment duties | `us-state-privacy.md` §3 |
| Profiling with legal or similarly significant effects | Opt-out and assessment duties | `us-state-privacy.md` §5 |
| CCPA categories of personal information | California notice duties | Cal. Civ. Code § 1798.140(v) |
| Data inventory | Minnesota requires one | Minn. Stat. § 325M (MCDPA) |
| Education records; FERPA exception relied on | Use and redisclosure limits | 34 CFR §§ 99.31, 99.33 |

## Exemption from keeping records

GDPR Art. 30(5) exempts organizations with fewer than 250 employees only when the processing is occasional, unlikely to result in a risk, and excludes Art. 9 and Art. 10 data. In practice almost no ongoing activity qualifies. FADP Ordinance Art. 24 has a similar small-company exemption. Record the reasoning if an entry relies on either exemption.

## Source values

Every field records its source: **Document** (name and version), **Stated by** (name, role, date), **Inferred** (from what), or **TBC**. A required field whose source is Inferred or TBC makes the entry Provisional.
