---
name: sf-event-reason-decision-tree
description: Use when you need to validate hire, rehire, transfer, promotion, termination, and job-change event reason logic before it breaks downstream processes.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, employee-central, agent-skill, consulting]
    related_skills: [sf-config-debt-workshop]
---

# EC Event Reason Decision Tree

Audits Employee Central event and event reason configuration so every hire, rehire, termination, transfer, promotion, leave, and data correction follows a defensible decision path. Detects duplicate event reasons, missing scenarios, wrong event categories, workflow trigger mismatches, payroll-impacting event errors, and integration mappings that rely on outdated eventReason values.

## When to Use

- Validate hire, rehire, transfer, promotion, termination, and job-change event reason logic before it breaks downstream processes.
- Client needs a practical review in the Employee Central area
- Preparing a release, audit, workshop, UAT pack, or remediation plan
- Translating SF configuration risk into business language

## Prerequisites

- Inputs: Event reason list, event derivation rules, workflow triggers, payroll/integration mappings
- Expected outputs: Decision tree, conflict report, missing event reason map, UAT scenarios
- Confirm tenant/snapshot date and audience before analysis
- Do not store credentials, employee-sensitive data, or tenant exports in the repo

## Workflow

1. **Inventory** - gather evidence, assess impact, and produce the client-safe artefact.
2. **Decision Tree** - gather evidence, assess impact, and produce the client-safe artefact.
3. **Conflict Check** - gather evidence, assess impact, and produce the client-safe artefact.
4. **UAT Pack** - gather evidence, assess impact, and produce the client-safe artefact.

## Analysis Checklist

- Capture configuration evidence and source date
- Separate expected variation from defects
- Link every finding to business impact: payroll, compliance, hiring, reporting, integration, or employee experience
- Group repeated findings into themes
- Produce remediation actions with owner, effort, dependency, and validation step
- Flag internal-only observations separately from client-ready narrative

## Edge Cases

- **Rehire with new employment vs rehire on old employment**: validate explicitly and decide whether it is expected design or defect
- **Data correction using business event reason**: validate explicitly and decide whether it is expected design or defect
- **Promotion plus transfer in same effective-dated change**: validate explicitly and decide whether it is expected design or defect
- **Global assignment start/end events**: validate explicitly and decide whether it is expected design or defect
- **Termination followed by rescind or no-show**: validate explicitly and decide whether it is expected design or defect
- **Country-specific event reason overrides**: validate explicitly and decide whether it is expected design or defect

## Example Prompt

> Build an EC event reason decision tree and show where our hire, rehire, transfer, promotion, and termination logic conflicts.

## Example Output Shape

92 event reasons reviewed. CRITICAL: 4, HIGH: 9. Top issue: promotion and transfer both map to DATACHG for payroll export, making downstream payroll unable to distinguish salary-impacting changes. Decision tree created with 37 valid paths and 6 missing event reasons.

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
