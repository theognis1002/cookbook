Audit the entire project and make all metadata, config, and documentation files production-ready for open source release. This is a generic skill — detect the project type and adapt accordingly.

## Step 1: Analyze the Project

Before making any changes, thoroughly explore the codebase:

1. Identify the project type and language(s) (Python, Node, Rust, Go, Java, etc.)
2. Identify the package manager (uv, pip, npm, pnpm, yarn, cargo, go mod, etc.)
3. Identify frameworks and key dependencies
4. Check for Docker usage (Dockerfile, docker-compose.yml)
5. Check for CI/CD configs (.github/workflows, .gitlab-ci.yml, etc.)
6. Inventory all existing metadata files
7. Read the main source files to understand what the project actually does
8. Check git history for project context (contributors, age, activity)

## Step 2: Audit and Fix Each File

Work through each category below. For existing files, update them. For missing files that are needed, create them. Do NOT create files that aren't relevant to the project.

### 2.1 — README.md

Ensure the README contains all of these sections (adapt titles to fit the project):

- **Project title and one-line description** (clear, concise)
- **Badges** (if CI exists, add build status; add license badge)
- **Overview / What it does** (2-4 sentences, non-technical-friendly)
- **Features** (bulleted list of key capabilities)
- **Prerequisites** (runtime, tools, services needed)
- **Quick Start** (numbered steps: clone, install, configure, run)
- **Usage / Examples** (concrete examples with code blocks)
- **Architecture** (brief description or diagram for non-trivial projects)
- **Configuration** (environment variables, config files — reference .env.example)
- **Development** (how to set up a dev environment, run tests, lint)
- **Contributing** (link to CONTRIBUTING.md)
- **License** (name + link to LICENSE file)

Rules:
- Do NOT use emojis unless the existing README already uses them
- Keep it factual — do not add marketing fluff
- Code blocks must specify the language for syntax highlighting
- All install/run commands must be copy-pasteable and correct
- If a README already exists and is good, only fill gaps — don't rewrite what works

### 2.2 — LICENSE

- If no LICENSE file exists, ask the user which license they want (suggest MIT for general OSS, Apache 2.0 for enterprise-friendly)
- Ensure the year and copyright holder name are correct
- The file must be named `LICENSE` (no extension)

### 2.3 — .gitignore

Ensure comprehensive coverage for the detected language/ecosystem. Must include at minimum:

**Universal:**
- OS files: `.DS_Store`, `Thumbs.db`, `*.swp`, `*~`
- Editor/IDE: `.vscode/`, `.idea/`, `*.sublime-*`, `.vim/`
- Secrets: `.env`, `.env.*`, `!.env.example`

**Python:** `__pycache__/`, `*.py[cod]`, `*.egg-info/`, `dist/`, `build/`, `.venv/`, `*.egg`, `.mypy_cache/`, `.pytest_cache/`, `.ruff_cache/`, `htmlcov/`, `.coverage`

**Node:** `node_modules/`, `dist/`, `.next/`, `.nuxt/`, `*.tsbuildinfo`, `.turbo/`, `coverage/`

**Rust:** `target/`, `Cargo.lock` (for libraries only)

**Go:** binary output directories

Do NOT remove existing entries that are project-specific. Merge intelligently.

### 2.4 — .dockerignore (only if Docker is used)

If the project has a Dockerfile or docker-compose.yml, ensure .dockerignore exists with:
- Everything in .gitignore
- `.git/`
- `README.md`, `LICENSE`, `CONTRIBUTING.md`, `CHANGELOG.md`, `docs/`
- `*.md` (unless the app serves markdown)
- `.github/`, `.gitlab/`
- Test directories (`tests/`, `test/`, `__tests__/`, `spec/`)
- `.venv/`, `node_modules/`, `target/`

### 2.5 — .env.example

- If a `.env` file exists, create or update `.env.example` with the same keys but placeholder values
- NEVER copy real secrets — use descriptive placeholders like `your-api-key-here`, `localhost`, `5432`
- Add a comment above each variable explaining what it's for
- If .env doesn't exist but the code reads environment variables, create .env.example for those variables

### 2.6 — CLAUDE.md (project-level)

Ensure the project CLAUDE.md is useful for AI-assisted development. It should contain:

- **Project summary** (1-2 sentences: what it is, what it does)
- **Tech stack** (language, framework, key deps)
- **How to run** (exact commands: install deps, run dev, run prod)
- **How to test** (exact test command, test framework)
- **How to lint/format** (exact commands)
- **Project structure** (brief description of key directories/files)
- **Key patterns** (architectural decisions, conventions used in the codebase)
- **Environment variables** (reference .env.example)

Rules:
- Keep it concise and machine-actionable — commands over prose
- This file is for AI coding assistants, not humans (though humans can read it)
- Do NOT duplicate the full README — focus on "how to work on this codebase"

### 2.7 — Package Manager Config

**Python (pyproject.toml):**
- Ensure `name`, `version`, `description` are filled in (not placeholder text)
- Add `license` field
- Add `authors` field if missing
- Add `keywords` and `classifiers` if reasonable
- Ensure `requires-python` is set
- Add `[project.urls]` with Homepage/Repository/Issues if a git remote exists

**Node (package.json):**
- Ensure `name`, `version`, `description`, `license`, `author` are set
- Ensure `engines` specifies the Node version
- Add `repository`, `bugs`, `homepage` URLs if a git remote exists
- Ensure `scripts` has at least: start, dev, test, lint (where applicable)
- Add `keywords` if reasonable

**Rust (Cargo.toml):**
- Ensure `name`, `version`, `description`, `license`, `edition` are set
- Add `repository` if a git remote exists
- Add `keywords` and `categories` if reasonable

