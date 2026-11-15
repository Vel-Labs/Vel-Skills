---
name: "project-personalize"
description: "Convert the scaffold into a real project by running the initializer, replacing placeholders, updating project contracts, and preserving contract/core/test governance boundaries."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-04-26"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Initializes a scaffold-based repository while preserving its existing contracts.
---

# Project Personalize

## Purpose

Apply the project personalize workflow to a project using the matching scaffold contracts.

## Inputs

The attached project and the applicable project files listed below.

Project personalization turns this template into a project-specific repo without losing the governance, contract, core, test, and audit baseline.

## Project references

- `REPO_PROFILE.json`
- `docs/project/TEMPLATE_USAGE.md`
- `docs/agents/START_HERE.md`
- `templates/personalization-checklist.md`

## Workflow

1. Run `npm run init:template:dry-run` to preview changes.
2. Run `npm run init:template` with project-specific values.
3. Replace remaining project-specific placeholders intentionally.
4. Update `contracts/` with the first project-specific canonical contract.
5. Keep reusable enforcement in `packages/core/`.
6. Run `npm run check`.
7. Update `DECISIONS.md`, `CHANGELOG.md`, and audit evidence if authority changed.

## Non-goals

Do not add adapters, demos, providers, deployment, or UI during personalization unless the human explicitly expands scope.

## Outputs

Use the checklist in `templates/` to make the personalization pass auditable.

## Checks

Check the initialized project against its repository profile and validation commands.

## Failure modes & recovery

If the initializer or profile is absent, locate the owning project scaffold before changing the repo.
