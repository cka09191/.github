# Operating Model

## Ticket ownership

Every ticket names one primary owner and one active human role: proposer,
director, worker, or accountable approver. A shared implementation ticket must
also separate the human-reserved scope from the agent-support scope.

## Lifecycle

`Proposal → Refinement → Ready → In Progress → Early Check → Review → Done`

`Blocked` and `Parked` are explicit side states. A ticket may not skip `Early
Check` when it changes architecture, data contracts, model evaluation, cloud
boundaries, or a scope reserved for human learning.

## Four change layers

1. Intent: human role, product-value principles, portfolio authority, risk and
   cost ownership.
2. Shared policy: reusable ticket models, skills, templates, and automation.
3. Project control: product design, architecture, backlog, decisions, learning
   records, and implementation evidence pointers.
4. Implementation: independently buildable code, tests, migrations, CI, and
   essential operational documentation.

A ticket is filed where its authoritative change belongs. Cross-layer work uses
a project-control initiative linked to separate tickets in each changed layer.

## Durable records

Record intent not present in code, decisions and rejected alternatives, ticket
state and elapsed time, review results, learning evidence, and exact pointers to
commits, pull requests, tests, and artifacts. Do not copy diffs, credentials,
private media, or complete agent conversations.
