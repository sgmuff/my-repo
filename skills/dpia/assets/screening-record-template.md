---
id: SCR-YYYY-NNN
type: screening
title: <Activity name>
status: Draft
outcome: Not indicated
outcome_status: Provisional
version: 0.1
requesting_business_area: <business area>
system_owner: <team or person, if different>
prepared_by: Claude (privacy-governance suite), for <privacy lead>
date_prepared: YYYY-MM-DD
next_review: <date, or "on material change">
roles: {gdpr: <...>, us_state: <...>, ferpa: <...>, eu_ai_act: <...>}
references:
  - <file> (<version covered>), last verified YYYY-MM-DD
---

# DPIA screening record: <Activity name>

## Summary

<Two or three sentences, opening with the conclusion and its status: "The available information doesn't indicate likely high risk, so a full DPIA isn't warranted (Provisional; depends on F2 and F4)." Then the main reason, then what the activity is. If a US state assessment, an AI impact assessment, or FERPA contract terms are still needed, say so here in a blockquote that opens with **Blocker:** or **Decision needed:**.>

> **Decision needed:** The privacy lead confirms the screening outcome (`approvals.md`).

## Activity

| Field | Value |
|---|---|
| Description | |
| Requesting business area | |
| System owner | |
| Company roles | |
| Data subjects and approximate number | |
| Personal data | |
| Special category, children's, student, or US-sensitive data | None, or a list |
| Vendors | |
| Transfers | |
| Related records | RoPA entry, vendor reviews (link each one) |
| Reference files relied on | |

## Facts relied on

| # | Fact | Status | Evidence or source |
|---|---|---|---|
| F1 | | Confirmed, Stated by requester, Unverified assumption, or TBC | |

## Screening

<Screening table from references/screening.md §6, starting with territorial scope.>

## Conclusion and conditions

On the facts above, this activity is unlikely to result in a high risk to individuals' rights and freedoms, so GDPR Art. 35(1) does not call for a full DPIA. This is the skill's provisional position until the privacy lead confirms it.

The conclusion holds only while these conditions stay true:

- <condition, such as "No customer content is sent to the vendor">
- <condition>

If any of them changes, screen the activity again.

## Recommendations (optional)

<Good-practice items that are not DPIA actions, such as updating the privacy notice or adding a RoPA entry.>

## Sign-off

| Decision | Approver role | Name | Date | Decision |
|---|---|---|---|---|
| Screening outcome | Privacy lead | | | Confirmed or Changed |
| Requesting business area acknowledgment | <Business area> contact | | | Acknowledged |
