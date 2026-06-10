---
name: sf-test-scenario-generator
description: Use when you need to generate UAT test scenarios from live SF business rules and workflow config -- covering happy path, edge cases, and cross-process interactions.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, testing, uat, quality-assurance, scenarios]
    related_skills: [sf-config-debt-scanner]
---

# SF Test Scenario Generator

Generate realistic, coverage-complete test scenarios from your actual business rules, not generic templates.

## When to Use

- Preparing for UAT before a release
- Building a regression test suite
- Onboarding new testers who don't know the configuration
- Proving to auditors that all business rules have test coverage
- After a business rule change -- regenerate affected scenarios

## Prerequisites

- Business rule configuration export
- Workflow/approval process definitions
- Knowledge of which rules changed (for targeted regeneration)

## Workflow

### Step 1: Parse Configuration

Extract from business rules:
- Trigger conditions (when does the rule fire?)
- Field reads (what data does it check?)
- Field writes (what data does it set?)
- Error/raise conditions (what should it block?)

### Step 2: Generate Scenarios

For each rule, generate:
- **Happy path**: all conditions met, rule fires successfully
- **Edge case -- null input**: what if the checked field is empty?
- **Edge case -- boundary**: what if the value is at the max/min?
- **Error condition**: what if the rule should block the save?
- **Cross-rule interaction**: what if Rule A and Rule B fire together?

### Step 3: Build Test Cases

Each test case includes:
- Pre-conditions (data setup needed)
- Test steps (exactly what to do in the UI)
- Expected result (what the system should do)
- Test data (which employee, which values)
- Rules validated (traceability to specific business rules)

### Step 4: Produce Traceability Matrix

Map every business rule to at least one test case. For audit sign-off, show:
- Rule ID → Test Case ID
- Coverage status (covered / partial / uncovered)
- Last run date

## Edge Cases

- **Effective-dated rules**: generate scenarios across effective date boundaries
- **Compound rules (A AND B AND C)**: test all false combinations, not just all true
- **Workflows with external approvers**: test what happens when the external system is down
- **Propagation cascades**: test rules that trigger other rules through 3+ levels
- **Dynamic role resolution**: test with different role assignments (manager, HRBP, etc.)
- **Off-cycle events**: mid-period changes, retroactive updates, future-dated changes

## Common Pitfalls

1. **Only testing the happy path**: 80% of production issues come from edge cases. Generate at least one edge case per rule.
2. **No cross-rule scenarios**: Rules don't execute in isolation. Test the combinations that happen in real workflows.
3. **Missing test data setup**: A scenario that says "change department to Sales" but no employee is in a non-Sales department to start with is useless.
4. **Not covering error conditions**: If a rule is supposed to block invalid data, test that it actually blocks it.
5. **Forgetting propagation rules**: A Person rule that sets a field used by a Position rule -- test the full chain, not each rule alone.

## Verification Checklist

- [ ] Every business rule has at least one test scenario
- [ ] Happy path and edge case coverage >90%
- [ ] Cross-rule interaction scenarios included
- [ ] Test data requirements documented per scenario
- [ ] Traceability matrix produced
- [ ] Error/block conditions tested
- [ ] Propagation chains tested end-to-end
