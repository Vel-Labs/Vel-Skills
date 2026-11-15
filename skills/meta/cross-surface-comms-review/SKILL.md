---
name: "cross-surface-comms-review"
description: "Adapt or review source-of-truth business, community, launch, support, or proposal copy across Docs, Sheets, Slack, Reddit, decks, and local Markdown while preserving approval state and human-review boundaries."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-05-24"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Adapts channel copy while preserving source and reviewer state.
---

# Cross-Surface Comms Review

## Purpose

Adapt source material while keeping the approval state traceable.

## Inputs

- Source artifact, its owner, and the target surface.

## Non-goals

- Signed records, credential material, and final legal or compliance approval.

## When To Use

Use when work starts in one canonical surface and needs to be adapted, reviewed,
or summarized for another channel, especially:

- Google Docs or Sheets to Slack, Reddit, deck, AMA, FAQ, or support-script copy.
- Local Markdown packs to Google Docs, Slides, or channel-specific posts.
- Proposal, launch, defensive-comms, product-feedback, or community-safety drafts.

Do not use this for signed contracts, tax, bank, finance records, credential
material, or final legal/compliance approval.

## Human Outcome

The source-of-truth artifact stays identifiable, channel-specific drafts are
clearly non-final unless approval evidence says otherwise, and approval/reviewer
state is not flattened into publish-ready language.

## Workflow

1. Identify the source-of-truth artifact, its current owner, and the target
   channel or review surface.
2. Record the current approval state using the source's own fields, comments, or
   visible reviewer status. If approval is unknown, say unknown.
3. Preserve the source structure before adapting tone: tabs, sections, tables,
   row-level approval columns, reviewer comments, and rationale fields matter.
4. Draft channel-specific copy with the channel constraints in mind, but keep
   unsupported claims and final-approval language out.
5. Keep sensitive boundaries explicit: human approval, hardware/signing gates,
   third-party platform control, cost caps, consent, and draft/report-only status.
6. Produce a short review note with source, target channel, changes made,
   approval state, and human decisions needed.
7. If the work affects active business/client material, add or update the
   relevant review item instead of treating the draft as accepted.

## Checks

- Source artifact and target channel are both named.
- Draft/publication/approval state is stated separately.
- Reviewer comments or row-level approval columns are preserved when present.
- Platform-specific limits and safety rules are handled in the channel draft.
- No agent claims to have sent, posted, approved, or published unless that action
  was explicitly requested and separately verified.

## Outputs

Use the smallest durable output that fits the task:

- channel-ready draft with a source reference;
- review memo;
- comment-resolution checklist;
- approval-state summary;
- proposal or launch-copy delta.

## Completion Criteria

- The human can see what changed and where it came from.
- Draft state and approval state are not confused.
- Remaining human decisions are concrete.
- Files changed, commands run, validation, assumptions, and risks are reported
  for non-trivial workspace work.

## Failure modes & recovery

If approval evidence is missing, record the state as unknown and preserve human decisions in the [review note template](templates/review-note.md).
