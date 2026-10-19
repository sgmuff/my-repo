| # | Step | Skill | Status | Starts | Triggered by | Finalize after |
|---|---|---|---|---|---|---|
| 1 | DPIA screening | `dpia` | Required | Now | new_processing = yes; indicators: children_or_students, audio_video_recording | — |
| 2 | Vendor review | `vendor-review` | Required | Now | vendor_involved = yes | — |
| 3 | AI intake | `ai-intake` | Required | Now | ai_involved = yes | — |
| 4 | Transfer screening | `tia` (no skill yet) | Required | After 2 | cross_border_access = yes | — |
| 5 | AI impact assessment | `ai-impact-assessment` | If ai_profiles_people = yes or ai_influences_decisions = yes | After 3 | — | — |
| 6 | AI Act deployer readiness | `ai-act-deployer` (no skill yet) | If ai_high_risk = yes | After 3 | ai_act_role = deployer | — |
| 7 | RoPA entry | `ropa` | Required | Now | new_processing = yes | 1, 2, 4 |
| 8 | Notice review | `notice-and-policy` | Required | Now | new_processing = yes | 7 |

**Why each step runs:**

1. Policy: screen all new processing; a full DPIA follows only if screening finds likely high risk (GDPR Art. 35)
2. Law: processor terms (GDPR Art. 28; state service provider terms)
3. Policy: every AI system is inventoried and tiered
4. Law: restricted transfers need a mechanism, and SCCs need a transfer assessment (GDPR Ch. V; SCCs Clause 14)
5. Policy: AI that profiles people or informs decisions about them gets an impact assessment
6. Law: high-risk deployer duties (AI Act Art. 26), from December 2, 2027 per eu-ai-act.md (verified 2026-10-16)
7. Law: records of processing (GDPR Art. 30)
8. Law: transparency (GDPR Art. 13-14; state notice at collection)

**Decision register.** Each blocks launch until recorded. Law: the law requires it where it applies. Policy: our own rule. Risk: a risk the owner must clear.

| About | Decision | Owner | Gate | Note |
|---|---|---|---|---|
| step 1 | Whether a full DPIA or state assessment is required; risk acceptance by rating | Privacy lead | Policy | — |
| step 2 | Onboard, onboard with conditions, or not | Approver for the residual rating | Law | — |
| step 3 | Internal AI tier, EU AI Act role, and EU AI Act classification, decided separately | Privacy lead | Policy | — |
| step 4 | Which flows are restricted, the mechanism for each, and supplementary measures | Privacy lead | Law | No skill yet: the owner runs this step by hand, and launch waits until the result is recorded |
| step 7 | Business owner confirms the facts; privacy lead approves the entry | Business owner, then privacy lead | Law | — |
| step 8 | Any notice change, and its timing | Privacy lead and counsel | Law | — |
| our-role | Our role for each purpose: controller, processor, or both (GDPR Art. 4(7)-(8), 28(10)) | Privacy lead | Law | — |
| recording-consent | Recording consent under state wiretap laws, including all-party consent states | Counsel | Law | — |
| ai-act-baseline | AI Act duties that apply whatever the tier: prohibited practices (Art. 5, such as emotion recognition in schools and workplaces) and transparency (Art. 50) | Privacy lead | Law | — |

**Legal checks that apply if a fact turns out yes:**

- lawful-basis (Privacy lead, law): if company_role = controller or both
- indirect-notice (Privacy lead and counsel, law): if indirect_collection = yes
- direct-marketing (Counsel, law): if direct_marketing = yes
- tracking-consent (Counsel, law): if tracking_tech = yes
- biometrics (Counsel, law): if biometrics = yes
- coppa (Counsel, law): if children_under_13 = yes
- student-privacy (Privacy lead and counsel, law): if school_context = yes
- vendor-own-use (Privacy lead, law): if vendor_own_use = yes
- scraped-source (Counsel, risk): if indirect_collection = yes and scraped_data = yes
- session-replay (Counsel, risk): if tracking_tech = yes and session_replay = yes
- us-sale-sharing (Privacy lead and counsel, law): if vendor_own_use = yes or tracking_tech = yes

**Assumed:** suspected_breach = no, dsr_received = no, regulator_inquiry = no, lawful_basis = not-proposed. Say so if any is wrong.

**Launch gate:** nothing in this plan authorizes processing. Launch waits for every required decision above.
