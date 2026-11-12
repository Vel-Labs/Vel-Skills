# Codex CUA

Use `mcp__cua_repl` when it is exposed to the executing agent. Read its current
tool instructions and the runtime documentation returned at initialization.
Use the documented entry point for the user's selected browser, tab, or app.
Do not copy guessed API methods from this skill or another host.

Discover capabilities using documented APIs only. Check session/storage isolation,
viewport control, network throttling, screenshot handling, and input-focus sharing
before promising them. Do not assume a subagent inherits a parent's live REPL
variables or an independently controlled browser. Supply its assigned surface
identifier only when the tool supports that handoff.

Opening a URL through an app navigation tool does not itself operate or test the
page. Use actual interaction and inspect the resulting UI. Codex-provided CUA
availability also does not establish that the same server is connectable from
Claude Code or another host; that integration requires separate verification.

If browser contexts or independent desktops cannot be established, use sequential
journeys with supported fresh-session handling and disclose remaining shared state.
Do not clear the user's existing browser data to manufacture a clean session.
