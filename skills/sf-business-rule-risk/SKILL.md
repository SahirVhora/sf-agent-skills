---
name: sf-business-rule-risk
description: Use when auditing SF business rules for logic errors, silent failures, cross-object conflicts, and unreachable branches.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, business-rules, audit, governance, risk]
    related_skills: [sf-config-debt-scanner]
---

# SF Business Rule Risk Review

Audit every business rule for logic defects, silent failures, and cross-object conflicts that corrupt employee data.

## When to Use

- Before a release to catch rule conflicts that testing missed
- After a merger/acquisition when combining two SF configurations
- When fields show unexpected values and no one knows which rule is responsible
- During governance maturity assessment
- As a periodic health check (recommended: quarterly)

## Prerequisites

- Business rule configuration export (from Provisioning or API)
- Access to target SF tenant schema ($metadata)

## Workflow

### Step 1: Rule Inventory

Extract all rules with:
- Rule ID and name
- Base object (which entity triggers)
- Trigger condition (onSave, onChange, onView, onInit)
- Rule type (if-then-else, raise message, assignment)

### Step 2: Parse Logic Trees

For each rule, map:
- All if-conditions → which fields evaluated
- All then-actions → which fields written
- All else-actions → fallback behaviour
- Fields read vs fields written → cross-rule interference

### Step 3: Interaction Mapping

Identify:
- **Rules that write the same field** (conflict risk)
- **Rules that read what another writes** (ordering dependency)
- **Rules with no trigger condition** (always-on, possibly unintentional)
- **Unreachable branches** (conditions that can never be true)
- **Rules referencing deprecated fields** (silently broken)

### Step 4: Risk Scoring

| Pattern | Severity | Example |
|---------|----------|---------|
| Two rules write same field, different triggers | CRITICAL | BR-A writes department on hire; BR-B writes department on jobChange |
| Rule reads a field another rule conditionally writes | HIGH | BR-C reads costCenter after BR-D sets it under some conditions |
| Rule has no trigger condition | HIGH | Runs on every save, may cascade unexpectedly |
| Unreachable branch | MEDIUM | Dead code, maintenance burden |
| Rule references deprecated field | MEDIUM | May still run but target field no longer exists |

## Edge Cases

- **Cross-entity rules**: Rules spanning multiple objects (e.g., Person → Employment → Position). Flag as complex.
- **OnSave vs onChange ordering**: Execution order depends on UI save sequence, not rule definition. Test ordering explicitly.
- **Inactive rules in exports**: Some systems export inactive rules. Filter before analysis.
- **MDF business rules**: Different engine from EC business rules. Handle separately.
- **Propagation rules**: Rules that trigger other rules. Map the cascade to find chains >3 deep.
- **Rules that suppress each other**: Rule A sets field X, Rule B checks X and clears it. Map mutual suppression.

## Common Pitfalls

1. **Assuming rule order matches definition order**: It doesn't. Test execution order in a sandbox.
2. **Ignoring raise-message rules**: They don't write data but block saves. If they're unreachable, users can save invalid data.
3. **Not testing edge values**: Rules that check "if department = Sales" break when department is null (null ≠ Sales).
4. **Missing cross-object impact**: A Person rule may affect Position data through propagation. Map the full chain.

## Verification Checklist

- [ ] Every active rule inventoried and parsed
- [ ] Field write conflicts identified and scored
- [ ] Unreachable branches flagged
- [ ] Deprecated field references caught
- [ ] Execution order dependencies documented
- [ ] Client-safe summary with top-5 risks produced
