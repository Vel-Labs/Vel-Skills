# Evidence and findings

Each tester returns a compact journey record: persona, build, verified runtime
conditions, entry point, actions, final state, and completed/abandoned/blocked
outcome. Record deviations from the brief and which relevant steps were reached.

For each finding, record:

- Stable finding ID and concise description of the observed obstacle.
- Intended action, UI evidence that established the expectation, and actual result.
- Minimal reproduction steps, URL/screen, and necessary test-state preconditions.
- Screenshot at the obstacle and additional evidence needed to demonstrate it.
- Whether the tester recovered, abandoned, or could not proceed; include how.
- Observed consequence, suspected cause separately, and any uncertainty.

Capture the first success state as well as failures. Screenshots support a claim;
they do not by themselves prove persistence, delivery, or a backend operation.
If capture is unavailable, record the gap rather than invent a path or screenshot.
Avoid exposing credentials, tokens, or unrelated personal content in captures.
Preserve evidence relevant to the task without collecting unrelated user data.

Do not invent frustration, satisfaction, elapsed time, or comprehension. Report
what the agent did and what the interface required. A perceived ambiguity is an
interpretation supported by quoted UI text or a screenshot, not a measured human
reaction. Feature preferences are not automatically defects.

## Consolidation

Preserve observation IDs when merging. Merge only when evidence supports a common
cause; similar symptoms may need separate findings until diagnosis. For each
merged issue count unique affected personas out of personas exposed to that
condition. Mark unknown exposure explicitly. Never count an upstream-blocked
persona as a downstream pass or repeated clicks as additional users.

Prioritize consequences:

1. Data loss, privacy/security exposure, or unauthorized consequential effects.
2. Blocked first success or a core action that produces an incorrect result.
3. Recoverable failures or substantial accessibility/usability obstacles.
4. Ambiguity, minor friction, and polish.

Use frequency and recovery cost within these groups. Adapt priority to the actual
impact: an accessibility barrier preventing core use is a blocker, not mere polish.

## Final report

Include the run conditions, journey outcomes, ranked findings, and a concise
verification summary. Each finding retains evidence links, affected/exposed count,
fix status, and regression result. Distinguish replay success from a fresh journey
pass. Distinguish source changes from installed, deployed, or released behavior.
List unsupported conditions and skipped checks with their reason. Avoid a second
report or machine-readable schema unless an actual downstream consumer needs it.
