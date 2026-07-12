#!/usr/bin/env python3
"""Evaluate minimum evidence contracts for flagship SF agent skills."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "evaluations" / "flagship_contracts.json"


def evaluate() -> list[str]:
    contracts = json.loads(CONTRACTS.read_text(encoding="utf-8"))
    failures: list[str] = []
    for contract in contracts:
        skill_id = contract["skill"]
        skill_path = ROOT / "skills" / skill_id / "SKILL.md"
        if not skill_path.exists():
            failures.append(f"{skill_id}: missing SKILL.md")
            continue
        content = skill_path.read_text(encoding="utf-8").lower()
        missing = [term for term in contract["required_concepts"] if term.lower() not in content]
        if missing:
            failures.append(f"{skill_id}: missing contract concepts: {', '.join(missing)}")
        else:
            print(f"PASS: {skill_id} ({len(contract['required_concepts'])} controls)")
    return failures


def main() -> int:
    failures = evaluate()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("\nAll flagship evidence contracts passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
