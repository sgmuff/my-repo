# US breach notification laws

| Field | Value |
|---|---|
| Status | **Draft reference. Counsel must review this file once before `incident-assessment` is used on a live incident.** Record the review in the row below. |
| Counsel review | Not yet reviewed (reviewer, date, scope: TODO) |
| Covers | The breach notification statutes of the 50 states, the District of Columbia, Puerto Rico, Guam, and the US Virgin Islands; federal and sector laws to flag |
| Version covered | As of 2026-10-16 |
| Sources | 2025–2026 changes checked against: Ashurst Perkins Coie, *2025 breach notification law update* (October 15, 2025); Covington Inside Privacy on Oklahoma SB 626 (August 2025) and on New York's GBL § 899-aa amendment (January 2025); Troutman Pepper and Hunton on California SB 446 (October–November 2025). Other rows are compiled from the statutes' known text and secondary matrices, and were **not** re-read against each statute. |
| Last verified | 2026-10-16 (changes only; see the Sources row) |
| Review interval | Quarterly. States amend these laws every session. |
| Volatile points | Every row. The most recent changes: California (30-day individual deadline and AG deadline, from January 1, 2026); New York (30-day deadline, December 24, 2024); Oklahoma (AG notice and expanded definitions, from January 1, 2026); North Dakota (financial institutions notify the commissioner within 45 days, 2025). |

This file supports triage, not a final legal conclusion. For every jurisdiction where affected people live, the `incident-assessment` skill states the obligation as Provisional, with a verify flag pointing to the statute, until counsel confirms it.

## Contents

1. How the state laws work
2. State table
3. Notice content
4. Federal and sector laws to flag
5. Student data

---

## 1. How the state laws work

Each law applies to the personal information of **its own residents**, wherever the company is. An incident affecting people in 30 states engages 30 laws. Work through these questions for each state:

1. **Is the data "personal information" under that state's definition?** The common core is a first name or initial and last name, combined with an SSN, a driver's license or state ID number, or a financial account or card number with any code needed to access it. Many states add more: online credentials (username or email plus password or security question), medical and health insurance information, biometrics, passport and other government ID numbers, taxpayer ID numbers, and dates of birth. Check the definition, not the common core.
2. **Was it a "breach"?** Most statutes require unauthorized **acquisition**. Some, such as New Jersey, Connecticut, Florida, and Puerto Rico (*verify*), also cover unauthorized **access**. Good-faith access by an employee for a legitimate purpose, with no further misuse, is usually excluded.
3. **Encryption safe harbor.** Encrypted data is usually excluded, unless the key was also taken or compromised. Some states also exclude redacted data.
4. **Risk-of-harm analysis.** Many states drop the notice duty if, after a reasonable investigation, misuse isn't reasonably likely. Several require the determination in writing, kept for years (often 5), or sent to the attorney general. California, Illinois, Massachusetts, Minnesota, Nevada, New Jersey (*verify*), Texas, and others allow no such analysis, or only a narrow one. When in doubt, assume notice is required.
5. **Owner or maintainer?** The company that owns or licenses the data notifies people. A company that only maintains it, as a processor or service provider, notifies the owner, usually immediately or within a short fixed period (New York: 30 days). It doesn't notify individuals itself unless its contract says to.
6. **Timing.** Fixed deadlines run from discovery or notification of the breach (§2). Where there is none, the standard is "the most expedient time possible and without unreasonable delay." A law enforcement request can delay notice in nearly every state.
7. **Regulators.** Many states require notice to the attorney general (or another agency) when a threshold number of residents is affected, sometimes before or at the same time as individual notice.
8. **Consumer reporting agencies.** Most states require notice to the nationwide credit bureaus above a threshold, usually 1,000 residents.
9. **Method.** Written or electronic notice (electronic only where consistent with E-SIGN or the existing relationship), or substitute notice (website posting, email, and media) when costs or numbers exceed the statute's limits.

---

## 2. State table

"Regulator" means the attorney general unless stated. Thresholds are counts of affected state residents. "RoH" means a risk-of-harm analysis can avoid notice. All rows are Provisional until counsel's review is recorded above.

