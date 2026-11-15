---
name: "workflow-packaging-audit"
description: "Look back across recent work history to find repeated manual workflows worth packaging as skills, subagents, automations, extensions, or deliberate skips."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-07-27"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Finds repeated work worth packaging. Replaced workspace folder names with caller-supplied evidence locations.
---

# Workflow Packaging Audit

## Purpose

Identify repeated manual work worth packaging as a reusable workflow.

## Inputs

- Recent source records and locations of existing skills, agents, operational contracts and any governed loop registry.

## Non-goals

- Installing hooks, running schedulers, or mutating live automations without authorization.

## When To Use

Use when asked to review recent work, Codex history, memories, Chronicle context,
or workspace activity to identify repeated manual workflows that should become
reusable assets.

## Evidence Order

Use available evidence in this order:

1. Recent Codex sessions, task summaries, local reports, and GoalBuddy notes.
2. Codex Memories and rollout summaries to find patterns repeated across
   sessions.
3. Chronicle, if enabled, for discovery only. Confirm important details in the
   source system when practical.
4. Existing skills, custom agents, worker contracts, heartbeats, and automations
   so new assets reuse or extend what already exists.

Stay inside the current workspace boundaries. Do not use network, install
packages, run schedulers, or mutate automations unless explicitly authorized.

## Candidate Test

Only act on a candidate when it passes all four checks:

- occurred at least twice, or is clearly likely to recur and costly to repeat;
- has stable inputs, a repeatable procedure, and a clear output or stopping
  condition;
- would materially improve speed, quality, consistency, or reliability;
- is not already adequately covered by existing skills, agents, or automation.

## Recommended Form

Choose the smallest appropriate form:

- `skill`: reusable workflow or playbook.
- `subagent`: bounded specialist role or investigation suitable for delegation.
- `automation`: scheduled or recurring check, report, reminder, or monitor.
- `extend existing`: improve a current skill, agent, or ops contract.
- `extend loop`: add a trigger, scope, fixed verifier profile, or proof rule to
  an existing governed LoopRegistry definition when ownership and purpose match.
- `register loop`: propose one new LoopRegistry definition for a stable,
  evidence-backed event or recurring workflow not covered by an existing loop.
- `skip`: too one-off, ambiguous, sensitive, poorly evidenced, or already
  covered.

Prefer skills for repeatable procedures, subagents for delegated review or
investigation roles, and governed loops for typed event-to-proof workflows.
Automations remain appropriate only for separately authorized cadence-driven
report-first work. A loop recommendation does not install a hook, activate a
schedule, or grant execution authority.

## Workflow

1. Use applicable workspace/project guidance already in context; open missing
   relevant rules without a general startup tour.
2. Inspect existing coverage for the candidate in the supplied skills, agent, and operations locations or relevant project-local folders; avoid a full catalog
   when a targeted lookup is sufficient.
3. Search recent memory and local reports for repeated manual lanes.
4. Build a compact shortlist before creating anything.
5. For a loop-shaped candidate, inspect the project’s loop registry, when present and choose
   exactly `extend loop`, `register loop`, or `skip`. Prefer extension when the
   owner, trigger family, scope, and proof outcome already match.
6. An audit produces recommendations. Create a high-confidence missing item
   only when the current task authorizes creation, keeping it narrow, practical,
   source-aware, and easy to validate.
7. Do not create speculative, overlapping, broad, or automation-like assets from
   weak evidence.
8. Finish with created/extended items, deliberate skips, and items needing more
   evidence.

Do not turn LoopRegistry contract categories such as triggers, budgets, graph
shapes, hooks, memory, isolation, or verifier classes into one empty skill per
category. They belong under the coherent `loop-engineering` workflow unless a
later candidate independently passes the four checks above.

## Outputs

Use `templates/workflow-packaging-audit-report.md` when a durable report has a
real handoff or decision consumer. A contained audit can report in chat.

The shortlist must include:

- repeated workflow;
- supporting evidence and dates;
- frequency/confidence;
- recommended form;
- for loop-shaped candidates, `extend loop`, `register loop`, or `skip` plus
  the existing/proposed loop ID;
- why it is or is not worth creating.

The closeout must include:

- what was created or extended;
- what was deliberately skipped;
- what needs more evidence before packaging;
- commands run and validation;
- assumptions and remaining risks.

## Checks

Before claiming completion:

- Confirm new or updated assets are registered where the workspace expects them.
- Re-read created `SKILL.md` or contract files for scope creep and overlap.
- List files changed.
- State if source systems were not live-confirmed and what evidence was
  memory-derived or Chronicle-derived.

## Failure modes & recovery

If evidence is weak or an owner is unclear, report the candidate as needing evidence.
