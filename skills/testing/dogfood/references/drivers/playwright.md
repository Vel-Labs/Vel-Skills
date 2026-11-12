# Supported browser automation

Use an already available, host-permitted Playwright interface or equivalent
browser driver. Follow its current tool documentation and applicable browser skill
when required by the host. This reference does not authorize bypassing a mandated
CUA interface or installing a new dependency.

Use separate browser contexts and distinct test accounts/data where available.
Verify viewport and network controls through the supported interface. A 375 CSS
pixel viewport is responsive coverage; it does not establish physical-phone,
mobile-browser, touch-keyboard, or slow-network coverage by itself. Record actual
latency/throughput settings rather than relying only on a preset name.

Navigate rendered controls using visible text, roles, and accessible names. Inspect
screenshots at obstacles and first success. Keep direct API calls, page-state
inspection, and source diagnostics out of the persona journey. Do not seed the
desired final state as a substitute for completing the flow.

Use existing project regression infrastructure for deterministic replays when
appropriate. Keep those results distinct from fresh exploratory journeys.
