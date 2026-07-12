# Evidence-contract evaluations

These checks test whether the five flagship workflows contain the minimum
controls needed for client use. They do not claim that an AI model will always
produce a correct answer. They verify that each published workflow explicitly
requires evidence, distinguishes assumptions, protects sensitive data, retains
human approval, and includes follow-up validation.

Run:

```bash
python3 scripts/evaluate_flagship_skills.py
```

The cases are intentionally dependency-free and deterministic. A release should
not call a flagship workflow "client-ready" while its evidence contract fails.
