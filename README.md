# Vel-Skills

Vel's personal library of reusable agent skills.

Each skill is a folder: a `SKILL.md` plus the helper files it names. Cursor, Codex, and Claude-style agents load a skill by reading that folder when a task matches the `description` in its frontmatter.

## Layout

```
skills/<group>/<kebab-name>/   # one skill; SKILL.md plus helpers
  SKILL.md
templates/SKILL_TEMPLATE.md     # blank skeleton for a new skill
private/                        # optional local directory, ignored by git
SKILLS_INDEX.md                 # grouped index with review dates (generated)
CONTRIBUTING.md                 # skill contract and new-skill checklist
```

`<group>` is a short topic (`media`, and others as they are added). `<kebab-name>` matches the `name` in that skill's frontmatter. Helper scripts and notes stay inside the skill folder and are referenced by relative path.

## Install a skill locally

Keep the skill and its helpers together in this checkout. From the repository
root, link the skill into each agent's skills directory.

```bash
mkdir -p ~/.codex/skills ~/.claude/skills ~/.cursor/skills
ln -s "$PWD/skills/media/app-demo-video" ~/.codex/skills/app-demo-video
ln -s "$PWD/skills/media/app-demo-video" ~/.claude/skills/app-demo-video
ln -s "$PWD/skills/media/app-demo-video" ~/.cursor/skills/app-demo-video
```

Link private skills from `private/<name>/`. Keep vendor-managed installs in
their original locations. Restart agents that discover skills at startup.

If an agent does not follow symlinks (some Cursor versions do not), copy the
whole folder instead, so the skill's relative paths keep working:

```bash
cp -R skills/media/app-demo-video ~/.cursor/skills/app-demo-video
```

A copy does not update with the library. Copy it again after pulling changes.

## Review dates

Every public and private skill records its source and review date. Before
using an overdue skill, tell the user its last review date and source and offer
to review it. See [skill-review](skills/meta/skill-review/SKILL.md).

```bash
python3 skills/meta/skill-review/check_reviews.py
python3 skills/meta/skill-review/check_reviews.py --include-private --check-links
```

## Skills

