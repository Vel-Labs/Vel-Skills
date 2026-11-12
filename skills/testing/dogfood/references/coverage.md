# Shared coverage

Select checks relevant to the target journey and existing project requirements.
Record applicability and actual results; this is not a universal compliance audit.

- Keyboard traversal, visible focus, actionable names, and completing core actions
  without a pointer. Claim screen-reader coverage only when actually exercised.
- Loading, empty, validation-error, and service-error states; discoverable recovery.
- Refresh/back/forward navigation and resuming an interrupted flow.
- Saved-state persistence after reload and a fresh authorized session where useful.
- Authentication boundaries and session expiry when safely reproducible.
- Responsive layout and required browser coverage, including dialogs and keyboards
  where the available device or emulator genuinely supports them.
- Repeated submissions and accidental duplicate actions using disposable data.

Use authorized local/test fixtures for error injection. Do not disrupt production
services to manufacture failure states. Keep technical boundary checks separate
from persona observations and state when a condition could not be exercised.