| Jurisdiction | Statute | Individual notice deadline | Regulator notice | CRA notice | RoH | Notable |
|---|---|---|---|---|---|---|
| Alabama | Ala. Code § 8-38-1 et seq. | 45 days | >1,000, within 45 days | >1,000 | Yes | |
| Alaska | Alaska Stat. § 45.48.010 et seq. | Most expedient | Written no-harm determination to the AG | >1,000 | Yes, with AG notice | |
| Arizona | A.R.S. § 18-551 to 18-552 | 45 days | >1,000, within 45 days (AG and director of homeland security, *verify*) | >1,000 | Yes | |
| Arkansas | Ark. Code § 4-110-101 et seq. | Most expedient | >1,000, at the same time as individuals or within 45 days | >1,000 | Yes | Biometric data in the definition |
| California | Cal. Civ. Code § 1798.82 | **30 calendar days** from discovery or notification (SB 446, from Jan. 1, 2026), subject to law enforcement delay | **>500: sample notice to the AG within 15 calendar days of notifying individuals** (SB 446) | — | No | Prescribed headings and format. Private right of action for certain breaches under Cal. Civ. Code § 1798.150 (CCPA). |
| Colorado | C.R.S. § 6-1-716 | 30 days | ≥500, within 30 days | >1,000 | Yes | |
| Connecticut | Conn. Gen. Stat. § 36a-701b | 60 days | Not later than individual notice | — | Yes | 24 months of identity theft protection if SSN or TIN involved |
| Delaware | 6 Del. C. § 12B-101 et seq. | 60 days | >500, not later than individual notice | — | Yes | 1 year of credit monitoring if SSN involved |
| District of Columbia | D.C. Code § 28-3851 et seq. | Most expedient | ≥50, not later than individual notice | >1,000 | Yes | 18 months of identity theft protection if SSN or TIN involved |
| Florida | Fla. Stat. § 501.171 | 30 days | ≥500, within 30 days | >1,000 | Yes (written, to the AG) | Covers unauthorized access |
| Georgia | O.C.G.A. § 10-1-910 et seq. | Most expedient | — | >10,000 | — | Applies mainly to information brokers and data collectors (*verify*) |
| Hawaii | Haw. Rev. Stat. § 487N-1 et seq. | Without unreasonable delay | >1,000, Office of Consumer Protection | >1,000 | Yes | |
| Idaho | Idaho Code § 28-51-104 et seq. | Most expedient | State agencies only | — | Yes | |
| Illinois | 815 ILCS 530 | Most expedient | >500, not later than individual notice | — | No | Biometric, medical, and health insurance data in the definition |
| Indiana | Ind. Code § 24-4.9 | Without unreasonable delay, not later than 45 days | Any breach | >1,000 | Yes | |
| Iowa | Iowa Code § 715C | Most expedient | >500, within 5 business days of individual notice | — | Yes (written) | |
| Kansas | K.S.A. § 50-7a01 et seq. | Most expedient | — | >1,000 | Yes | |
| Kentucky | KRS § 365.732 | Most expedient | — | >1,000 | Yes | |
| Louisiana | La. R.S. 51:3071 et seq. | 60 days | Within 10 days of individual notice | — | Yes (written, keep 5 years) | |
| Maine | 10 M.R.S. § 1346 et seq. | 30 days after becoming aware | Any breach (AG or the relevant regulator) | >1,000 | Yes | |
| Maryland | Md. Code, Com. Law § 14-3501 et seq. | 45 days | Before individual notice | >1,000 | Yes (keep 3 years) | |
| Massachusetts | M.G.L. c. 93H | As soon as practicable | Any breach: AG and Office of Consumer Affairs and Business Regulation | As the director directs (*verify*) | No | Resident notice must **not** describe the nature of the breach or the number affected. 18 months of credit monitoring if SSN involved. |
| Michigan | MCL § 445.72 | Without unreasonable delay | — | >1,000 | Yes | |
| Minnesota | Minn. Stat. § 325E.61 | Most expedient | — | >500, within 48 hours | No | |
| Mississippi | Miss. Code § 75-24-29 | Without unreasonable delay | — | — | Yes | |
| Missouri | RSMo § 407.1500 | Without unreasonable delay | >1,000 | >1,000 | Yes (written, keep 5 years) | |
| Montana | Mont. Code § 30-14-1704 | Without unreasonable delay | At the same time as individuals (Office of Consumer Protection) | Yes (*verify*) | Yes (*verify*) | |
| Nebraska | Neb. Rev. Stat. § 87-801 et seq. | As soon as possible | Not later than individual notice | — | Yes | |
| Nevada | NRS 603A.010 et seq. | Most expedient | — | >1,000 | No | |
| New Hampshire | RSA 359-C:19 et seq. | As soon as possible | Any breach | >1,000 | Yes | |
| New Jersey | N.J.S.A. 56:8-161 et seq. | Most expedient | State Police, before individual notice | >1,000 | Yes (written, keep 5 years) | Covers unauthorized access |
| New Mexico | N.M. Stat. § 57-12C-1 et seq. | 45 days | >1,000, within 45 days | >1,000 | Yes | |
| New York | GBL § 899-aa | **Most expedient, and not later than 30 days after discovery** (amended Dec. 24, 2024); no delay for scoping or restoring systems | AG, Department of State, and State Police; NYDFS only for DFS-covered entities (72 hours under 23 NYCRR 500.17) | >5,000 | Narrow (inadvertent disclosure by authorized persons, written determination) | Medical and health insurance information in the definition. Maintainers notify owners within 30 days. |
| North Carolina | N.C.G.S. § 75-65 | Without unreasonable delay | Any breach | >1,000 | Yes | |
| North Dakota | N.D.C.C. § 51-30 | Most expedient | >250 | — | Yes (*verify*) | Financial institutions: commissioner of financial institutions within 45 days if >500 consumers (HB 1127, 2025) |
| Ohio | ORC § 1349.19 | 45 days | — | >1,000 | Yes | |
| Oklahoma | 24 O.S. § 161 et seq., as amended by SB 626 | Without unreasonable delay | **≥500: within 60 days of individual notice** (from Jan. 1, 2026) | >1,000 | Yes | Government ID numbers, unique electronic identifiers, and biometric data added to the definition. Reasonable safeguards are an affirmative defense to civil penalties. |
| Oregon | ORS 646A.600 et seq. | 45 days | >250 | >1,000 | Yes (written, keep 5 years) | |
| Pennsylvania | 73 P.S. § 2301 et seq., as amended in 2024 | Without unreasonable delay | >500, at the same time as individuals (*verify* threshold) | >1,000 | — | 12 months of credit monitoring where SSN, bank account, or driver's license or state ID number is involved (*verify*) |
| Rhode Island | R.I. Gen. Laws § 11-49.3-1 et seq. | 45 days | >500 | >500 | Yes | |
| South Carolina | S.C. Code § 39-1-90 | Most expedient | >1,000, Department of Consumer Affairs | >1,000 | Yes | |
| South Dakota | SDCL § 22-40-19 et seq. | 60 days | >250 | Yes, any | Yes (with AG notice of the determination) | |
| Tennessee | Tenn. Code § 47-18-2107 | 45 days | — | >1,000 | No (*verify*) | |
| Texas | Tex. Bus. & Com. Code § 521.053 | 60 days | ≥250, within 30 days (*verify* threshold) | >10,000 | No | |
| Utah | Utah Code § 13-44-101 et seq. | Most expedient | ≥500: AG and the Utah Cyber Center (2024 amendment, *verify*) | >1,000 | Yes | |
| Vermont | 9 V.S.A. § 2430, 2435 | 45 days | Preliminary notice within 14 business days of discovery | >1,000 | Yes (with notice to the AG) | |
| Virginia | Va. Code § 18.2-186.6 | Without unreasonable delay | Any breach | >1,000 | Yes | |
| Washington | RCW 19.255.010 | 30 days | >500, within 30 days | — | Yes | |
| West Virginia | W. Va. Code § 46A-2A-101 et seq. | Most expedient | — | >1,000 | Yes | |
| Wisconsin | Wis. Stat. § 134.98 | 45 days | — | >1,000 | Yes | |
| Wyoming | Wyo. Stat. § 40-12-501 et seq. | Most expedient | — | — | Yes | |
| Puerto Rico | 10 L.P.R.A. § 4051 et seq. | As expeditiously as possible | Department of Consumer Affairs within 10 days of detection | — | — (*verify*) | |
| Guam | 9 GCA § 48-10 et seq. | Without unreasonable delay | — | — | Yes (*verify*) | |
| US Virgin Islands | 14 V.I.C. § 2208 et seq. | Most expedient | — | — | — (*verify*) | |