### 2.8 — CONTRIBUTING.md (create if missing)

Short, practical contributing guide:
- How to set up the development environment
- How to run tests
- PR process (branch naming if conventions exist, review expectations)
- Code style / linting requirements
- Link to issues / discussion for questions
- Keep it under 80 lines — nobody reads long contributing guides

### 2.9 — SECURITY.md (create if missing)

Standard security policy:
- How to report vulnerabilities (email or private issue)
- Supported versions (or state "latest only")
- Response timeline expectation
- Keep it under 30 lines

### 2.10 — .editorconfig (create if missing)

Add a minimal .editorconfig for consistent formatting:
- `root = true`
- Default: utf-8, LF line endings, final newline, trim trailing whitespace
- Language-appropriate indent style and size (detect from existing code)
- Markdown: preserve trailing whitespace (line breaks)

### 2.11 — Pre-commit Hooks & Git Hooks

Set up pre-commit hooks appropriate to the project's ecosystem. Detect which system is already in use, if any, and prefer it. If none exists, choose the right one for the stack.

**Detection order:** Check for existing `.pre-commit-config.yaml`, `.husky/`, `.lefthook.yml`, `.lintstagedrc*`, or `lint-staged` in package.json.

**Python projects — use [pre-commit](https://pre-commit.com/):**
- Create `.pre-commit-config.yaml` if missing
- Include hooks appropriate to the project. Common defaults:
  - `pre-commit-hooks`: `trailing-whitespace`, `end-of-file-fixer`, `check-yaml`, `check-added-large-files`, `check-merge-conflict`, `detect-private-key`
  - `ruff-pre-commit`: `ruff` (lint) and `ruff-format` (format) — if ruff is used or no linter exists yet
  - `mypy` — if type checking is used in the project
- Add `pre-commit` to dev dependencies in pyproject.toml (under `[project.optional-dependencies]` or `[dependency-groups]` as appropriate)
- Do NOT add framework-specific hooks the project doesn't use

**Node/TypeScript projects — use [Husky](https://typicode.github.io/husky/) + [lint-staged](https://github.com/lint-staged/lint-staged):**
- Initialize husky if `.husky/` doesn't exist: ensure `prepare` script is in package.json (`"prepare": "husky"`)
- Create `.husky/pre-commit` with `npx lint-staged` (or `pnpm exec lint-staged` / `yarn lint-staged` matching the project's package manager)
- Configure lint-staged (in `package.json` under `"lint-staged"` key, or `.lintstagedrc.json`):
  - `*.{js,jsx,ts,tsx}`: run the project's linter (eslint, biome, etc.) and formatter (prettier, biome, etc.)
  - `*.{json,md,yml,yaml,css,scss}`: run formatter if one exists
- Add `husky` and `lint-staged` to devDependencies if not present
- If the project uses Biome instead of ESLint/Prettier, configure lint-staged to use `biome check --apply`

**Rust projects — use a simple `.githooks/` or shell-based approach:**
- Create `.githooks/pre-commit` running `cargo fmt --check && cargo clippy -- -D warnings`
- Add a note in CONTRIBUTING.md: `git config core.hooksPath .githooks`
- Or, if the project already uses `cargo-husky`, configure that instead

**Go projects — use [pre-commit](https://pre-commit.com/) or a shell hook:**
- If pre-commit is used: add `golangci-lint` and `gofmt` hooks
- Otherwise: create `.githooks/pre-commit` running `gofmt -l . && golangci-lint run`

**Multi-language / monorepo projects:**
- Use pre-commit (it supports multiple languages natively)
- Or use Husky + lint-staged at the root if it's Node-based

**General rules for all pre-commit setups:**
- Hooks should be fast — lint and format only staged files, not the entire repo
- Do NOT include hooks that run the full test suite (that belongs in CI)
- Do NOT include hooks for tools that aren't already in the project's deps (except the hook runner itself)
- If a linter/formatter doesn't exist in the project yet, prefer: ruff (Python), biome or eslint+prettier (Node), clippy+rustfmt (Rust), golangci-lint (Go)
- Ensure `.gitignore` does NOT ignore the hook config files (`.pre-commit-config.yaml`, `.husky/`)

### 2.12 — CI/CD Configs (only if they already exist)

If CI configs exist (.github/workflows/*.yml, etc.), audit them:
- Ensure they run on the correct branches
- Ensure they test on the correct language/runtime versions
- Do NOT create CI configs from scratch unless the user asks

## Step 3: Verify Consistency

After making changes:

1. Ensure .gitignore and .env.example are consistent (every .env key has an example)
2. Ensure README quick-start commands match the actual project setup
3. Ensure CLAUDE.md commands match the actual project setup
4. Ensure the license name in README matches the LICENSE file
5. Ensure no secrets are exposed in any committed file — scan for API keys, tokens, passwords
6. Ensure pre-commit hook config references tools that are actually in the project's dependencies
7. Ensure CONTRIBUTING.md mentions the pre-commit setup and how to install hooks
8. Run `git diff` and present a summary of all changes made

## Step 4: Report

Present a final checklist to the user:

```
OSS Readiness Report
====================
[x] README.md — updated (added Features, Contributing sections)
[x] LICENSE — created (MIT)
[x] .gitignore — updated (added IDE, OS entries)
[ ] .dockerignore — skipped (no Docker usage)
[x] .env.example — updated (added 2 new variables)
...
```

Include any manual action items the user still needs to handle (e.g., "Update the copyright holder name in LICENSE", "Add your actual project URL to pyproject.toml").
