---
name: sf-position-integrity-review
description: Use when you need to validate position management data integrity -- find orphans, broken hierarchies, cyclical chains, and missing incumbents before they cause payroll errors.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, position-management, integrity, payroll, hierarchy]
    related_skills: [sf-config-debt-scanner]
---

# SF Position Integrity Review

Scan position management data for structural inconsistencies that cause payroll, reporting, and org-chart failures.

## When to Use

- Before payroll processing to catch missing incumbents
- After a reorganisation to validate hierarchy chains
- During pre-migration data quality assessment
- When org chart visualisations show broken reporting lines
- As part of quarterly data integrity health checks

## Prerequisites

- Position and employee data from SF (OData export, CSV, or API response)
- SF Position Integrity Checker tool (if available)
- Or raw Position OData entities with parentPosition, incumbent, and status fields

## Evidence and Human Control

- Capture source evidence with tenant, population, effective date and extraction timestamp.
- Separate validation evidence from assumptions about payroll, workflow and integration impact.
- Treat employee identifiers and incumbent details as sensitive data; minimise and mask them in client outputs.
- Require human approval from HR data and HRIS/SF owners before any remediation or writeback.
- Re-run the integrity checks after remediation and reconcile the before/after population.

## Workflow (Manual Analysis)

### Step 1: Extract position data

Pull from SF OData or use existing export:
```
curl -u user:pass "https://apiXX.sapsf.eu/odata/v2/Position?\$select=code,parentPosition,incumbent,status,effectiveStartDate,effectiveEndDate,lastModifiedDateTime&\$top=5000"
```

### Step 2: Validate structural integrity

Check for:
- **Orphaned positions**: parentPosition references a code that doesn't exist
- **Broken chains**: position chain longer than expected (default: 15 levels)
- **Cyclical references**: A → B → C → A
- **No incumbent**: incumbent field null for > 90 days
- **Mismatched counts**: active positions vs active employees mismatch

### Step 3: Categorise and score

| Finding Type | Severity | Business Impact |
|-------------|----------|-----------------|
| Cyclical hierarchy | CRITICAL | Infinitely recursive org charts crash reporting |
| Orphaned position (no parent) | HIGH | Position invisible in hierarchy, excluded from approvals |
| No incumbent > 90 days | HIGH | Vacant positions accumulating, budget unbudgeted |
| Broken chain > 15 levels | MEDIUM | Slow hierarchy queries, navigation timeout |
| Inactive position with active incumbent | CRITICAL | Employee assigned to non-existent role |

### Step 4: Produce fix recommendations

For each finding, output:
- Position code and name
- Current state (what's wrong)
- Root cause (why it happened)
- Fix action (exactly what to change)
- Rollback instructions

## Edge Cases

- **Matrix organisations**: ignore parentPosition ambiguity; validate both reporting lines independently
- **Dual-employed incumbents (global assignments)**: flag as expected if concurrentEmployment is active
- **C-suite positions**: positions reporting to board (external) have no parent in EC -- flag as expected
- **MDF position types**: if client uses custom position objects, adapt entity name
- **Positions frozen mid-reorg**: exclude positions with effectiveStatus=frozen from orphan checks
- **Empty tenant / greenfield**: produce a "no data" baseline report with setup recommendations

## Common Pitfalls

1. **Counting every orphan as a defect**: Some orphans are intentional (board reporting, external secondments). Always include a "likely-intentional" filter.
2. **Not checking effective dates**: A position with no incumbent may be future-dated. Check effectiveStartDate.
3. **Missing the payroll impact**: Always link each finding to a concrete downstream effect (payroll error, reporting gap, compliance risk).
4. **Over-communicating the noise**: 500+ findings are overwhelming. Cluster similar issues and present top-N by business impact.

## Verification Checklist

- [ ] All active positions processed
- [ ] Orphans categorised (intentional vs defect)
- [ ] Hierarchy cycles identified and isolated
- [ ] Payroll-impact findings flagged separately
- [ ] Fix recommendations include specific API or UI paths
- [ ] Client-safe summary produced
