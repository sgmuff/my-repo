# Connected tools

The suite is company-agnostic. It uses whatever tools the session has and works fully without any of them. This file explains how to find each tool, what a skill may do with it, and what to do when it isn't there.

## Ground rules

- **Read freely.** Reading a contract from document storage or an existing ticket needs no extra permission.
- **Write only after confirmation.** Before creating or updating tickets or documents in a shared system, show the user the exact list of changes and get a yes in this session. One confirmation can cover the whole list.
- **No calendars.** See "Calendars: not used" below.
- **Never send.** Email and messaging tools are for drafts only. A person sends anything that leaves the organization (`approvals.md`).
- **Record what you did.** Put ticket keys, event links, and document URLs in the deliverable's metadata (`tickets:`) and in the action plan, so the paper trail links both ways.

## Detecting tools

Look at the tools available in the session. MCP tools appear with names like `mcp__<server>__<tool>`. Match on the server name:

| System | Look for | Command-line fallback |
|---|---|---|
| Jira | `atlassian`, `jira` | The `acli` or `jira` CLI, if installed and authenticated |
| Confluence | `atlassian`, `confluence` | None. The suite doesn't publish (see Publishing below). |
| ServiceNow | `servicenow`, `snow`, `now` | The REST API through `curl`, only if the user has set it up and says so |
| Google Drive or Docs | `google_drive`, `drive` | None |
| SharePoint or OneDrive | `sharepoint`, `onedrive`, `microsoft` | None |
| Email | `gmail`, `outlook`, `mail` | None |

If the company profile names a system that isn't connected, say so once and use the fallback. Don't ask the user to connect it mid-run.

## Ticketing: Jira

Use Jira for action items that need an owner outside the privacy team.

- **When:** after the deliverable is drafted, offer to create one issue per action (`A1`, `A2`, …). Launch blockers come first.
- **Fields:** project key from the company profile; summary `"[<document ID> <action ID>] <action>"`; description with the risk it addresses, the document path, and the acceptance criterion; assignee only if the user named a person; due date; labels `privacy` or `ai-governance` and the document type.
- **Link back:** write each issue key into the action plan's "Ticket" column and the document's `tickets:` metadata.
- **Updates:** when a later run finds an action closed in Jira, update the action plan status and cite the issue.

## Ticketing: ServiceNow

ServiceNow deployments vary, so use the table named in the company profile.

- **GRC or IRM module:** record risks in the risk register table and actions as issues or remediation tasks linked to the risk.
- **ITSM only:** create a task or request per action, using the same summary format as Jira.
- **DSRs and incidents (later waves):** if the company runs privacy requests or security incidents through ServiceNow, read the record as the source of facts and dates, and attach the draft as a work note only after confirmation.

## Fallback when no ticketing tool is connected

Add a "Ticket" column to the action plan and leave it blank. Then add a paste-ready import block as an appendix to the deliverable (not in the chat reply):

```csv
Summary,Description,Due date,Labels
"[DPIA-2026-004 A1] Get DPA amendment with zero retention","Addresses R1. See compliance/assessments/dpia/2026-10-16-support-copilot.md",2026-12-01,privacy
```

Both Jira and ServiceNow accept CSV imports.

## Document sources

Use connected storage to read the inputs a skill needs: PRDs, architecture docs, vendor contracts and DPAs, security reports, earlier assessments. Cite each document by title, URL, and the date you read it. Don't copy confidential source documents into the repository; link to them.

Without a connected source, ask the user to paste the text or put the file in the repository, and read it from there.

## Calendars: not used

Don't connect to a calendar, don't create calendar events, and don't offer to, even when a calendar tool is connected. A date belongs to an owner in the action plan, not to someone's calendar, and an event created by a model is easy to miss and hard to audit. A company that wants calendar entries can change this rule here.

Deadlines still matter: review dates, DSR response deadlines, breach notification clocks, and AIUC-1 quarterly testing. Record each one as an action in the deliverable's action plan, with a `YYYY-MM-DD` due date, so it reaches Jira or ServiceNow with the other actions.

## Email

When the deliverable includes outbound text, such as a reply to a data subject, a vendor follow-up, or a request for missing facts, offer to save it as an email draft if an email tool is connected. The draft's first line says "DRAFT: not sent," and the deliverable records that a draft exists. A person reviews and sends it.

## Publishing (not active)

The suite doesn't publish. The company profile names any publishing target ("Connected systems"); until one is enabled there, keep deliverables in the repository as Markdown, and don't publish anything. The portable Markdown rules in `conventions.md`, section 2, keep documents ready for a wiki or document store.
