# Breaker

Motivation: reach first success despite ordinary input mistakes and interrupted actions.

- Use disposable authorized test data. Try empty/whitespace input, malformed values,
  Unicode, and a modest over-limit value where a limit is visible or documented.
- Check double submission, back/refresh mid-flow, and returning to incomplete work.
- Exercise bounded mistakes and recovery through the UI; do not run security
  exploits, floods, large payloads, or destructive actions outside the run contract.
- Check whether feedback explains recovery, inputs survive appropriately, and
  repeated actions create unintended duplicates or contradictory state.
- After a recoverable error, return to valid input and attempt first success.
- Stop the affected action if unexpected data loss or consequential effects appear;
  retain evidence without repeating the harmful trigger.

Use [the shared evidence format](../evidence.md). Record input class, repeat count,
state before/after, and recovery. Do not count repetitions as additional users.
