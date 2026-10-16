# Gradebook Sync: data dictionary and architecture notes

*Test fixture. Fictional system.*

Gradebook Sync pulls rosters and grades from district learning management systems (Canvas, Schoology) into our reading app nightly, and pushes reading-level scores back.

## Tables

| Table | Column | Type | Notes |
|---|---|---|---|
| students | student_id | uuid | internal ID |
| students | district_student_number | text | from SIS |
| students | first_name, last_name | text | |
| students | date_of_birth | date | |
| students | grade_level | int | |
| students | iep_flag | bool | from district roster export |
| students | ell_status | text | English language learner status |
| enrollments | section_id, teacher_id | uuid | |
| grades | assignment_id, score, submitted_at | | pulled from LMS |
| reading_levels | student_id, lexile_estimate, computed_at | | computed by our recommendation model |
| sync_logs | district_id, payload_json, created_at | | full request and response bodies |

## Infrastructure

- Postgres on AWS us-east-1; nightly backups kept 35 days
- sync_logs kept indefinitely "for debugging"
- Error monitoring through a third-party service that captures request payloads on exceptions
- District admins authorize the integration through OAuth in their LMS
