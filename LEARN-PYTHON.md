# LEARN-PYTHON.md
Python learning plan + working agreement for Codex review in VS Code.

## 1) Context
I am learning Python from fundamentals to practical development (tooling, testing, packaging, and web/API frameworks). I will write code in this repo using VS Code. Codex should review code, point out correctness issues, edge cases, and suggest small, actionable improvements.

## 2) Primary objectives
By the end of this plan I want to be able to:
- Write clean, idiomatic Python (core syntax + standard library).
- Structure projects (modules/packages), manage dependencies with a virtual environment, and ship a small CLI.
- Write tests and use basic tooling (formatter/linter/type hints).
- Build a small API service (FastAPI) and optionally persist data (SQLite + ORM).
- Understand when to use common frameworks: FastAPI, Django, Flask, and Streamlit.

## 3) Working agreement: how Codex should help
When asked to review:
- Focus on correctness, clarity, Python idioms, error handling, edge cases, and tests.
- Keep edits scoped: propose minimal diffs rather than refactors unless requested.
- Prefer standard library solutions unless a dependency is clearly justified.
- If proposing changes, include the reason and expected behavior change.
- If tests exist, run them (or instruct exactly how to run) and report results.

## 4) Tooling (local dev)
Target Python: 3.12+ (3.11 is acceptable).

Repo conventions:
- Virtual environment: `.venv/` (do not commit)
- Dependencies: `requirements.txt` or `pyproject.toml` (pick one and stay consistent)

Recommended quality tools:
- `pytest` (tests)
- `ruff` (lint + format)
- `mypy` (optional type checking)

## 5) Coding standards
- Use type hints for public functions once comfortable.
- Write small functions and avoid deep nesting.
- Prefer `pathlib` for filesystem paths.
- Use `dataclasses` for simple data containers.
- Use explicit exceptions (avoid blanket `except Exception` unless re-raising with context).

## 6) Daily routine (60-90 min)
1. 20 min concept learning
2. 30 min coding exercises
3. 20 min mini-project work
4. 10 min recap notes (what I learned, what was hard, what to practice again)

## 7) 12-week roadmap (deliverable-driven)

### Weeks 1-2: Core Python basics
Topics:
- Variables, data types, operators, input/output
- Conditionals, loops, functions
- Basic collections and file handling

Deliverables:
- 20-30 short exercises
- `exercises/week01/word_frequency.py`
- `exercises/week02/expense_tracker_cli.py` (JSON-based)

### Weeks 3-4: Intermediate Python
Topics:
- Collections in depth (`list`, `dict`, `set`, `tuple`)
- Strings, exceptions, modules, imports, packages
- OOP basics (classes, objects, inheritance)
- Testing and quality (`pytest`, `ruff`, optional `mypy`)

Deliverables:
- Refactor expense tracker into a small package
- At least 15 meaningful tests
- Clean lint/format run

### Weeks 5-6: Python development skills + FastAPI
Topics:
- Git/GitHub workflow basics
- Debugging/logging practices
- HTTP and JSON handling
- FastAPI routes, validation, error handling, dependency injection, async basics

Deliverables:
- CLI that fetches data from a public API and persists normalized output
- Expense tracker API:
  - `POST /expenses`
  - `GET /expenses`
  - `GET /reports/monthly`

### Weeks 7-8: Database and ORM
Topics:
- SQLite + SQL basics
- SQLAlchemy or SQLModel
- Alembic migrations

Deliverables:
- Persist API data in SQLite
- Add filtered queries
- Add and apply migrations

### Weeks 9-10: Framework track 2 (Django)
Topics:
- Django models, admin, views, templates
- Auth, forms, ORM

Deliverable:
- Small Django app (blog or task manager)

### Weeks 11-12: Framework track 3 + capstone
Topics:
- Choose one: Flask (lightweight web app) or Streamlit (data app/dashboard)
- Packaging/deployment basics (`pyproject.toml`, Docker intro, hosting)

Deliverables:
- Capstone project
- Deployed app/API + README with run/deploy instructions

## 8) Frameworks to prioritize
- `FastAPI`: modern APIs and backend development
- `Django`: full-stack web framework
- `Flask`: minimal framework for lightweight apps
- `Streamlit`: quick data apps and dashboards
- `pytest`: essential testing framework

## 9) Current focus (start here)
### Week 1, Day 1
Goal: write a script that reads a `.txt` file and prints the top 10 most frequent words.

Requirements:
- Input: path to a `.txt` file (CLI argument)
- Normalize: lowercase and remove punctuation
- Tokenization: split on whitespace after normalization
- Count frequencies
- Output: top 10 words with counts (descending by count, ties alphabetical)

Suggested files:
- `exercises/week01/word_frequency.py`
- `exercises/week01/sample.txt`

Definition of done:
- Works on a sample text file
- Handles empty file gracefully
- Includes a small self-check or test

## 10) How to ask Codex (copy/paste prompts)
- "Review `exercises/week01/word_frequency.py` for correctness and Python style. Suggest minimal improvements."
- "Run the script on `exercises/week01/sample.txt` and confirm the output format."
- "Add 3-5 pytest tests for word frequency (including punctuation, empty file, ties). Keep changes minimal."
- "Create Week 1 Day 2 tasks and a short quiz based on my progress."

## 11) Review checklist (what Codex should verify)
- Correctness: counting and sorting rules
- Edge cases: empty input, non-existent file, Unicode punctuation
- CLI usability: helpful error messages and usage
- Code quality: readability, small functions, no unnecessary dependencies
- Tests: run and ensure green
