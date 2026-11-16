---
name: cross-agent-dispatch
description: Use when Claude Code should hand a task to OpenAI Codex, or Codex should hand a task to Claude Code, through the other agent's CLI as a background run that wakes the dispatcher when it exits. Covers the worktree, brief file, model and effort choice by kind of work, resume, and review before merge.
metadata:
  origin: internal
  source: Vel-Skills
  created: "2026-11-16"
  reviewed: "2026-11-16"
  reviewed-by: Claude (Opus 5.5)
  review-every-days: "90"
  review-due: "2027-02-14"
  notes: "Checked with codex-cli 0.162.0 and Claude Code 2.1.294. Model tiers are guidance; a project's own model decisions win."
---

# Cross-agent dispatch (Claude Code ⇄ Codex)

## Purpose

Let either coding agent hand a bounded task to the other through its
command-line interface, run it in the background, wake when it exits, and
review the result before anything merges. Pick the worker model by the kind of
work, not by habit.

Use it when:

- the person asks one agent to send work to the other ("give this to Codex",
  "have Claude review it");
- a brief names a model from the other vendor;
- the work suits the other agent better (see the task guide) and the person has
  allowed cross-agent dispatch for this task or project.

This skill gives no authority. The dispatcher's task scope and the repository's
own agent rules still apply to the worker.

## Inputs

- A target repository and a task with a clear outcome and checks.
- The other agent's CLI, installed and signed in: `codex` for Codex, `claude`
  for Claude Code.
- A run folder outside the repository (for example the session's scratch or
  temp directory) for the brief, logs and results.

## Outputs

- A branch and worktree holding the worker's changes, or a read-only answer.
- In the run folder: the brief, the full log, the worker's final message, and
  its session id for follow-ups.
- The dispatcher's review: accept, follow up, or discard.

## Non-goals

- Same-vendor fan-out. Use the host's own subagents or sessions for that.
- Merging, releasing or publishing. The worker never does these; the
  dispatcher does them only through the project's normal route and authority.
- Fixed model rules. The task guide is a default that projects can override.

## Workflow

### The contract

- **One worker, one worktree, one branch.** Never two writers in one checkout.
- **The worker never merges, force-pushes, deletes branches or publishes.** It
  commits, pushes its own branch, or opens a PR only if the brief says so.
- **The dispatcher never merges unreviewed output.** Read the diff, rerun the
  checks, and compare against the brief first.
- **Runs are non-interactive.** Nobody answers the worker's questions. Every
  brief says so and tells the worker to record blockers and continue.
- **Wake on exit, don't poll.** Start the CLI as a background command so the
  host tells the dispatcher when it exits.

### Task guide: which model

A project's own decision record, a brief's suggested model, or the person's
word wins over this table.

| Kind of work | Codex model (`-m`, effort) | Claude model (`--model`) |
|---|---|---|
| Critical: security, sign-in, secrets, privacy, governance, schema or migration design, cross-system design, reviews | `gpt-6-astra`, high | `opus` |
| Extensive builds with a clear brief and strong tests | `gpt-6.1-sol`, high | `sonnet` |
| Mechanical work with a clear spec and checks: roll-ups, regenerated contracts or types, fixtures from a spec, mechanical refactors | `gpt-6.1-terra`, high (always high) | `sonnet` or `haiku` |
| Small tasks: lookups, tagging, one-file mechanical edits | `gpt-6-luna`, medium | `haiku` |

- **Terra never writes text that states outside facts** (research, prices,
  legal or platform claims). It guesses too often when it doesn't know.
- **Mixed work takes the tier of its most critical part.**
- Astra costs about five times Sol per token. Use it only for critical work.
- Claude effort: add `--effort high` for critical work.
- Check the slugs before a run. Codex lists its models in
  `$CODEX_HOME/models_cache.json` (default `~/.codex`). Claude aliases
  (`opus`, `sonnet`, `haiku`, `fable`) resolve to the latest model. If a slug
  is gone, pick the nearest tier and say so in the report.

### The brief

Write the brief to a file, not the command line. Start every brief with:

```text
This run is non-interactive. Nobody will answer questions. If something blocks
you, record the blocker in your final message, take the safest reasonable
choice, and continue. Do not merge, force-push, delete branches or publish.
```

Then give: one outcome; allowed and forbidden paths; the project rules to read
first; acceptance checks with exact commands; whether to commit, push or open
a PR; and the shape of the final message (changed files, checks run with
results, blockers, open questions).

