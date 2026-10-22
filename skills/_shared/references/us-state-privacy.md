---
title: US state comprehensive privacy laws
summary: 24 comprehensive state privacy laws, CCPA regulations, state AI laws
version_summary: Status as of 2026-10-16
last_verified: '2026-10-16'
review_by: '2027-01-16'
review_interval: Quarterly. State legislatures amend these laws every session.
index_interval: Quarterly
source_quality: primary
counsel_review:
  status: not-recorded
covers: The 24 enacted comprehensive state consumer privacy laws (20 in effect, 4 effective 2027–2028); CCPA regulations on risk assessments, ADMT, and cybersecurity audits; state AI laws that affect assessments
version: Status as of 2026-10-16
sources: Statute texts on each legislature's site; CPPA regulations (cppa.ca.gov); Colorado Privacy Act Rules (4 CCR 904-3); IAPP US State Privacy Legislation Tracker; law firm summaries listed under "Checked" below
verification_scope: 2026 developments (new laws, Colorado SB 26-189, CCPA regulation dates) checked against the sources below. Statute section numbers and pre-2026 thresholds come from the earlier DPIA reference and were not re-read against each statute. Spot-check a citation before quoting it to a regulator or customer.
volatile_points: §2 thresholds for Alabama, Louisiana, Oklahoma, and Vermont (secondary sources conflict); §6 Colorado ADMT rules (rulemaking open); §6 AI laws generally
checked: Venable 2026 mid-year update (July 2026); Morgan Lewis (July 2026); Lewis Rice on Oklahoma and Alabama; Privacy World (August 2026); Seyfarth and Eckert Seamans on Colorado SB 26-189 (May 2026); MoFo and Hunton on CCPA regulations (September–October 2025)
---

# US state comprehensive privacy laws

Use this file to decide which state laws apply to an activity, which assessments it triggers, and what processor contracts must say. Breach notification laws are separate and arrive with the `incident-assessment` skill (Wave 3). Consumer rights and deadlines will be detailed in the `dsr-response` skill's matrix (Wave 2).

## Contents

1. How to use this file
2. State table: applicability and assessments
3. Common obligations
4. Processor and service provider contracts
5. Assessment triggers and the crosswalk
6. California CPPA regulations
7. Colorado
8. Virginia
9. AI-specific state laws
10. Exemptions that often matter

---

## 1. How to use this file

Answer two questions separately, for each state. They need different facts, and mixing them produces overconfident conclusions.

1. **Does the law apply to the company?** The company profile lists the states in scope. If it says "all," treat every state whose law is in effect on the activity's start date as a candidate, and note laws that take effect during the activity's life. Applicability depends on thresholds, exemptions (§10), and the company's role for this activity. A district's or customer's service provider and a business acting for its own purposes have different obligations. If the profile hasn't confirmed thresholds, applicability is **Open**, not "No."
2. **Does this activity trigger a specific obligation?** Most states share one trigger list (§5). California and a few others add their own. Tie each conclusion to the statutory or regulatory provision, not to a general description of the feature.
3. **Then the content.** Build one assessment that satisfies every triggered state, using the crosswalk in §5.

"No state assessment is triggered" is a strong statement. Make it only when both questions are answered on confirmed facts. Otherwise write "Provisional: no trigger identified on current facts; applicability assessment incomplete (F<n>)," and list the facts needed.

> **Verify:** The thresholds in §2 are summaries. Before telling anyone a law does or doesn't apply, check the statute's applicability section and record the date checked.

---

## 2. State table: applicability and assessments

Thresholds are counts of state residents ("consumers") whose personal data the business controls or processes in a year, excluding payment-only data unless noted. "Sale %" means the share of gross revenue from selling personal data.

