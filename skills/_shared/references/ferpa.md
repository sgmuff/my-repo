# FERPA

| Field | Value |
|---|---|
| Covers | Family Educational Rights and Privacy Act, 20 U.S.C. § 1232g, and 34 CFR Part 99; COPPA (16 CFR Part 312) as amended in 2025; state student privacy laws in California, New York, Illinois, and Texas |
| Version covered | 34 CFR Part 99 as shown on eCFR, current to July 10, 2026 |
| Sources | ecfr.gov (Title 34, Part 99); studentprivacy.ed.gov (Student Privacy Policy Office and PTAC guidance); Federal Register, April 22, 2025, FR Doc. 2025-05904 (COPPA amendments); NYSED and NY OGS guidance on Education Law § 2-d; secondary summaries of SOPIPA and SOPPA |
| Last verified | 2026-10-16 |
| Verification scope | Confirmed that no FERPA rule was proposed or finalized in 2026. The Department of Education's semiannual regulatory agenda (July 2026) lists FERPA as a rulemaking priority. Section content reflects the stable regulation text. |
| Review interval | Every six months, or when the Department publishes a FERPA notice of proposed rulemaking |
| Volatile points | §1 (possible rulemaking on the 2026 agenda); §10 (COPPA 2.0 pending; school authorization treatment); §11 (state laws checked against secondary sources only) |

## Contents

1. Status
2. Who FERPA binds, and what it protects
3. Roles for a company that handles student data
4. Disclosure without consent: the exceptions that matter to vendors
5. Rights of parents and eligible students
6. Recordkeeping and redisclosure
7. Vendor contract checklist
8. Enforcement
9. How FERPA interacts with other laws
10. COPPA
11. State student privacy laws

---

## 1. Status

The regulations were last substantively amended in 2011. The Department of Education's July 2026 semiannual regulatory agenda lists FERPA among its rulemaking priorities, but no proposed rule had been published as of October 16, 2026. *Volatile:* check the Federal Register before relying on this file for a new contract or policy.

---

## 2. Who FERPA binds, and what it protects

- **Covered institutions:** educational agencies and institutions that receive funds under a program administered by the US Department of Education (34 CFR § 99.1). This includes nearly all public K–12 schools and districts and most postsecondary institutions.
- **Education records:** records directly related to a student and maintained by the institution or by a party acting for it (§ 99.3). Exclusions include sole-possession notes, law enforcement unit records, certain employment records, treatment records, and alumni records.
- **Personally identifiable information (PII):** direct identifiers, indirect identifiers such as date of birth, and any other information that, alone or combined, is linked or linkable to a specific student and would let a reasonable person in the school community identify the student with reasonable certainty (§ 99.3).
- **Parents and eligible students:** rights belong to parents until the student turns 18 or attends a postsecondary institution, when they transfer to the "eligible student" (§ 99.5).
- **Directory information:** information not generally considered harmful if disclosed, such as name and enrollment status, which the institution may disclose after notice and an opportunity to opt out (§ 99.37).

---

## 3. Roles for a company that handles student data

FERPA regulates the institution, not the vendor. A vendor is bound through the exception the institution relies on and the contract that implements it. On each run, propose one of these roles and confirm it (`conventions.md`, §5):

| Role | When | What follows |
|---|---|---|
| Educational agency or institution | The company is a school, district, or postsecondary institution | It owns all FERPA duties |
| School official (vendor) | An institution outsources a service it would otherwise perform itself, under § 99.31(a)(1)(i)(B) | Use only for the authorized purpose; under the institution's direct control; no redisclosure (§ 99.33(a)) |
| Authorized representative (audit or evaluation) | A state or local education authority designates the company to audit or evaluate education programs (§§ 99.31(a)(3), 99.35) | A written agreement with required terms is mandatory |
| Organization conducting studies | Studies for or on behalf of institutions (§ 99.31(a)(6)) | A written agreement; destroy data when no longer needed |
| Other recipient | Receives directory information or data with consent | Bound by the consent or the directory information notice |

Many education companies are also a GDPR processor or a state-law processor for the same data, and a controller for their own product analytics. Record each role separately.

---

## 4. Disclosure without consent: the exceptions that matter to vendors

The default is written consent before disclosing PII from education records (§ 99.30). The exceptions most relevant to vendors:

**School official exception, § 99.31(a)(1)(i)(B).** A contractor, consultant, volunteer, or other outside party may be treated as a school official if it:

1. performs an institutional service or function for which the institution would otherwise use employees;
2. is under the institution's direct control with respect to the use and maintenance of education records;
3. is subject to § 99.33(a) on the use and redisclosure of PII; and
4. meets the criteria in the institution's annual notification for who counts as a school official with a legitimate educational interest (§ 99.7(a)(3)(iii)).

