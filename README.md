# Daedalus Playground

Small target repository for smoke testing Daedalus workflow onboarding.

The code is intentionally simple: a tiny Python package under `src/` plus one
pytest file. Daedalus workflow smoke tests can safely create issues, bootstrap a
`WORKFLOW.md`, dispatch an agent, open a pull request, and run CI against this
repository without touching production code.

## Local Checks

```bash
python3 -m pip install -e .[test]
pytest
```

## Daedalus Smoke Path

From this repository checkout:

```bash
hermes daedalus bootstrap
hermes daedalus validate
```

Use GitHub issues as disposable workflow inputs. A good smoke issue is a small,
testable change such as adding another greeting format or calculator helper.

