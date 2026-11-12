# Frontend dramatic framing

Style the product as if it will be filmed. A reserved caption bar cannot invent motion, typography, or copy the UI does not already have.

Drop `theme.css` into the app (or merge `tailwind-theme.css` if you use Tailwind v4). Load Inter and JetBrains Mono; naming them in a theme is not enough.

## Why the UI has to perform

The edit is a reserved bar, short punch-ins, a title card, and an end card. The body of the video is the app. If numbers pop on, if a run is a spinner, if the landing page reads like a settings form, the cut will still feel like a recording of a dashboard, not a trailer. Build the flair into the product, then point the camera at it.

## Tokens

```
ink-950  #05060A   page
ink-900  #0A0C14
ink-800  #11131F   panels, menu
ink-700  #1A1D2E   wells, chips
ink-600  #25283A   borders
ink-500  #32364A   muted borders
ink-400  #4A4E66
ink-300  #8B90A8   muted copy
ink-200  #C5C8D6
ink-100  #E5E7F0   body
ink-50   #F4F5F8

cyan-400 #22D3EE   in-scope, live, progress
cyan-300 #67E8F9   glow / highlight
violet   #A855F7   paid or heavy engine
violet-300 #A78BFA
fuchsia  #E879F9 / #F0ABFC
emerald  #10B981   match, complete, money-in
rose     #F43F5E   threat, hard stop
amber    #F59E0B   gap, assumption, unapproved
gold     #FBBF24   achievement burst, warning icon
```

Background: `#05060A` plus a **static aurora** (violet ~16% at 18% 12%, fuchsia 10% at 82% 8%, cyan 8% at 50% 100%) and a 48px grid at 3.5% white that fades after ~560px. Cards are **glass**: `rgba(17,19,31,0.78)` (or 0.88 for dense panels) with `backdrop-filter: blur(16–20px)`, a 1px `rgba(255,255,255,0.06)` border, and `0 0 0 1px rgba(0,0,0,0.4)` inset. Sidebar can be slightly more opaque, with a cyan 4px active rail.

Semantic glow: a 14–18px colored shadow + a 1px inset highlight in the same family (cyan in-scope, rose threat, emerald match, amber gap or assumption, violet paid engine, gold for a burst).

Type: Inter for UI, JetBrains Mono for clocks, event feeds, and codes. Tabular numbers everywhere a figure will tick. Hero about 48–60px `font-black tracking-tight leading-none`. One word of the hero in a text gradient `#67E8F9 → #A78BFA → #F0ABFC`. Kickers 11–13px uppercase, tracking 0.14–0.25em, weight 700–800, often cyan. Eyebrows 10px, tracking 0.2em, ink-400.

Mark: a compact monogram or glyph in a rounded square with a soft aurora behind it, 4px radius.

## Motion

One easing everywhere motion should feel expensive: `cubic-bezier(0.16, 1, 0.3, 1)`.

| Beat | Timing |
| --- | --- |
| Shared tween | 0.45s (0.28s for leaves) |
| Count-up (default / KPI / projection) | 1.1s / 1.6s / 1.8s, digits from the previous value |
| Active-step pulse (opacity + border) | 1.4s infinite alternate |
| Expanding ring on the active step | 1.3s infinite |
| CTA / step shimmer sweep | 1.6s linear infinite |
| Check-in + particle burst | spring ~0.45s, burst 0.55s |
| Achievement toast in / out | ~0.5s / ~0.4s, hold ~1.7s |
| Pipeline fade-up | 0.5s, items stagger 0.08s from 16px |
| Dashboard hero scale-in | 0.6s from 0.96, 12px rise |
| Auto-scroll to results | 0.8s smooth, starts ~900ms after the run completes |
| Event-feed row | 0.3s, 8px rise |

Do not wait on the server to "feel fast." Queue incoming events and release them on a readable cadence (about 450ms after a step starts, 1500ms after a step ends, 300ms when the payload is a batch of results, 120ms for progress ticks). Durations, token counts, and costs stay exactly what the backend reported; only when they appear is delayed.

## Component patterns

