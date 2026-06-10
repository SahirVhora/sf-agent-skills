---
name: sf-recruiting-offer-approval-audit
description: Use when you need to check rcm requisition templates, offer approvals, and handoff logic before hiring stalls.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, recruiting, agent-skill, consulting]
    related_skills: [sf-config-debt-workshop]
---

# Recruiting Requisition and Offer Approval Audit

Audits SAP SuccessFactors Recruiting configuration across requisition templates, offer approvals, route maps, candidate status transitions, field permissions, and Recruiting-to-Onboarding handoff. Flags inconsistent template fields, missing approvers, approval loops, offer fields not mapped to onboarding, candidate status dead-ends, and country-specific compliance gaps.

## When to Use

- Check RCM requisition templates, offer approvals, and handoff logic before hiring stalls.
- Client needs a practical review in the Recruiting area
- Preparing a release, audit, workshop, UAT pack, or remediation plan
- Translating SF configuration risk into business language

## Prerequisites

- Inputs: RCM requisition templates, offer approval rules, route maps, field permissions, onboarding handoff config
- Expected outputs: Template health report, approval path gaps, candidate handoff risks, hiring process UAT pack
- Confirm tenant/snapshot date and audience before analysis
- Do not store credentials, employee-sensitive data, or tenant exports in the repo

## Workflow

1. **Template Inventory** - gather evidence, assess impact, and produce the client-safe artefact.
2. **Approval Map** - gather evidence, assess impact, and produce the client-safe artefact.
3. **Handoff Check** - gather evidence, assess impact, and produce the client-safe artefact.
4. **UAT Pack** - gather evidence, assess impact, and produce the client-safe artefact.

## Analysis Checklist

- Capture configuration evidence and source date
- Separate expected variation from defects
- Link every finding to business impact: payroll, compliance, hiring, reporting, integration, or employee experience
- Group repeated findings into themes
- Produce remediation actions with owner, effort, dependency, and validation step
- Flag internal-only observations separately from client-ready narrative

## Edge Cases

- **Internal candidate follows different route map**: validate explicitly and decide whether it is expected design or defect
- **Offer approval differs by compensation threshold**: validate explicitly and decide whether it is expected design or defect
- **Hiring manager changes during requisition approval**: validate explicitly and decide whether it is expected design or defect
- **Candidate accepts offer after requisition is closed**: validate explicitly and decide whether it is expected design or defect
- **Country-specific offer letter fields missing**: validate explicitly and decide whether it is expected design or defect
- **Recruiting-to-Onboarding handoff fails for rehire**: validate explicitly and decide whether it is expected design or defect

## Example Prompt

> Audit our recruiting requisition templates and offer approval routing and show what could stall hiring or break onboarding handoff.

## Example Output Shape

23 requisition templates and 11 offer routes reviewed. HIGH: 8 issues. Top risk: UK senior role offer approval skips Finance when salary exceeds threshold because compensation field differs across templates. Handoff gap: 4 offer fields required by Onboarding are blank for internal candidates.

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
