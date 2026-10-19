| # | Step | Skill | Status | Starts | Triggered by | Finalize after |
|---|---|---|---|---|---|---|
| 1 | Containment | Human action | Required, time-critical | Now | processing_started = yes | — |
| 2 | Incident assessment | `incident-assessment` | Required, time-critical | Now | suspected_breach = yes | — |
| 3 | Vendor review | `vendor-review` | Required | Now | vendor_involved = yes | — |

**Why each step runs:**

1. Risk: Processing is running before review
2. Law: notification clocks may be running (GDPR Art. 33-34; state breach laws)
3. Law: processor terms (GDPR Art. 28; state service provider terms)

**Decision register.** Each blocks launch until recorded. Law: the law requires it where it applies. Policy: our own rule. Risk: a risk the owner must clear.

| About | Decision | Owner | Gate | Note |
|---|---|---|---|---|
| step 1 | Pause, limit, or continue what is already running | Privacy lead | Risk | — |
| step 2 | Whether to notify, and whom | Privacy lead and counsel | Law | — |
| step 3 | Onboard, onboard with conditions, or not | Approver for the residual rating | Law | — |

**Legal checks that apply if a fact turns out yes:**

- direct-marketing (Counsel, law): if direct_marketing = yes
- tracking-consent (Counsel, law): if tracking_tech = yes
- recording-consent (Counsel, law): if audio_video_recording = yes
- biometrics (Counsel, law): if biometrics = yes
- coppa (Counsel, law): if children_or_students = yes and children_under_13 = yes
- student-privacy (Privacy lead and counsel, law): if children_or_students = yes and school_context = yes
- vendor-own-use (Privacy lead, law): if vendor_own_use = yes
- session-replay (Counsel, risk): if tracking_tech = yes and session_replay = yes
- us-sale-sharing (Privacy lead and counsel, law): if vendor_own_use = yes or tracking_tech = yes

**Assumed:** dsr_received = no, regulator_inquiry = no, lawful_basis = not-proposed. Say so if any is wrong.

**Launch gate:** nothing in this plan authorizes processing. Launch waits for every required decision above.