The institution must use reasonable methods to make sure school officials access only the records in which they have legitimate educational interests (§ 99.31(a)(1)(ii)).

**A contract clause alone doesn't establish the exception.** The four conditions are facts about the relationship, especially "direct control" over the use and maintenance of the records, and the limits on use and redisclosure. Check how the institution actually controls the use: what the contract permits, what the product does, and whether the institution can see and stop new uses. A new purpose, such as tuning the company's own model or building product analytics, needs its own analysis:

- Is it an institutional service the school would otherwise perform, or the company's own commercial purpose?
- Does the institution authorize it, specifically and in writing?
- Is the data identifiable, pseudonymized, or de-identified under § 99.31(b)? Derived features aren't automatically de-identified.
- Can the data or the model keep student information after a deletion request or the end of the contract?

Treat the answer as Provisional until counsel confirms it. District approval alone may not resolve the COPPA and state-law questions (§10–11).

**Studies exception, § 99.31(a)(6).** Studies to develop, validate, or administer predictive tests, administer student aid programs, or improve instruction. The written agreement must specify the purpose, scope, duration, and data; limit use to the stated purpose; restrict access to people with a need; and require destruction when no longer needed, with a time period (§ 99.31(a)(6)(iii)(C)).

**Audit or evaluation exception, §§ 99.31(a)(3), 99.35.** Disclosures to authorized representatives of state and local education authorities, under a written agreement with the terms in § 99.35(a)(3).

**De-identified data, § 99.31(b).** Disclosure without consent is allowed after removing all PII, with a reasonable determination that the student's identity isn't personally identifiable. Re-identification risk counts, including from combining with other releases.

---

## 5. Rights of parents and eligible students

| Right | Rule |
|---|---|
| Inspect and review | Within a reasonable period, not more than **45 days** after the request (§ 99.10(b)) |
| Seek amendment | Request amendment of inaccurate or misleading records, with a right to a hearing (§§ 99.20–99.22) |
| Consent to disclosure | Written, signed, and dated, specifying the records, purpose, and recipients (§ 99.30) |
| Annual notification | The institution notifies parents and eligible students of their rights each year (§ 99.7) |
| Complain | To the Department's Student Privacy Policy Office (§ 99.63) |

When a vendor holds education records as a school official, requests come through the institution. The vendor's contract should require it to help the institution respond within the 45 days.

---

## 6. Recordkeeping and redisclosure

- **Record of disclosures (§ 99.32):** the institution keeps a record of each request for and disclosure of PII, with the parties and their legitimate interests. School official disclosures and directory information are excluded.
- **Redisclosure (§ 99.33):** a recipient may not redisclose PII without consent, except on the institution's behalf under a § 99.31 exception, with the institution recording it. A third party that improperly rediscloses PII can be barred from receiving PII from that institution for at least five years (§ 99.67(c)).

---

## 7. Vendor contract checklist

FERPA itself specifies contract terms only for the studies and audit or evaluation exceptions. For the school official exception, the Department's Privacy Technical Assistance Center (PTAC) recommends terms in *Protecting Student Privacy While Using Online Educational Services: Requirements and Best Practices* (February 2014) and its model terms of service guidance. Check that the contract:

- [ ] Names the exception relied on and the institutional service performed
- [ ] Keeps the institution in direct control of the use and maintenance of education records
- [ ] Limits use to the authorized purpose, with no use for advertising, profiling, or product development unrelated to the service, unless the institution authorizes it
- [ ] Prohibits redisclosure except as the institution directs (§ 99.33)
- [ ] Restricts access to vendor staff with a need, with training
- [ ] Requires security safeguards appropriate to the data
- [ ] Requires deletion or return at the end of the contract or on request, with certification
- [ ] Commits the vendor to help with parent and eligible student requests to inspect and amend
- [ ] Sets breach notification to the institution, with a deadline (FERPA has no statutory breach duty, but states do)
- [ ] Gives the institution audit or inspection rights
- [ ] Addresses de-identified data: whether the vendor may keep or use it, and a ban on re-identification
- [ ] Covers sub-processors with flow-down terms
- [ ] For studies or audits, includes every term required by § 99.31(a)(6)(iii)(C) or § 99.35(a)(3)

State student privacy laws often require more. Common examples are California Education Code § 49073.1 and SOPIPA, New York Education Law § 2-d, and the Illinois SOPPA. Flag them when an institution or student is in that state, and check whether they're in scope.

---

## 8. Enforcement

The Student Privacy Policy Office investigates complaints (§§ 99.60–99.67). The ultimate sanction is withholding Department of Education funds from the institution. FERPA creates no private right of action (*Gonzaga University v. Doe*, 536 U.S. 273 (2002)). The practical risk for a vendor is contractual: loss of the customer, a five-year bar under § 99.67(c), and state student privacy laws, some of which allow attorney general enforcement.

---

