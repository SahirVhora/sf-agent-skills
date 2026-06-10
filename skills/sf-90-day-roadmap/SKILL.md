---
name: sf-90-day-roadmap
description: Use when you need to turn a list of config debt findings into a phased, client-ready 90-day remediation plan with sprint-by-sprint actions.
version: 1.0.0
author: SahirVhora
license: MIT
metadata:
  hermes:
    tags: [sapsf, roadmap, remediation, consulting, planning]
    related_skills: [sf-config-debt-scanner]
---

# SF 90-Day Remediation Roadmap

Turn findings into action. Produce a prioritised 90-day plan the client can start executing on Monday.

## When to Use

- Client received findings and asks "what do we do now?"
- Post-audit remediation planning
- Building a project plan for configuration cleanup
- Quarterly governance planning cycle
- Proposal/SOW scope definition

## Prerequisites

- List of config debt findings with severities
- Understanding of client's team capacity (how many people, how many hours)
- Client's change management process (change freezes, release windows)

## Workflow

### Step 1: Score and Sort

Rate findings automatically:
```
mcp__sf_config_debt_scanner__sf_rate_findings(findings_json="...")
```

Sort by: severity → business impact → effort → dependency.

### Step 2: Cluster into Sprints

Group related findings into thematic sprints:
- **Sprint theme**: what all findings in this sprint share
- **Deliverables**: 2-4 concrete outputs
- **Effort**: person-days estimate
- **Dependencies**: what must be fixed first
- **Owner**: which team/role does the work

### Step 3: Phase into 90 Days

Standard phasing:
- **Phase 1 (Days 1-30)**: Critical findings only. Quick wins that unblock later work.
- **Phase 2 (Days 31-60)**: High severity. More complex changes that depend on Phase 1.
- **Phase 3 (Days 61-90)**: Remaining medium/low. Documentation, governance setup, automation.

### Step 4: Package for Client

Add:
- **Executive summary**: one paragraph on what 90 days achieves
- **Risk register**: what could go wrong and how to mitigate
- **Success metrics**: how to know when each sprint is done
- **Governance cadence**: weekly check-in, sprint review, phase gate

## Edge Cases

- **100+ findings**: triage ruthlessly. Top 20 make the 90-day plan. Rest go to a backlog.
- **Only low-severity findings**: consider a 30-day plan instead; 90 days is overkill.
- **Mixed-source findings**: findings from different scan tools need normalised scoring.
- **No effort data**: use standard sizing (critical=2 days, high=1 day, medium=0.5 day, low=0.25 day) and note the assumption.
- **Change freeze during roadmap**: Phase around the freeze window.
- **Findings that are by-design**: some config debt is intentional. Exclude from remediation plan or flag as "accepted risk."

## Common Pitfalls

1. **Grouping unrelated findings into one sprint**: Each sprint should have a clear theme the client can explain to their boss.
2. **Ignoring dependencies**: Fixing picklists before business rules will re-break the rules. Sequence correctly.
3. **No success metric**: "Fixed 12 findings" means nothing. "Payroll accuracy improved from 96% to 99.5%" means something.
4. **Overpromising speed**: 90 days is fast for config cleanup in large tenants. Be realistic about effort.
5. **Not planning for regression testing**: Every sprint needs UAT time. Build it into the plan.

## Verification Checklist

- [ ] Findings scored and sorted by severity and impact
- [ ] Sprints are thematic with 2-4 deliverables each
- [ ] Dependencies identified and sequenced
- [ ] Success metrics defined per phase
- [ ] Client capacity considered (not just ideal-world plan)
- [ ] Change freeze windows accommodated
- [ ] Governance cadence included
