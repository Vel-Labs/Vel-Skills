---
name: "godot-mobile-optimization-checker"
description: "Audit Godot projects and generated asset packs for mobile-first performance issues, including large textures, transparent padding waste, asset counts, file sizes, folder hygiene, and desktop compatibility notes. Use before integration, milestone review, or export."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-05-31"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Reports large images, transparent margins, and mobile readiness risks. Personal Godot workflow tooling for game development and art.
---

# Godot Mobile Optimization Checker

## Inputs

Godot project and report directory.

## Outputs

Asset audit and platform readiness notes.

## Non-goals

Deleting, resizing, or replacing assets based solely on the audit.

## Purpose

Review assets and project structure for mobile-first Godot development.

## Checks

- image dimensions
- file sizes
- transparent padding waste where possible
- possible oversized textures
- huge atlases
- missing manifests
- mobile/desktop notes

## Workflow

```bash
python3 ./scripts/audit_assets.py \
  --project-dir /absolute/path/to/godot_project \
  --output-dir /absolute/path/to/report
```

## Failure modes & recovery

If a script reports missing or invalid input, correct the input and rerun. Inspect any existing output before explicitly choosing an overwrite option.
