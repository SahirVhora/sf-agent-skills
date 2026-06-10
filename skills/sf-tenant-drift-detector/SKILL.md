---
name: sf-tenant-drift-detector
description: Use when you need to compare sandbox and production so releases do not fail because the tenants quietly diverged.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, release-governance, agent-skill, consulting]
    related_skills: [sf-config-debt-workshop]
---

# Tenant Drift Detector

Compares configuration snapshots across preview, test, staging, and production tenants. Detects changes in business rules, picklists, foundation objects, MDF objects, event reasons, workflows, RBP roles, and metadata fields. Classifies each drift item by release impact and whether it is intentional, missing transport, hotfix, or unknown. Produces a release gate decision with blockers and recommended reconciliation order.

## When to Use

- Compare sandbox and production so releases do not fail because the tenants quietly diverged.
- Client asks for an evidence-backed review in the Release Governance area
- Preparing a workshop, release gate, audit pack, or remediation plan
- Converting raw SF configuration into a client-safe recommendation

## Prerequisites

- Inputs: Metadata/config snapshots from two or more SF tenants
- Expected outputs: Drift report, release risk score, deploy blockers, rollback watchlist
- Confirm client audience and whether output should be board-level, technical, or mixed
- Never store credentials or employee-sensitive data in the repo or final deliverable

## Workflow

1. **Snapshot** - gather evidence, classify impact, and create a client-safe output.
2. **Diff** - gather evidence, classify impact, and create a client-safe output.
3. **Classify** - gather evidence, classify impact, and create a client-safe output.
4. **Release Gate** - gather evidence, classify impact, and create a client-safe output.

## Analysis Checklist

- Confirm the configuration objects and source tenant/snapshot date
- Separate configuration evidence from assumptions
- Score findings by business impact, not just technical severity
- Group repeated findings into themes so the client gets a short action list
- Flag internal-only notes before writing the client-facing summary
- Produce remediation actions with owner, effort, dependency, and success metric

## Edge Cases

- **Intentional hotfix in production**: validate explicitly before final recommendation
- **Preview tenant upgraded before production**: validate explicitly before final recommendation
- **Different country rollout scope per tenant**: validate explicitly before final recommendation
- **Inactive config present in only one tenant**: validate explicitly before final recommendation
- **Config Center export missing some objects**: validate explicitly before final recommendation
- **Emergency release overlapping SAP release cycle**: validate explicitly before final recommendation

## Example Prompt

> Compare our preview and production SF tenants and tell us what drift could break the next release.

## Example Output Shape

412 objects compared. 37 drift items found: 4 blockers, 12 review required, 21 informational. Top blocker: business rule BR-HIRE-014 differs between preview and production and writes different eventReason values on hire. Release gate: no-go until production hotfix is reconciled.

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
