---
name: modern-web-guidance
description: Apply pinned Chrome guidance to web UI changes and verify the affected interaction in a real browser, including dialog focus, motion, color scheme, or layout stability.
license: Apache-2.0 for the guides (see LICENSE); the wrapper is part of Vel-Skills.
metadata:
  origin: adapted
  source: https://github.com/GoogleChrome/modern-web-guidance
  source-ref: 4dd968349e54ca45a05dd5c818fb035c9054b022 (Release v1.0.0, 2026-11-10)
  verification-source: https://github.com/vercel-labs/agent-browser
  verification-ref: 25b5d76f2843bce7be6c59a56d3461b162ad4ac9
  created: "2026-11-14"
  reviewed: "2026-11-19"
  reviewed-by: Codex (GPT-6), extending the Claude Code review
  review-every-days: "14"
  review-due: "2026-12-03"
  notes: Pinned Chrome guides and browser checks adapted from Vercel Labs. Runtime npx downloads and guide-search telemetry are omitted.
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
- Record the guide ID, browser state, observed result, and any untested behavior.

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
4. For a regression, reproduce it before editing when feasible. Open the built UI
   through its normal entry point in an available browser. Use the project’s
   existing harness or an installed agent-browser. Pick the check that exercises
   the changed behavior.

   | Behavior | Observe in the browser |
   | --- | --- |
   | Modal focus | Open with the keyboard. Confirm initial focus, tab containment, Escape dismissal and focus return to the opener. |
   | Reduced motion | Trigger the same interaction under both motion preferences. Inspect the affected element’s animation or transition while it runs. |
   | Color scheme | Switch the browser preference and check computed foreground and background on the actual control in each theme. |
   | Layout shift | Reproduce the load or interaction at the same viewport. Capture layout-shift entries and identify which element moved. |

5. Report the observation with its guide. State which behavior remains unverified
   if the browser or target state is unavailable. Restore emulated settings.

Browser verification adapts the Apache-2.0 [Vercel Labs workflow](https://github.com/vercel-labs/agent-browser/blob/25b5d76f2843bce7be6c59a56d3461b162ad4ac9/skill-data/modern-web-guidance/SKILL.md).
The maintained local guide snapshot and project browser tooling supply its inputs.

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
