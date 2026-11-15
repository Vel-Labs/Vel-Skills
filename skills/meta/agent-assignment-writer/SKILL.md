---
name: "agent-assignment-writer"
description: "Create bounded human or agent workstream prompts with clear file ownership, dependencies, validation, docs updates, and stop conditions. Use this when delegating work or preparing a fresh parallel-agent assignment."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-04-26"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Creates bounded assignments with explicit ownership and verification.
---

# Agent Assignment Writer

## Purpose

Apply the agent assignment writer workflow to a project using the matching scaffold contracts.

## Inputs

The attached project and the applicable project files listed below.

## Non-goals

Delegation beyond current authority or uncoordinated overlapping file ownership.

Agent assignment writing is the discipline of turning a project need into a bounded, auditable workstream that another human or agent can execute without widening scope or colliding with other work.

## Project references

- `REPO_PROFILE.json`
- `templates/agent-assignment.md`
- `templates/fresh-agent-handoff.md`
- `docs/governance/multi-agent-workflow.md`
- `docs/governance/worktree-governance.md`

## Workflow

1. Identify the smallest workstream that can be owned by one agent.
2. State the branch or worktree if one is required.
3. List allowed files and forbidden files.
4. Name dependencies and upstream contracts.
5. Include validation commands from `REPO_PROFILE.json`.
6. Include docs, decisions, changelog, and audit files to update.
7. Include stop conditions.
8. Require a final summary with exact commands and results.

## Checks

Assignments should be narrow enough that two agents can work without touching the same files unless a human explicitly coordinates the overlap. If the assignment requires changing governance doctrine, architecture boundaries, or core contracts, call that out as a governance-locked change.

## Outputs

Use the templates in `templates/` as the starting point. Keep project-specific wording concise, but preserve explicit allowed files, forbidden files, validation, and stop conditions.

## Failure modes & recovery

If paths overlap, narrow the assignment or record the coordinator’s explicit ownership decision.
