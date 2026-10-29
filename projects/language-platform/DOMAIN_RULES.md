# Language Learning Platform — commercial domain guardrails

## Business goal
Provide a secure language-learning experience. Confirm whether the MVP is 1:1 tutoring, group classes, self-paced content, or a combination before implementation.

## Non-negotiable domain rules
- Define roles (e.g. student, teacher, parent/guardian, admin) and enforce permissions server-side, not just by hiding UI.
- Protect learner profiles, notes, attendance, progress, messages, and recordings. Use least-privilege access and explicit retention/deletion policies.
- If minors may use the platform, design age-appropriate consent/guardian flows and review applicable Australian child privacy/safety requirements before launch.
- Booking must prevent double-booking and handle time zones, daylight saving, cancellation windows, and concurrent requests atomically.
- Payment state must be confirmed from trusted payment-provider events, with verified webhook signatures and idempotent processing; never trust browser-side payment success alone.
- Keep lesson scheduling, lesson completion, billing, and learning progress as distinct state machines.
- Track changes to teacher availability, booking status, refunds, and admin overrides with audit events.
- Content and AI feedback must distinguish automated suggestions from teacher-assessed outcomes. Avoid exposing one learner's content to another.
- Provide accessible mobile-first learning flows and clear loading, error, and offline states.

## Minimum acceptance tests
- Role access, cross-user data isolation, concurrent booking, daylight-saving transitions, cancellations, payment retries/duplicate webhooks, failed payment, refunds, lesson status changes, progress privacy, and account deletion/export.

## Decisions needed from owner
- Age group? Learning format? Languages? Pricing? Scheduling? Payment provider? Video platform? Parent accounts? AI features? Retention and consent requirements?
