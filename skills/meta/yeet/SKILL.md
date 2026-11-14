---
name: "yeet"
description: "Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`)."
license: "Apache-2.0"
metadata:
  origin: adapted
  source: https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/yeet
  source-ref: 49f948faa9258a0c61caceaf225e179651397431
  created: "2026-01-27"
  reviewed: "2026-11-14"
  reviewed-by: Codex (GPT-6)
  review-every-days: "30"
  review-due: "2026-12-14"
  notes: Requires explicit staging and disables GitHub CLI telemetry.
---

## First: check this skill is still reviewed

Compare today's date with `review-due`. If overdue, tell the user when it was
reviewed and identify `source` and `source-ref`. Offer to review upstream.
If the user declines or is unavailable, use this pinned copy and report that
its review is overdue.

# Yeet

<!-- Vel-Skills added its review contract and portability or safety changes. -->

## Purpose

Complete authorized GitHub pull request delivery.

## Inputs

- A repository, explicit publish authorization, paths in scope, and authenticated GitHub CLI.

## Outputs

- The pushed commit and pull request URL.

## Non-goals

- Committing unrelated changes, merging, or publishing without authorization.

## Prerequisites

Set `GH_TELEMETRY=false` for GitHub CLI commands. See [GitHub CLI telemetry](https://docs.github.com/en/github-cli/github-cli/github-cli-telemetry).

- Require GitHub CLI `gh`. Check `gh --version`. If missing, ask the user to install `gh` and stop.
- Require authenticated `gh` session. Run `gh auth status`. If not authenticated, ask the user to run `gh auth login` (and re-run `gh auth status`) before continuing.

## Naming conventions

- Branch: `{description}` when starting from main/master/default.
- Commit: `{description}` (terse).
- PR title: `{description}` summarizing the full diff.

## PR template discovery

Before creating the PR, resolve the repository root and look for the active GitHub PR template from there:

```shell
repo_root="$(git rev-parse --show-toplevel)"
```

Template candidates, in order:

- `.github/pull_request_template.md`
- `.github/PULL_REQUEST_TEMPLATE.md`
- One `*.md` file under `.github/pull_request_template/`
- One `*.md` file under `.github/PULL_REQUEST_TEMPLATE/`

Use paths as emitted from the repository root, such as `.github/pull_request_template.md`, not `./.github/pull_request_template.md`.

If exactly one template is found, read it before composing the final PR body and pass it to `gh pr create` with `--template "$template"`.

If multiple template files are found, stop before PR creation and ask which template to use. If no template exists, use the fallback body shape in this skill.

## Workflow

- If on main/master/default, create a branch: `git checkout -b "{description}"`
- Otherwise stay on the current branch.
- Confirm status and stage only explicitly scoped paths with `git add -- <paths>`.
- Commit tersely with the description: `git commit -m "{description}"`
- Run checks if not already. If checks fail due to missing deps/tools, use the project’s existing or preapproved dependencies and rerun once.
- Push with tracking: `git push -u origin $(git branch --show-current)`
- If git push fails due to workflow auth errors, check permissions and repository identity before retrying.
- Discover and read the repository PR template, if any.
- Check whether the current branch already has a PR: `gh pr view "$(git branch --show-current)" --json number,isDraft,url`
- If a PR already exists, update that PR in place. Do not create another PR, and do not change whether the existing PR is draft or ready for review.
- If no PR exists, open a new draft PR:
  - With one template: `GH_PROMPT_DISABLED=1 GIT_TERMINAL_PROMPT=0 gh pr create --draft --fill --template "$template" --head "$(git branch --show-current)"`
  - Without a template: `GH_PROMPT_DISABLED=1 GIT_TERMINAL_PROMPT=0 gh pr create --draft --fill --head "$(git branch --show-current)"`
- Edit the PR title and body so they reflect the actual net change in the diff.
- Write the PR description to a temp file with real newlines and pass it via `--body-file` or `gh pr edit --body-file` to avoid `\n`-escaped markdown.

## Determining the PR

When updating a PR created earlier in the flow, infer the PR from the current branch when possible:

```shell
git branch --show-current
gh pr view "$(git branch --show-current)" --json number --jq '.number'
```

If this finds an existing PR, preserve its current review state. Never convert an existing ready-for-review PR back to draft as part of `yeet`; only new PRs created by this flow should start as draft.

## PR Title

Format: `<type>(<scope>): <subject>`

`<scope>` is optional. A scope consist of a noun describing a section of the codebase (component, service or subsytem).

### Example

```
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.
```

More Examples:

- `feat`: (new feature for the user, not a new feature for build script)
- `fix`: (bug fix for the user, not a fix to a build script)
- `docs`: (changes to the documentation)
- `style`: (formatting, missing semi colons, etc; no production code change)
- `refactor`: (refactoring production code, eg. renaming a variable)
- `test`: (adding missing tests, refactoring tests; no production code change)
- `chore`: (updating grunt tasks etc; no production code change)


## PR Body Contents

When invoked, use `gh` to edit the pull request body and title to reflect the contents of the specified PR. Make sure to check the existing pull request body to see if there is key information that should be preserved. For example, NEVER remove an image in the existing pull request body, as the author may have no way to recover it if you remove it.

When a repository PR template exists, adapt the final PR body to that template. Preserve meaningful headings, required checklists, and repo-specific prompts, but replace placeholder text with net-diff-specific content or `N/A` where the template asks for it. Do not discard template sections just because the fallback shape below is shorter.

It is critically important to explain _why_ the change is being made. If the current conversation in which this skill is invoked has discussed the motivation, be sure to capture this in the pull request body.

The body should also explain _what_ changed, but this should appear after the _why_.

Limit discussion to the _net change_ of the commit. It is generally frowned upon to discuss changes that were attempted but later undone in the course of the development of the pull request. When rewriting the pull request body, you may need to eliminate details such as these when they are no longer appropriate / of interest to future readers.

Avoid references to absolute paths on my local disk. When talking about a path that is within the repository, simply use the repo-relative path.

Default to omitting `Verification`. Add it only when you have behavioral evidence worth preserving for reviewers: a reproduced bug, a before/after check, a targeted test that exercises the changed behavior, or a manual scenario with input and observed outcome. Do not use it for generic commands or automation results such as package tests, type checks, linters, formatters, pre-commit/pre-push hooks, or CI status.

If the repository template requires a validation or verification section, keep that section and avoid generic filler: include meaningful commands/results, a targeted manual scenario, or `Not run` with a reason.

Use professional Markdown:

- Put code, paths, commands, flags, and identifiers in backticks.
- Use fenced code blocks for shell transcripts or multi-line examples.
- Use GitHub permalinks when citing existing code relevant to the change.
- Reference relevant issues or related PRs, but do not reference the PR in its own body.

### Suggested PR Body Shape

Use this as a fallback when the repository does not have a PR template:

```markdown
## Why

Describe the user-facing or maintainer-facing problem, including cause and effect where useful.

## What Changed

Describe the net implementation change in concise prose.
```

## Checks

- Verify the diff, test results, branch, and public-safe PR body.

## Failure modes & recovery

If the remote rejects the push, inspect the reason and reconcile with the current branch without overwriting remote work.