### Direction 1: Claude Code → Codex

1. Make a worktree and branch from the latest main:

   ```bash
   git -C <repo> fetch origin
   git -C <repo> worktree add -b <branch> <worktree> origin/main
   ```

2. Write the brief to `<run-dir>/brief.md`, outside the worktree.
3. Start Codex as a **background** command (in Claude Code, Bash with
   `run_in_background: true`):

   ```bash
   codex exec -m <model> -c model_reasoning_effort=<effort> \
     -C <worktree> -o <run-dir>/last-message.md \
     - < <run-dir>/brief.md > <run-dir>/codex.log 2>&1
   ```

   - Codex uses the sandbox and approval policy from its config. A background
     run cannot answer approval prompts, so the config or flags must not need
     them. For a read-only task add `-s read-only`.
   - `-o` writes only the final message. The log holds the full transcript.
4. When the host wakes you, read `last-message.md` first, then the log if
   needed. The log header has the session id:

   ```bash
   grep -m1 'session id' <run-dir>/codex.log
   ```

5. Follow up in the same Codex session, again in the background:

   ```bash
   codex exec resume <session-id> -o <run-dir>/last-message-2.md \
     - < <run-dir>/followup.md > <run-dir>/codex-2.log 2>&1
   ```

### Direction 2: Codex → Claude Code

1. **Check sign-in.** The `claude` CLI keeps its own sign-in, apart from the
   desktop app. `claude auth status` must show `"loggedIn": true`. If not,
   stop and ask the person to run `claude auth login` themselves. Never handle
   the credential.
2. Make the worktree and brief as in direction 1.
3. Run Claude in print mode as a background job or long-running command,
   whichever the Codex host supports. It must not wait on a terminal:

   ```bash
   cd <worktree> && claude -p --model <opus|sonnet|haiku> \
     --permission-mode <mode> --permission-prompts none \
     --output-format json \
     < <run-dir>/brief.md > <run-dir>/claude.json 2> <run-dir>/claude.err
   ```

   - The working directory is the shell's current directory; there is no
     `--cd` flag. Use `--add-dir` for extra folders.
   - `--permission-prompts none` denies anything that would prompt, so the run
     never hangs on a question.
   - Permission mode: `plan` for read-only work and reviews; `acceptEdits` for
     edits without shell commands; `auto` or `bypassPermissions` for builds
     that run tests, and only inside a dedicated worktree. Narrow it with
     `--allowed-tools "Bash(git *) Bash(python3 *)"` and similar.
   - Optional limits: `--max-budget-usd <n>`, `--effort high`.
4. Read the result. With `--output-format json` the file is one object:
   `.result` is the final message and `.session_id` the id; `.is_error` and
   `.total_cost_usd` are there too:

   ```bash
   python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); print(d["session_id"]); print(d["result"])' <run-dir>/claude.json
   ```

5. Follow up in the same session, from the same directory:

   ```bash
   cd <worktree> && claude -p --resume <session-id> --permission-mode <mode> \
     --permission-prompts none --output-format json \
     < <run-dir>/followup.md > <run-dir>/claude-2.json
   ```

### Review and integrate

1. Read the final message. Treat it as a claim, not proof.
2. Inspect the worktree: `git -C <worktree> status`,
   `git -C <worktree> diff origin/main...HEAD`, and any files outside the
   allowed paths.
3. Rerun the project's checks yourself.
4. Accept, follow up through resume, or discard. Merge only through the
   project's normal route and with the authority it gives the dispatcher.
5. Remove the worktree only when its branch is merged or the person says so.

## Checks

- The worker's final message exists and names the checks it ran.
- The dispatcher reran those checks and they pass.
- The diff touches only the allowed paths.
- No merge, force-push or publish happened without the person's authority.

## Failure modes & recovery

| What went wrong | What to do |
|---|---|
| Worker asked a question and stopped | Resume with the answer, and add the missing fact to future briefs. |
| `codex exec` exits at once | Read the log: wrong slug, bad `-c` value, or a sign-in problem. Check the models cache. |
| `claude -p` hangs | It was waiting on stdin or a prompt. Redirect stdin from the brief and pass `--permission-prompts none`. |
| `claude.json` has `"is_error": true` with "Failed to authenticate" | The CLI is signed out. Ask the person to run `claude auth login`. |
| Worker touched files outside its scope | Discard those changes; tighten the brief or the permission mode. |
| Both agents edited one checkout | Stop both, keep the diff, and give each its own worktree. |
