---
id: DPIA-2026-004
type: dpia
title: Gradebook sync with district SIS
status: In review
stage: Ready for sign-off
requesting_business_area: Product (K-12)
system_owner: Integrations team
date_prepared: 2026-08-12
next_review: 2027-08-12
residual_risk: {current: High, target: Low, confirmed: false}
launch_authorized: false
---

# DPIA

## Risk register

| ID | Risk (who is harmed, how, and why) | Tag | Inherent L × S | Existing controls | Current residual | Planned controls (actions) | Evidence that verifies them | Target residual | Owner | Rationale |
|---|---|---|---|---|---|---|---|---|---|---|
| R1 | Students' deleted records are recreated by the nightly roster sync, so deletion requests fail | NIST PF CT.DM-P5 | Probable × Significant = **High** | None verified | **High** | A1 | Sync log showing tombstones honored | Remote × Significant = **Low** | Integrations | |
| R2 | Teachers' grade comments exposed to other districts through a shared tenant | NIST PF PR.AC-P | Possible × Severe = **High** | Tenant isolation (SOC 2) | **Medium** | A2 | Pen test result | Remote × Severe = **Medium** | Security | |

## Action plan

| ID | Action | Addresses | Depends on | Acceptance criterion | Owner | Due | Launch blocker? (Legal or Readiness) | Evidence link | Verified by | Ticket | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A1 | Honor deletion tombstones in roster sync | R1 | — | Test deletes stay deleted after 3 syncs | Integrations | 2026-09-30 | Yes, Legal | | | PRIV-112 | Open |
| A2 | Tenant isolation pen test | R2 | — | No cross-tenant read | Security | 2026-11-30 | Yes, Readiness | | | PRIV-113 | Open |
