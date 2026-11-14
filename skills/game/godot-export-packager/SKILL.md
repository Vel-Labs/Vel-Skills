---
name: "godot-export-packager"
description: "Prepare Godot export readiness materials, release checklists, build folders, export preset examples, version manifests, and post-build QA notes for mobile-first and desktop-capable games. Use when a project is nearing test build or release packaging."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-05-31"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Creates export manifests and platform QA checklists. Personal Godot workflow tooling for game development and art.
---

# Godot Export Packager

## Inputs

Project folder, version, and target platforms.

## Non-goals

Building or publishing a release.

## Purpose

Prepare a project for test builds and releases. This skill does not run Godot itself unless explicitly integrated into the user's environment. It creates checklists, release manifests, and export preset examples.

## Workflow

```bash
python3 ./scripts/create_export_readiness_pack.py \
  --project-dir /absolute/path/to/godot_project \
  --version 0.1.0 \
  --targets android ios windows macos linux
```

## Outputs

```text
exports/release_0_1_0/
  release_manifest.json
  export_checklist.md
  export_presets.example.cfg
  qa_matrix.md
```

## Checks

Verify the build version and every requested platform in the manifest.

## Failure modes & recovery

If a script reports missing or invalid input, correct the input and rerun. Inspect any existing output before explicitly choosing an overwrite option.
