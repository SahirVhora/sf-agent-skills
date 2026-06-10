---
name: sf-workflow-stuck-item-triage
description: Use when you need to unblock approvals by finding stale approvers, invalid routes, and escalation gaps.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, operations, agent-skill, consulting]
    related_skills: [sf-config-debt-workshop]
---

# Workflow Stuck Item Triage

Analyses pending and failed workflows to identify why approvals are stuck. Detects inactive approvers, terminated managers, missing HRBP assignments, invalid dynamic roles, duplicate pending steps, escalation loops, and workflows blocked by future-dated job changes. Produces a prioritized triage queue and prevention improvements.

## When to Use

- Unblock approvals by finding stale approvers, invalid routes, and escalation gaps.
- Client asks for an evidence-backed review in the Operations area
- Preparing a workshop, release gate, audit pack, or remediation plan
- Converting raw SF configuration into a client-safe recommendation

## Prerequisites

- Inputs: Workflow instances, approver assignments, employee/job status, escalation rules
- Expected outputs: Stuck workflow queue, root-cause clusters, reassignment plan, prevention rules
- Confirm client audience and whether output should be board-level, technical, or mixed
- Never store credentials or employee-sensitive data in the repo or final deliverable

## Workflow

1. **Queue** - gather evidence, classify impact, and create a client-safe output.
2. **Root Cause** - gather evidence, classify impact, and create a client-safe output.
3. **Reassign** - gather evidence, classify impact, and create a client-safe output.
4. **Prevent** - gather evidence, classify impact, and create a client-safe output.

## Analysis Checklist

- Confirm the configuration objects and source tenant/snapshot date
- Separate configuration evidence from assumptions
- Score findings by business impact, not just technical severity
- Group repeated findings into themes so the client gets a short action list
- Flag internal-only notes before writing the client-facing summary
- Produce remediation actions with owner, effort, dependency, and success metric

## Edge Cases

- **Approver is active but on long-term leave**: validate explicitly before final recommendation
- **Dynamic group resolves to zero people**: validate explicitly before final recommendation
- **Workflow stuck because manager change is future-dated**: validate explicitly before final recommendation
- **Mass approvals during reorg**: validate explicitly before final recommendation
- **Duplicate pending workflows from resubmission**: validate explicitly before final recommendation
- **Country-specific workflow path missing backup approver**: validate explicitly before final recommendation

## Example Prompt

> Find all stuck SF workflows and give us the root causes plus the quickest way to unblock them.

## Example Output Shape

319 open workflow items reviewed. 42 are stale over 14 days. Root causes: 18 terminated approvers, 9 empty dynamic roles, 7 escalation loops, 8 future-dated manager dependencies. Immediate unblock: reassign 27 items to HR Operations queue and correct 3 dynamic role definitions.

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