> **Verify:** Every row before relying on it. Counsel should confirm each state that an incident touches, and the annual review should re-read each statute.

---

## 3. Notice content

**Most states require:** a description of the incident in general terms; the types of personal information involved; what the company has done to protect the data from further unauthorized access; a contact for questions; and advice to review account statements and monitor credit reports, with the toll-free numbers and addresses of the credit bureaus and the FTC.

**State-specific rules to check include:**

- **California:** the title "Notice of Data Breach," with prescribed headings ("What Happened," "What Information Was Involved," "What We Are Doing," "What You Can Do," "For More Information"), at least 10-point type, and date information. Offer 12 months of identity theft prevention services at no cost where the breach exposed SSNs or ID numbers and the company was the source (*verify*).
- **Massachusetts:** the resident notice must **not** describe the nature of the breach or the number of residents affected. It must explain the right to obtain a police report and how to request a security freeze.
- **Credit monitoring offers:** Connecticut (24 months), Delaware (1 year), the District of Columbia (18 months), Massachusetts (18 months), Pennsylvania (12 months), and California (12 months), each where SSNs or similar identifiers were involved. *Verify* each.
- **Regulator forms:** several attorneys general require their own online form (for example, California, Maryland, Massachusetts, New York, and Texas). Use the current form.

---

