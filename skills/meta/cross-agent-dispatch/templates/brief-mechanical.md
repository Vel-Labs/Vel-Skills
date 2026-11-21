<!--
Mechanical brief: roll-ups, regenerated contracts or types, fixtures from a given
spec, mechanical refactors, bookkeeping. Usual tier: Terra (medium) or
Sonnet; Luna or Haiku for a single-file edit. The work must have a clear spec and
checks that catch mistakes. Terra never writes text that states outside facts.
Replace every <placeholder>. Check against the brief checklist in ../SKILL.md.
-->

Do **<task id>** in <project>: <one sentence on the mechanical change>.

The spec is `<path or the list below>`. Follow it exactly; this task needs no design choices. If it seems to need one, record the question, take the option that changes least, and continue. You run non-interactively: nobody will answer a question.

How to work:
- **Where you are.** Worktree `<worktree>`, branch `<branch>`, cut from `<base branch>` at `<base commit>`. Run `<setup command>` once first.
- **The change.** <exact steps, e.g. "mark packages X and Y done in the stage README wave table and change log", "rename A to B in these files", "regenerate with these commands">.
- **Your files.** Write only: `<allowed paths>`.
- **Generated files.** Regenerate `<files>` with `<commands>`. Never hand-edit them.
- **Facts.** Copy numbers, dates and links from `<source files>`. Don't add facts from memory.
- **Gate.** Run `<fast gate | full gate command>`; it must pass. Never loosen a check.
- **Finishing.** Commit with explicit paths, push normally, and <open a PR to `<base>` | don't open a PR>.
- **Hard limits.** Do not merge, force-push, delete branches or publish.

End with: the commit (and PR link if any), the files changed, and the gate totals.