- **Header:** logo + wordmark, a monospace clock, a compact **read-only / safety** chip (the product does not write back to the source). Engine and status sit in a right cluster.
- **Landing hero:** kicker, then a 3–6 word headline with one gradient word, then a subhead that promises what the viewer will watch unlock. A two-file drop zone with a dashed, hovering glow. A primary CTA in a cyan-fuchsia vertical gradient, shimmer, and cyan glow (`Ignite the pipeline` for a live run, `Play the recorded run` for a replay).
- **Confirm step:** if a paid engine is about to run, show a pricing callout before the same CTA. Link to official pricing; do not invent a rate.
- **Stepper:** vertical rail, index glyph, Title Case step name, optional subtitle, a trailing achievement with a gold star after it lands. The active row pulses; completed rows get a spring check and a particle burst.
- **Live column:** a "live pulse" kicker, a monospace timer, a scrolling event feed. Cyan / rose / emerald / amber by event kind.
- **Dashboard:** a results hero ("N records. Mission complete.") and a four-tile KPI row (count, time, cost, confidence). Confidence can be a ring. Then charts, then a sample of tagged records, then projections.
- **Toasts:** fixed bottom-center, gold star, Title Case achievement, ~1.7s hold, stacked.
- **Cost / value panel:** this is part of the product, not a video-only slide. Exact metered numbers (enough fraction digits that a sub-cent figure does not become $0.00). Color: emerald for a complete total, violet for a paid engine, amber for an assumption or an unapproved item. Each modeling assumption is named on the tile. A caveats block in the page is what the end card will echo.
- **Replay / retake URLs:** `?replay=<id>` auto-starts a previously metered run (optional `?speed=`); `?run=<id>` reopens a finished run for a dashboard retake without re-billing. The UI must say when it is a replay.

## Copy (voice, plus illustrative examples)

Write like a trailer, then prove it with digits.

**Hero.** One short metaphor, one gradient word, one promise of what will unlock.

> Turn the feed into **signal**.
>
> Watch every pass unlock — then land on cost, confidence, and the gaps that still need work.

**CTAs.** Ignition for a live run, playback for a replay: `Ignite the pipeline`, `Play the recorded run`, `Re-run on the live engine`.

**Achievements.** Two or three words, Title Case, toasted and then starred on the step. Illustrative set:

- Data Locked In
- Knowledge Base Armed
- Signal From Noise
- Threat Shield Up
- Answers Aligned
- Gaps Mapped
- Drafts Staged
- Mission Complete

**Safety and scope.** A header chip that the tool is read-only. In-scope vs out-of-scope, stated in the UI. Unapproved output is tagged, not silently shown as ready to send.

**Threat and work.** Threats have a named shield (`Threat Shield Up`). Gaps are work to do, not a failure (`Gaps Mapped`, "Work to do, mapped.").

**Costs.** "Metered, not estimated." "These tiles are the same product, not a slide." Assumptions labeled (`assuming N items / month`).

Do not write the hero or the CTA like a settings page ("Upload a CSV", "Start job") unless a second line immediately supplies the metaphor and the stakes.

## Pre-record checklist

- [ ] Inter + JetBrains Mono actually load (network tab or computed style)
- [ ] 1920×900 still reads: hero, stepper, dashboard tiles, cost panel
- [ ] Landing has a kicker, a gradient word, an ignition CTA, a two-file drop zone
- [ ] Paid engines confirm before they spend
- [ ] Steps have a title, a 2–3 word achievement, a pulse, a check, a toast
- [ ] Counts tick; they do not pop
- [ ] Event feed is paced so a pass can be read and punched-in
- [ ] Results auto-scroll after a short beat, with a scale-in hero
- [ ] Dashboard shows count, wall time, exact cost, confidence
- [ ] An in-app full-workflow cost / value panel exists, with named assumptions and caveats
- [ ] `?replay=` and `?run=` deep links work, and replay is labeled
- [ ] No on-page caption overlay; captions will live in the reserved bar
- [ ] Safety / read-only language is visible in the header

If the "app" is still a notebook, a CLI, or a spreadsheet, build this UI around the real data first, then record it. Do not start in a slide deck.
