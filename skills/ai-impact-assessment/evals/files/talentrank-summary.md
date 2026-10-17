# TalentRank: product summary and validation excerpt

*Test fixture. TalentRank and Hirewise, Inc. are fictional.*

## What it does

TalentRank (by Hirewise, Inc.) reads résumés and application answers for open roles, scores each applicant from 0 to 100 for "role fit," and sorts the recruiter's queue. Applicants scoring under 40 are moved to a "low priority" folder automatically. Recruiters can open that folder but, according to our recruiting team, rarely do. Hirewise describes the score as "advisory."

We plan to use it for all engineering and sales hiring from January 2027: about 18,000 applicants a year, in the US (including California, New York City, Colorado, and Illinois) and Ireland. We license it under our own brand inside our careers site, labeled "Smart Match."

## Validation excerpt (from Hirewise's 2025 validation report)

- Trained on 1.2 million anonymized résumés from Hirewise customers, 2018–2024, labeled with "hired / not hired" outcomes.
- Overall AUC: 0.81 on a holdout set of 40,000 résumés.
- Adverse impact analysis (US, gender inferred from first names): selection rate ratio at the score-40 threshold, women versus men, 0.84. Race and ethnicity were not tested ("data not available").
- Age, disability, and non-US populations were not tested.
- Model last retrained in March 2025. No monitoring of production score distributions is described.
- Hirewise states it holds "an independent bias audit for NYC Local Law 144," dated November 2024.
