---
name: "promote-work"
description: "Move work from capture or draft state into active, reviewed, accepted, or archived state without losing context."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-05-04"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Records lifecycle transitions and preserves the review trail.
---

# Promote Work

## Purpose

Move an authorized artifact to its next lifecycle state.

## Inputs

- The artifact, its owner, the current state, and the requested target.

## Outputs

- The approved state and destination, with a review trail. Start a proposal from [the template](templates/promotion-proposal.md).

## Non-goals

- Moving or overwriting important files without authorization.

## When To Use
Use when a draft, agent output, AI eval, business idea, or project artifact is ready to move to its next lifecycle state.

## Human Outcome
The work has a clear new status, destination, and review trail.

## Agent Permissions
Agents may draft promotion proposals. Agents must not move or overwrite important files unless explicitly instructed.

## Workflow

1. Identify current state: capture, draft, active, review, accepted, or archive-candidate.
2. Identify target state and destination.
3. Check nearest README and AGENTS boundaries.
4. Create a promotion proposal if the work touches sensitive, business, personal, legal, finance, or commercial-use material.
5. Move or update files only if explicitly allowed.
6. Update an existing dashboard or review queue when the owner needs that status
   or a durable follow-up; do not create paperwork for an ordinary file update.
7. Report changed files and unresolved review needs.

## Promotion Paths

These are examples, not a mandatory lifecycle. Existing project/task owners
define acceptance; ordinary edits need no new intake, report or board.
- General: `capture -> triage -> draft -> active -> review -> accepted -> archived`
- AI Lab: `candidate -> eval-run -> benchmarked -> reviewed -> approved-for-use`
- Delegated work: `bounded assignment -> implementation and verification -> coordinating owner review`
- Business: `idea/draft -> review queue -> human-approved record -> archive/reference`

## Templates
- `templates/promotion-proposal.md`

## Checks

- Current and target state are explicit.
- Review requirements are not skipped.
- Dashboard status is updated when appropriate.

## Failure modes & recovery

If authority or the destination is uncertain, prepare a proposal and leave the artifact in place.
