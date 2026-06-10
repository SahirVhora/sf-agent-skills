---
name: sf-release-impact-triage
description: Use when you need to turn sap release notes into a tenant-specific test plan and stakeholder briefing.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, release-governance, agent-skill, consulting]
    related_skills: [sf-config-debt-workshop]
---

# Release Impact Triage

Reads SAP SuccessFactors release content and maps each item to the modules and configuration patterns used by the client. Separates action-required, review-and-test, and informational items. Produces a compact triage board with owners, regression tests, change communications, and watch items for the release weekend.

## When to Use

- Turn SAP release notes into a tenant-specific test plan and stakeholder briefing.
- Client asks for an evidence-backed review in the Release Governance area
- Preparing a workshop, release gate, audit pack, or remediation plan
- Converting raw SF configuration into a client-safe recommendation

## Prerequisites

- Inputs: SAP release notes, enabled modules, tenant config summary, previous incidents
- Expected outputs: Impact matrix, regression test scope, owner list, executive change brief
- Confirm client audience and whether output should be board-level, technical, or mixed
- Never store credentials or employee-sensitive data in the repo or final deliverable

## Workflow

1. **Parse Notes** - gather evidence, classify impact, and create a client-safe output.
2. **Match Tenant** - gather evidence, classify impact, and create a client-safe output.
3. **Prioritise** - gather evidence, classify impact, and create a client-safe output.
4. **Test Plan** - gather evidence, classify impact, and create a client-safe output.

## Analysis Checklist

- Confirm the configuration objects and source tenant/snapshot date
- Separate configuration evidence from assumptions
- Score findings by business impact, not just technical severity
- Group repeated findings into themes so the client gets a short action list
- Flag internal-only notes before writing the client-facing summary
- Produce remediation actions with owner, effort, dependency, and success metric

## Edge Cases

- **Feature auto-enabled by SAP**: validate explicitly before final recommendation
- **Module licensed but not actively used**: validate explicitly before final recommendation
- **Localized change applies only to one country**: validate explicitly before final recommendation
- **Deprecated feature still used in old process**: validate explicitly before final recommendation
- **Regression test owner unknown**: validate explicitly before final recommendation
- **Preview tenant data too stale for meaningful test**: validate explicitly before final recommendation

## Example Prompt

> Review the latest SF release notes against our enabled modules and produce a regression test plan.

## Example Output Shape

76 release items triaged. Action required: 6, review and test: 19, informational: 51. Top item: Time Tracking validation change impacts UK hourly population, regression tests assigned to Payroll Ops and HRIS. Executive brief: 3 key risks and release weekend checkpoint plan.

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
