# app-demo-video

A reusable skill for demo, promo, or launch videos of a working app (or of a pipeline / dataset that you first stand up as a small camera-ready frontend). The flair lives in the product; the edit is a reserved caption bar, punch-ins, and typographic title and end cards. No generative video, image, or TTS.

Start with `SKILL.md`. Styling tokens and the pre-record checklist are in `FRONTEND_STYLE.md`. An anonymized worked example of three cuts (overlay captions vs. a slide deck vs. a reserved bar on a live session) is in `REFERENCE_CASE.md`.

## Setup

Requires **ffmpeg** and Python 3.

```bash
python3 -m venv .venv && .venv/bin/pip install playwright pillow && .venv/bin/python -m playwright install chromium
```

Optional: drop a heavy italic grotesk (Geist Italic 900 is a good stand-in) in `./fonts`, or set `APP_DEMO_FONT` and `APP_DEMO_FONT_ITALIC`.

## Record and edit

1. Style the app with `theme.css` (and `tailwind-theme.css` if you use Tailwind v4). Follow the checklist in `FRONTEND_STYLE.md`.
2. Fill in `actions()` in `record_demo_template.py` for your UI, then:

```bash
.venv/bin/python ./record_demo_template.py --out demo_raw.webm
./edit_demo.sh --input demo_raw.webm --timeline example_timeline.json --output demo.mp4
```

The editor composites a 1920×900 take onto a 1920×1080 canvas with a reserved 180px caption bar, a ~2s title card, hard cuts, ~0.4s 1.3× punch-ins on the app pane, and a ~3s caveats end card. Target 60–70s, silent by default.

## Files

| File | Role |
| --- | --- |
| `SKILL.md` | When to use the skill, tokens, workflow, failure modes |
| `FRONTEND_STYLE.md` | Design tokens, motion, copy voice, pre-record checklist |
| `theme.css` | Drop-in CSS variables, aurora / glass / glow, keyframes |
| `tailwind-theme.css` | Tailwind v4 `@theme` snippet |
| `record_demo_template.py` | Parameterized Playwright recorder |
| `edit_demo.py` / `edit_demo.sh` | Title, captions, punch-ins, end card, encode |
| `example_timeline.json` | Beat list the editor reads |
| `REFERENCE_CASE.md` | Anonymized worked example and lessons from three cuts |
