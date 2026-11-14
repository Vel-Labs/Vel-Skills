---
name: "godot-scene-builder"
description: "Create Godot `.tscn` scene starters and matching GDScript stubs for actors, props, rooms, interactables, UI containers, and click-to-move setups. Use when the user needs scene architecture or import-ready node hierarchies."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-05-31"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Creates starter Godot scenes and matching GDScript stubs. Origin unknown.
---

# Godot Scene Builder

## Inputs

Project folder, scene name, and scene type.

## Outputs

A scene bundle with its script stub.

## Non-goals

Completing gameplay logic.

## Purpose

Create reusable scene bundles for Godot.

## Scene Types

- `actor`: controllable or NPC character with `AnimatedSprite2D`
- `prop`: static/stateful interactable with `Sprite2D` and `Area2D`
- `room`: `Node2D` room shell with prop containers and navigation hooks
- `ui`: `Control` scene shell
- `click_to_move`: room/player setup for tap/click destination gameplay

## Workflow

```bash
python3 ./scripts/create_scene_bundle.py \
  --project-dir /absolute/path/to/godot_project \
  --scene-name PlayerActor \
  --scene-type actor
```

## Checks

Verify the scene file and referenced script exist.

## Failure modes & recovery

If a script reports missing or invalid input, correct the input and rerun. Inspect any existing output before explicitly choosing an overwrite option.
