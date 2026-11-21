<!--
Integration brief: prove that work merged in parallel fits together. Tests and a
report only; no fixes. Usual tier: Sol 6.2 (high) or Sonnet. Use Astra (medium) or
Opus when the integration crosses system, tenant or data boundaries.
Replace every <placeholder>. Check against the brief checklist in ../SKILL.md.
-->

Build **<integration id>** of <project>: prove that <list of merged packages or branches> work together and with <the existing end-to-end path>, on <environments, planes or tenants>.

Your spec is `<path/to/spec.md>`. It is the source of truth. Read these first, in order: <project agent rules>, <standards>, <integration procedure>. Then read the spec, the progress notes and decisions of each package under test, and the previous integration report `<path>`.

How to work:
- **Where you are.** You are in your own git worktree at `<worktree>`, on branch `<branch>`, cut from `<base branch>` at `<base commit>`. Run `<setup command>` once first. You run non-interactively: nobody will answer a question.
- **Decisions.** When you would ask a question, record it as a decision, take the conservative option, and continue.
- **Your files.** Write only: `<test folders>` and `<report path>`, plus bookkeeping (<status, progress notes, index rows, decision records>).
- **Tests and the report only.** Don't fix what the tests find. Record each finding in the report with a severity and a suggested owner. A real defect gets a strict expected-failure that names the finding, never a loosened assertion.
- **Expected values.** Every expected number comes from fixtures and hand-derived counts, never from the code's output.
- **Boundaries.** Check that <tenants, clients or planes> can't reach each other's data, and that <production composition> gives the same results as <test composition>. Use fake fixture secrets only. Never print a secret.
- **Shared resources.** <database host:port, services>. Tests create their own schemas. Use ports `<ports>`. Re-run a connection or port failure alone before you treat it as real.
- **Setup and spend.** Locked tools only (`<install commands>`). Install nothing globally. No model spend and no real client data.
- **The report.** Follow the shape of `<previous report>`: what was proven, boundaries and negative controls, findings, updated checkpoint steps, and what was not verified.
- **Finishing.** Run the full gate, `<full gate command>`; it must pass. Set the spec to `<in-review>` with a progress note. Commit with explicit paths, push normally, and open a PR to `<base branch>` with the gate totals and a Next block in the body.
- **Hard limits.** Do not merge, force-push, delete branches or publish.

End with: the PR link, the gate totals, the findings by severity, and the Next block.
