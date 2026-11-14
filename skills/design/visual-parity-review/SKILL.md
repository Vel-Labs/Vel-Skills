---
name: visual-parity-review
description: Use before calling any person-facing screen, page or visual deliverable "done", "built to the design" or "matching the mockup". Captures the reference and the build side by side at the same size, data, theme and state, lists every gap, fixes them, and applies the design operating principles in this skill. Use it for every screen package, every redesign, and any claim that something "looks right".
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-11-14"
  reviewed: "2026-11-14"
  reviewed-by: Claude Code (Opus 5.5)
  review-every-days: "90"
  review-due: "2027-02-12"
  notes: Born from a screen package reported as "built to the mockups" without a visual comparison. Includes the design principles that review produced (depth, both appearances, no invented values, phone-first).
---

# Visual Parity Review

## Purpose

Make "it matches the design" something a person can see, not take on trust. For
every screen the person gets the approved reference and the build next to each
other, in the theme and appearance they will actually use, with a written list of
gaps. Each gap is fixed or recorded as a deliberate deviation with a reason.

"Built to the mockups" is a visual claim. Tests, structure and region names do not
prove it. Until a side-by-side review passes, say "follows the structure of the
mockups; not yet compared visually", and do not report the work as done.

## Inputs

- The approved references: mockups, a design canvas, prior screenshots or a brand
  page, with each one's size (board or viewport), state and data.
- The running build, with the same demo or fixture data.
- The user's default theme and appearance, and any theme limits.
- [scripts/capture.mjs](scripts/capture.mjs) and
  [scripts/side_by_side.py](scripts/side_by_side.py).

## Outputs

- One comparison image per screen: reference, build in dark, build in light.
- A gap table: screen · region · reference · build · severity · fix or deliberate
  deviation (with reason).
- The fixes, and the comparison published to the person.

## Non-goals

- Replacing functional tests, accessibility scans or code review.
- Changing an approved reference design, or publishing or deploying anything.
- Building web components correctly; use `web/modern-web-guidance` for that.

## Design operating principles

Apply these to every person-facing deliverable, with or without a reference.

1. **Compare what the person will see.** Capture the default theme, appearance,
   brand and allow-list the real user gets, not the theme the designer used. If
   the two differ (for example, a client allow-list excludes the mockup's theme),
   that difference is the first gap to report.
2. **Every appearance gets the same craft.** Light is not dark with the colours
   turned off. Both carry depth (layered surfaces, soft shadows or glows),
   saturated accents, background atmosphere and the same motion. A flat grey
   light mode is a defect.
3. **Fills and text are different tokens.** Saturated colours colour bars, dots,
   edges, tints and glows. Text uses ink or status tokens with checked contrast.
   A brand colour validated only against white never colours text.
4. **Headline, then detail.** Show one glanceable value per item ("2 approvers",
   "$100 a month", "4 pages"), with one plain sentence under it. Never print a
   raw structure, and never let a table clip mid-row.
5. **No invented values.** Every number, threshold, status chip and time target
   on screen comes from a named source. A label nothing computes ("Normal",
   "15 min") is removed or marked as a sample.
6. **States must look different.** Done, next, to do, selected, urgent, disabled
   and sample each have a distinct, consistent treatment. The next action is a
   link, not a label.
7. **Phone is designed, not wrapped.** The first phone screen shows the content
   that matters. Chrome (switchers, settings, customise) compresses to one row or
   moves behind a control. No horizontal page scroll at 375 or 390 px.
8. **Geometry is fixed.** Cards in a row share a height, nothing reflows when
   data arrives, and no text is clipped by a fixed box. Text either fits or
   truncates with an ellipsis and a full value one step away.
9. **Watch for framework collisions.** A component class that shares a name
   with a utility framework class (Tailwind `ring`, `block`, `shadow` and so on)
   picks up stray styles. Prefix component classes.
10. **Spacing follows the reference.** Title-to-subtitle gaps, panel radii and
    row heights are compared and matched, not eyeballed.
11. **Depth and response make it feel valuable.** Brand, marketing and social
    teams judge by look and feel as much as by data. Give panels raised
    elevation off the page, set items inside them slightly recessed, and let
    interactive items lift, glow or highlight under the pointer. Add press
    feedback and an indicator on the current navigation item. Never fade
    content in on page open: text must be readable (and pass contrast) from
    the first frame. Keep it subtle, define it as tokens so every appearance
    gets it, respect reduced motion, and switch it off in High Contrast. A
    flat page with correct data still reads as low value.
12. **Appearance is personal.** Never restrict someone's theme, light/dark or
    contrast choice by client policy. A client sets the default, and people
    choose what they like or need.

## Workflow

1. **Inventory.** List each reference with its size (board or viewport), state
   (for example mid-run, selected stream, modal open) and data. Find the user's
   default theme and appearance, and any allow-list.
2. **Render the references.** Open them at their own size. If a reference needs a
   runtime (a design canvas, a component bundle), fetch that runtime and serve
   the files locally. Do not approximate a reference from its source text.
3. **Capture the build.** Use the same viewport, data, state and the user's
   default theme. Capture every appearance the product offers (light and dark at
   least) and phone width.
4. **Compose and review.** Put reference and build images side by side
   (`./scripts/side_by_side.py`; capture with `./scripts/capture.mjs`). Review region by region using the checklist
   below. Write a gap table: screen · region · reference · build · severity ·
   fix or deliberate deviation (with reason).
5. **Fix.** Fix gaps you own in the source of truth (tokens before components,
   components before screens). Record deliberate deviations where the project
   records decisions.
6. **Recapture and re-review.** Repeat steps 3 to 5 until the gap table holds
   only accepted deviations. Then run the project's contrast, overflow and
   accessibility checks in every theme.
7. **Show it.** Publish the side-by-side images with the gap table to the
   person, not only build screenshots. Say plainly what matches, what is a
   deliberate deviation, and what remains.

## Checks

- Background atmosphere, panel surface, edge and shadow match in each appearance.
- Accent and status colours are as saturated as the reference; tints are visible.
- Type: heading face, size and weight; numbers tabular; title-to-subtitle spacing.
- Every region in the reference exists, in the same order, with the same emphasis.
- Values are headlines with a plain line, never clipped structures.
- State treatments (done, next, selected, urgent, sample, disabled) are distinct.
- Nothing is invented; each value has a source.
- Phone: the first screen shows content; no horizontal scroll; tap targets at least 40 px.
- No stray outlines, double borders or framework-class collisions.
- Motion: real events animate in every appearance; reduced motion is respected.
- Depth: panels raised, inner items recessed, hover lift and glow, press feedback,
  active navigation indicator; captured at least one hover state per screen.

## Failure modes & recovery

| What went wrong | How to recover |
| --- | --- |
| The reference needs a runtime that is not in the repo | Fetch the runtime the reference was made with (for example the design canvas's bundle) and serve it locally; never approximate the reference from its source text. |
| The build only looks right in the designer's theme | Compare in the user's default theme and report the theme difference as the first gap. |
| A visual fix breaks contrast or overflow checks | Fix it at the token level, then rerun the project's checks in every theme. |
| An entrance animation fails accessibility scans | Do not fade content in on page open; animate only real events. |
| Fixed card heights clip content | Summarise the value as a headline, then pin each part's size so nothing shrinks. |

## Associated files

- [scripts/capture.mjs](scripts/capture.mjs): captures pages at given sizes and
  colour schemes with Playwright, resolved from the project you run it in.
- [scripts/side_by_side.py](scripts/side_by_side.py): composes reference and build
  images into one labelled comparison per screen (requires Pillow).
