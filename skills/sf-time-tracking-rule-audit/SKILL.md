---
name: sf-time-tracking-rule-audit
description: Use when you need to audit time valuation, holiday calendars, overtime logic, and payroll handoff risks.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, time-and-payroll, agent-skill, consulting]
    related_skills: [sf-config-debt-workshop]
---

# Time Tracking Rule Audit

Reviews Time Tracking configuration for payroll-impacting errors: incorrect holiday calendars, missing time profiles, overtime threshold mismatches, break deductions, cross-midnight shifts, time account posting logic, and payroll wage-type mappings. Produces a regression test pack and payroll cut-off risk report.

## When to Use

- Audit time valuation, holiday calendars, overtime logic, and payroll handoff risks.
- Client asks for an evidence-backed review in the Time and Payroll area
- Preparing a workshop, release gate, audit pack, or remediation plan
- Converting raw SF configuration into a client-safe recommendation

## Prerequisites

- Inputs: Time profiles, time valuation rules, work schedules, holiday calendars, payroll mappings
- Expected outputs: Time rule risk report, payroll handoff checks, country exception map, UAT scenarios
- Confirm client audience and whether output should be board-level, technical, or mixed
- Never store credentials or employee-sensitive data in the repo or final deliverable

## Workflow

1. **Calendar** - gather evidence, classify impact, and create a client-safe output.
2. **Rule Logic** - gather evidence, classify impact, and create a client-safe output.
3. **Payroll Mapping** - gather evidence, classify impact, and create a client-safe output.
4. **Regression** - gather evidence, classify impact, and create a client-safe output.

## Analysis Checklist

- Confirm the configuration objects and source tenant/snapshot date
- Separate configuration evidence from assumptions
- Score findings by business impact, not just technical severity
- Group repeated findings into themes so the client gets a short action list
- Flag internal-only notes before writing the client-facing summary
- Produce remediation actions with owner, effort, dependency, and success metric

## Edge Cases

- **Cross-midnight shift spanning two pay periods**: validate explicitly before final recommendation
- **Public holiday differs by region**: validate explicitly before final recommendation
- **Overtime rule changes mid-year**: validate explicitly before final recommendation
- **Employee transfers country during time period**: validate explicitly before final recommendation
- **Absence overlaps recorded working time**: validate explicitly before final recommendation
- **Rounding rule differs between SF and payroll**: validate explicitly before final recommendation

## Example Prompt

> Audit our SF Time Tracking rules and tell us what could cause payroll errors.

## Example Output Shape

92 time rules reviewed across 7 countries. CRITICAL: 3, HIGH: 11. Top risk: UK night-shift rule posts overtime after 8 hours but payroll expects threshold at 7.5 hours, creating underpayment risk. Regression pack: 44 scenarios covering holidays, overtime, absences, and transfers.

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
