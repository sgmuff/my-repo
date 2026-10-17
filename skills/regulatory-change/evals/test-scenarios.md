# Regulatory change test scenarios

## Should trigger

| # | Request |
|---|---|
| 1 | "Outside counsel says the Digital Omnibus passed. What does it mean for us?" |
| 2 | "AIUC-1 released a new version. Update our references." |
| 3 | "Run the quarterly regulatory sweep." |
| 4 | "Does the new Oklahoma privacy law apply to us?" |

## Should not trigger (near misses)

| # | Request | Where it belongs |
|---|---|---|
| 1 | "Does the Oklahoma breach law require notice for this incident?" | `incident-assessment` |
| 2 | "Assess our program against the NIST Privacy Framework." | `program-assessment` |
| 3 | "Do we need a DPIA for the new analytics vendor?" | `dpia` |

## What a good run looks like

- Classifies the stage first, and acts according to it.
- Confirms the change against a primary source, or marks conclusions Provisional when it can't.
- Maps the impact with `find_citations.py` and the crosswalk.
- Writes a change memo with exact proposed text, and doesn't edit reference files before the privacy lead approves.
- For AIUC-1 releases, runs `aiuc_release_diff.py` and checks the changelog.
- Replies in about 150 words.

## Scenario runs

See `evals.json` for the prompts, fixtures in `files/`, and expected outputs.
