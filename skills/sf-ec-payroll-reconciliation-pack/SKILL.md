---
name: sf-ec-payroll-reconciliation-pack
description: Use when you need to compare ec configuration against payroll expectations so employee changes do not create pay errors.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, time-and-payroll, agent-skill, consulting]
    related_skills: [sf-config-debt-workshop]
---

# EC to Payroll Reconciliation Pack

Creates a payroll reconciliation pack that checks whether Employee Central changes produce the fields, events, pay components, cost centres, and effective dates payroll expects. Focuses on configuration and mapping alignment, not storing payroll amounts. Flags event reason mismatch, missing pay components, stale payroll area mappings, effective date overlaps, and cut-off risks before payroll processing.

## When to Use

- Compare EC configuration against payroll expectations so employee changes do not create pay errors.
- Client needs a practical review in the Time and Payroll area
- Preparing a release, audit, workshop, UAT pack, or remediation plan
- Translating SF configuration risk into business language

## Prerequisites

- Inputs: EC job/person/pay field mappings, payroll interface spec, event reason mappings, pay component setup
- Expected outputs: Payroll reconciliation checklist, mismatch categories, cut-off readiness score, exception plan
- Confirm tenant/snapshot date and audience before analysis
- Do not store credentials, employee-sensitive data, or tenant exports in the repo

## Workflow

1. **Map** - gather evidence, assess impact, and produce the client-safe artefact.
2. **Compare** - gather evidence, assess impact, and produce the client-safe artefact.
3. **Score** - gather evidence, assess impact, and produce the client-safe artefact.
4. **Cut-Off Pack** - gather evidence, assess impact, and produce the client-safe artefact.

## Analysis Checklist

- Capture configuration evidence and source date
- Separate expected variation from defects
- Link every finding to business impact: payroll, compliance, hiring, reporting, integration, or employee experience
- Group repeated findings into themes
- Produce remediation actions with owner, effort, dependency, and validation step
- Flag internal-only observations separately from client-ready narrative

## Edge Cases

- **Retroactive job change after payroll cut-off**: validate explicitly and decide whether it is expected design or defect
- **Mid-period cost centre transfer**: validate explicitly and decide whether it is expected design or defect
- **Pay component starts before hire date**: validate explicitly and decide whether it is expected design or defect
- **Terminated employee receives future-dated change**: validate explicitly and decide whether it is expected design or defect
- **Global assignment split payroll**: validate explicitly and decide whether it is expected design or defect
- **Payroll provider expects label but SF sends externalCode**: validate explicitly and decide whether it is expected design or defect

## Example Prompt

> Create an EC to payroll reconciliation pack and show which mappings or event reasons could cause payroll errors this month.

## Example Output Shape

Payroll readiness: 74/100. 5 blockers: transfer event maps to wrong payroll action, 3 pay components missing wage-type mapping, 2 cost centre values inactive in payroll, and retro changes after cut-off have no exception workflow. Recommendation: no-go until blockers cleared.

## Common Pitfalls

1. **Treating all mismatches as defects**: Some differences are intentional by country, worker type, or process design.
2. **Ignoring effective dates**: Many SF issues only appear when future-dated and retroactive changes are included.
3. **Missing downstream systems**: Check payroll, onboarding, reporting, integrations, and approvals before recommending a fix.
4. **No owner or success metric**: A finding without owner, effort, and validation is not actionable.
5. **Using technical language with business stakeholders**: Translate every issue into risk, cost, time, or compliance impact.

## Verification Checklist

- [ ] Source evidence and snapshot date captured
- [ ] Edge cases reviewed explicitly
- [ ] Findings scored by severity and business impact
- [ ] Remediation plan includes owner, effort, dependency, and validation step
- [ ] Client-safe summary produced
- [ ] Internal-only notes separated
- [ ] UAT or follow-up validation pack included
