---
name: sf-exec-summary
description: Use when you need to turn technical SF config debt findings into a one-page executive summary for CHRO, CIO, or project sponsor.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, executive-summary, consulting, board-ready]
    related_skills: [sf-config-debt-scanner]
---

# SF Executive Summary Writer

Convert raw findings into board-ready language. One page. Business impact only. No technical jargon.

## When to Use

- Client asked for an executive summary for their leadership team
- Board presentation prep
- Building a business case for remediation funding
- Post-audit debrief with non-technical stakeholders
- Client says "just give me the highlights"

## Prerequisites

- Config debt findings or assessment results
- Target audience (CHRO, CIO, CFO, Project Sponsor, Steering Committee)
- Optional: client's business priorities (cost reduction, compliance, user experience)

## Workflow

### Step 1: Parse and Classify

Tag each finding by business impact:
- **Compliance risk**: GDPR, SOX, internal audit findings
- **Financial impact**: payroll errors, incorrect cost allocation
- **Operational efficiency**: manual workarounds, slow processes, rework
- **User experience**: confusing interfaces, missing data, broken workflows
- **Data quality**: inconsistent reporting, unreliable analytics

### Step 2: Identify Top Business Risks

Pick the top 3 findings that matter to business leaders:
- Explain what the risk is in plain language
- Quantify the impact (how many employees affected, what it costs)
- State what happens if it's not fixed

### Step 3: Draft the Summary

Structure:
1. **Overall health score** (one number with context)
2. **Top 3 business risks** (each one paragraph, no jargon)
3. **Recommended next 3 actions** (what, who, how long, what it costs)
4. **90-day outlook** (what good looks like)

### Step 4: Sanitise

Produce two versions:
- **Board version**: business language only, no technical detail, no severity labels, confidence-focused
- **Internal version**: full detail with all findings, technical notes, raw scores

## Edge Cases

- **Zero findings**: draft an affirmation report -- "your configuration is healthy; here's what to monitor"
- **300+ findings**: summarise by theme, not by finding. "One finding about each field" → "17% of fields have blank rates above 80%"
- **Mixed audience**: board members + technical leads. Primary document is board-level with an appendix for technical detail.
- **Stale data**: findings from an audit 6 months ago. Add a caveat: "based on configuration snapshot dated [date]"
- **Multiple tenants/countries**: produce separate summary per tenant, then a combined overview
- **Client wants benchmark comparison**: note that benchmarks require industry data, which may not be available

## Common Pitfalls

1. **Dumping all findings into the executive summary**: The board doesn't need to know about picklist value #47. Give them the three things that matter.
2. **Using severity labels with non-technical audience**: "CRITICAL" scares people. "This affects payroll accuracy for 1,200 employees" informs them.
3. **No call to action**: Every executive summary must end with "here's what we recommend you do next."
4. **Assuming the reader knows SF terminology**: Write "employee data" not "Person entity." Write "approval routing" not "workflow configuration."
5. **Not quantifying impact**: "Config debt is high" → "Configuration issues could cause payroll errors affecting up to 1,200 employees, with an estimated correction cost of 3-5 days of HRIS team time per incident."

## Verification Checklist

- [ ] Overall health score calculated
- [ ] Top 3 business risks in plain language
- [ ] Each risk quantified (employees affected, cost, time)
- [ ] Recommended next actions with owners and timelines
- [ ] Board version sanitised (no technical jargon)
- [ ] Internal version available for technical team
- [ ] Date, tenant reference, and confidence score included
