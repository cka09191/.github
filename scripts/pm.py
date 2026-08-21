#!/usr/bin/env python3
"""Small, dependency-free project-management repository helper."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PROJECT_KEYS = {
    "version",
    "project_key",
    "display_name",
    "management_repository",
    "implementation_repository",
    "portfolio_owner",
    "portfolio_project_number",
    "default_human",
    "issue_form_source",
    "policy_version",
}
REQUIRED_FORMS = {"work-item.yml", "proposal.yml", "decision.yml", "config.yml"}


def load_project() -> dict[str, object]:
    path = ROOT / "config" / "project.json"
    if not path.exists():
        path = ROOT / "config" / "project.example.json"
    return json.loads(path.read_text(encoding="utf-8"))


def doctor() -> int:
    errors: list[str] = []
    project = load_project()
    missing = sorted(REQUIRED_PROJECT_KEYS - project.keys())
    if missing:
        errors.append(f"project config missing keys: {', '.join(missing)}")
    if project.get("version") != 1:
        errors.append("project config version must be 1")
    labels = json.loads((ROOT / "config" / "labels.json").read_text(encoding="utf-8"))
    names = [item.get("name") for item in labels.get("labels", [])]
    if not names or len(names) != len(set(names)):
        errors.append("labels must be non-empty and unique")
    form_dir = ROOT / ".github" / "ISSUE_TEMPLATE"
    found_forms = {path.name for path in form_dir.glob("*.yml")}
    missing_forms = sorted(REQUIRED_FORMS - found_forms)
    if missing_forms and not project.get("issue_form_source"):
        errors.append(f"missing issue forms: {', '.join(missing_forms)}")
    if errors:
        for error in errors:
            print(f"FAIL {error}", file=sys.stderr)
        return 1
    form_mode = "local" if not missing_forms else f"inherited:{project['issue_form_source']}"
    print(
        f"OK project={project['project_key']} policy={project['policy_version']} "
        f"forms={form_mode}"
    )
    return 0


def gh_issue_list(label: str | None = None) -> int:
    project = load_project()
    command = [
        "gh",
        "issue",
        "list",
        "--repo",
        str(project["management_repository"]),
        "--limit",
        "100",
        "--json",
        "number,title,state,labels,assignees,updatedAt,url",
    ]
    if label:
        command.extend(["--label", label])
    result = subprocess.run(command, check=False)
    return result.returncode


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("doctor")
    subparsers.add_parser("list")
    subparsers.add_parser("user-candidates")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.command == "doctor":
        return doctor()
    if args.command == "list":
        return gh_issue_list()
    return gh_issue_list("owner:user")


if __name__ == "__main__":
    raise SystemExit(main())