<!-- skills-table:start -->
| Skill | Group | What it is for | Next review |
| --- | --- | --- | --- |
| [jupyter-notebook](skills/data/jupyter-notebook/SKILL.md) | data | Use when the user asks to create, scaffold, or edit Jupyter notebooks (`.ipynb`) for experiments, explorations, or tutorials; prefer the bundled templates and run the helper script `new_notebook.py` to generate a clean starting notebook. | 2026-12-14 |
| [canvas-design](skills/design/canvas-design/SKILL.md) | design | Create beautiful visual art in .png and .pdf documents using design philosophy. You should use this skill when the user asks to create a poster, piece of art, design, or other static piece. Create original visual designs, never copying existing artists' work to avoid copyright violations. | 2026-12-14 |
| [visual-parity-review](skills/design/visual-parity-review/SKILL.md) | design | Use before calling any person-facing screen, page or visual deliverable "done", "built to the design" or "matching the mockup". Captures the reference and the build side by side at the same size, data, theme and state, lists every gap, fixes them, and applies the design operating principles in this skill. Use it for every screen package, every redesign, and any claim that something "looks right". | 2027-02-12 |
| [godot-export-packager](skills/game/godot-export-packager/SKILL.md) | game | Prepare Godot export readiness materials, release checklists, build folders, export preset examples, version manifests, and post-build QA notes for mobile-first and desktop-capable games. Use when a project is nearing test build or release packaging. | 2027-02-12 |
| [godot-feature-scaffolder](skills/game/godot-feature-scaffolder/SKILL.md) | game | Break a gameplay feature into Godot scenes, scripts, assets, tasks, acceptance criteria, and integration handoffs. Use for feature planning, mechanic definition, TODO breakdowns, and scaffolding feature modules inside a Godot project. | 2027-02-12 |
| [godot-game-dev-pipeline](skills/game/godot-game-dev-pipeline/SKILL.md) | game | Orchestrate a complete Godot game-development workflow for mobile-first, desktop-capable 2D projects. Use for game planning, feature decomposition, asset routing, Godot integration contracts, scene architecture, QA, optimization, and export readiness. Coordinates sibling skills such as sprite-generator, godot-project-scaffolder, godot-feature-scaffolder, godot-scene-builder, godot-ui-kit-generator, godot-sprite-importer, godot-mobile-optimization-checker, and godot-export-packager. | 2027-02-12 |
| [godot-mobile-optimization-checker](skills/game/godot-mobile-optimization-checker/SKILL.md) | game | Audit Godot projects and generated asset packs for mobile-first performance issues, including large textures, transparent padding waste, asset counts, file sizes, folder hygiene, and desktop compatibility notes. Use before integration, milestone review, or export. | 2027-02-12 |
| [godot-project-scaffolder](skills/game/godot-project-scaffolder/SKILL.md) | game | Create a Godot 4.x project skeleton for mobile-first, desktop-capable 2D games, including folders, starter scenes, scripts, README, asset directories, and project manifests. Use when a user wants a new Godot project structure or clean game repo foundation. | 2027-02-12 |
| [godot-scene-builder](skills/game/godot-scene-builder/SKILL.md) | game | Create Godot `.tscn` scene starters and matching GDScript stubs for actors, props, rooms, interactables, UI containers, and click-to-move setups. Use when the user needs scene architecture or import-ready node hierarchies. | 2027-02-12 |
| [godot-sprite-importer](skills/game/godot-sprite-importer/SKILL.md) | game | Convert generated sprite outputs into Godot-ready import manifests, copied asset folders, starter SpriteFrames resources, node setup notes, and validation summaries. Use after sprite-generator or a project-local sprite worker has produced PNG/WebP sheets or frame folders. | 2027-02-12 |
| [godot-ui-kit-generator](skills/game/godot-ui-kit-generator/SKILL.md) | game | Plan and scaffold mobile-first Godot UI/HUD/menu kits, including Control scene stubs, UI asset manifests, safe-area notes, touch target rules, and handoffs to sprite-generator for UI art. Use when the user needs buttons, HUD panels, menus, icons, meters, or mobile/desktop UI layout guidance. | 2027-02-12 |
| [sprite-generator](skills/game/sprite-generator/SKILL.md) | game | Create, repair, validate, preview, and package game-ready sprite assets for Godot from references or vivid descriptions. Use when a user wants a character, prop, furniture state set, animation strip, map, dollhouse room, UI-adjacent game object, style-matched variations, or a Godot-ready atlas with SpriteFrames resources. This skill delegates actual art generation to the installed image generation skill/tool and uses bundled scripts only for deterministic prompt planning, chroma-key cleanup, frame extraction, atlas composition, QA, previews, and Godot packaging. | 2027-02-12 |
| [app-demo-video](skills/media/app-demo-video/SKILL.md) | media | Use when making a demo, promo, or launch video of a working app, prototype, pipeline, or dataset with real data and dramatic, click-baity framing, including when the content has no UI yet and should be stood up as a camera-ready frontend first, or when a past cut felt like a slide deck or had captions covering the UI. | 2027-02-12 |
| [pdf](skills/media/pdf/SKILL.md) | media | Use when tasks involve reading, creating, or reviewing PDF files where rendering and layout matter; prefer visual checks by rendering pages (Poppler) and use Python tools such as `reportlab`, `pdfplumber`, and `pypdf` for generation and extraction. | 2026-12-14 |
| [screenshot](skills/media/screenshot/SKILL.md) | media | Use when the user explicitly asks for a desktop or system screenshot (full screen, specific app or window, or a pixel region), or when tool-specific capture capabilities are unavailable and an OS-level capture is needed. | 2026-12-14 |
| [agent-assignment-writer](skills/meta/agent-assignment-writer/SKILL.md) | meta | Create bounded human or agent workstream prompts with clear file ownership, dependencies, validation, docs updates, and stop conditions. Use this when delegating work or preparing a fresh parallel-agent assignment. | 2027-02-12 |
| [archive-candidate-review](skills/meta/archive-candidate-review/SKILL.md) | meta | Identify old or inactive files/folders that may be ready for archive without moving or deleting them. | 2027-02-12 |
| [cli-creator](skills/meta/cli-creator/SKILL.md) | meta | Build a composable CLI for Codex from API docs, an OpenAPI spec, existing curl examples, an SDK, a web app, an admin tool, or a local script. Use when the user wants Codex to create a command-line tool that can run from any repo, expose composable read/write commands, return stable JSON, manage auth, and pair with a companion skill. | 2026-12-14 |
| [contract-steward](skills/meta/contract-steward/SKILL.md) | meta | Add or update canonical contracts, schemas, lifecycle rules, examples, and fail-closed validation without duplicating truth in tests or implementation packages. | 2027-02-12 |
| [core-enforcement](skills/meta/core-enforcement/SKILL.md) | meta | Implement reusable enforcement logic in packages/core against canonical contracts while keeping adapters, demos, providers, UI, and schema ownership out of core. | 2027-02-12 |
| [cross-surface-comms-review](skills/meta/cross-surface-comms-review/SKILL.md) | meta | Adapt or review source-of-truth business, community, launch, support, or proposal copy across Docs, Sheets, Slack, Reddit, decks, and local Markdown while preserving approval state and human-review boundaries. | 2027-02-12 |
| [gh-address-comments](skills/meta/gh-address-comments/SKILL.md) | meta | Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in. | 2026-12-14 |
| [goal-board-hygiene](skills/meta/goal-board-hygiene/SKILL.md) | meta | Audit and reconcile an existing oversized or structurally confused GoalBuddy board when phases, tasks, milestones, or planning ledgers no longer agree. Use for board hygiene, not ordinary goal creation, product planning, or implementation work. | 2027-02-12 |
| [internal-comms](skills/meta/internal-comms/SKILL.md) | meta | A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.). | 2026-12-14 |
| [openai-docs](skills/meta/openai-docs/SKILL.md) | meta | Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations, help choosing the latest model for a use case, or model upgrade and prompt-upgrade guidance; prioritize OpenAI docs MCP tools, use bundled references only as helper context, and restrict any fallback browsing to official OpenAI domains. | 2026-11-28 |
| [phase-closeout-audit](skills/meta/phase-closeout-audit/SKILL.md) | meta | Close a scaffold or project phase with exact scope, files changed, verification evidence, findings, follow-up, decisions, changelog, and roadmap/current-state updates. | 2027-02-12 |
| [project-personalize](skills/meta/project-personalize/SKILL.md) | meta | Convert the scaffold into a real project by running the initializer, replacing placeholders, updating project contracts, and preserving contract/core/test governance boundaries. | 2027-02-12 |
| [promote-work](skills/meta/promote-work/SKILL.md) | meta | Move work from capture or draft state into active, reviewed, accepted, or archived state without losing context. | 2027-02-12 |
| [resume-tailoring](skills/meta/resume-tailoring/SKILL.md) | meta | Tailor evidence-backed resumes to job descriptions while preserving benchmark specificity, recovering prior answers, interviewing only for material gaps, and verifying PDF and DOCX exports. | 2027-02-12 |
| [skill-review](skills/meta/skill-review/SKILL.md) | meta | Use when adding a skill to this library, when a skill's review is due or overdue, when importing a skill from another repository or vendor, or when rebuilding the skills index. Records where each skill came from and when it was last reviewed, checks review dates, and regenerates SKILLS_INDEX.md. | 2027-02-12 |
| [workflow-packaging-audit](skills/meta/workflow-packaging-audit/SKILL.md) | meta | Look back across recent work history to find repeated manual workflows worth packaging as skills, subagents, automations, extensions, or deliberate skips. | 2027-02-12 |
| [yeet](skills/meta/yeet/SKILL.md) | meta | Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`). | 2026-12-14 |
| [dogfood](skills/testing/dogfood/SKILL.md) | testing | Dogfood an application through independent first-time-user journeys in real browsers, consolidate evidence, and verify authorized fixes. Use for hands-on product dogfooding and launch-readiness checks. | 2027-02-12 |
| [gh-fix-ci](skills/testing/gh-fix-ci/SKILL.md) | testing | Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval. Treat external providers (for example Buildkite) as out of scope and report only the details URL. | 2026-12-14 |
| [playwright](skills/testing/playwright/SKILL.md) | testing | Use when the task requires automating a real browser from the terminal (navigation, form filling, snapshots, screenshots, data extraction, UI-flow debugging) via `playwright-cli` or the bundled wrapper script. | 2026-12-14 |
| [playwright-interactive](skills/testing/playwright-interactive/SKILL.md) | testing | Persistent browser and Electron interaction through `js_repl` for fast iterative UI debugging. | 2026-12-14 |
| [security-best-practices](skills/testing/security-best-practices/SKILL.md) | testing | Perform language and framework specific security best-practice reviews and suggest improvements. Trigger only when the user explicitly requests security best practices guidance, a security review/report, or secure-by-default coding help. Trigger only for supported languages (python, javascript/typescript, go). Do not trigger for general code review, debugging, or non-security tasks. | 2026-12-14 |
| [security-threat-model](skills/testing/security-threat-model/SKILL.md) | testing | Repository-grounded threat modeling that enumerates trust boundaries, assets, attacker capabilities, abuse paths, and mitigations, and writes a concise Markdown threat model. Trigger only when the user explicitly asks to threat model a codebase or path, enumerate threats/abuse paths, or perform AppSec threat modeling. Do not trigger for general architecture summaries, code review, or non-security design work. | 2026-12-14 |
| [chatgpt-apps](skills/web/chatgpt-apps/SKILL.md) | web | Build, scaffold, refactor, and troubleshoot ChatGPT Apps SDK applications that combine an MCP server and widget UI. Use when Codex needs to design tools, register UI resources, wire the MCP Apps bridge or ChatGPT compatibility APIs, apply Apps SDK metadata or CSP or domain settings, or produce a docs-aligned project scaffold. Prefer a docs-first workflow by invoking the openai-docs skill or OpenAI developer docs MCP tools before generating code. | 2026-11-28 |
| [cloudflare-deploy](skills/web/cloudflare-deploy/SKILL.md) | web | Deploy applications and infrastructure to Cloudflare using Workers, Pages, and related platform services. Use when the user asks to deploy, host, publish, or set up a project on Cloudflare. | 2026-11-28 |
| [modern-web-guidance](skills/web/modern-web-guidance/SKILL.md) | web | Use when building or changing web UI, CSS layout or animation, forms, accessibility, dark mode, performance (LCP, INP, CLS), web security or client-side JS. A pinned, reviewed copy of Google Chrome's modern web guides; read the matching guide before writing ad-hoc code or adding a dependency. Not for backend, infrastructure or tooling work. | 2026-11-28 |
| [netlify-deploy](skills/web/netlify-deploy/SKILL.md) | web | Deploy web projects to Netlify using the Netlify CLI (`netlify`). Use when the user asks to deploy, host, publish, or link a site/repo on Netlify, including preview and production deploys. | 2026-11-28 |
| [render-deploy](skills/web/render-deploy/SKILL.md) | web | Deploy applications to Render by analyzing codebases, generating render.yaml Blueprints, and providing Dashboard deeplinks. Use when the user wants to deploy, host, publish, or set up their application on Render's cloud platform. | 2026-11-28 |
| [vercel-deploy](skills/web/vercel-deploy/SKILL.md) | web | Deploy applications and websites to Vercel. Use when the user requests deployment actions like \"deploy my app\", \"deploy and give me the link\", \"push this live\", or \"create a preview deployment\". | 2026-11-28 |
<!-- skills-table:end -->

The same list, grouped, with origin, review dates and notes, is in [SKILLS_INDEX.md](SKILLS_INDEX.md). Both are generated by `python3 skills/meta/skill-review/build_index.py`; do not edit them by hand. The contract for adding a skill is in [CONTRIBUTING.md](CONTRIBUTING.md).
