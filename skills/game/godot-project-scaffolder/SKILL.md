---
name: "godot-project-scaffolder"
description: "Create a Godot 4.x project skeleton for mobile-first, desktop-capable 2D games, including folders, starter scenes, scripts, README, asset directories, and project manifests. Use when a user wants a new Godot project structure or clean game repo foundation."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-05-31"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Creates a baseline Godot 4.x project structure. Origin unknown.
---

# Godot Project Scaffolder

## Inputs

Project name, output directory, and preset.

## Non-goals

Implementing game features beyond the scaffold.

## Purpose

Create the initial Godot project structure and baseline files for a mobile-first 2D game that also supports desktop/laptop.

## Outputs

```text
project-root/
  project.godot
  README.md
  scenes/
    Main.tscn
    rooms/
    ui/
  scripts/
    main.gd
    game_state.gd
    input_router.gd
  assets/
    sprites/
    ui/
    audio/
    fonts/
  generated_assets/
  art_source/
  design/
  pipeline_runs/
  exports/
  tools/
```

## Workflow

```bash
python3 ./scripts/create_godot_project.py \
  --project-name "Starter Adventure" \
  --output-dir /absolute/path/to/starter_adventure \
  --preset mobile_2d \

```

## Handoff

After scaffolding, use:

- `godot-feature-scaffolder` for gameplay feature modules
- `godot-scene-builder` for scene bundles
- `godot-ui-kit-generator` for HUD/menu structures
- `godot-sprite-importer` for generated sprite sheets

## Checks

Verify project.godot, scene, and script paths resolve.

## Failure modes & recovery

If a script reports missing or invalid input, correct the input and rerun. Inspect any existing output before explicitly choosing an overwrite option.
