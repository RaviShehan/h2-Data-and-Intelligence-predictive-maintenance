# H2 Data Intelligence Security Guide

This document explains the security and Git safety practices used in the H2 Data and Intelligence component.

## 1. Environment Variables

The project uses a `.env` file to store local database configuration.

Example:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=h2_predictive_maintenance
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
```

The `.env` file must not be pushed to GitHub because it may contain real passwords.

A safe example file is provided:

```text
.env.example
```

Developers should copy `.env.example` to `.env` and replace the password locally.

## 2. Files Ignored by Git

The `.gitignore` file should include:

```text
.env
data/raw/
venv/
__pycache__/
*.pyc
```

These files and folders are ignored because they may contain secrets, large data, or generated files.

## 3. Raw Dataset Safety

The raw NASA IMS Bearing Dataset is stored locally inside:

```text
data/raw/
```

This folder is ignored by Git because the raw dataset is large and should not be uploaded to GitHub.

Only the processed dataset is used in the project:

```text
data/training_data_real.csv
```

## 4. Database Password Safety

The PostgreSQL password should only be stored in the local `.env` file.

Do not write the real password inside:

* README files
* Python source code
* screenshots
* Git commits
* GitHub issues
* documentation files

## 5. Safe Git Workflow

Before pushing, always check:

```bash
git status
```

Make sure `.env` and `data/raw/` are not included.

Then push only safe files:

```bash
git add .
git commit -m "Commit message"
git push
```

## 6. If a Password Is Accidentally Exposed

If a real database password is accidentally shown in code, screenshots, or GitHub:

1. Change the PostgreSQL password immediately.
2. Update the local `.env` file.
3. Remove the password from code or documentation.
4. Commit the cleaned files.
5. Avoid reusing the exposed password.

## 7. API Security Limitations

This project is currently a local university project.

Current limitations:

* No user authentication is implemented.
* API endpoints are open locally.
* No HTTPS is configured.
* No production secrets manager is used.
* No rate limiting is implemented.

## 8. Future Security Improvements

Future improvements can include:

* Add API authentication
* Add role-based access control
* Use HTTPS in deployment
* Use Docker secrets or cloud secret manager
* Add API rate limiting
* Add input logging and audit logs
* Add stronger database user permissions
