# ING Cookie Tests

This repository contains a small Playwright + pytest test suite verifying the cookie consent flow on the ING landing page.

## Quick setup

Before procedding, make sure you have `python` installed on your computer.

1. Create and activate a virtual environment (recommended path: `.venv`):

```bash
python3 -m venv .venv
source .venv/bin/activate    # zsh this command can defer depending on the OS.
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Install Playwright browsers (required for running tests locally):

```bash
python -m playwright install --with-deps
```

## Running the tests locally

From the repository root with your venv activated:

- Run the full suite (default is headless):

```bash
pytest
```

- Run tests for a specific browser:

```bash
pytest --browser=chromium       # or firefox, webkit
```

- Run tests in headed mode (visible browser window):

```bash
pytest --browser=chromium --headed
```

## CI/CD configuration

File: `.github/workflows/playwright.yaml`.

This setup allows cross-browser test runs on every push/PR and keeps traces and reports for failed runs.

Key considerations:

- Supports parallel runs (chrome, firefox, safari)
- caches python packages for faster runs.
- generates artifacts video/screenshots/trace after each test run to `test-results` folder.
