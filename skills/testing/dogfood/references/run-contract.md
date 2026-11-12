# Run contract

Use a concise brief in the report or working context, not a separate planning
ceremony. Record:

- Target URL/application and observed version, revision, or build identifier.
  If unknown, say so; do not invent a deployment-to-source relationship.
- Intended audience, entry point, user motivation, and observable first success.
- Included journeys and explicit exclusions.
- Test accounts/data and relevant permitted actions. Reuse authorized setup.
- Observe-only or fixes authorized, based on the user's actual request.
- Requested browser, viewport, network conditions, and other relevant constraints.
- Evidence output location and how resulting state will be verified.

Provisioning accounts, running services, purchases, messages, publishing, deletion,
and production changes retain the authority requirements of the task and host.
Technical access is not permission. The breaker needs disposable test data and
bounded actions; do not run destructive or load testing against arbitrary systems.
Stop the smallest affected action when authority is absent. Keep testing other
authorized paths and record where a journey could not continue.

Use the project's existing output convention. If none exists, choose a local
task artifact directory outside tracked source and report its path. Do not create
a new board, tracking system, repository, or recurring job for this skill.

Each tester receives the motivation and success outcome, not implementation
instructions. Account setup may be supplied when outside the journey; do not
pre-complete onboarding when onboarding is what the run evaluates.
