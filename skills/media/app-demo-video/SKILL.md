---
name: app-demo-video
description: Use when making a demo, promo, or launch video of a working app, prototype, pipeline, or dataset with real data and dramatic, click-baity framing, including when the content has no UI yet and should be stood up as a camera-ready frontend first, or when a past cut felt like a slide deck or had captions covering the UI.
---

# App demo video

## Core idea

The flair lives in the app. Build a dark, cinematic UI that ticks, pulses, and announces real results; then record that UI; then add a reserved caption bar, punch-ins, and typographic title and end cards in the edit.

If the content is not an app yet — a pipeline, a scored dataset, a cost model, a CLI — stand it up first as a small camera-ready frontend (see `FRONTEND_STYLE.md` and `theme.css`). Do not jump straight to typographic slides or a video model.

Do not generate the demo with a video-generation model, an image-generation model, or TTS. Title and end cards are typography. The default picture is silent; do not add stock music or a voice unless the brief asks for sound.

A worked, anonymized example of three cuts (overlay captions vs. a slide deck vs. a reserved bar on a live session) is in `REFERENCE_CASE.md`.

## Assets

All paths are relative to this skill folder.

- `FRONTEND_STYLE.md` — design tokens, component patterns, copy voice, motion specs, pre-record checklist
- `theme.css` — drop-in CSS variables, aurora / glass / glow, keyframes
- `tailwind-theme.css` — Tailwind v4 `@theme` snippet
- `./record_demo_template.py` — parameterized Playwright recorder
- `./edit_demo.py` / `./edit_demo.sh` — title, captions, punch-ins, end card, encode
- `example_timeline.json` — beat list the editor reads
- `REFERENCE_CASE.md` — anonymized worked example and the lessons from three cuts

## Visual style (quick ref)

In-app theme (also in `FRONTEND_STYLE.md` and `theme.css`):

| Role | Hex |
| --- | --- |
| Page ink | `#05060A` / `#0A0C14` / `#11131F` / `#1A1D2E` |
| Body text | `#E5E7F0` |
| Cyan (in-scope / live) | `#22D3EE` / `#67E8F9` |
| Violet (heavy or paid engine) | `#A855F7` / `#A78BFA` |
| Fuchsia (gradient end) | `#F0ABFC` |
| Emerald (match / complete / totals) | `#10B981` |
| Rose (threat / hard stop) | `#F43F5E` |
| Amber (gap, assumption, unapproved) | `#F59E0B` |
| Gold (achievement burst) | `#FBBF24` |

Aurora wash, fading 48px grid, glass cards, color-coded glows. Inter for UI, JetBrains Mono for clocks and feeds, tabular numbers. Load the fonts; naming them in a theme is not enough (`theme.css` includes the import). Hero is `font-black tracking-tight` at about 48–60px, with one word in a `#67E8F9 → #A78BFA → #F0ABFC` text gradient. Kickers are 11–13px uppercase at 0.14–0.25em.

Caption-bar / title-card theme (the edit layer, not the app):

| Role | Hex |
| --- | --- |
| Background | `#08070C` |
| Gold rule / kicker | `#E1A01D` |
| Headline | `#F3ECE3` |
| Subtext | `#9A958C` |

Headline type in the editor is a heavy italic grotesk. `./edit_demo.py` will use `./fonts`, or `APP_DEMO_FONT` / `APP_DEMO_FONT_ITALIC`, or a system DejaVu / Liberation face. Geist Italic 900 is a good stand-in if you have it.

## Motion

Shared easing: `cubic-bezier(0.16, 1, 0.3, 1)`. Counters tick from the previous value (1.1s default, 1.6s on KPI tiles, 1.8s on projections). Active steps pulse (1.4s) with an expanding ring (1.3s). Completion is a spring check plus a particle burst. An achievement toast holds about 1.7s. The CTA and the active step shimmer (1.6s loop).

Pace incoming events so each pass is readable (about 1.5s after a step ends). Server times and counts stay real; only when they appear is delayed. After the run finishes, wait about 900ms, then smooth-scroll to a scale-in results hero.

## Copy voice

Write like a trailer, then prove it with digits.

