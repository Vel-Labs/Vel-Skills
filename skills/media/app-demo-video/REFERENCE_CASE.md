# Reference case: a classifier web app demo

An anonymized worked example of three cuts of the same product demo. Figures below are **illustrative**, rounded for this write-up, and are not the original run metrics. The point is the structure and the lessons.

The product was a multi-pass classifier web app: upload a table of records, watch passes unlock, then land on a cost and confidence dashboard. No generative video, image, or TTS was used. The only model in the *content* was the classifier the app itself called. Recording was Playwright (headless Chrome) plus ffmpeg.

---

## What the three cuts were

| Cut | Length (approx.) | Picture | What it was |
| --- | --- | --- | --- |
| v1 | ~66s, 1440×900, 30 fps, H.264, no audio | Continuous screen recording of the real app | Replay of a real ~25-record run. In-page caption pills sat on top of the UI. No title card, no punch-ins, no reserved bar. |
| v2 | ~83s, 1920×1080, 30 fps, H.264, no audio | Motion typography + a 3-up collage of static app screenshots, reserved gold caption bar | A cost-story "deck." Same type system as v3, but the body was slides with ~1s crossfades. |
| v3 | ~68s, 1920×1080, 25 fps, H.264, silent AAC | Real app in a 1920×900 pane + 180px reserved caption bar, title card, punch-ins, end card | A **live** run of about 60 records, typography from v2 applied to a real session. |

v1 already felt like a real demo: the app performed (passes unlocking, toasts, ticking numbers) and the captions quoted measured figures. v3 kept that session and fixed the framing. v2 kept the typography and lost the session.

---

## Lesson 1 — v1: in-page captions cover the UI

v1 was a scripted Playwright take at 1440×900: landing, template download, upload, replay of a previously metered run, dashboard scroll. One ffmpeg transcode to H.264 (`libx264`, preset slow, CRF 22, yuv420p, 30 fps).

Captions were a fixed HTML pill near the bottom of the page. They were readable and punchy, but they covered buttons and later the charts. That is the failure mode this skill's reserved bar exists to prevent.

Illustrative dashboard figures for this cut (rounded): about 25 records in about 4s, on the order of $0.02 for the run, a fraction of a tenth of a cent per record, a couple of threat flags, linear projections at 1k and 10k records.

The "dramatic" part in v1 was mostly the app's own motion plus short caption lines. The later editorial layer (title card, reserved bar, punch-ins, end card) landed in v3.

---

## Lesson 2 — v2: collages and crossfades become a deck

v2 reused a 1920×1080 typographic system — reserved 180px bar, gold rule, cream italic headlines, tracked gold kickers — but the body was not a session:

- Title card and giant measured-number cards
- A **three-up collage** of static app screenshots labeled as a step-by-step process
- Editorial beats about threats caught and cost per record
- Volume-scenario cards and a caveats card
- About **1.0–1.2s crossfades** between slides
- No live pointer, no upload, no timeline unlocking in real time

The bar already said, in spirit, "captions stay here, never on the UI." The cut still felt like a slide deck because the app appeared as stills in a layout, not as something in use. Process walkthroughs belong in a separate deck.

---

## Lesson 3 — v3: reserved bar, punch-ins, hard cuts, live run

v3 recorded the **live** app (not a fixture replay) at a 1920×900 viewport, then composited a 180px bar underneath to make 1920×1080 at 25 fps (Playwright's native rate, not forced to 30). The UI was never cropped. A silent AAC track was muxed for player compatibility; there was no voice and no music.

Illustrative live-run figures (rounded, not the original digits): about 60 records, about 50 accounts, on the order of 10 seconds of wall clock, about $0.05 metered, about 10 API requests, high confidence, a handful of threat flags, some matches, many records with no approved match (work to do). Cost-per-item in the in-app panel was on the order of a couple of cents without a link and a couple of dimes with a link. Volume tiles used a clearly labeled monthly assumption plus two historically grounded totals.

### Approximate timeline

| Time | Beat | Transition |
| --- | --- | --- |
| 0–2s | Title card: a real demo, a live run, real records | Hard cut to the app at 2s |
| 2–8s | Landing, download the template | Caption: "Open the app. Download the CSV template." |
| 8–13.5s | File validated, record and account counts | Hard cut on the bar |
| 13.5–16s | Confirm the paid engine, ignite | "Live run on the real API. Confirm, then ignite." |
| 16–22s | Full-frame timeline firing | "Each pass's achievement lands in real time." plus wall clock and request count |
| 22–28s | Punch-ins on the threat gate and the match pass | **~0.4s zoom-in / zoom-out**; the caption bar stays fixed |
| 22s caption | "Threat shield up" plus the measured threat count | |
| 26s caption | Matches vs. gaps: "Work to do, mapped." | |
| 28–33s | Back to a full-frame timeline, run complete | |
| 33s | Hard cut; close on the threat callout | |
| 35s | ~0.4s move to the results dashboard | Mission-complete line: count, wall clock, metered total, per-record and per-account cost |
| 38–42s | Token / cost charts | "Metered, not estimated." |
| 42–50s | Sample verdicts (threat, match, gap) | "Caught a threat. Matched an approved reply. And a gap: no approved reply fits." |
| 50–58s | Jump to the **in-app** full-pipeline cost panel | "Now the app's full-pipeline cost panel — not a slide." then the per-item totals |
| 58–65s | Volume scenario cards in the app | Assumption vs. historically grounded volumes, labeled as such |
| 65–68s | Caveats end card | Hard cut; ~3s hold. Name the limits in plain language. |

Caption changes were **hard cuts**. Punch-ins were short (~10–12 frames at 25 fps) zoom/crop animations of the **app pane only**. Title and end were hard cuts, not the ~1s crossfades from v2.

Copy was loud in the verbs ("caught", "shield up", "work to do, mapped", "not a slide") and strict about digits: every figure was on the dashboard or in the run metrics, or was labeled as an assumption or a linear projection.

---

## What actually mattered

1. **The real app, used.** Upload, engine choice, a live or faithfully replayed run, the timeline unlocking, the dashboard. Not a collage of screenshots.
2. **Only real numbers.** Copy can be loud, but every figure comes from the run or from official list prices shown in the app.
3. **Pacing.** Short holds on landing and upload, then the run close to real time, then a guided scroll through results. About one minute.
4. **Captions that add a sentence, not a paragraph.** A kicker plus one or two short sentences, in their own bar so they never cover charts or buttons.
5. **Punch-ins** (~1.3×, ~0.4s) on the moment a pass unlocks (threat hits, match vs gap, the glowing total-cost tile).
6. **End on the full-workflow comparison in the app**, then a caveats card. Process walkthroughs belong in a separate deck.

The in-app system (aurora, glass, ticking counters, paced steps, achievement toasts, exact costs, an in-app cost panel) was already in v1. v3 pointed the camera at it and stopped covering it. v2 replaced that performance with slides.
