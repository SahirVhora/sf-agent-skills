---
name: sf-migration-readiness
description: Use when preparing to load employee or org data into SF -- pre-flight schema diff, picklist validation, constraint checks, and go/no-go recommendation.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, migration, data-load, readiness, pre-flight]
    related_skills: [sf-config-debt-scanner]
---

# SF Migration Readiness Check

Pre-load validation that catches rejects before they happen. Compares source data against target SF tenant schema and produces a go/no-go recommendation.

## When to Use

- Before loading employee master data into a new SF tenant
- Before delta loads during phased migration
- After data transformation to verify output matches target schema

## Evidence and Human Control

- Capture source evidence for the source file, target metadata, mappings and validation timestamp.
- Separate observed defects from assumptions about business meaning or acceptable defaults.
- Treat migration files as sensitive data; minimise extracts and never include credentials in outputs.
- A go/no-go recommendation is decision support: accountable programme and data owners retain human approval.
- Re-run schema, picklist and constraint validation after every material correction and retain the results.
- When switching from test to production tenant (schema may differ)
- Before weekend cutover load

## Prerequisites

- Source migration files (CSV, Excel, or structured data)
- Target SF tenant metadata (from $metadata or OData API)
- Picklist value sets from target tenant

## Workflow

### Step 1: Schema Extraction

Get target schema:
```
mcp__sf_config_debt_scanner__sf_scan_metadata_xml(xml_text="...")
```
Or pull entity metadata for specific entities.

### Step 2: Schema Diff

Compare each source field against target:

- Field exists? → field name in target metadata
- Required field populated? → nullable=false in metadata
- Data type matches? → Edm.String vs Edm.DateTime vs Edm.Decimal
- Field length within limit? → maxLength attribute
- Picklist value valid? → externalCode exists in target picklist

### Step 3: Constraint Checks

- **Association integrity**: personIdExternal → valid person record
- **Date-effective overlaps**: no two records for same person with overlapping effectiveStartDate/effectiveEndDate
- **Compound key uniqueness**: no duplicate personIdExternal + startDate combinations
- **Mandatory associations**: department, location, jobClass all resolve in target

### Step 4: Go/No-Go Decision

| Readiness Score | Recommendation |
|-----------------|----------------|
| 95-100 | Go -- no blockers |
| 85-94 | Go with caution -- minor fixes during load acceptable |
| 70-84 | No-go -- fix critical issues before load |
| <70 | Stop -- significant schema misalignment |

## Edge Cases

- **Source has extra fields not in target**: flag as ignored (not loaded); confirm they're not mapped elsewhere
- **Picklist external code vs label**: check if source uses labels instead of external codes (common migration error)
- **Multi-language picklist values**: source may reference en_US label but target needs externalCode
- **Compound keys in upsert mode**: personIdExternal + startDate must uniquely identify a record
- **Bulk load vs delta**: delta mode needs effectiveEndDate handling for closed records
- **Downstream propagation rules**: loaded data may trigger business rules; check rule impact before finalising

## Common Pitfalls

1. **Assuming test and production schemas match**: They often diverge after parallel configuration changes. Diff them first.
2. **Not checking field lengths**: SF rejects silently with HTTP 422. Pre-check lengths and truncate or flag.
3. **Missing effectiveEndDate for delta loads**: Leaving open-ended records causes overlap with new loads.
4. **Using labels instead of external codes**: Picklists accept external codes, not display labels.
5. **Ignoring required associations**: A position load may fail if department, location, or jobClass don't resolve in target.

## Verification Checklist

- [ ] All source fields matched to target schema
- [ ] Required fields populated in every row
- [ ] Picklist values validated against target
- [ ] Date-effective intervals non-overlapping
- [ ] Association integrity confirmed
- [ ] Sample load of 10-20 records successfully processed
- [ ] Go/no-go recommendation with specific pre-load actions