- Hero: one short metaphor, one gradient word. The subhead says what the viewer will *watch* unlock, then that they will land on a cost and confidence readout.
- Live CTA: a verb of ignition. Replay CTA: a verb of playback.
- Each step has a concrete title and a 2–3 word Title Case achievement, toasted on complete and starred on the row.
- Gaps are work, not failures. Threats have a named shield. Unapproved output is tagged in the UI. A safety / read-only line stays in the header.
- Costs are exact (enough fraction digits that a sub-cent figure does not become $0.00) and labeled metered vs estimate. Assumptions are named on the tile.
- The full-workflow cost or value comparison, and its caveats, live in the product so the camera can scroll to them.

## Demo UX

- `?replay=<id>` (optional `?speed=`) auto-starts a previously metered run at its real timings, and the UI says it is a replay.
- `?run=<id>` (optional `?backend=`) reopens a finished run for dashboard retakes without re-billing.
- Live path: upload or connect real data → confirm a paid engine if needed → ignite → paced timeline + request feed → dashboard, projections, cost panel, caveats.

## Workflow

1. **Style the frontend for camera.** If there is no UI yet, stand one up. Apply `theme.css` (and `tailwind-theme.css` if the app uses Tailwind v4). Follow the checklist in `FRONTEND_STYLE.md`.
2. **Lock the real data.** Use a live run or a faithful replay fixture. Every later caption must be able to quote a figure that appears on screen or in the run's own metrics.
3. **Record with Playwright** at **1920×900**. No on-page caption pills — those cover the UI. Script a continuous take (landing → workflow → results) with 2–4s holds and a slow scroll. Use `./record_demo_template.py`. Keep Playwright's native frame rate (often 25 fps).
4. **Edit** with `./edit_demo.sh`. Canvas is 1920×1080: a 1920×900 app pane over a reserved **180px** bar (`#08070C` / `#E1A01D` / `#F3ECE3` / `#9A958C`). About **2s** title card, **hard cuts** (not 1s crossfades), **~0.4s 1.3× punch-ins** on the app pane only (bar stays fixed). End on the **in-app** cost or value comparison, then a **~3s** caveats card. Target **60–70s**. Silent by default (a quiet AAC track is fine for player compatibility).
5. **Verify frames.** Confirm the bar never covers the UI, punch-ins do not clip the bar, and every captioned figure is on screen or labeled as an assumption.
6. **Process walkthroughs belong in a separate deck.** Architecture, how-it-works, and takeaway cards do not replace the session in this video.

## Caption voice

- Kicker: a few tracked-out uppercase words (`LIVE SESSION`, `MISSION COMPLETE`, `THE CATCH`).
- Headline: one or two short sentences. Period, not ellipsis.
- Put the surprising measured fact first: counts, time, cost, what was caught.
- Point at what is on screen now, then add the takeaway. Do not narrate a tutorial.
- When you cut to an in-app cost panel, say that it is the app's own panel, not a slide.

## Failure modes

| Mistake | Fix |
| --- | --- |
| In-page HTML/CSS caption overlay | Reserved bar under the app, always |
| Screenshot collage or typographic "process" slides as the body | Record the session; move process cards to a deck |
| Crossfades between every beat | Hard cuts; reserve motion for punch-ins and the app itself |
| Invented or rounded-without-label figures | Copy the run's digits; label assumptions |
| Punch-in zooms the whole 1080p frame and clips the bar | Zoom the 1920×900 pane only |
| Ending on architecture or a how-it-works graphic | End on the product's cost/value comparison, then caveats |
| Generating a "demo" with a video model | Playwright + ffmpeg only |
| Voiceover or music added "to make it cinematic" | Default is silent; the picture and captions carry it |
| Flat UI, numbers popping on, no in-app cost panel | Style the app first (`FRONTEND_STYLE.md`); do not try to fix it only in the edit |
| Hero or CTA written like a settings page | Metaphor + gradient word; ignition verb for live, playback verb for replay |
| Fonts named in CSS but never loaded | Add the Inter + JetBrains Mono import from `theme.css` |
| Dataset or CLI recorded as slides because "there is no app" | Stand up a small frontend for flair first, then record it |

