---
name: sf-foundation-object-cleanup
description: Use when auditing SF foundation objects (Location, Department, Cost Center, Legal Entity) for broken hierarchies, duplicates, and missing associations.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, foundation-objects, hierarchy, data-quality, cleanup]
    related_skills: [sf-config-debt-scanner]
---

# SF Foundation Object Cleanup

Clean up foundation object data so hierarchies render correctly, reporting aggregates work, and approvals route properly.

## When to Use

- Org chart shows disconnected nodes or missing departments
- Cost center reporting produces incorrect roll-ups
- Location hierarchy has gaps (country → region → site broken)
- Pre-migration foundation data quality check
- Reorganisation aftermath cleanup

## Prerequisites

- Foundation object data exports (OData or Provisioning CSV)
- List of expected hierarchy structures (from client)
- List of external systems consuming SF foundation objects

## Workflow

### Step 1: Extract All Foundation Objects

Target entities:
- FOLocation
- FODepartment
- FODivision
- FOCostCenter
- FOLegalEntity
- FOPayComponent

### Step 2: Hierarchy Validation

For each foundation object:
- **Parent-child integrity**: parent field references a valid externalCode that exists
- **Circular references**: A → B → C → A (walks back to root checking for loops)
- **Orphaned nodes**: node has no parent but is not root-level
- **Duplicate external codes**: same externalCode used for different nodes

### Step 3: Usage Check

For each foundation object node:
- How many positions reference it?
- How many employees map to it?
- Is it referenced in active workflows?
- Is it referenced in business rules?

### Step 4: Cleanup Plan

Produce:
- List of nodes to fix with exact corrective action
- Sequence (resolve parents before children)
- Pre-cleanup snapshot for rollback
- Post-cleanup validation checks

## Edge Cases

- **Time-dependent hierarchies**: nodes with effectiveStartDate/effectiveEndDate; validate across time
- **Multi-country structures**: same legal entity owns locations in multiple countries
- **Cost center reorganisation**: mid-financial-year changes need retroactive handling
- **External system IDs**: SAP Finance cost centers must match SF FOCostCenter externalCodes
- **Circular references that are intentional**: some organisations model matrix structures with bidirectional links (rare, but validate)
- **Foundation objects in workflows**: changing a department name may break approval routing

## Common Pitfalls

1. **Fixing the hierarchy without re-pointing positions**: Positions still point to old nodes. Run position integrity check after cleanup.
2. **Renaming externalCodes**: Breaks every integration. Add new code, transition, then deprecate old.
3. **Not checking effective dates**: A node may be inactive for future dates but look active today.
4. **Assuming one root per hierarchy**: Some organisations have multiple root locations, departments, or cost centers.
5. **Missing the reporting impact**: A broken cost center hierarchy means financial reports are wrong. Quantify the business impact.

## Verification Checklist

- [ ] All foundation objects inventoried
- [ ] Hierarchy loops identified and isolated
- [ ] Orphaned nodes flagged with fix action
- [ ] External integration dependencies listed
- [ ] Cleanup sequence documented with rollback
- [ ] Post-cleanup integrity check plan ready
