---
name: sf-position-jobinfo-alignment-audit
description: Use when you need to find where position attributes and employee jobinfo have drifted apart.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, data-integrity, agent-skill, consulting]
    related_skills: [sf-config-debt-workshop]
---

# Position to Job Info Alignment Audit

Compares Position Management fields against employee JobInfo values to find misalignment in department, division, cost centre, location, job classification, manager, FTE, and custom attributes. Identifies whether drift is caused by missing propagation rules, manual overrides, inactive positions, future-dated changes, or reorganisation timing. Produces a safe correction plan grouped by business impact.

## When to Use

- Find where Position attributes and employee JobInfo have drifted apart.
- Client needs a practical review in the Data Integrity area
- Preparing a release, audit, workshop, UAT pack, or remediation plan
- Translating SF configuration risk into business language

## Prerequisites

- Inputs: Position data, JobInfo data, propagation rules, sync settings, effective-dated snapshots
- Expected outputs: Alignment score, mismatch report, propagation rule gaps, safe correction plan
- Confirm tenant/snapshot date and audience before analysis
- Do not store credentials, employee-sensitive data, or tenant exports in the repo

## Workflow

1. **Extract** - gather evidence, assess impact, and produce the client-safe artefact.
2. **Compare** - gather evidence, assess impact, and produce the client-safe artefact.
3. **Root Cause** - gather evidence, assess impact, and produce the client-safe artefact.
4. **Correction Plan** - gather evidence, assess impact, and produce the client-safe artefact.

## Analysis Checklist

- Capture configuration evidence and source date
- Separate expected variation from defects
- Link every finding to business impact: payroll, compliance, hiring, reporting, integration, or employee experience
- Group repeated findings into themes
- Produce remediation actions with owner, effort, dependency, and validation step
- Flag internal-only observations separately from client-ready narrative

## Edge Cases

- **Manual override intentionally differs from position**: validate explicitly and decide whether it is expected design or defect
- **Future-dated position change not yet reflected in JobInfo**: validate explicitly and decide whether it is expected design or defect
- **Shared position with multiple incumbents**: validate explicitly and decide whether it is expected design or defect
- **Vacant position changed before hire assigned**: validate explicitly and decide whether it is expected design or defect
- **Country-specific propagation exceptions**: validate explicitly and decide whether it is expected design or defect
- **Matrix manager differs from position manager**: validate explicitly and decide whether it is expected design or defect

## Example Prompt

> Compare Position and JobInfo data and show where attributes are misaligned or propagation rules are missing.

## Example Output Shape

Alignment score: 81/100. 264 mismatches found: 112 cost centre, 79 department, 41 location, 32 manager. Top risk: 47 employees in Finance have JobInfo cost centres that differ from their positions after reorg, causing finance reporting leakage. Fix plan groups mismatches by propagation rule gap.

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
