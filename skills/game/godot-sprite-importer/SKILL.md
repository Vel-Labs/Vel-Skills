---
name: "godot-sprite-importer"
description: "Convert generated sprite outputs into Godot-ready import manifests, copied asset folders, starter SpriteFrames resources, node setup notes, and validation summaries. Use after sprite-generator or a project-local sprite worker has produced PNG/WebP sheets or frame folders."
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-05-31"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Packages generated sprite sheets and frame metadata for Godot. Origin unknown.
---

# Godot Sprite Importer

## Non-goals

Generating the art itself.

## Purpose

Bridge generated sprite assets into a Godot project.

This skill does not create art. It packages generated art for Godot import.

## Inputs

- generated sprite pack folder
- `spritesheet.png` or `spritesheet.webp`
- optional `frames/frames-manifest.json`
- optional separate frame PNGs

## Outputs

```text
project/assets/sprites/<pack_name>/
  spritesheet.png
  spritesheet.webp
  frames/
  import_manifest.json
  node_setup_notes.md
  <pack_name>_spriteframes.tres
```

## Workflow

```bash
python3 ./scripts/import_sprite_pack.py \
  --project-dir /absolute/path/to/godot_project \
  --pack-name couch_states \
  --source-dir /absolute/path/to/generated_sprite_pack
```

If a manifest contains grid/cell data, use `./scripts/create_spriteframes_tres.py` to make a starter `SpriteFrames` resource.

## Checks

Check copied image paths and verify metadata before generating SpriteFrames.

## Failure modes & recovery

If a script reports missing or invalid input, correct the input and rerun. Inspect any existing output before explicitly choosing an overwrite option.
