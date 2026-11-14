#!/usr/bin/env python3
"""Generate the GitHub Pages skill catalog JSON from the published site data.

Usage:
    python scripts/generate_catalog.py          # rewrite docs/data/skill-catalog.json
    python scripts/generate_catalog.py --check  # fail if the catalog is missing or stale
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "docs" / "index.html"
CATALOG_PATH = ROOT / "docs" / "data" / "skill-catalog.json"
REQUIRED_FIELDS = {
    "id",
    "name",
    "tagline",
    "category",
    "severity",
    "inputs",
    "outputs",
    "time",
    "phases",
    "detail",
    "edgeCases",
    "prompt",
    "exampleOutput",
}


def load_inline_skills() -> list[dict]:
    html = INDEX_PATH.read_text(encoding="utf-8")
    match = re.search(r"var allSkills = (\[.*?\]);", html, re.S)
    if not match:
        raise RuntimeError("Could not find inline allSkills array in docs/index.html")
    skills = json.loads(match.group(1))
    if not isinstance(skills, list):
        raise RuntimeError("Inline allSkills value is not a list")
    return skills


def validate_skills(skills: list[dict]) -> None:
    skill_ids = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
    catalog_ids = {skill.get("id") for skill in skills}
    missing_from_catalog = sorted(skill_ids - catalog_ids)
    missing_from_disk = sorted(catalog_ids - skill_ids)
    if missing_from_catalog:
        raise RuntimeError(
            "Skill directories missing from catalog: " + ", ".join(missing_from_catalog)
        )
    if missing_from_disk:
        raise RuntimeError(
            "Catalog entries missing SKILL.md files: " + ", ".join(missing_from_disk)
        )
    for skill in skills:
        missing_fields = sorted(REQUIRED_FIELDS - set(skill))
        if missing_fields:
            raise RuntimeError(
                f"Skill {skill.get('id', '?')} missing fields: "
                + ", ".join(missing_fields)
            )


def check_catalog(skills: list[dict]) -> int:
    """Fail if the committed catalog is missing or out of step with the site."""
    if not CATALOG_PATH.exists():
        print(f"FAIL: {CATALOG_PATH.relative_to(ROOT)} is missing. "
              "Run: python scripts/generate_catalog.py")
        return 1
    try:
        committed = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        print(f"FAIL: {CATALOG_PATH.relative_to(ROOT)} is not valid JSON: {exc}")
        return 1
    problems = []
    if committed.get("skills") != skills:
        problems.append("skills differ from docs/index.html allSkills")
    meta = committed.get("metadata", {})
    if meta.get("totalSkills") != len(skills):
        problems.append(
            f"metadata.totalSkills is {meta.get('totalSkills')}, expected {len(skills)}"
        )
    if meta.get("categories") != sorted({s["category"] for s in skills}):
        problems.append("metadata.categories out of date")
    if problems:
        print("FAIL: skill-catalog.json is out of date: " + "; ".join(problems))
        print("Run: python scripts/generate_catalog.py and commit the result")
        return 1
    print(f"PASS: skill-catalog.json matches docs/index.html ({len(skills)} skills)")
    return 0


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    skills = load_inline_skills()
    validate_skills(skills)
    if "--check" in argv:
        return check_catalog(skills)
    categories = sorted({skill["category"] for skill in skills})
    catalog = {
        "metadata": {
            "generatedAt": datetime.now(timezone.utc)
            .replace(microsecond=0)
            .isoformat(),
            "source": "docs/index.html inline allSkills",
            "totalSkills": len(skills),
            "categories": categories,
        },
        "skills": skills,
    }
    CATALOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CATALOG_PATH.write_text(
        json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {CATALOG_PATH.relative_to(ROOT)} ({len(skills)} skills)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
