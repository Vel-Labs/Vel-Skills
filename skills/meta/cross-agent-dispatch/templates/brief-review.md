<!--
Review brief: read-only review of a diff, PR or design. Usual tier: Astra (high)
or Opus. Run it read-only: Codex `-s read-only`, Claude `--permission-mode plan`.
Replace every <placeholder>. Check against the brief checklist in ../SKILL.md.
-->

Review **<PR, branch range or design doc>** of <project> for <correctness | security and privacy | conformance to the spec | all of these>.

This is read-only. Do not edit, commit, push or comment on any PR. You run non-interactively: nobody will answer a question. If something is unclear, state your assumption in the review and continue.

What to review:
- **Target.** `<git diff origin/<base>...<branch>>` in `<worktree or repo path>`, or `<doc path>`.
- **Against.** The spec `<path>`, the project's standards `<path>`, and decisions `<paths>`.
- **Focus.** <the risks that matter here, e.g. data crossing tenant boundaries, secrets in logs, migrations that can't roll back, expected values taken from code output>.
- **Out of scope.** <style nits, areas owned by other reviews>.

You may run read-only commands: `<test or gate command>` if it writes nothing outside temp folders, `git log`, `git diff`, and file reads.

End with findings, most severe first. For each: severity (blocker, major, minor), file and line, what's wrong, a concrete case that shows it, and the fix you suggest. Then list what you checked and found sound, and what you could not verify.