## 4. Federal and sector laws to flag

These laws are outside the suite's scope. Flag them for counsel when the facts point to them:

| Trigger | Law | Typical duty |
|---|---|---|
| Public company, material cybersecurity incident | SEC Form 8-K, Item 1.05 | Disclose within 4 business days of determining materiality |
| Non-bank financial institution under the FTC's Safeguards Rule, ≥500 consumers' unencrypted data | 16 CFR § 314.4(j) | Notify the FTC within 30 days of discovery |
| NYDFS-regulated entity | 23 NYCRR 500.17 | Notify DFS within 72 hours |
| Protected health information | HIPAA Breach Notification Rule, 45 CFR §§ 164.400–414 | Individuals within 60 days; HHS; media if >500 in a state |
| Health apps and connected devices outside HIPAA | FTC Health Breach Notification Rule, 16 CFR Part 318 | Individuals and FTC |
| Critical infrastructure | CIRCIA (rule pending, *verify* status) | Report to CISA |
| Federal contractors and defense | DFARS 252.204-7012 | Report to DoD within 72 hours |
| Telecommunications carriers | FCC CPNI breach rules | Notify the FCC, FBI, and Secret Service; then customers |
| Insurance licensees | State insurance data security laws (NAIC model) | Notify the insurance commissioner, often within 72 hours |

---

## 5. Student data

- **FERPA** has no breach notification duty, but an unauthorized disclosure of education records is a FERPA violation by the institution, and the Department of Education expects notice to affected parents and students as good practice. Vendors notify the institution under their contracts.
- **New York Education Law § 2-d:** third-party contractors notify the educational agency **within 7 calendar days** of discovery (8 NYCRR 121.10(a)), and reimburse notification costs where they caused the breach.
- **Other state student privacy laws and district data privacy agreements** set their own deadlines, often 48 to 72 hours. Check each contract (`ferpa.md`, §11).
