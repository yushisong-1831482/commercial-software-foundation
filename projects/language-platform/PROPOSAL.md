# Language Platform proposal — approval required

## Product requirements and MVP boundary
Goal: a private, accessible learning service. Owner must choose learning format, age groups, region, required roles and core journey. Accounts, profiles, lessons, progress, attendance, bookings, notifications and payments are candidates only. Do not implement or collect learner data until scope and privacy controls are approved. Exclude payment, recording and AI features until individually approved.

## Architecture proposal
Separate identity, learner access policy, scheduling, learning records and optional billing. Use a transactional relational store for bookings and permissions; private object storage with authorized download for materials. Integrate a managed identity provider after reviewing residency, account recovery and session controls. Framework/database/provider choices remain open. Pages suits static content; evaluate Workers for dynamic APIs only after framework/runtime and scheduling requirements are known.

## Conceptual database design
Possible entities: account, role_assignment, teacher_profile, learner_profile, guardian_relationship, lesson, availability, booking, attendance, progress_entry, material_grant, payment_event and audit_event. Include only approved MVP entities. Unique/transactional constraints prevent concurrent booking; store instants in UTC and an IANA timezone for display/recurrence. Keep booking, attendance, progress and payment states independent. Retention and deletion policy must cover backups and provider copies.

## Authentication and authorization
Deny by default. Define an approved role-resource-action matrix and test each route server-side. Teachers access only assigned learners; learners only their own permitted records; guardian access requires a verified, revocable relationship. Administrator access is audited and least privilege. These roles are provisional. Use secure sessions, CSRF protections where applicable, rate limits, account recovery and privileged-user MFA. Never trust client role claims or payment success screens.

## Privacy and security requirements
Before collection assess applicability of the Australian Privacy Act, Australian Privacy Principles, Notifiable Data Breaches scheme, relevant state/territory rules and child-safety obligations with qualified advice. Determine age/consent/guardian flows, data minimisation, residency, overseas disclosure, retention, access/export/deletion and complaint handling. Do not claim legal compliance. Avoid collecting exact birth dates unless justified. Never put learner notes or recordings in telemetry. Payment providers hold card data; signed, idempotent webhooks drive payment state if payments are approved.

## Testing strategy
Test login/logout/recovery, every approved role and relationship boundary, cross-learner access, booking races, timezone/DST transitions, booking changes, validation and mobile accessibility. If billing is approved add duplicate/out-of-order webhook and refund state tests in provider sandbox. Application checks are not yet implemented.

## Deployment and operations
Use isolated synthetic preview records, distinct identities/storage/secrets, private preview access, and reviewed release gates. No public app or resources are created by this proposal. Agree owner, availability target, RPO/RTO and recovery drills before commercial launch. Confirm provider contracts and privacy review before student enrolment.
