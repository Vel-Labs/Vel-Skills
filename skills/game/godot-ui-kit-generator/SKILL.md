---
name: "godot-ui-kit-generator"
description: "Plan and scaffold mobile-first Godot UI/HUD/menu kits, including Control scene stubs, UI asset manifests, safe-area notes, touch target rules, and handoffs to sprite-generator for UI art. Use when the user needs buttons, HUD panels, menus, icons, meters, or mobile/desktop UI layout guidance."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-05-31"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Scaffolds mobile-first HUD and menu resources. Origin unknown.
---

# Godot UI Kit Generator

## Inputs

Project folder, kit name, target screens, and icon needs.

## Outputs

UI stubs, a manifest, and routed icon and texture requests.

## Non-goals

Generating or approving visual assets.

## Purpose

Create UI/HUD/menu structures and asset requests for Godot.

## Boundary

This skill designs and scaffolds the UI kit. For actual visual art generation, route texture/icon requests to:

- `sprite-generator` for generic UI art
- a project-local style worker only when the user has intentionally personalized and installed one

## Workflow

```bash
python3 ./scripts/create_ui_kit.py \
  --project-dir /absolute/path/to/godot_project \
  --kit-name first_playable_hud \
  --screens hud pause inventory \
  --icons confirm warning coin heart
```

## Defaults

- mobile-first safe-area aware layout
- touch target minimums
- desktop-compatible anchors
- UI asset manifest for generated icons/buttons/panels

## Checks

Check touch targets, anchors, and the asset requests for each screen.

## Failure modes & recovery

If a script reports missing or invalid input, correct the input and rerun. Inspect any existing output before explicitly choosing an overwrite option.
