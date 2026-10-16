# Vendor review intake

Fill in each field from what the user supplied, and record each fact with its status (Confirmed, Stated by requester, Stated by vendor, Unverified assumption, or TBC). Then ask about the gaps:

- **[R1] Round 1, blockers:** send first, alone, in one short numbered message (usually under 12 questions). Ask only the R1 items that are actually open.
- **[R2] Round 2, completion:** send with the draft.

Items marked **Evidence** ask for a document. A trust center page or questionnaire answer counts as "Stated by vendor," not as a contract term.

## A. The engagement

1. [R1] Vendor legal name and the entity that will sign; the products, services, and features in scope, including any AI features
2. [R1] What the company will use it for, stated specifically, and which internal activities or systems it supports
3. [R2] **Requesting business area** and **system owner**, if different
4. [R1] New vendor, renewal, expansion (new service, new feature, new data), or reassessment after a vendor notice
5. [R1] Whether the vendor already has, or has had, access to company personal data, including a pilot, trial, or AI feature turned on by default. If so, what data, since when, and whether it can be paused.
6. [R2] Contract dates: signature target, term, renewal, and notice periods

## B. Data and people

7. [R1] Categories of personal data the vendor will receive or access, and whose (customers' end users, employees, students, children, prospects)
8. [R1] Special category, biometric, children's, student, or US-sensitive data, including what users might type or upload
9. [R2] Approximate volume and the regions of the people concerned
10. [R1] For student data: which institutions and states, and the FERPA exception relied on (`../../_shared/references/ferpa.md`)

## C. Documents

11. [R1] **Evidence:** the DPA or data processing terms, the MSA or terms of service, any AI or "acceptable use" terms, and the order form. Say which version applies and whether the online terms can change.
12. [R1] **Evidence:** the current subprocessor list, including model providers and hosting regions
13. [R1] **Evidence:** the latest SOC 2 Type II or ISO 27001 report (with scope and date), and any bridge letter
14. [R2] **Evidence:** the vendor's completed security or privacy questionnaire, if any
15. [R2] **Evidence:** the DPF listing for the signing entity, or the SCCs and UK or Swiss addenda

## D. Configuration

16. [R1] Settings the company controls that change the data protection picture: data retention, zero-retention or no-training switches, regional hosting, sharing defaults, admin controls for AI features. **Evidence:** screenshots or exports of the settings as configured.
17. [R2] Integrations: what data flows to and from the vendor, how (API, SSO, file upload, connector), and who at the company can change it

## E. AI module (when the vendor supplies AI)

18. [R1] What the AI does with company data: summarize, generate, classify, score, recommend, or act through tools. For agents: which tools, systems, and permissions.
19. [R1] Whether the vendor or its model providers train, fine-tune, or evaluate on company inputs, outputs, or files, the default, and where the commitment is written. **Evidence:** the clause or the setting.
20. [R1] What is retained (prompts, outputs, files, embeddings, abuse-monitoring logs), for how long, and where
21. [R2] Output ownership and IP protection
22. [R2] Notice of model or provider changes
23. [R1] Whether the vendor holds AIUC-1 certification. **Evidence:** the certificate and audit report, showing the product in scope, the release audited, the report date, and exclusions. Otherwise, any other AI assurance, such as ISO/IEC 42001 certification or third-party red-team results.
24. [R1] How the company will use the outputs, especially any decision about a person (hiring, grading, access, pricing, discipline) or any evaluation of employees. Has HR, or employee representation where required, reviewed that use? This decides the AI Act classification and whether an AI impact assessment is needed.
25. [R1] For any score or inference about people: the vendor's technical definition, the inputs used, and sample outputs. **Evidence:** product documentation.
26. [R2] For recording tools: whether sensitive meetings can be excluded, who can access recordings, and how deletion reaches transcripts, summaries, exports, and backups.
27. [R2] Whether the vendor's training or retention has already applied to company data, and what happened to it.

## F. Exit

28. [R2] Return and deletion at the end of the contract, including backups, subprocessors, derived data, and fine-tuned models
29. [R2] Who internally owns the vendor relationship and the reassessment
