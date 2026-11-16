<!--
Resume brief: a follow-up sent into a running worker session with
`codex exec resume <id>` or `claude -p --resume <id>`. Use it for a ruling on a
blocker or a request to merge main. A resume costs a full round trip, so make
the ruling complete: files, sides to keep, regenerate commands, gate, end message.
Replace every <placeholder>. Delete the section you don't need.
-->

<Dispatcher role>, <date>: <one line on what changed, e.g. "PR #<n> merged to `<base>` at <commit>, and your PR #<m> now conflicts with it" | "Ruling on your blocker about <topic>">.

**Ruling** (if answering a blocker): <the decision, in one or two sentences>. You may now also write `<newly allowed paths>`. <Who owns the generated file in question.> Record this as a decision that cites the ruling.

Do this on branch `<branch>`:
1. `git fetch origin` and `git merge origin/<base>`. A normal merge: no rebase, no force-push.
2. Resolve `<files>` by keeping both sides' rows and entries. <For `<file>`, keep <ours | theirs | both, with this note>.>
3. For source data that feeds generated files (`<e.g. cards source JSON>`), keep both sides' changes, then regenerate.
4. Regenerate every generated file: `<command>` for `<files>`, `<command>` for `<files>`. Never hand-edit or hand-merge generated files.
5. Run `<fast gate command>` <because this merge touched only docs and generated files> | `<full gate command>`. It must pass. Never loosen a check.
6. Commit with explicit paths and push normally to PR #<m>. Update the gate totals in the PR body.

Do not merge the PR, force-push, delete branches or publish. You run non-interactively: if something new blocks you, record it, take the conservative option, and continue.

End with: the commit, the gate totals, and anything you could not resolve.
