---
name: sf-integration-health-monitor
description: Use when you need to find brittle integration center, cpi, and odata jobs before downstream systems go stale.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, integration, agent-skill, consulting]
    related_skills: [sf-config-debt-workshop]
---

# Integration Health Monitor

Audits SuccessFactors integration jobs for failure patterns, stale schedules, missing owners, weak retry handling, payload drift, and downstream data freshness risks. Covers Integration Center, CPI/iFlow, scheduled exports, API consumers, and middleware dependencies. Produces a practical operations dashboard and runbook for HRIS support.

## When to Use

- Find brittle Integration Center, CPI, and OData jobs before downstream systems go stale.
- Client asks for an evidence-backed review in the Integration area
- Preparing a workshop, release gate, audit pack, or remediation plan
- Converting raw SF configuration into a client-safe recommendation

## Prerequisites

- Inputs: Integration Center job list, CPI iFlow inventory, OData error logs, schedule details
- Expected outputs: Integration risk dashboard, stale-data map, failure pattern report, runbook fixes
- Confirm client audience and whether output should be board-level, technical, or mixed
- Never store credentials or employee-sensitive data in the repo or final deliverable

## Workflow

1. **Inventory** - gather evidence, classify impact, and create a client-safe output.
2. **Error Pattern** - gather evidence, classify impact, and create a client-safe output.
3. **Freshness Check** - gather evidence, classify impact, and create a client-safe output.
4. **Runbook** - gather evidence, classify impact, and create a client-safe output.

## Analysis Checklist

- Confirm the configuration objects and source tenant/snapshot date
- Separate configuration evidence from assumptions
- Score findings by business impact, not just technical severity
- Group repeated findings into themes so the client gets a short action list
- Flag internal-only notes before writing the client-facing summary
- Produce remediation actions with owner, effort, dependency, and success metric

## Edge Cases

- **Job succeeds but sends zero records**: validate explicitly before final recommendation
- **Payload schema changed without job failure**: validate explicitly before final recommendation
- **Time-zone schedule drift around daylight saving**: validate explicitly before final recommendation
- **Downstream endpoint accepts file but rejects rows later**: validate explicitly before final recommendation
- **Multiple jobs update the same target system**: validate explicitly before final recommendation
- **Credential expiry date not visible in SF job list**: validate explicitly before final recommendation

## Example Prompt

> Audit our SF integrations and show which jobs are brittle, failing silently, or causing stale downstream data.

## Example Output Shape

58 integrations reviewed. 7 high-risk jobs, 11 medium-risk jobs. Top risk: nightly cost center export reports success but has sent zero rows for 9 days after a picklist filter change. Recommended action: add freshness check, owner alert, and row-count threshold before payroll cut-off.

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
