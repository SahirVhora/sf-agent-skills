---
name: sf-client-discovery
description: Use when you need to generate structured discovery questions for a new or existing SF client -- adapted to what is already known about their tenant.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, consulting, discovery, workshop, client]
    related_skills: [sf-config-debt-scanner]
---

# SF Client Discovery

Generate structured, audience-appropriate discovery questions that uncover the real configuration pain points.

## When to Use

- First client engagement (greenfields discovery)
- Pre-workshop preparation
- Expanding scope with an existing client
- Building a proposal or SOW
- Client has configuration issues but can't articulate them

## Prerequisites

- Optional: previous scan results, tenant metadata summary, client briefing notes
- Knowledge of client's SF modules in use (EC, Compensation, Recruiting, etc.)
- Client context (size, countries, merger history, known pain points)

## Workflow

### Step 1: Load Context

If scan results exist, extract key themes to tailor questions. If no data, start with broad discovery categories.

### Step 2: Generate Questions

Use the MCP assessment tool for config-debt-specific questions:
```
mcp__sf_config_debt_scanner__sf_assessment_questions(category="all")
```

Supplement with module-specific questions:
- **Governance**: Who owns config changes? Change approval process? Audit trail?
- **Custom Fields**: How many? Who creates them? Any field rationalisation done?
- **Business Rules**: Who writes and tests rules? Documentation? Rule conflict testing?
- **Foundation Objects**: How often are hierarchies updated? Who owns them?
- **MDF**: Custom objects in use? Who maintains them? Integration dependencies?
- **Integrations**: How many? Middleware? Error handling? Monitoring?

### Step 3: Pain-Point Prioritisation

Ask the client to rank pain points. Use forced-choice questions:
- "If you could fix one thing about your SF setup tomorrow, what would it be?"
- "What takes your HRIS team the most time each week?"
- "What do users complain about most?"
- "What broke last time you made a config change?"

### Step 4: Package Workshop Agenda

Produce a timed agenda:
- 15 min: context and goals
- 30 min: pain-point deep-dive
- 30 min: guided discovery (question bank)
- 15 min: executive debrief and next steps

## Edge Cases

- **Greenfields (never reviewed)**: stick to generic assessment questions; don't assume problems
- **Post-migration review**: focus on migration-specific pain points (data quality, missing fields, broken integrations)
- **Multi-country rollout**: adapt questions per country where config may diverge
- **Post-merger consolidation**: ask about both tenants separately, then consolidation plan
- **Non-English client**: generate questions in client's language
- **Procurement/legal audience**: strip technical detail; focus on risk, compliance, and cost

## Common Pitfalls

1. **Leading questions**: "Your custom fields are out of control, right?" → "How do you manage custom field creation?"
2. **Too many questions**: 30+ questions overwhelm. Top 15, grouped by theme, with optional deep-dive sections.
3. **No success definition**: Always ask "what does a successful review look like?" early.
4. **Technical jargon with non-technical audience**: HR Directors don't know what MDF or OData means.
5. **Not sending pre-read**: Clients who see questions in advance give better answers. Include a 5-question pre-read.

## Verification Checklist

- [ ] Questions categorised by governance area
- [ ] Pain-point prioritisation exercise included
- [ ] Success definition captured first
- [ ] Audience-appropriate language used
- [ ] Timed workshop agenda produced
- [ ] Pre-read questions prepared
- [ ] Next-steps decision tree included
