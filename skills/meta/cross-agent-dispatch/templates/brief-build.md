<!--
Build brief. Usual tier: Sol 6.1 (high) or Sonnet. Use Astra (high) or Opus when
the spec touches security, privacy, governance, schema or several systems.
Replace every <placeholder>. Delete lines that don't apply. Check the brief
against the brief checklist in ../SKILL.md before dispatch.
-->

Build **<package or task id>** of <project>: <one sentence on the outcome a person will notice>.

Your spec is `<path/to/spec.md>`. It is the source of truth. Read these first, in order: <project agent rules, e.g. AGENTS.md>, <standards folder>, <start and finish procedures>. Then read the spec and everything its read-first section names.

How to work:
- **Where you are.** You are in your own git worktree at `<worktree>`, on branch `<branch>`, cut from `<base branch>` at `<base commit>`. Run `<setup command>` once first. You run non-interactively: nobody will answer a question.
- **Decisions.** When you would ask a question, record it as a decision in `<decision record location>`, take the conservative option, and continue. Mark any choice that is hard to reverse.
- **Your files.** Write only: `<allowed paths>`. This includes the layer the project's standards require for this work: `<e.g. data layer folder for SQL>`. Bookkeeping is also allowed: <status, progress notes, index rows, decision records>.
- **Generated files.** This change regenerates `<generated files>`. Regenerate them with `<commands>`; never hand-edit them. <You own them for this wave. | `<other worker>` owns them; leave them alone and note what would change.>
- **Out of scope.** Don't change `<paths or systems>`. If you find a problem there, record it as a finding with a suggested owner.
- **Acceptance.** <tests or checks with exact commands>. Expected results come from the spec and fixtures, never from the code's output. Never loosen a check.
- **Shared resources.** <database host:port, shared services>. Use ports `<ports>` if you need them. Re-run a connection or port failure alone before you treat it as real.
- **Setup and spend.** Use the project's locked tools only (`<lockfile install commands>`). Install nothing globally. No model spend and no real client data.
- **Finishing.** Run the full gate, `<full gate command>`; it must pass. Set the spec's status to `<in-review>` with a progress note. Commit with explicit paths, push normally, and open a PR to `<base branch>`. Put the gate's printed totals and a Next block in the PR body.
- **Hard limits.** Do not merge, force-push, delete branches or publish. Never print a secret.

End with: the PR link, the gate totals, decisions you took (hard-to-reverse ones marked), blockers, and the Next block.
