#!/usr/bin/env python3
"""Generate the GitHub Pages skill catalog JSON from the published site data."""

from __future__ import annotations

import json
import re
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


def main() -> int:
    skills = load_inline_skills()
    validate_skills(skills)
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
