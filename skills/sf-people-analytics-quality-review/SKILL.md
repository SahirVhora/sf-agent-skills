---
name: sf-people-analytics-quality-review
description: Use when you need to check whether reports are trusted, performant, governed, and safe to use for decisions.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, analytics, agent-skill, consulting]
    related_skills: [sf-config-debt-workshop]
---

# People Analytics Quality Review

Reviews People Analytics, Report Center, and story reports for duplicate reports, stale owners, missing data definitions, weak filters, row-level security gaps, slow queries, and inconsistent KPI logic. Produces a report rationalisation plan and governance model so HR leaders know which dashboards to trust.

## When to Use

- Check whether reports are trusted, performant, governed, and safe to use for decisions.
- Client asks for an evidence-backed review in the Analytics area
- Preparing a workshop, release gate, audit pack, or remediation plan
- Converting raw SF configuration into a client-safe recommendation

## Prerequisites

- Inputs: Report catalog, story definitions, user access, refresh schedules, business KPIs
- Expected outputs: Report health score, duplicate report map, data trust issues, governance actions
- Confirm client audience and whether output should be board-level, technical, or mixed
- Never store credentials or employee-sensitive data in the repo or final deliverable

## Workflow

1. **Catalog** - gather evidence, classify impact, and create a client-safe output.
2. **Trust Check** - gather evidence, classify impact, and create a client-safe output.
3. **Performance** - gather evidence, classify impact, and create a client-safe output.
4. **Governance** - gather evidence, classify impact, and create a client-safe output.

## Analysis Checklist

- Confirm the configuration objects and source tenant/snapshot date
- Separate configuration evidence from assumptions
- Score findings by business impact, not just technical severity
- Group repeated findings into themes so the client gets a short action list
- Flag internal-only notes before writing the client-facing summary
- Produce remediation actions with owner, effort, dependency, and success metric

## Edge Cases

- **Two reports use same title but different filters**: validate explicitly before final recommendation
- **Owner left the business**: validate explicitly before final recommendation
- **Report includes terminated employees unexpectedly**: validate explicitly before final recommendation
- **Country filter missing for works council region**: validate explicitly before final recommendation
- **Story dashboard joins incompatible datasets**: validate explicitly before final recommendation
- **Scheduled report sends sensitive data to large group**: validate explicitly before final recommendation

## Example Prompt

> Review our People Analytics reports and tell us which dashboards are safe, duplicated, or misleading.

## Example Output Shape

184 reports reviewed. 39 duplicates, 22 stale owners, 14 reports with sensitive fields sent by schedule, 9 KPI conflicts. Recommendation: retire 51 reports, certify 23 executive dashboards, and add report owner review every quarter.

## Common Pitfalls

1. **Delivering raw technical noise**: Summarise by business impact and put raw details in an appendix.
2. **Ignoring country or legal-entity variation**: Many SF issues are only defects in one population.
3. **Missing downstream impact**: Always map the finding to payroll, compliance, reporting, integration, or user experience.
4. **No rollback plan**: Every remediation step needs a safe fallback.
5. **No validation step**: Re-run the relevant check after fixing config and compare before/after evidence.

## Verification Checklist

- [ ] Source evidence captured with tenant/snapshot date
- [ ] Findings scored by severity and business impact
- [ ] Edge cases reviewed explicitly
- [ ] Remediation actions include owner, effort, dependency, and success metric
- [ ] Client-safe summary produced
- [ ] Internal-only notes separated
- [ ] Follow-up validation plan included
