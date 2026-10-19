| # | Step | Skill | Status | Starts | Triggered by | Finalize after |
|---|---|---|---|---|---|---|
| 1 | DPIA screening | `dpia` | Required | Now | new_processing = yes | — |
| 2 | Vendor review | `vendor-review` | Required | Now | vendor_involved = yes | — |
| 3 | Transfer screening | `tia` (no skill yet) | If cross_border_access = yes | After 2 | — | — |
| 4 | RoPA entry | `ropa` | Required | Now | new_processing = yes | 1, 2 |
| 5 | Notice review | `notice-and-policy` | Required | Now | new_processing = yes | 4 |

**Why each step runs:**

1. Policy: screen all new processing; a full DPIA follows only if screening finds likely high risk (GDPR Art. 35)
2. Law: processor terms (GDPR Art. 28; state service provider terms)
3. Law: restricted transfers need a mechanism, and SCCs need a transfer assessment (GDPR Ch. V; SCCs Clause 14)
4. Law: records of processing (GDPR Art. 30)
5. Law: transparency (GDPR Art. 13-14; state notice at collection)

**Decision register.** Each blocks launch until recorded. Law: the law requires it where it applies. Policy: our own rule. Risk: a risk the owner must clear.

| About | Decision | Owner | Gate | Note |
|---|---|---|---|---|
| step 1 | Whether a full DPIA or state assessment is required; risk acceptance by rating | Privacy lead | Policy | — |
| step 2 | Onboard, onboard with conditions, or not | Approver for the residual rating | Law | — |
| step 4 | Business owner confirms the facts; privacy lead approves the entry | Business owner, then privacy lead | Law | — |
| step 5 | Any notice change, and its timing | Privacy lead and counsel | Law | — |
| lawful-basis | A lawful basis for each purpose we decide, documented before processing starts (GDPR Art. 6). The DPIA informs it but doesn't choose it. | Privacy lead | Law | — |
| tracking-consent | Consent for cookies and device storage (ePrivacy Directive Art. 5(3); PECR reg. 6) and state tracking rules | Counsel | Law | — |
| vendor-own-use | Vendor use for its own purposes: forbid it in the contract, or treat the vendor as a controller for that use (GDPR Art. 28(3)(a), 28(10)) | Privacy lead | Law | — |
| session-replay | Session replay: consent before recording, and masking of form fields and other sensitive input | Counsel | Risk | — |
| us-sale-sharing | Whether disclosures to the vendor are a sale or sharing under state privacy laws, and the opt-out and Global Privacy Control duties that follow | Privacy lead and counsel | Law | — |

**Legal checks that apply if a fact turns out yes:**

- indirect-notice (Privacy lead and counsel, law): if indirect_collection = yes
- direct-marketing (Counsel, law): if direct_marketing = yes
- recording-consent (Counsel, law): if audio_video_recording = yes
- biometrics (Counsel, law): if biometrics = yes
- coppa (Counsel, law): if children_or_students = yes and children_under_13 = yes
- student-privacy (Privacy lead and counsel, law): if children_or_students = yes and school_context = yes
- scraped-source (Counsel, risk): if indirect_collection = yes and scraped_data = yes

**Assumed:** suspected_breach = no, dsr_received = no, regulator_inquiry = no, lawful_basis = not-proposed. Say so if any is wrong.

**Launch gate:** nothing in this plan authorizes processing. Launch waits for every required decision above.