| State | Law | Effective | Applicability (summary) | Assessment duty |
|---|---|---|---|---|
| California | CCPA as amended by CPRA; Cal. Civ. Code § 1798.100 et seq.; CCPA Regs. 11 CCR § 7000 et seq. | Jan 1, 2020; CPRA Jan 1, 2023; new regulations Jan 1, 2026 | Annual gross revenue over $25M (inflation-adjusted, $26.625M from 2025); or buys, sells, or shares PI of 100,000+ consumers or households; or 50%+ of revenue from selling or sharing PI | Yes: CCPA Regs. risk assessments (§6) |
| Virginia | VCDPA, Va. Code § 59.1-575 et seq. | Jan 1, 2023 | 100,000; or 25,000 and 50%+ sale % | Yes (§8) |
| Colorado | CPA, C.R.S. § 6-1-1301 et seq.; CPA Rules | Jul 1, 2023 | 100,000; or 25,000 and any revenue or discount from sale | Yes, with prescriptive content (§7) |
| Connecticut | CTDPA, Conn. Gen. Stat. § 42-515 et seq., as amended by SB 1295 (2025) | Jul 1, 2023; amendments Jul 1, 2026 | From Jul 1, 2026: 35,000; or controls or processes sensitive data; or offers personal data for sale | Yes; amendments add impact assessments for profiling that informs decisions with legal or similarly significant effects |
| Utah | UCPA, Utah Code § 13-61-101 et seq. | Dec 31, 2023 | Revenue of $25M+ **and** 100,000, or 25,000 and 50%+ sale % | No |
| Florida | FDBR, Fla. Stat. § 501.701 et seq. | Jul 1, 2024 | Only controllers with $1B+ global revenue plus a device, app store, or smart speaker test) | Yes, for covered controllers |
| Texas | TDPSA, Tex. Bus. & Com. Code § 541.001 et seq. | Jul 1, 2024 | Does business in Texas and is not an SBA small business (no numeric threshold). Small businesses still need consent to sell sensitive data. | Yes |
| Oregon | OCPA, ORS 646A.570 et seq. | Jul 1, 2024 | 100,000; or 25,000 and 25%+ sale % | Yes; keep 5 years |
| Montana | MCDPA, Mont. Code § 30-14-2801 et seq., as amended by SB 297 (2025) | Oct 1, 2024; amendments Oct 1, 2025 | From Oct 1, 2025: 25,000; or 15,000 and 25%+ sale % | Yes |
| Iowa | ICDPA, Iowa Code ch. 715D | Jan 1, 2025 | 100,000; or 25,000 and 50%+ sale % | No |
| Delaware | DPDPA, 6 Del. C. § 12D-101 et seq. | Jan 1, 2025 | 35,000; or 10,000 and 20%+ sale % | Yes (for processing from Jul 1, 2025) |
| New Hampshire | NH Rev. Stat. ch. 507-H | Jan 1, 2025 | 35,000; or 10,000 and 25%+ sale % | Yes |
| New Jersey | NJDPA, N.J.S.A. 56:8-166.4 et seq.; NJ Division of Consumer Affairs rules | Jan 15, 2025 | 100,000; or 25,000 and any revenue or discount from sale | Yes, **before** the processing starts |
| Nebraska | NDPA, Neb. Rev. Stat. § 87-1101 et seq. | Jan 1, 2025 | Does business in Nebraska and is not an SBA small business (no numeric threshold) | Yes |
| Tennessee | TIPA, Tenn. Code § 47-18-3201 et seq. | Jul 1, 2025 | Revenue over $25M **and** 175,000, or 25,000 and 50%+ sale % | Yes. A **written** privacy program that reasonably conforms to the NIST Privacy Framework, that the company maintains and follows, and that provides the consumer rights TIPA requires, is an affirmative defense. The program must be updated to conform to a revised framework within 2 years of NIST publishing it (*verify* the statute's wording; Privacy Framework 1.1 was still a draft on 2026-10-16). |
| Minnesota | MCDPA, Minn. Stat. § 325M.10 et seq. | Jul 31, 2025 | 100,000; or 25,000 and 25%+ sale % | Yes, plus a duty to keep a data inventory and documented policies |
| Maryland | MODPA, Md. Code, Com. Law § 14-4601 et seq. | Oct 1, 2025 (for processing from Apr 1, 2026) | 35,000; or 10,000 and 20%+ sale % | Yes, covering each algorithm used. Strict minimization: collection limited to what is reasonably necessary to provide or maintain a specific product or service the consumer requested. Sale of sensitive data banned. |
| Indiana | ICDPA, Ind. Code § 24-15 | Jan 1, 2026 | 100,000; or 25,000 and 50%+ sale % | Yes |
| Kentucky | KCDPA, KRS 367.3611 et seq. | Jan 1, 2026 | 100,000; or 25,000 and 50%+ sale % | Yes |
| Rhode Island | RIDTPPA, R.I. Gen. Laws § 6-48.1 | Jan 1, 2026 | 35,000; or 10,000 and 20%+ sale % | Yes |
| Oklahoma | Oklahoma Consumer Data Privacy Act (2026) | Jan 1, 2027 | Most sources: 100,000; or 25,000 and 50%+ sale %. *Volatile: one source differs.* | Yes: standard triggers, before the processing |
| Louisiana | Louisiana consumer privacy act (2026) | Jan 1, 2027 | *Volatile: sources conflict.* | Yes |
| Alabama | Alabama Personal Data Protection Act (HB 351, signed Apr 17, 2026) | May 1, 2027 | *Volatile: sources conflict.* | No assessment requirement reported |
| Vermont | Vermont Data Privacy and Online Surveillance Act (signed Jun 16, 2026) | Jan 1, 2028 | 35,000; or sensitive data of 3,000; or offers data of 3,000 for sale. Consumer health data duties apply with no threshold. | Yes, plus a separate assessment for profiling with legal or similarly significant effects (purpose, risk analysis, data categories, performance metrics, transparency, post-deployment monitoring) |

> **Verify:** Oklahoma, Louisiana, Alabama, and Vermont were enacted in 2026. Secondary sources disagree on their thresholds, and one source gives Vermont's effective date as January 1, 2027. Read the enrolled bill before relying on any of these four.

Under most of these laws, the attorney general can request an assessment, usually with 30 to 90 days to produce it. Requested assessments are generally confidential and exempt from public records requests. One assessment can cover a set of comparable processing operations, and an assessment done for another law counts if it is reasonably comparable in scope and effect. That is why one well-built DPIA can satisfy all of them.

---

## 3. Common obligations

Nearly every state law (California and a few others differ in detail) requires the following. Use this list when reviewing a notice, a vendor, or a ROPA entry.

- **Consumer rights:** access (confirm and obtain), correction, deletion, portability, and opt-out of targeted advertising, sale, and profiling in furtherance of decisions with legal or similarly significant effects. Response within **45 days**, extendable once by 45 days with notice. An appeal process, with the attorney general's contact details in the decision.
- **Sensitive data:** opt-in consent in most states. California and Utah use an opt-out or a "limit" right instead. Definitions vary: check for precise geolocation, account credentials, government IDs, financial account details, communications content (California), neural data (California, Colorado, and others), citizenship or immigration status, data of a known child, and transgender or nonbinary status (some states).
- **Children and teens:** COPPA-level consent for known children under 13. Several states add opt-in consent or bans on targeted advertising and sale for teens up to 16 or 18.
- **Universal opt-out signals:** honor Global Privacy Control in California, Colorado, Connecticut, Texas, Oregon, Montana, Delaware, New Hampshire, New Jersey, Nebraska, Minnesota, Maryland, and others.
- **Privacy notice:** categories of data, purposes, how to exercise rights and appeal, categories shared with third parties, categories of third parties, and a clear disclosure of sale and targeted advertising with an opt-out method.
- **Data minimization and purpose limitation:** collection adequate, relevant, and reasonably necessary for disclosed purposes. Maryland is stricter (see §2).
- **Security:** reasonable administrative, technical, and physical safeguards.
- **Minnesota extras:** a data inventory, documented policies, and a right to question the result of profiling.

---

## 4. Processor and service provider contracts

Use this in vendor reviews alongside GDPR Art. 28 (`gdpr.md`, §8).

**Virginia-model states** (Virginia, Colorado, Connecticut, and most later laws) require a binding contract that sets out:

- Instructions for processing, the nature and purpose, the type of data, the duration, and both parties' rights and obligations
- A duty of confidentiality on each person processing the data
- Deletion or return of the data at the end of the services, unless law requires retention
- Making available all information needed to show compliance
- Allowing and cooperating with reasonable assessments by the controller or its designee, or arranging an independent assessment at least annually
- Engaging subcontractors only under a written contract with the same obligations, after giving the controller an opportunity to object
- Helping the controller meet its obligations, including consumer requests, security, breach notification, and data protection assessments

**California** (Cal. Civ. Code §§ 1798.100(d), 1798.140(ag) and (j); CCPA Regs. § 7051) requires a service provider or contractor contract that:

- Prohibits selling or sharing the PI
- Limits use to the specific business purposes in the contract, and prohibits use outside the direct business relationship
- Prohibits combining the PI with data from other sources, except as the regulations allow
- Requires compliance with the CCPA and the same level of privacy protection
- Grants the business the right to take reasonable steps to ensure compliant use, and to stop and remediate unauthorized use
- Requires the service provider to notify the business if it can no longer meet its obligations
- For contractors, includes a certification that the contractor understands and will comply with the restrictions

A vendor without these terms is a "third party," and disclosing PI to it may be a sale or share.

---

## 5. Assessment triggers and the crosswalk

### Common triggers

Most state laws require a data protection assessment when processing presents a heightened risk of harm:

- **Targeted advertising**
- **Sale** of personal data
- **Sensitive data** processing
- **Profiling** that presents a reasonably foreseeable risk of unfair or deceptive treatment or unlawful disparate impact; financial, physical, or reputational injury; intrusion upon seclusion; or other substantial injury
- **Minors:** several states (such as Colorado and Connecticut) add heightened-risk duties when the controller knows, or willfully disregards, that a user is a minor

A GDPR DPIA screen can come back "Not required" while a state assessment is still mandatory. Targeted advertising and selling data are the usual examples. A processor must give a controller the information it needs for its assessment.

### Writing the crosswalk

In the assessment, add a table like this, plus labeled subsections for any extra content:

| Regime | Law applies to the company? | Activity triggers the obligation? | Provision | Status | Facts still needed | Where satisfied | Extra content added |
|---|---|---|---|---|---|---|---|
| CA CPPA risk assessment | Yes (thresholds confirmed by <name>) | Yes: sensitive PI (contents of communications) | CCPA Regs. § 7150 | Provisional | F4: whether the business is the intended recipient | §3, §5, §6 | §8.1 weighing, go or no-go, contributor list |
| Colorado DPA | Open (threshold TBC) | Likely: sensitive data | C.R.S. § 6-1-1309; Rule 8.04 | Open | F3: Colorado consumer count | §3–§6 | §8.2 Rule 8.04 items |
| Virginia DPA | No: below threshold (per company profile) | — | VCDPA § 59.1-576 | Provisional | — | — | — |

Then add:

- **Benefit-risk weighing statement** (one paragraph): the benefits to each stakeholder, the residual risks, and the conclusion. State that the benefits outweigh the risks, or that they don't. If they don't, recommend not going ahead.
- **Go or no-go statement:** for California, whether the business will start the processing.
- **Contributors and approvers:** names and titles, which the sign-off section already captures.
- **Review cadence:** the strictest that applies. Annual review for Colorado profiling, and an update within 45 days of a material change for California.

---

## 6. California CPPA regulations

The regulations on risk assessments, ADMT, and cybersecurity audits were approved in September 2025 and took effect January 1, 2026, with staggered compliance dates.

### Risk assessments (CCPA Regs. §§ 7150–7157)

**When required:** before starting processing that presents a significant risk to consumers' privacy:

- Selling or sharing personal information
- Processing sensitive personal information (a narrow exception covers employees' sensitive data used only for certain HR purposes)
- Using ADMT to make a significant decision about a consumer
- Using automated processing to infer or extrapolate traits from systematic observation of a consumer acting as an applicant, student, employee, or independent contractor
- Using automated processing to infer or extrapolate traits based on a consumer's presence at a sensitive location
- Processing personal information to train ADMT for a significant decision, or to train facial recognition, emotion recognition, or other biometric identification or verification technology

**Timing:**

- New processing: assess before it starts.
- Processing under way on January 1, 2026: assess by December 31, 2027.
- First attestation and summary to the CPPA: April 1, 2028, then annually.
- Review at least every 3 years, and update within 45 days of a material change.

**Required content** (add to the crosswalk if a field isn't already covered):

- The specific purpose; "improve services" is not specific enough
- The categories of personal information, including the minimum needed
- Operational elements: collection method, retention, number of consumers, disclosures to consumers, technology used, any ADMT logic, and recipients
- The benefits to the business, consumers, other stakeholders, and the public
- The negative impacts on consumers' privacy
- The safeguards planned
- **Whether the business will start the processing.** This is the business owner's decision, made on the privacy or legal determination of which requirements apply. The executive attestation to the CPPA is separate (`approvals.md`, "Who decides what").
- The names and positions of contributors, reviewers, and approvers, and the approval date. *Verify* the exact naming requirement in the regulation text before telling contributors their names will appear. Colorado Rule 8.04 has a similar requirement for reviewers and approvers.

**The core test:** the regulations aim to restrict or stop processing whenever the risks to consumers' privacy outweigh the benefits. Write an explicit weighing paragraph and a go or no-go statement.

**Retention:** keep the assessment while the processing continues, or for 5 years after completion, whichever is later.

### ADMT

Businesses using ADMT to make significant decisions (financial or lending services, housing, education enrollment or opportunities, employment or independent contracting, and healthcare services) must provide a pre-use notice, an opt-out (with exceptions), and access rights, from **January 1, 2027**.

### Cybersecurity audits

Annual independent audits for businesses whose processing presents significant risk to security. First certification due April 1, 2028 (revenue over $100M), April 1, 2029 ($50M–$100M), or April 1, 2030 (under $50M).

---

## 7. Colorado: Privacy Act Rules, Part 8

A data protection assessment must be a genuine, thoughtful analysis. Rule 8.04 lists the content. Most of it maps onto a DPIA, but check for:

- A short summary of the processing
- The categories of personal data, with sensitive data flagged
- The context, including the relationship between controller and consumer, and what the consumer reasonably expects
- The nature and operational elements of the processing
- The benefits and the potential risks, from the consumer's point of view
- The safeguards, and how they reduce the risks
- Consumer de-identification, if any
- The processors and third parties involved
- Internal and external consultations
- For profiling: the items in Rule 9.06, covering the logic, data sources, testing for accuracy and bias, and human involvement
- The dates of review and approval, and the names and titles of the reviewers

Assessments of profiling must be reviewed every year. Others must be reviewed periodically and whenever the processing changes materially. Keep each assessment for 3 years after the processing ends. The minors amendment (heightened-risk duties for known minors) took effect October 1, 2025.

---

## 8. Virginia: VCDPA § 59.1-580

An assessment is required for targeted advertising, sale, profiling with a reasonably foreseeable risk of the harms in §5, sensitive data, and any other processing with a heightened risk of harm. It applies to processing created or generated after January 1, 2023. The assessment must identify and weigh the benefits to the controller, the consumer, other stakeholders, and the public against the risks to the consumer's rights, and show how safeguards reduce those risks. Factor in de-identified data, consumers' reasonable expectations, the context, and the relationship between controller and consumer.

---

## 9. AI-specific state laws

*Volatile throughout.* Check the current status before stating any obligation.

- **Colorado SB 26-189 (signed May 14, 2026)** repealed and replaced the Colorado AI Act (SB 24-205) before it took effect. The replacement regulates "automated decision-making technology" used in consequential decisions, takes effect **January 1, 2027**, and drops the original duty of care, risk management program, and annual impact assessments. The attorney general proposed ADMT and chatbot rules on August 11, 2026, with comments due October 26, 2026. Don't cite SB 24-205 duties as live.
- **California ADMT** (CCPA regulations, §6): pre-use notice, opt-out, and access from January 1, 2027.
- **Employment AI:** NYC Local Law 144 (bias audits and notice for automated employment decision tools); Illinois HB 3773 amending the Human Rights Act (notice and anti-discrimination for AI in employment decisions, effective January 1, 2026). Flag as possible and check.
- **Texas TRAIGA (HB 149, effective January 1, 2026):** mostly government duties, plus some prohibited uses that apply to everyone.
- **Utah AI disclosure law:** disclosure duties for generative AI in regulated occupations and consumer interactions.

---

## 10. Exemptions that often matter

Most state laws exempt some entities or data. Check the specific statute; the pattern is:

- **Entity exemptions** (vary by state): nonprofits (not in Colorado, Oregon, Delaware, New Jersey, Minnesota, Maryland, and others), higher education institutions (exempt in many states but not in some, such as Oregon and Colorado), financial institutions under GLBA, covered entities under HIPAA.
- **Data exemptions:** data subject to FERPA, HIPAA, GLBA, FCRA, and DPPA. Most comprehensive state laws exclude data processed in an employment context or as a business contact, but the wording and scope differ by state. California covers employee, applicant, and B2B data in full. Don't conclude that California is the only state that reaches employee data: read each state's exemption, and check employment-specific laws as well (background screening, electronic monitoring notice, biometric, and fair-chance laws). Treat employee-data coverage as Open until each relevant state is checked.

For education businesses, note that the FERPA data exemption usually covers data **the institution** holds under FERPA. A vendor's own processing of student data for its own purposes may still fall under the state law. Check the exact wording, and see `ferpa.md`.
