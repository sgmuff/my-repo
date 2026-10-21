| # | Step | Skill | Status | Starts | Triggered by | Finalize after |
|---|---|---|---|---|---|---|
| 1 | DPIA screening | `dpia` | Required | Now | new_processing = yes; indicators: profiling, ai_profiles_people, indirect_collection | — |
| 2 | Vendor review | `vendor-review` | Required | Now | vendor_involved = yes | — |
| 3 | AI intake | `ai-intake` | Required | Now | ai_involved = yes | — |
| 4 | Transfer screening | `tia` | If cross_border_access = yes | After 2 | — | — |
| 5 | Legitimate interests assessment | `lia` | Required | Now | lawful_basis = legitimate-interests | — |
| 6 | AI impact assessment | `ai-impact-assessment` | Required | After 3 | ai_profiles_people = yes | — |
| 7 | AI Act deployer readiness | `ai-act-deployer` | If ai_high_risk = yes | After 3 | ai_act_role = deployer | — |
| 8 | RoPA entry | `ropa` | Required | Now | new_processing = yes | 1, 2, 5 |
| 9 | Notice review | `notice-and-policy` | Required | Now | new_processing = yes; indirect_collection = yes | 8 |

**Why each step runs:**

1. Policy: screen all new processing; a full DPIA follows only if screening finds likely high risk (GDPR Art. 35)
2. Law: processor terms (GDPR Art. 28; state service provider terms)
3. Policy: every AI system is inventoried and tiered
4. Law: restricted transfers need a mechanism, and SCCs need a transfer assessment (GDPR Ch. V; SCCs Clause 14)
5. Law: legitimate interests needs a documented three-part test (GDPR Art. 6(1)(f), 5(2))
6. Policy: AI that profiles people or informs decisions about them gets an impact assessment
7. Law: high-risk deployer duties (AI Act Art. 26), from December 2, 2027 per eu-ai-act.md (verified 2026-10-16)
8. Law: records of processing (GDPR Art. 30)
9. Law: transparency (GDPR Art. 13-14; state notice at collection)

**Decision register.** Each blocks launch until recorded. Law: the law requires it where it applies. Policy: our own rule. Risk: a risk the owner must clear.

| About | Decision | Owner | Gate | Note |
|---|---|---|---|---|
| step 1 | Whether a full DPIA or state assessment is required; risk acceptance by rating | Privacy lead | Policy | — |
| step 2 | Onboard, onboard with conditions, or not | Approver for the residual rating | Law | — |
| step 3 | Internal AI tier, EU AI Act role, and EU AI Act classification, decided separately | Privacy lead | Policy | — |
| step 5 | The LIA for each purpose; it feeds the lawful-basis decision | Privacy lead | Law | — |
| step 6 | Residual AI risk; whether any customer owes a FRIA (AI Act Art. 27) | Privacy lead | Policy | — |
| step 8 | Business owner confirms the facts; privacy lead approves the entry | Business owner, then privacy lead | Law | — |
| step 9 | Any notice change, and its timing | Privacy lead and counsel | Law | — |
| lawful-basis | A lawful basis for each purpose we decide, documented before processing starts (GDPR Art. 6). The DPIA informs it but doesn't choose it. | Privacy lead | Law | — |
| indirect-notice | Notice to people whose data we didn't collect from them: content, timing, and any exception (GDPR Art. 14) | Privacy lead and counsel | Law | — |
| direct-marketing | Handling the absolute right to object to direct marketing (GDPR Art. 21(2)-(3)), and e-marketing consent rules (ePrivacy, PECR, CAN-SPAM) | Counsel | Law | — |
| ai-act-baseline | AI Act duties that apply whatever the tier: prohibited practices (Art. 5, such as emotion recognition in schools and workplaces) and transparency (Art. 50) | Privacy lead | Law | — |

**Legal checks that apply if a fact turns out yes:**

- tracking-consent (Counsel, law): if tracking_tech = yes
- recording-consent (Counsel, law): if audio_video_recording = yes
- biometrics (Counsel, law): if biometrics = yes
- vendor-own-use (Privacy lead, law): if vendor_own_use = yes
- scraped-source (Counsel, risk): if scraped_data = yes
- session-replay (Counsel, risk): if tracking_tech = yes and session_replay = yes
- us-sale-sharing (Privacy lead and counsel, law): if vendor_own_use = yes or tracking_tech = yes

**Assumed:** suspected_breach = no, dsr_received = no, regulator_inquiry = no. Say so if any is wrong.

**Launch gate:** nothing in this plan authorizes processing. Launch waits for every required decision above.
