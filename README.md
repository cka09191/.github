# GitHub Project Management Defaults

A public, reusable starting point for project backlogs that deliberately keeps
project-control records separate from product implementation.

It provides:

- GitHub Issue Forms for proposals, decisions, and bounded work items;
- explicit human roles, learning scope, early-discovery checkpoints, and
  risk/cost gates;
- a small dependency-free repository doctor and Issue-listing CLI;
- a four-layer operating model for intent, shared policy, project control, and
  implementation;
- reusable labels and validation CI.

This repository is a generic template, not the private policy or backlog of any
particular project. It contains no product source, credentials, private assets,
provider configuration, or project-specific acceptance rules.

## Use as account defaults

Fork or generate this repository as a public repository named `.github` under
your personal account or organization. Repositories without their own
`.github/ISSUE_TEMPLATE` directory will inherit these Issue Forms.

GitHub treats any local file in a target repository's `ISSUE_TEMPLATE`
directory as an override of the complete default directory. Keep that directory
absent unless the repository intentionally owns a full replacement set.

## Use as a project-control repository

1. Use this repository as a template.
2. Copy `config/project.example.json` to `config/project.json` and replace the
   placeholders.
3. Set `issue_form_source` to your account's public `.github` repository, or
   retain the local Issue Forms.
4. Create the labels in `config/labels.json` in the new repository.
5. Run the validation commands.

```sh
python3 scripts/pm.py doctor
python3 -m unittest discover -s tests
```

GitHub Issues remain the canonical tickets. The repository stores project
design, decisions, learning records, and evidence pointers; implementation code
remains independently buildable elsewhere.

## License

MIT. See `LICENSE`.
