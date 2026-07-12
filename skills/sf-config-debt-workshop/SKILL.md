---
name: sf-config-debt-workshop
description: Use when you need to run a complete SAP SuccessFactors EC config debt workshop -- discovery questions, assessment, scoring, and 90-day roadmap -- from a $metadata XML or live tenant.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, config-debt, workshop, ec, governance, assessment]
    related_skills: [sf-config-debt-scanner]
---

# SF Config Debt Workshop

Run a full client-facing config debt workshop for SAP SuccessFactors Employee Central. From raw metadata to board-ready deliverables in one workflow.

## When to Use

- A client asks "is our SF configuration healthy?"
- Pre-migration readiness assessment
- Post-go-live configuration audit
- Building a governance business case for an HR transformation project
- Preparing for a client workshop where you need to demonstrate config debt risk

## Prerequisites

- SF Config Debt Scanner MCP server running (connects via `mcp__sf_config_debt_scanner__*` tools)
- Either: access to SF tenant (API credentials), OR a `$metadata` XML export file
- No employee data is extracted -- schema and counts only

## Evidence and Human Control

- Capture source evidence with tenant, scope and snapshot date.
- Separate observed configuration evidence from assumptions and stakeholder statements.
- No employee data is required or permitted in the deliverable.
- Remediation needs named human approval from the HRIS/SF owner; the skill never writes configuration.
- Re-run the scan after remediation and retain before/after evidence.

## Workflow

### Step 1: Discovery

Start with assessment questions:

```
mcp__sf_config_debt_scanner__sf_assessment_questions(category="all")
```

This returns categorised discovery questions covering governance, custom fields, MDF, picklists, event reasons, foundation objects, and business rules. Use these as the client workshop opening.

### Step 2: Scan (Choose Path)

**Path A -- Live tenant scan:**

```
mcp__sf_config_debt_scanner__sf_test_connection(base_url="https://apiXX.sapsf.eu")
```

Confirm connectivity, then:

```
mcp__sf_config_debt_scanner__sf_scan_tenant(base_url="https://apiXX.sapsf.eu", auth_method="basic", username="...", password="...")
```

**Path B -- Offline XML scan (no tenant access needed):**

```
mcp__sf_config_debt_scanner__sf_scan_metadata_xml(xml_text="...")
```

### Step 3: Score Findings

Rate the findings automatically:

```
mcp__sf_config_debt_scanner__sf_rate_findings(findings_json="...")
```

Returns: overall debt score, area breakdown, prioritised 90-day roadmap.

### Step 4: Package Output

Produce the workshop pack:

1. **Discovery question bank** (from Step 1)
2. **Findings with severity** (from Step 2/3)
3. **Executive summary** -- top 3 business risks in plain language
4. **90-day phased roadmap** (from `sf_rate_findings`)
5. **Next-steps decision tree** -- what the client should do on Monday morning

Package in client-safe language. Flag internal-only observations separately.

## Edge Cases

- **Tenant unreachable**: fall back to XML path; note in output that counts could not be verified live
- **Truncated XML**: partial scan still produces findings on visible entities
- **Empty tenant**: produce a clean-baseline report stating no debt found
- **Very large tenant**: increase MCP timeout to 300s; sf_scan_tenant handles batching
- **OAuth2 auth**: set auth_method="oauth2" and provide client_id, client_secret, company_id
- **Custom field limits**: pass high_field_limit, custom_field_limit parameters to adjust thresholds per client

## Common Pitfalls

1. **Sharing internal findings with client**: Rate findings output contains unvarnished severity labels. Sanitise before presenting to non-technical audiences. Flag internal sections with `[INTERNAL ONLY]`.
2. **Forgetting to test connection first**: Use `sf_test_connection` before `sf_scan_tenant` -- it's faster to fail early if credentials are wrong.
3. **Trusting old XML exports**: $metadata changes over time. Note the export date in output.
4. **Thresholds too aggressive for small tenants**: A company with 200 employees doesn't need the same limits as one with 50,000. Adjust custom_field_limit and high_field_limit.
5. **Missing the business impact translation**: Don't deliver raw field counts. Translate to business risk: "blank cost center fields → incorrect payroll cost allocation → finance reconciliation errors".

## Verification Checklist

- [ ] Connection tested (live) or XML validated (offline)
- [ ] Findings scored and sorted by severity
- [ ] Roadmap includes concrete actions with effort estimates
- [ ] Executive summary uses business language, not technical jargon
- [ ] Internal-only observations flagged
- [ ] Client document has date, tenant reference, and confidence score
