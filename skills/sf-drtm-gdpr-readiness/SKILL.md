---
name: sf-drtm-gdpr-readiness
description: Use when you need to check whether data retention rules are configured, defensible, and safe to execute.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, compliance, agent-skill, consulting]
    related_skills: [sf-config-debt-workshop]
---

# DRTM and GDPR Readiness

Assesses Data Retention Time Management configuration against GDPR and local retention policies. Checks whether countries, legal entities, employee groups, and data domains have retention rules, whether retention periods conflict with policy, and whether purge jobs could delete data needed for payroll, litigation hold, or statutory reporting. Produces a compliance-ready sign-off pack.

## When to Use

- Check whether data retention rules are configured, defensible, and safe to execute.
- Client asks for an evidence-backed review in the Compliance area
- Preparing a workshop, release gate, audit pack, or remediation plan
- Converting raw SF configuration into a client-safe recommendation

## Prerequisites

- Inputs: DRTM config, legal entity/country list, retention policies, purge simulation output
- Expected outputs: Retention coverage map, purge risk report, legal sign-off checklist, remediation plan
- Confirm client audience and whether output should be board-level, technical, or mixed
- Never store credentials or employee-sensitive data in the repo or final deliverable

## Workflow

1. **Policy Map** - gather evidence, classify impact, and create a client-safe output.
2. **Coverage Check** - gather evidence, classify impact, and create a client-safe output.
3. **Purge Simulation** - gather evidence, classify impact, and create a client-safe output.
4. **Sign-Off** - gather evidence, classify impact, and create a client-safe output.

## Analysis Checklist

- Confirm the configuration objects and source tenant/snapshot date
- Separate configuration evidence from assumptions
- Score findings by business impact, not just technical severity
- Group repeated findings into themes so the client gets a short action list
- Flag internal-only notes before writing the client-facing summary
- Produce remediation actions with owner, effort, dependency, and success metric

## Edge Cases

- **Employees with multiple employments across countries**: validate explicitly before final recommendation
- **Legal hold exceptions**: validate explicitly before final recommendation
- **Historical payroll dependencies**: validate explicitly before final recommendation
- **Terminated employees rehired after purge window**: validate explicitly before final recommendation
- **Country-specific retention overrides**: validate explicitly before final recommendation
- **Incomplete purge simulation logs**: validate explicitly before final recommendation

## Example Prompt

> Review our DRTM setup and tell us if we are safe to run purge jobs this quarter.

## Example Output Shape

Coverage score: 71/100. 8 countries lack approved retention rules, 3 legal entities have conflicting purge windows, and payroll evidence retention is shorter than Finance policy in Spain. Recommendation: stop purge run until legal sign-off and payroll dependency exception list are updated.

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
