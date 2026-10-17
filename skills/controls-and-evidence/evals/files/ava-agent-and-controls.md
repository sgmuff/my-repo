# "Ava" support agent and current controls

*Test fixture. Fictional company and product.*

## The agent

Ava is our customer-facing support agent in the web app chat. It's built on a third-party foundation model through an API. Ava answers product questions from our help center, looks up a customer's orders, and can issue refunds of up to $50 without a human. Larger refunds go to a human queue. It greets users with "Hi, I'm Ava! How can I help?" Sales wants AIUC-1 certification by Q2 2027 to unblock enterprise deals.

## Existing controls (from our SOC 2 Type II report, period July 1, 2025 to June 30, 2026, and team notes)

| Ref | Control | Notes |
|---|---|---|
| CC6.1 | Okta enforces SSO and MFA for workforce accounts | Tested in SOC 2, no exceptions |
| CC6.2 | Quarterly access review of production systems | Tested; one exception (late Q3 review) |
| CC8.1 | Code changes require pull request approval and CI tests | Tested; covers Ava's code repo |
| CC7.2 | Application logs to Datadog, kept 90 days | Ava's conversations are logged, including tool calls |
| CC7.3 | Incident response plan | General security plan; doesn't mention AI failures |
| CC9.2 | Vendor risk review at onboarding and annually | The model provider was reviewed at onboarding in 2025 |
| CC6.7 | Encryption at rest and in transit | Tested |
| — | Ava system prompt tells it to refuse off-topic requests | No testing of how well it works |
| — | Refund tool enforces a $50 cap in code | Unit tested |
| — | AI acceptable use policy for employees | Approved March 2026 |
| — | No red-teaming, hallucination evaluation, or third-party testing so far | — |
