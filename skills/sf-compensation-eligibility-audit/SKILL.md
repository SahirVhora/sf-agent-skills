---
name: sf-compensation-eligibility-audit
description: Use when you need to catch worksheet eligibility, proration, budget, and guideline logic before compensation planning opens.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, compensation, agent-skill, consulting]
    related_skills: [sf-config-debt-workshop]
---

# Compensation Eligibility Audit

Audits Compensation and Variable Pay configuration before cycle launch. Checks eligibility rules, guideline formulas, proration logic, currency conversion, budget allocation, route maps, executive review permissions, and worksheet population rules. Produces a readiness score and cycle-launch test plan.

## When to Use

- Catch worksheet eligibility, proration, budget, and guideline logic before compensation planning opens.
- Client asks for an evidence-backed review in the Compensation area
- Preparing a workshop, release gate, audit pack, or remediation plan
- Converting raw SF configuration into a client-safe recommendation

## Prerequisites

- Inputs: Compensation template config, eligibility rules, proration settings, budget model, employee sample
- Expected outputs: Eligibility risk matrix, worksheet test plan, budget/proration checks, executive readiness score
- Confirm client audience and whether output should be board-level, technical, or mixed
- Never store credentials or employee-sensitive data in the repo or final deliverable

## Workflow

1. **Eligibility** - gather evidence, classify impact, and create a client-safe output.
2. **Proration** - gather evidence, classify impact, and create a client-safe output.
3. **Budget** - gather evidence, classify impact, and create a client-safe output.
4. **Worksheet UAT** - gather evidence, classify impact, and create a client-safe output.

## Analysis Checklist

- Confirm the configuration objects and source tenant/snapshot date
- Separate configuration evidence from assumptions
- Score findings by business impact, not just technical severity
- Group repeated findings into themes so the client gets a short action list
- Flag internal-only notes before writing the client-facing summary
- Produce remediation actions with owner, effort, dependency, and success metric

## Edge Cases

- **Employee changes job mid-cycle**: validate explicitly before final recommendation
- **Global assignment with multiple currencies**: validate explicitly before final recommendation
- **Eligibility based on custom field with blanks**: validate explicitly before final recommendation
- **Manager has direct and matrix reports**: validate explicitly before final recommendation
- **Leave of absence affects proration**: validate explicitly before final recommendation
- **Budget owner changes after worksheets generate**: validate explicitly before final recommendation

## Example Prompt

> Audit our compensation cycle setup before launch and show what could break worksheets or budgets.

## Example Output Shape

Cycle readiness: 78/100. 4 launch blockers: blank eligibility field excludes 312 employees, proration formula overpays LOA population, EUR to GBP conversion table stale, and executive worksheet role grants edit access instead of view-only. Recommended action: fix blockers before forms launch.

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
