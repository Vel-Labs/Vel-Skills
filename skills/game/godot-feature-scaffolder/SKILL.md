---
name: "godot-feature-scaffolder"
description: "Break a gameplay feature into Godot scenes, scripts, assets, tasks, acceptance criteria, and integration handoffs. Use for feature planning, mechanic definition, TODO breakdowns, and scaffolding feature modules inside a Godot project."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-05-31"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Scaffolds a feature plan, tasks, acceptance criteria, and asset requests. Origin unknown.
---

# Godot Feature Scaffolder

## Inputs

Project folder, feature name, kind, summary, and needed assets.

## Non-goals

Implementing the mechanic or generating art.

## Purpose

Turn a gameplay idea into a concrete feature module that can be implemented in Godot.

Examples:

- click-to-move pathing
- resource collection loop
- shop interaction system
- timing minigame
- inventory or task checklist
- character emotion state machine

## Outputs

```text
design/features/<feature_slug>/
  feature_spec.json
  tasks.md
  acceptance_criteria.md
  asset_requests.json
  scene_plan.md
  script_plan.md
```

## Workflow

```bash
python3 ./scripts/create_feature_spec.py \
  --project-dir /absolute/path/to/godot_project \
  --feature-name "Click To Move Pathing" \
  --kind movement \
  --summary "Tap a destination and have the player walk there." \
  --assets player_walk_sprite destination_marker path_dots
```

After the feature is defined, route scenes to `godot-scene-builder`, UI to `godot-ui-kit-generator`, and art to the correct sprite skill.

## Checks

Verify the plan lists acceptance criteria and required assets.

## Failure modes & recovery

If a script reports missing or invalid input, correct the input and rerun. Inspect any existing output before explicitly choosing an overwrite option.
