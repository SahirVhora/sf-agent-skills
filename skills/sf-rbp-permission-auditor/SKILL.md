---
name: sf-rbp-permission-auditor
description: Use when you need to detect over-permissioned roles, hidden access paths, and sod risks before audit season.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, security, agent-skill, consulting]
    related_skills: [sf-config-debt-workshop]
---

# RBP Permission Auditor

Audits SuccessFactors Role-Based Permissions across roles, groups, target populations, proxy settings, and sensitive admin grants. Flags excessive admin access, employee-data visibility beyond business need, toxic combinations such as compensation plus personal data export, and permission drift between sandbox and production. Produces a client-safe access-risk pack for HRIS, IT security, and audit stakeholders.

## When to Use

- Detect over-permissioned roles, hidden access paths, and SoD risks before audit season.
- Client asks for an evidence-backed review in the Security area
- Preparing a workshop, release gate, audit pack, or remediation plan
- Converting raw SF configuration into a client-safe recommendation

## Prerequisites

- Inputs: Role, group, target population, proxy, and permission export snapshots
- Expected outputs: Permission risk matrix, toxic-combination report, remediation plan, sign-off pack
- Confirm client audience and whether output should be board-level, technical, or mixed
- Never store credentials or employee-sensitive data in the repo or final deliverable

## Workflow

1. **Inventory** - gather evidence, classify impact, and create a client-safe output.
2. **Probe** - gather evidence, classify impact, and create a client-safe output.
3. **Score** - gather evidence, classify impact, and create a client-safe output.
4. **Remediate** - gather evidence, classify impact, and create a client-safe output.

## Analysis Checklist

- Confirm the configuration objects and source tenant/snapshot date
- Separate configuration evidence from assumptions
- Score findings by business impact, not just technical severity
- Group repeated findings into themes so the client gets a short action list
- Flag internal-only notes before writing the client-facing summary
- Produce remediation actions with owner, effort, dependency, and success metric

## Edge Cases

- **Dynamic groups with stale membership**: validate explicitly before final recommendation
- **Target populations that include terminated users**: validate explicitly before final recommendation
- **Proxy access bypassing normal manager visibility**: validate explicitly before final recommendation
- **Permission roles inherited through multiple groups**: validate explicitly before final recommendation
- **Emergency admin roles never removed**: validate explicitly before final recommendation
- **Country-specific data visibility exceptions**: validate explicitly before final recommendation

## Example Prompt

> Audit our SF RBP setup and show which roles create access or segregation-of-duty risks.

## Example Output Shape

126 permission roles reviewed. CRITICAL: 5, HIGH: 17. Top risk: HR Operations role grants export access to compensation and national ID fields for all employees, including countries outside support scope. Immediate action: split role by country and remove export permission pending DPO review.

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