## 9. How FERPA interacts with other laws

- **State comprehensive privacy laws:** most exempt data that is subject to FERPA, and some exempt institutions of higher education entirely. The exemption usually follows the data in the institution's hands. A vendor's own-purpose processing may still be covered. See `us-state-privacy.md`, §10.
- **GDPR:** applies to student data from EU students or EU institutions regardless of FERPA. No exemption.
- **COPPA:** see §10.
- **State student privacy laws:** see §11. They apply alongside FERPA and often reach the vendor directly.
- **PPRA (34 CFR Part 98):** limits surveys on protected topics and marketing uses of student data in K–12.
- **EU AI Act:** AI used to determine admission, evaluate learning outcomes, assess the appropriate level of education, or monitor prohibited behavior during tests is high-risk (AI Act Annex III, point 3). See `eu-ai-act.md`.

**Keep school privacy and consumer privacy analyses apart.** An education activity usually turns on FERPA, COPPA, and state student privacy laws first, and on consumer privacy laws second. Don't infer applicability from where students live. Analyze the company's role under each law and each district's contract.

---

## 10. COPPA

The Children's Online Privacy Protection Rule, 16 CFR Part 312, applies to operators of websites and online services directed to children under 13, and to operators with actual knowledge that they collect personal information from a child under 13.

**Amended rule.** The FTC's amendments were published April 22, 2025, took effect June 23, 2025, and required compliance by **April 22, 2026**, with limited exceptions. They include separate verifiable parental consent for disclosing children's data to third parties (including for targeted advertising), a written data retention policy, a written information security program, and changes to definitions such as "personal information." *Verify* the specific provisions against the Federal Register notice (FR Doc. 2025-05904, April 22, 2025) before citing them.

**School authorization.** The 2024 proposal would have written a school-authorization exception into the rule. Reports indicate the final rule didn't adopt it, so school authorization still rests on the FTC's longstanding guidance: a school may consent on parents' behalf only where the operator collects the information for the use and benefit of the school, and for no other commercial purpose. *Verify:* confirm the final rule's treatment in the Federal Register notice and the FTC's current COPPA FAQ.

In practice:

- Ask whether any users are under 13, whether the service is directed to children, and whether the company has actual knowledge of ages.
- Use for the school's educational purpose may rest on school authorization. Use for the company's own purposes, such as model training, product development, or advertising, generally needs verifiable parental consent, or must stop.
- The operator stays responsible for COPPA compliance even when a school consents on parents' behalf. A vendor can't treat school authorization as moving its COPPA duties to the district.
- COPPA 2.0 (teens up to 16) passed the Senate on March 5, 2026, and wasn't law as of October 16, 2026. *Volatile.*

---

## 11. State student privacy laws

Most states have a student privacy law that binds operators of K–12 services directly, often with contract requirements stricter than FERPA's. Check the laws of each state where the company's district customers are, and read each district's data privacy agreement, since these laws often operate through it. *Verify* each statute before citing it. This section summarizes, and the details change.

| State | Law | What it requires of vendors (summary) |
|---|---|---|
| California | Student Online Personal Information Protection Act (SOPIPA), Cal. Bus. & Prof. Code § 22584; Cal. Educ. Code § 49073.1 | SOPIPA: no targeted advertising, no profiling of students for non-educational purposes, no sale; reasonable security; delete on the school's request. § 49073.1: required terms in contracts between local educational agencies and third parties for digital records, including ownership, use limits, deletion, and breach notice. Early Learning Personal Information Protection Act (ELPIPA) extends SOPIPA to preschool. |
| New York | Education Law § 2-d; Commissioner's Regulations, 8 NYCRR Part 121 | A data security and privacy plan accepted by the agency; the district's Parents' Bill of Rights signed into the contract; safeguards aligned with the NIST Cybersecurity Framework; access limited to those who need it; encryption; no sale or use for marketing or commercial purposes; breach notice to the agency **within 7 calendar days** of discovery (8 NYCRR 121.10(a)), with reimbursement of the agency's notification costs where the vendor caused the breach |
| Illinois | Student Online Personal Protection Act (SOPPA), 105 ILCS 85, as amended effective July 1, 2021 | A written data privacy agreement with each district, with statutory terms; published lists of vendors and data elements; breach notice deadlines; deletion duties |
| Texas | Tex. Educ. Code ch. 32, subch. D (student information and operators) | SOPIPA-style restrictions on targeted advertising, profiling, and sale, plus security and deletion duties. *Verify the section numbers.* |

Many districts use the Student Data Privacy Consortium's National Data Privacy Agreement, with state-specific exhibits. When a district's agreement is stricter than the law, the agreement governs the company's obligations to that district.

For a vendor, the usual pressure points are model training and product analytics on student data, targeted advertising, sub-processors, deletion at contract end, and short breach notice clocks.
