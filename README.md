# SF Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/SahirVhora/sf-agent-skills/pulls)

**AI skills for SAP SuccessFactors consultants.** Turn messy configuration, migration risk, and workshop prep into repeatable AI-assisted workflows.

Ten production skills covering governance, data quality, data integrity, migration, consulting, and quality assurance. Each skill is a composable, auditable workflow that an AI agent can execute - with zero employee data extraction.

## Live Site

**[sahirvhora.github.io/sf-agent-skills](https://sahirvhora.github.io/sf-agent-skills/)** - Browse the skill catalog, see example outputs, and inspect edge-case coverage.

## Skills included

| # | Skill | Domain | Severity | Time |
|---|-------|--------|----------|------|
| 1 | Config Debt Workshop | Governance | HIGH | 15-25 min |
| 2 | Business Rule Risk Review | Governance | HIGH | 15-30 min |
| 3 | Position Integrity Review | Data Integrity | CRITICAL | 10-20 min |
| 4 | Migration Readiness Check | Migration | CRITICAL | 10-15 min |
| 5 | Picklist Rationalisation | Data Quality | MEDIUM | 8-12 min |
| 6 | Foundation Object Cleanup | Data Quality | HIGH | 12-20 min |
| 7 | Client Discovery Questions | Consulting | MEDIUM | 5-10 min |
| 8 | 90-Day Remediation Roadmap | Consulting | HIGH | 5-8 min |
| 9 | Executive Summary Writer | Consulting | MEDIUM | 2-4 min |
| 10 | Test Scenario Generator | QA | HIGH | 8-15 min |

Each skill SKILL.md includes: prerequisites, full workflow steps, edge cases with handling, common pitfalls, and a verification checklist.

## How it works

1. A consultant needs to do something - run a config debt workshop, validate position data, prepare a migration.
2. They load the relevant skill into their AI agent (Hermes Agent, Claude Code, Cursor, etc.).
3. The agent follows the skill workflow: extracts what it needs, validates inputs, handles edge cases, and produces a structured, client-safe output.
4. The consultant reviews and delivers to the client.

## Zero-data-extraction guarantee

- No employee data is ever extracted, stored, or transmitted
- Skills operate on configuration metadata and schema only
- Tenant credentials are never persisted or logged
- Output is client-safe by default; internal technical notes are flagged separately

## For non-technical consultants

This is an AI skill pack - think of it as a recipe book for AI assistants. You don't need to write code. You install the skills, point your AI assistant at the tenant or files, and ask for the deliverable in plain English. Each skill produces a structured, reviewed output you can share directly with clients.

See the [live catalog](https://sahirvhora.github.io/sf-agent-skills/) for example prompts and outputs for every skill.

## Installation

### Hermes Agent

```bash
# Clone the repo
git clone https://github.com/SahirVhora/sf-agent-skills.git

# Copy skills to Hermes
cp -r sf-agent-skills/skills/* ~/.hermes/skills/
```

Then in Hermes: "Run the sf-config-debt-workshop skill against our tenant."

### Claude Code

```bash
# Copy skills to Claude skills directory
cp -r sf-agent-skills/skills/* ~/.claude/skills/
```

### Cursor

Add the skills directory to your project's `.cursorrules` or load individual SKILL.md files into the agent context.

## Repo structure

```
sf-agent-skills/
  docs/
    index.html              # GitHub Pages skill catalog
    data/
      skill-catalog.json    # Machine-readable skill manifest
    assets/                 # OG images and static assets
    examples/               # Sample output examples
  skills/
    sf-config-debt-workshop/
      SKILL.md
    sf-position-integrity-review/
      SKILL.md
    sf-migration-readiness/
      SKILL.md
    ... (10 skills total)
  README.md
  .nojekyll
```

## Related projects

- [sf-config-debt-radar](https://github.com/SahirVhora/sf-config-debt-radar) - MCP server that powers the config debt scan tools
- [sf-metadata-vault](https://github.com/SahirVhora/sf-metadata-vault) - Browse and compare SF metadata
- [sf-position-integrity-checker](https://github.com/SahirVhora/sf-position-integrity-checker) - Position integrity validation

## Contributing

PRs welcome. Each skill follows a standard structure (see existing SKILL.md files). Add new skills that automate repeatable SAP SF consulting workflows. Include edge cases, pitfalls, and verification checklists.

## License

MIT - see [LICENSE](LICENSE)
