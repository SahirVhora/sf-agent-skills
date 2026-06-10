---
name: sf-picklist-rationalisation
description: Use when audit picklist bloat -- find unused, duplicated, and overlapping picklist values across SF, then produce a safe consolidation plan.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, picklists, data-quality, consolidation, cleanup]
    related_skills: [sf-config-debt-scanner]
---

# SF Picklist Rationalisation

Find unused, duplicated, and bloated picklists, then produce a safe consolidation plan that doesn't break integrations.

## When to Use

- Picklist dropdowns have grown to 50+ values and users complain
- Multiple picklists serve the same purpose but with slightly different values
- Pre-migration cleanup to reduce configuration debt
- Integration mapping fails because external codes don't match
- Governance review shows unmaintained picklists

## Prerequisites

- Picklist metadata from SF tenant (OData or export)
- Picklist value usage statistics (from data or counts)
- List of integrations that reference picklist external codes

## Workflow

### Step 1: Inventory

Extract all picklists with:
- Picklist ID and label
- Value count
- Each value: externalCode, label, status (active/inactive), effective dates
- Parent picklist relationships (dependent fields)

### Step 2: Usage Analysis

For each picklist value:
- Count of employee/job/position records using it
- Count of business rules referencing it
- Count of calculated fields referencing it
- Integration mapping usage (externalCode in API payloads)

### Step 3: Duplicate Detection

Find duplicates across picklists:
- Same label, different externalCode → label confusion
- Same externalCode, different labels → translation drift
- Values that are subsets (one picklist is a superset of another) → consolidation candidate

### Step 4: Consolidation Plan

Recommend:
- Which picklists to merge (with before/after value maps)
- Which values to deprecate (with replacement mapping)
- Which values to rename (externalCode standardisation)
- Safe execution order so dependent objects don't break

## Edge Cases

- **Picklists shared across countries**: values may have different labels in different locales
- **Integration-dependent external codes**: changing externalCode breaks API consumers
- **Effective-dated values**: values with future effectiveStartDate; don't clean up prematurely
- **Parent-child picklists**: changing a parent value requires updating all children
- **Values in calculated fields**: harder to detect than business rules; grep calculated field formulas
- **Inactive but referenced values**: may be inactive but still referenced by historical data

## Common Pitfalls

1. **Deleting a value used by an integration**: Always check API logs or integration specs before deprecating.
2. **Merging picklists with different effective-dating**: Standardise dating strategy before merge.
3. **Not updating business rules**: Rules that reference old external codes silently stop working.
4. **Forgetting dependent picklists**: Changing a parent picklist value changes which child values are available.
5. **Renaming external codes mid-project**: Breaks every active integration. Deprecate old code, add new code, transition gradually.

## Verification Checklist

- [ ] All picklists inventoried with usage counts
- [ ] Duplicate map produced
- [ ] Integration dependencies listed for every value
- [ ] Deprecation plan sequenced (no dependency breaks)
- [ ] Rollback plan documented (restore previous externalCode)
- [ ] Test tenant verification completed before production
