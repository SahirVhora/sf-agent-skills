---
name: sf-onboarding-compliance-review
description: Use when you need to validate forms, tasks, document flows, and local compliance before new hires start.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, onboarding, agent-skill, consulting]
    related_skills: [sf-config-debt-workshop]
---

# Onboarding Compliance Review

Audits SuccessFactors Onboarding 2.0 processes for missing forms, country-specific compliance gaps, task assignment failures, document template drift, duplicate new-hire tasks, and handoff breaks between Recruiting, Onboarding, and EC. Produces a country-by-country readiness matrix and UAT pack.

## When to Use

- Validate forms, tasks, document flows, and local compliance before new hires start.
- Client asks for an evidence-backed review in the Onboarding area
- Preparing a workshop, release gate, audit pack, or remediation plan
- Converting raw SF configuration into a client-safe recommendation

## Prerequisites

- Inputs: Onboarding process config, task templates, compliance forms, country/localisation list
- Expected outputs: Compliance gap report, task coverage matrix, new-hire risk list, remediation actions
- Confirm client audience and whether output should be board-level, technical, or mixed
- Never store credentials or employee-sensitive data in the repo or final deliverable

## Workflow

1. **Process Map** - gather evidence, classify impact, and create a client-safe output.
2. **Form Coverage** - gather evidence, classify impact, and create a client-safe output.
3. **Task Logic** - gather evidence, classify impact, and create a client-safe output.
4. **Compliance Pack** - gather evidence, classify impact, and create a client-safe output.

## Analysis Checklist

- Confirm the configuration objects and source tenant/snapshot date
- Separate configuration evidence from assumptions
- Score findings by business impact, not just technical severity
- Group repeated findings into themes so the client gets a short action list
- Flag internal-only notes before writing the client-facing summary
- Produce remediation actions with owner, effort, dependency, and success metric

## Edge Cases

- **Remote hire with no office location**: validate explicitly before final recommendation
- **Cross-border hire moving between legal entities**: validate explicitly before final recommendation
- **Candidate data missing before EC hire conversion**: validate explicitly before final recommendation
- **Compliance form differs by province/state**: validate explicitly before final recommendation
- **Rehire uses old onboarding process**: validate explicitly before final recommendation
- **Task owner role resolves after start date**: validate explicitly before final recommendation

## Example Prompt

> Review our Onboarding setup for compliance and task coverage gaps across all countries.

## Example Output Shape

12 countries reviewed. 4 high-risk gaps: missing right-to-work task for UK remote hires, duplicate tax form in Canada, no fallback owner for equipment task, and rehire process skips policy acknowledgement. UAT pack includes 28 scenarios by country and worker type.

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
