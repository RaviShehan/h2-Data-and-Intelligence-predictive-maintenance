# H2 Data Intelligence CI/CD Guide

This document explains the GitHub Actions automated testing workflow used in the H2 Data and Intelligence component.

## 1. Purpose

The purpose of CI/CD in this project is to automatically check whether the project still works after code changes are pushed to GitHub.

CI means Continuous Integration.

In this project, CI is used to automatically run the pytest test suite on GitHub.

## 2. GitHub Actions Workflow File

The workflow file is located at:

```text
.github/workflows/tests.yml
```

This file tells GitHub Actions how to run automated tests.

## 3. When the Workflow Runs

The workflow runs automatically when:

* code is pushed to the `main` branch
* code is pushed to the `master` branch
* a pull request is opened to `main`
* a pull request is opened to `master`

## 4. What the Workflow Does

The workflow performs these steps:

1. Checks out the GitHub repository
2. Sets up Python 3.11
3. Starts a PostgreSQL service container
4. Installs project dependencies from `requirements.txt`
5. Runs the test suite using pytest

Test command:

```bash
python -m pytest tests
```

## 5. PostgreSQL in GitHub Actions

The workflow starts a temporary PostgreSQL database for testing.

Database configuration:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=h2_predictive_maintenance
DB_USER=postgres
DB_PASSWORD=postgres
```

This is only for GitHub Actions testing.

The real local `.env` file is not pushed to GitHub.

## 6. Expected Test Result

The expected result is:

```text
26 passed
```

This means the automated tests verify:

* FastAPI endpoints
* input validation
* feature extraction
* SciPy signal processing
* anomaly detection
* real NASA IMS model integration
* processed dataset structure
* feature importance report

## 7. Why This Is Useful

GitHub Actions makes the project more professional because tests are automatically checked after every push.

This helps detect errors early if code changes break the API, model integration, feature extraction, or documentation-related files.

## 8. How to Check Workflow Result

After pushing code to GitHub:

1. Open the GitHub repository
2. Click the `Actions` tab
3. Select `H2 Data Intelligence Tests`
4. Check whether the workflow passed or failed

A passing workflow means the project tests successfully ran on GitHub.

## 9. If the Workflow Fails

If the workflow fails:

1. Open the failed workflow run
2. Check the failed step
3. Read the error message
4. Fix the related file locally
5. Run tests locally:

```bash
venv\Scripts\python.exe -m pytest tests
```

6. Commit and push the fix

## 10. Viva Explanation

During viva, CI/CD can be explained like this:

The project uses GitHub Actions to automatically run the pytest test suite whenever code is pushed to GitHub. The workflow sets up Python, installs dependencies, starts a PostgreSQL service, and runs all tests. This proves that the project is continuously checked and reduces the chance of broken code being pushed.

