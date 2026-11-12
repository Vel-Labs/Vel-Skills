# Mobile first-time user

Motivation: complete the same useful outcome on a constrained connection and screen.

- Use a verified 375 CSS pixel viewport unless the run specifies another size.
- Apply slow-network conditions only through supported controls. Record latency
  and throughput values and whether they apply; never infer throttling from delay.
- Inspect overflow, clipped content, obstructing dialogs, usable control sizes,
  loading feedback, retries, and preservation of entered work after interruptions.
- Use touch, virtual keyboard, and mobile-browser behavior only when the actual
  environment supports them; label desktop responsive emulation accurately.
- If throttling is unavailable, continue responsive testing and mark network
  coverage unverified. Do not call the combined mobile scenario fully passed.

Use [the shared evidence format](../evidence.md). Capture the complete viewport
at obstacles and first success, with the applied conditions in the journey record.
