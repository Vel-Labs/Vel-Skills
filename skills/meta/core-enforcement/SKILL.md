---
name: "core-enforcement"
description: "Implement reusable enforcement logic in packages/core against canonical contracts while keeping adapters, demos, providers, UI, and schema ownership out of core."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-04-26"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Implements reusable enforcement against the project’s canonical contracts.
---

# Core Enforcement

## Purpose

Apply the core enforcement workflow to a project using the matching scaffold contracts.

## Inputs

The attached project and the applicable project files listed below.

## Outputs

Reusable enforcement and focused regression evidence.

Core enforcement is the executable layer that consumes canonical truth and makes it usable by future project code.

## Project references

- `REPO_PROFILE.json`
- `contracts/README.md`
- `packages/core/README.md`
- `tests/README.md`

## Workflow

1. Confirm the canonical contract already exists in `contracts/`.
2. Implement only reusable enforcement in `packages/core/`.
3. Keep modules small and extracted before they become broad orchestrators.
4. Return structured fail-closed results where practical.
5. Add focused tests in `tests/core/`.
6. Run `npm run test:focused`, `npm run typecheck`, and `npm run check`.

## Non-goals

`packages/core/` must not own adapters, demos, provider integrations, deployment, UI, or canonical schema definitions.

## Design Bias

Prefer small modules, explicit result types, deterministic file reads, and clear errors over clever abstractions. Core should be boring, inspectable, and easy for future packages to consume.

## Checks

Run focused tests, type checking, and the repository check.

## Failure modes & recovery

If the canonical contract is absent or ambiguous, clarify its ownership and meaning before adding enforcement.