## Quick start

Requires **ffmpeg** and Python 3.

```bash
python3 -m venv .venv && .venv/bin/pip install playwright pillow && .venv/bin/python -m playwright install chromium

# 1. Style the app (theme.css / FRONTEND_STYLE.md) so it performs on camera.
# 2. After the app is running and actions() in the recorder has been filled in:
.venv/bin/python ./record_demo_template.py --out demo_raw.webm
./edit_demo.sh --input demo_raw.webm --timeline example_timeline.json --output demo.mp4
```

Optional: put Geist (or another heavy italic grotesk) under `./fonts`, or set `APP_DEMO_FONT` and `APP_DEMO_FONT_ITALIC`.

## Purpose

Make a dramatic demo, promo, or launch video of a working app from a real session. Style a camera-ready frontend, record it with Playwright, and composite a reserved caption bar, punch-ins, and typographic title and end cards with ffmpeg. A pipeline, dataset, cost model, or CLI is stood up as that frontend first.

## Inputs

- A running app at the recorder base URL (`--base`, default `http://127.0.0.1:8765` in `record_demo_template.py`), or a small frontend built for the recording.
- Real data, or a faithful replay of a previously metered run. Captioned figures come from the screen or the run's metrics, or are labeled as assumptions.
- `actions()` filled in inside `record_demo_template.py`.
- A timeline JSON shaped like `example_timeline.json`.
- ffmpeg, Python 3, `playwright`, and `pillow`. Optional italic grotesk in `./fonts`, or `APP_DEMO_FONT` and `APP_DEMO_FONT_ITALIC`.
- `theme.css`, `tailwind-theme.css` when the app uses Tailwind v4, and the checklist in `FRONTEND_STYLE.md`.

## Outputs

- Raw take from `record_demo_template.py` (`.webm`, or `.mp4` with `--transcode`).
- Edited file from `edit_demo.sh`: 1920×1080 H.264, usually 60–70s, silent AAC. A 1920×900 app pane sits over a 180px caption bar, with an ~2s title card, hard cuts, ~0.4s 1.3× punch-ins on the app pane, and an ~3s caveats end card.

## Non-goals

- Video-generation models, image-generation models, and TTS.
- Stock music or a voice unless the brief asks for sound.
- In-page caption overlays, screenshot collages, and crossfaded process slides as the body.
- Invented figures, or rounded figures that are not labeled.
- Using an architecture or how-it-works deck in place of the session.

## Checks

- `FRONTEND_STYLE.md` pre-record checklist passes, including loaded Inter and JetBrains Mono and a readable 1920×900 frame.
- The reserved bar never covers the UI. Punch-ins move only the 1920×900 pane, so the bar stays full width and unclipped.
- Each captioned figure is on screen or in the run metrics, or both the caption and the end card call it an assumption or a projection.
- Cuts are hard cuts, length is about 60–70s, and the track is silent apart from the quiet AAC the editor muxes.
- `bash -n edit_demo.sh` and `python3 -m py_compile` on `edit_demo.py` and `record_demo_template.py` both succeed.

## Failure modes & recovery

Use the **Failure modes** table above. Recovery:

| What you see | What to do |
| --- | --- |
| Captions cover buttons or charts | Delete the in-page overlay. Put the line in the timeline and rerun `./edit_demo.sh`. |
| The body is stills, a collage, or crossfades | Record the session with `./record_demo_template.py` and hard-cut between beats. |
| A punch-in clips the bar | Keep `zoom` on the beat. `edit_demo.py` scales the app pane only. |
| A caption number is not on screen | Copy the dashboard or run-metric digit, or label the assumption on the tile and the end card. |
| Flat UI, numbers that pop, or no cost panel | Restyle from `theme.css` and `FRONTEND_STYLE.md`, then record again. |
| The editor exits because it cannot find a font | Add a `.ttf` under `./fonts`, or set `APP_DEMO_FONT` and `APP_DEMO_FONT_ITALIC`, then rerun `./edit_demo.sh`. |
| The source is a notebook, CLI, or spreadsheet | Build the small frontend in `FRONTEND_STYLE.md` around the real data, then record it. |
