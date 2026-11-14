---
name: modern-web-guidance
description: Use when building or changing web UI, CSS layout or animation, forms, accessibility, dark mode, performance (LCP, INP, CLS), web security or client-side JS. A pinned, reviewed copy of Google Chrome's modern web guides; read the matching guide before writing ad-hoc code or adding a dependency. Not for backend, infrastructure or tooling work.
license: Apache-2.0 for the guides (see LICENSE); the wrapper is part of Vel-Skills.
metadata:
  origin: adapted
  source: https://github.com/GoogleChrome/modern-web-guidance
  source-ref: 4dd968349e54ca45a05dd5c818fb035c9054b022 (Release v1.0.0, 2026-11-10)
  created: "2026-11-14"
  reviewed: "2026-11-14"
  reviewed-by: Claude Code (Opus 5.5)
  review-every-days: "14"
  review-due: "2026-11-28"
  notes: Guides only. Upstream's npx CLI is not used, so its default telemetry (search queries, agent name, OS sent to Google) and unpinned @latest execution are gone.
---

# Modern Web Guidance (pinned copy)

## First: check this skill is still reviewed

This skill is adapted from an external repository. Before relying on it, compare
today's date with `review-due` above.

- **On or before the due date:** use the skill.
- **After the due date:** tell the person, before doing the task:
  "Modern Web Guidance was last reviewed on <reviewed> against <source> at
  <source-ref>. Its review was due on <review-due>. Shall I check upstream for
  changes now?" If they agree, follow **Reviewing this skill** below. If they
  decline, or nobody can be asked, use the pinned copy and say in your report
  that the review is overdue.

The `meta/skill-review` skill lists every skill's review state at once.

## Purpose

Give coding agents current, platform-correct ways to build web UI: dialogs and
popovers, tables, dark mode and `color-scheme`, forms and autofill, accessibility,
custom selects, transitions and motion, responsive layout, container queries,
typography and colour, Core Web Vitals, image and font loading, HTML
sanitising, passkeys, web components, dates and time zones, and built-in AI.

## Inputs

- The task: what is being built or changed in the web front end.
- [INDEX.md](INDEX.md): every guide with its area, title and one-line summary.
- The guides under [guides/](guides/).
- The project's browser-support policy, if it states one.

## Outputs

- Code that follows the matching guides, including their fallbacks for
  features that are not Baseline widely available.
- One line per guide used in the report: which guide, and the pitfall it avoided.

## Non-goals

- Backend code, SQL, CI, Docker, scripts or build tooling.
- Judging whether a screen looks and feels right; use `design/visual-parity-review`.
- Running the upstream CLI or installing the upstream plugin.

## Workflow

1. Open [INDEX.md](INDEX.md) and pick the guides whose area and summary match the
   task. Prefer one specific guide plus its discipline guide (for example
   `ui-components/progress-ring` plus `css/css`).
2. Read the chosen files. Where a guide says
   `npx -y modern-web-guidance@latest retrieve "<id>"`, open the guide with that
   id from the index instead. **Never run the npx command.**
3. Apply the guidance in the project's framework without dropping the platform
   feature. Follow each guide's fallback advice unless the project states a
   browser-support policy.
4. Check the code against the guide before finishing, and name the guides used
   in the report.

### Reviewing this skill

1. From this folder, run `python3 ./scripts/refresh.py compare` to list guides
   added, removed and changed upstream since `source-ref`, with short diffs. It
   changes nothing.
2. Read the changes. Look for useful new guidance, guidance that conflicts with
   your rules, and any new instruction to run code, send data or fetch at runtime.
3. Report the changes and recommend adopt or hold.
4. On approval, run `python3 ./scripts/refresh.py apply <commit-sha>`, then update
   `source-ref`, `reviewed`, `reviewed-by` and `review-due` (reviewed +
   `review-every-days`) in the frontmatter, and rebuild the library index.
5. If you hold the update, still update `reviewed` and `review-due` and say why.

## Checks

- The review is not overdue, or the person was told and chose how to proceed.
- Every guide named in the report exists in [INDEX.md](INDEX.md).
- No npx, `@latest` or upstream CLI command was run.
- Files under [guides/](guides/) were not edited by hand.

## Failure modes & recovery

| What went wrong | How to recover |
| --- | --- |
| No guide matches the task | Search [INDEX.md](INDEX.md) with the concrete UI noun (dialog, table, select); if still nothing fits, proceed without and say so. |
| A guide tells you to run `npx … retrieve` | Open the guide with that id from the index instead. |
| The review is overdue and nobody can be asked | Use the pinned copy and report that the review is overdue. |
| `refresh.py` cannot download | It uses the GitHub CLI (`gh`); sign in, or review on github.com and record the result. |
| Upstream adds telemetry, a runtime fetch or code to run | Hold the update and record why in the review notes. |

## Associated files

- [INDEX.md](INDEX.md): generated by `./scripts/refresh.py index`.
- [guides/](guides/): upstream guides at `source-ref`, unchanged.
- [LICENSE](LICENSE): the upstream Apache-2.0 licence.
- [scripts/refresh.py](scripts/refresh.py): rebuild the index, compare with upstream,
  apply a reviewed update. Downloads only markdown and the licence.
