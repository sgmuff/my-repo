| # | Step | Skill | Status | Starts | Triggered by | Finalize after |
|---|---|---|---|---|---|---|
| 1 | Containment | Human action | If processing_started = yes, time-critical | Now | — | — |
| 2 | DPIA screening | `dpia` | If new_processing = yes | Now | — | — |
| 3 | Vendor review | `vendor-review` | If vendor_involved = yes | Now | — | — |
| 4 | AI intake | `ai-intake` | If ai_involved = yes | Now | — | — |
| 5 | Transfer screening | `tia` | If cross_border_access = yes | After 3 | — | — |
| 6 | AI impact assessment | `ai-impact-assessment` | If ai_profiles_people = yes or ai_influences_decisions = yes | After 4 | — | — |
| 7 | AI Act provider readiness | `ai-act-provider` (no skill yet) | If ai_act_role = provider and ai_high_risk = yes | After 4 | — | — |
| 8 | AI Act deployer readiness | `ai-act-deployer` (no skill yet) | If ai_act_role = deployer and ai_high_risk = yes | After 4 | — | — |
| 9 | RoPA entry | `ropa` | If new_processing = yes | Now | — | — |
| 10 | Notice review | `notice-and-policy` | If new_processing = yes or indirect_collection = yes | Now | — | — |

**Why each step runs:**

1. Risk: Processing is running before review
2. Policy: screen all new processing; a full DPIA follows only if screening finds likely high risk (GDPR Art. 35)
3. Law: processor terms (GDPR Art. 28; state service provider terms)
4. Policy: every AI system is inventoried and tiered
5. Law: restricted transfers need a mechanism, and SCCs need a transfer assessment (GDPR Ch. V; SCCs Clause 14)
6. Policy: AI that profiles people or informs decisions about them gets an impact assessment
7. Law: high-risk provider duties (AI Act Art. 9-17, 43, 72), from December 2, 2027 per eu-ai-act.md (verified 2026-10-16)
8. Law: high-risk deployer duties (AI Act Art. 26), from December 2, 2027 per eu-ai-act.md (verified 2026-10-16)
9. Law: records of processing (GDPR Art. 30)
10. Law: transparency (GDPR Art. 13-14; state notice at collection)

**Decision register.** Each blocks launch until recorded. Law: the law requires it where it applies. Policy: our own rule. Risk: a risk the owner must clear.

| About | Decision | Owner | Gate | Note |
|---|---|---|---|---|
| our-role | Our role for each purpose: controller, processor, or both (GDPR Art. 4(7)-(8), 28(10)) | Privacy lead | Law | — |

**Legal checks that apply if a fact turns out yes:**

- lawful-basis (Privacy lead, law): if new_processing = yes and company_role = controller or both
- indirect-notice (Privacy lead and counsel, law): if indirect_collection = yes
- direct-marketing (Counsel, law): if direct_marketing = yes
- tracking-consent (Counsel, law): if tracking_tech = yes
- recording-consent (Counsel, law): if audio_video_recording = yes
- biometrics (Counsel, law): if biometrics = yes
- coppa (Counsel, law): if children_or_students = yes and children_under_13 = yes
- student-privacy (Privacy lead and counsel, law): if children_or_students = yes and school_context = yes
- vendor-own-use (Privacy lead, law): if vendor_involved = yes and vendor_own_use = yes
- scraped-source (Counsel, risk): if indirect_collection = yes and scraped_data = yes
- session-replay (Counsel, risk): if tracking_tech = yes and session_replay = yes
- us-sale-sharing (Privacy lead and counsel, law): if vendor_own_use = yes or tracking_tech = yes
- ai-act-baseline (Privacy lead, law): if ai_involved = yes

**Assumed:** suspected_breach = no, dsr_received = no, regulator_inquiry = no, lawful_basis = not-proposed. Say so if any is wrong.

**Launch gate:** nothing in this plan authorizes processing. Launch waits for every required decision above.
