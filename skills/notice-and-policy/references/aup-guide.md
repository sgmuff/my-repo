# AI acceptable use policy guide

There are two different policies, often confused. Decide which one is needed, or both, and say so.

| Policy | Audience | Governs | Main drivers |
|---|---|---|---|
| **Employee AI use policy** | Staff and contractors | How people inside the company may use AI tools: approved tools, data they may put in, review of outputs, prohibited uses | ISO/IEC 42001 A.2.2, A.9.2–A.9.4; AI Act Art. 4 (AI literacy) and Art. 26(1)–(2) (use per instructions; oversight); NIST AI RMF GOVERN 1.2, MAP 3.4; GDPR Arts. 5, 25, 28, 32 for the data people paste in |
| **Product acceptable use policy** | Users of the company's own AI system or agent | What end users may and may not do with it, and what happens when they break the rules | **AIUC-1 E010** (mandatory): E010.1 policy, E010.2 violation detection, E010.3 user notification, E010.4 enforcement guardrails; NIST AI RMF MEASURE 2.4 |

AIUC-1 E010 is about the second kind. A certification readiness review needs the product policy *and* the detection and in-product notices behind it, not only the employee policy. Both get reviewed at least every 12 months.

## Employee AI use policy: contents

1. **Purpose and scope:** who it covers (employees, contractors, agencies), and which tools: standalone AI tools, AI features in approved software, browser extensions, coding assistants, and agents.
2. **Approved tools and configurations:** the list, or where it lives (the AI inventory, `ai-intake`), and how to request a new one. Unapproved tools aren't used for company data. A tool is approved in a configuration: company sign-on, the vendor's data-use and retention terms, admin settings, and which connectors, custom assistants, agents, sharing, and repositories are switched on. Turning on a new feature of an approved tool goes back through intake.
3. **Data rules:** what may go into which tool, by data class (public, internal, confidential, personal, special category, student, customer content, credentials and secrets). Customer data only in tools approved for it, under contract terms that bar training. Define each class by example: does "customer data" include customer source code, support tickets, logs, screenshots, and data processed for a customer? Say which rule wins when one record falls in two classes. For a company serving schools, much customer content is also student data, so the stricter rule applies, and the policy should say what that means for support and engineering work. Distinguish:
   - **Identifiable** data, which names or directly identifies a person.
   - **Pseudonymized** data, which can still be linked back and stays personal data. Masked production records usually fall here, so "masked" is not a safe substitute for "synthetic."
   - **De-identified or aggregate** data, which meets a defined standard. Prohibited by default until the company adopts one.
   - **Synthetic** data, generated without reproducing real records. Usually the approved alternative for testing.

   Whether a vendor becomes a subprocessor depends on the company's role for that data and the use, so don't state it as settled. Write the interim rule as: customer data doesn't go into a tool until the company has confirmed its authority to use it there, the vendor terms, and any customer authorization the contracts require.
4. **Output rules:** a person reviews outputs before relying on them or sending them outside. Disclose AI assistance where required. Watch for IP issues, and keep code licensing and secrets rules.
5. **Prohibited uses:** anything the AI Act prohibits (`eu-ai-act.md`, §4); decisions about people (hiring, evaluation, discipline, grading, admissions) without the review the AI intake requires; impersonation; generating unlawful or harassing content; bypassing security controls. For decisions about people, say plainly whether the use is banned or allowed after a documented assessment and written approval, and that approval never authorizes a use the law or a contract prohibits. Not every employment or education use is high-risk under the AI Act; classification depends on the intended purpose (`eu-ai-act.md`).
6. **Agents and automation:** no agent gets access to systems or data, or acts on the company's behalf, without intake and approval, with the permissions documented.
7. **Training and literacy:** what training is required, for whom, and how often, fitted to the tools and roles (AI Act Art. 4, as amended: measures to support AI literacy). Training records are evidence for Art. 4, not proof of meeting it.
8. **Reporting:** how to report a mistake, a leak, or a harmful output, including putting prohibited data into a tool by accident: report it at once, don't try to delete it quietly, and who handles vendor-side deletion and decides on customer or regulator notice (`incident-assessment`). An internal reporting deadline (such as 24 hours) is a company rule; don't present it alongside regulators' deadlines (GDPR Art. 33's 72 hours applies to the controller's notice to the authority, and only to notifiable breaches).
9. **Monitoring, enforcement, and exceptions:** who grants exceptions, and the consequences of breach. Treat monitoring as its own decision: routine security and admin logs differ from reviewing what employees type. Before the policy mentions monitoring, record what is collected (metadata, prompts, outputs), who can see it, why, and for how long, and update the employee privacy notice. For EU and UK staff, assess the lawful basis and proportionality, and whether a DPIA is required. Don't promise monitoring the company can't do, such as of personal accounts. Until decided, use neutral wording: logs from approved tools are used under the existing employee privacy notice and security policies. A signed acknowledgment confirms receipt and understanding; it isn't a contract change, which may need local procedures.
10. **Ownership and review:** the owner, approvers, the review date (at least every 12 months), and the version history.

### Keep three layers apart

- **The policy** (staff-facing): durable rules, written for employees. No provisional analysis, blocker IDs, or unapproved monitoring.
- **The configuration standard:** sign-on, retention, connectors, repository exclusions, training settings, logging. It changes more often, so keep it outside the policy, owned by IT or Security.
- **The procedures and drafting record:** how to request a tool, approve an exception, and report a disclosure, plus the fact register, decisions, legal analysis, and approvals.

### Approval gates before the policy takes effect

| Gate | Evidence |
|---|---|
| Customer data | Data rules approved; vendor terms verified; customer authorization where contracts require it |
| Student data | Definition and exceptions process approved; technical controls tested (such as repository exclusions) |
| Approved tools | Vendor terms and admin configuration verified |
| Other AI features | Intake route for embedded and new features in place |
| Monitoring | Scope decided; notices updated; DPIA decision recorded |
| Reporting and enforcement | Reporting channel, escalation, and disciplinary process in place |
| Ownership | Owner, approver, and operational owners named |

## Product acceptable use policy: contents (AIUC-1 E010)

1. **Prohibited end-user conduct:** jailbreak attempts, malicious prompt injection, unauthorized data extraction, generating harmful content, misuse of other customers' data, automated scraping, and use for unlawful purposes (E010.1).
2. **Where it lives:** a standalone policy or a section of the terms of service, linked from the product.
3. **Detection:** how violations are found, such as prompt analysis, output filtering, usage anomaly detection, and alerts on suspicious access (E010.2). Link the controls (`controls-and-evidence`).
4. **User notice on breach:** in-product warnings, blocked-request messages, or error screens explaining the violation (E010.3).
5. **Enforcement:** real-time blocking, violation tracking with case handling, account actions, and quarterly effectiveness reviews (E010.4).
6. **Review:** at least every 12 months.

## Evidence

Each policy needs more than the document: approval records, the training completion log (employee policy), the detection configuration and sample user notices (product policy), and the record of each annual review.
