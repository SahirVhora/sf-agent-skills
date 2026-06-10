---
name: sf-works-council-privacy-pack
description: Use when you need to prepare a client-safe explanation of sf changes for works council, dpo, and privacy review.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, compliance, agent-skill, consulting]
    related_skills: [sf-config-debt-workshop]
---

# Works Council and Privacy Impact Pack

Turns a planned SuccessFactors change into a plain-English works council and privacy review pack. Explains what is changing, which employee data is affected, who can see it, why it is needed, whether automation or profiling is involved, and what safeguards exist. Especially useful for Germany, France, Netherlands, and other high-consultation environments.

## When to Use

- Prepare a client-safe explanation of SF changes for works council, DPO, and privacy review.
- Client needs a practical review in the Compliance area
- Preparing a release, audit, workshop, UAT pack, or remediation plan
- Translating SF configuration risk into business language

## Prerequisites

- Inputs: Change description, affected fields, affected populations, access roles, data flows, country scope
- Expected outputs: Privacy impact summary, works council briefing, data access matrix, consultation checklist
- Confirm tenant/snapshot date and audience before analysis
- Do not store credentials, employee-sensitive data, or tenant exports in the repo

## Workflow

1. **Change Scope** - gather evidence, assess impact, and produce the client-safe artefact.
2. **Data Map** - gather evidence, assess impact, and produce the client-safe artefact.
3. **Impact Summary** - gather evidence, assess impact, and produce the client-safe artefact.
4. **Consultation Pack** - gather evidence, assess impact, and produce the client-safe artefact.

## Analysis Checklist

- Capture configuration evidence and source date
- Separate expected variation from defects
- Link every finding to business impact: payroll, compliance, hiring, reporting, integration, or employee experience
- Group repeated findings into themes
- Produce remediation actions with owner, effort, dependency, and validation step
- Flag internal-only observations separately from client-ready narrative

## Edge Cases

- **Change affects monitoring or productivity signals**: validate explicitly and decide whether it is expected design or defect
- **Sensitive fields visible to managers**: validate explicitly and decide whether it is expected design or defect
- **Cross-border data transfer to non-EU processor**: validate explicitly and decide whether it is expected design or defect
- **Automated decision support or AI inference involved**: validate explicitly and decide whether it is expected design or defect
- **Works council requests field-level access matrix**: validate explicitly and decide whether it is expected design or defect
- **Local country process differs from global template**: validate explicitly and decide whether it is expected design or defect

## Example Prompt

> Create a works council and privacy impact pack for a new SF change that adds manager visibility to absence and performance indicators.

## Example Output Shape

Privacy impact: High. Works council attention areas: manager visibility of absence trend, performance indicator context, cross-border reporting to global HR. Pack includes field-level data matrix, purpose statement, safeguards, consultation questions, and recommended changes to reduce monitoring concern.

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
