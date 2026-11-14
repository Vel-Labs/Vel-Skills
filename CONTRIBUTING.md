# Contributing

Each skill lives at `skills/<group>/<kebab-name>/`.

`<group>` is a short topic name such as `media`. `<kebab-name>` is lowercase words separated by hyphens, and it matches the `name` in that skill's frontmatter.

## SKILL.md

`SKILL.md` starts with YAML frontmatter. `name` is the folder name. `description` says when to use the skill, so an agent can match it to a task.

```yaml
---
name: kebab-name
description: When to use this skill.
metadata:
  origin: internal              # internal | external | adapted
  source: Vel-Skills            # upstream URL for external and adapted
  source-ref: <commit or tag>   # external and adapted only
  created: "YYYY-MM-DD"
  reviewed: "YYYY-MM-DD"
  reviewed-by: <person or agent>
  review-every-days: "90"       # 14 to 30 for external and adapted
  review-due: "YYYY-MM-DD"      # reviewed + review-every-days
  notes: <one line shown in the index>
---
```

The review fields are explained in [skills/meta/skill-review](skills/meta/skill-review/SKILL.md).
External and adapted skills are pinned copies: never fetch, `npx -y` or run `@latest`
upstream code at use time, and start the body with the review check section.

The body defines these sections:

- Purpose
- Inputs
- Outputs
- Non-goals
- Workflow
- Checks
- Failure modes & recovery

Helper files (scripts, styles, timelines, notes) sit in the same folder. Refer to them by relative path, such as `./edit_demo.sh` or `FRONTEND_STYLE.md`. Do not point at a path outside the skill folder.

Copy [templates/SKILL_TEMPLATE.md](templates/SKILL_TEMPLATE.md) when starting a skill.

## Secrets and portability

No secrets, tokens, personal data, or employer/client data anywhere in a skill: not in `SKILL.md`, not in examples, not in timelines, not in comments.

Scripts must be portable (no absolute machine paths). Prefer paths relative to the skill file, a temporary directory from the standard library, and flags the caller passes in. Do not commit virtualenvs, bytecode caches, or screen recordings. A sample video belongs under `examples/` only (see `.gitignore`).

## New-skill checklist

- [ ] Folder is `skills/<group>/<kebab-name>/`, and `name` in the frontmatter matches `<kebab-name>`.
- [ ] `description` says when to use the skill.
- [ ] Body includes Purpose, Inputs, Outputs, Non-goals, Workflow, Checks, and Failure modes & recovery.
- [ ] Every helper is referenced by a relative path, and those files are in the folder.
- [ ] No secrets, tokens, personal data, or employer/client data.
- [ ] Scripts are portable: no absolute machine paths.
- [ ] `bash -n` passes on each `.sh`. `python3 -m py_compile` passes on each `.py`. Caches from that check are not committed.
- [ ] `.sh` and `.py` files that are meant to be run are executable.
- [ ] Review metadata is filled in, and `review-due` equals `reviewed` plus `review-every-days`.
- [ ] External and adapted skills: `source` and an exact `source-ref`, a pinned copy, upstream telemetry or runtime fetching noted in `notes`, and the review check section first in the body.
- [ ] `python3 skills/meta/skill-review/build_index.py` was run (it writes `SKILLS_INDEX.md` and the `README.md` table), and `check_reviews.py` exits 0.
- [ ] No `__pycache__/`, `.venv/`, or stray `*.mp4` (samples only under `examples/`).
