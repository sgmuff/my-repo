# Risk register block

Paste this section into any assessment that rates risk. Scoring follows `references/risk-method.md`. Delete these instructions when you use it.

- Number risks `R1`, `R2`, and so on, and link each one to its actions.
- Score three ratings: inherent (as designed), current residual (verified controls only), and target residual (planned controls). A planned control never lowers the current rating.
- Justify each score in a few words, and name the evidence that would verify each planned control.
- The overall rating is the highest in each column, never an average.
- Tag each risk with the NIST PF subcategory (privacy) or AIUC-1 requirement (AI) it relates to, so program assessments can roll findings up.
- For a processor assistance pack, split the target into vendor residual and deployment residual (`risk-method.md`, §1).

---

## Risk register

**Residual risk: <not yet confirmed | confirmed>.** Current residual: **<rating>** (<which controls are verified, or "no controls verified yet">). Target residual: **<rating>**, subject to verification of <action IDs>. Scoring uses a 3x3 matrix: Remote, Possible, or Probable likelihood, against Minimal, Significant, or Severe severity.

| ID | Risk (who is harmed, how, and why) | Tag | Inherent L × S | Existing controls | Current residual | Planned controls (actions) | Evidence that verifies them | Target residual | Owner | Rationale |
|---|---|---|---|---|---|---|---|---|---|---|
| R1 | | NIST PF ID.RA-P3 | Probable × Severe = **High** | None verified | **High** | A1, A2 | Signed DPA clause; API config export | Remote × Significant = **Low** | | |

### Risk acceptance

| Rating accepted (current or target) | Accepted by (per `approvals.md`) | Name | Date | Conditions that must close before launch |
|---|---|---|---|---|
| | | | | |
