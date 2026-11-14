---
name: "archive-candidate-review"
description: "Identify old or inactive files/folders that may be ready for archive without moving or deleting them."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-05-04"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Reports archival candidates. Replaced workspace-specific command and paths with portable inspection.
---

# Archive Candidate Review

## Purpose

Identify stale work and cold storage candidates for a person to review.

## Inputs

- The assigned directory and age threshold.

## Outputs

- A read-only report using [the report template](templates/archive-review-report.md) when a handoff needs one.

## Non-goals

- Moving, deleting, or renaming any candidate.

## When To Use
Use when looking for stale work, completed projects, cold storage candidates, or old files that should leave active view.

## Human Outcome
There is a reviewable report of archive candidates. Nothing is moved or deleted automatically.

## Agent Permissions
Agents may generate reports. Agents must not move, delete, or rename archive candidates unless explicitly instructed.

## Workflow

1. Inspect the assigned folder and sort candidates by age. Use only a read-only archive report command already supplied by the project, if available.
2. Exclude caches, dependencies, git internals, and private/sensitive areas unless explicitly assigned.
3. Report candidates with last modified dates when available; use a durable
   report only when requested or needed for a handoff.
4. Record uncertain items in the current report or an existing review queue.
5. Move files only within explicit current-task authority; this review grants none.

## Templates
- `templates/archive-review-report.md`

## Checks

- Report lists candidates only.
- No files moved or deleted.
- Human review is requested for any uncertain item.

## Failure modes & recovery

If timestamps or ownership are unclear, mark candidates uncertain in the current report.
