# Browser execution

Select a host-supported tool that can operate the real application. Prefer Codex
CUA when available in Codex; read [drivers/codex-cua.md](drivers/codex-cua.md).
For another supported browser automation environment, read
[drivers/playwright.md](drivers/playwright.md). Honor explicit user tool choices
and host tool restrictions. These files describe execution choices, not tools
that the skill installs or provisions.

Before dispatch, verify in the actual worker environment:

- Target access, navigation, visible controls, screenshot capture and inspection.
- Session/account isolation and whether input focus or a desktop is shared.
- Requested viewport and network controls, including whether they actually apply.
- Evidence output handling and how each worker refers to its assigned surface.

Tool presence alone does not establish these capabilities. Record the driver,
browser, and verified conditions. A model must be able to inspect the evidence
required for its assignment; do not silently label text-only inspection visual QA.

Use visible UI and accessibility information to navigate. Do not read hidden
application state, source internals, or private endpoints to solve a persona's
journey. DOM-backed interaction with visible controls is acceptable; arbitrary
script injection that bypasses the user flow is not. Keep technical diagnosis
outside the independent observation pass.

Separate tabs do not establish isolated storage or accounts. Independent browser
contexts also do not isolate shared backend test data. Allocate distinct test data
when actions could interfere. Concurrent native desktop control requires separate
desktops; otherwise serialize interaction. Respect exclusive tool/session ownership.

If a required capability is missing, use an available permitted alternative or
mark only that condition unverified and continue useful authorized work. Do not
install software, connect an MCP server, or route through an unsupported interface
solely because this skill mentions it. Instructions cannot grant tool access.
