---
name: "phase-closeout-audit"
description: "Close a scaffold or project phase with exact scope, files changed, verification evidence, findings, follow-up, decisions, changelog, and roadmap/current-state updates."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-04-26"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Records verifiable phase closeout and owner follow-up.
---

# Phase Closeout Audit

## Purpose

Apply the phase closeout audit workflow to a project using the matching scaffold contracts.

## Inputs

The attached project and the applicable project files listed below.

## Non-goals

Starting downstream work without authorization.

Phase closeout is the evidence pass that turns completed work into inspectable project truth.

## Project references

- `templates/closeout-audit.md`
- `docs/roadmaps/CURRENT_STATE_AND_NEXT.md`
- `ROADMAP.md`
- `DECISIONS.md`
- `docs/decisions/`
- `CHANGELOG.md`

## Workflow

1. Inspect changed files and scope.
2. Run the broadest responsible verification, usually `npm run check`.
3. Create or update the closeout audit note.
4. Update roadmap/current-state routing.
5. Update `DECISIONS.md` if authority or architecture changed.
6. Add detailed entries to the relevant dated file under `docs/decisions/` when authority or architecture changed.
7. Update `CHANGELOG.md`.
8. State follow-up clearly and keep downstream work deferred unless explicitly authorized.

## Checks

Record exact commands and exact results. Do not mark work done from intent alone.

## Outputs

Use the template in `templates/` and keep the audit factual. Findings should be tied to files, commands, or explicit missing evidence.

## Failure modes & recovery

If a check cannot run, record the exact gap and keep the affected claim open.
