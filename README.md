# Vel-Skills

Vel's personal library of reusable agent skills.

Each skill is a folder: a `SKILL.md` plus the helper files it names. Cursor, Codex, and Claude-style agents load a skill by reading that folder when a task matches the `description` in its frontmatter.

## Layout

```
skills/<group>/<kebab-name>/   # one skill; SKILL.md plus helpers
  SKILL.md
templates/SKILL_TEMPLATE.md     # blank skeleton for a new skill
SKILLS_INDEX.md                 # grouped index
CONTRIBUTING.md                 # skill contract and new-skill checklist
```

`<group>` is a short topic (`media`, and others as they are added). `<kebab-name>` matches the `name` in that skill's frontmatter. Helper scripts and notes stay inside the skill folder and are referenced by relative path.

## Install a skill locally

Copy the skill folder into the agent's skills directory. The folder has to move as a unit so those relative paths keep working.

```bash
# Codex — keep the group
mkdir -p ~/.codex/skills/<group>
cp -R skills/<group>/<name> ~/.codex/skills/<group>/<name>

# Cursor
mkdir -p ~/.cursor/skills
cp -R skills/<group>/<name> ~/.cursor/skills/<name>
```

Example for the skill in this repo:

```bash
mkdir -p ~/.codex/skills/media ~/.cursor/skills
cp -R skills/media/app-demo-video ~/.codex/skills/media/app-demo-video
cp -R skills/media/app-demo-video ~/.cursor/skills/app-demo-video
```

Restart the agent session if it only reads skills at startup, then point it at the copied `SKILL.md`.

## Skills

| Skill | Group | What it is for |
| --- | --- | --- |
| [app-demo-video](skills/media/app-demo-video/SKILL.md) | media | Make a dramatic, real-data demo video of a working app by styling a camera-ready frontend, recording it with Playwright, and compositing a reserved caption bar with ffmpeg. |
| [dogfood](skills/testing/dogfood/SKILL.md) | testing | Dogfood an application through independent first-time-user journeys in real browsers, consolidate evidence, and verify authorized fixes. |

The same list, grouped, is in [SKILLS_INDEX.md](SKILLS_INDEX.md). The contract for adding a skill is in [CONTRIBUTING.md](CONTRIBUTING.md).
