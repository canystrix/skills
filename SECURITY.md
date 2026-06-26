# Security Policy

## Reporting a Vulnerability

This is a private repository. If you discover a security vulnerability, contact the repository owner directly.

## Security Controls

This repository is protected by:

- **Pre-commit hooks:** Secrets detection via gitleaks (JWT, private keys, API keys, credentials)
- **Pre-push hooks:** Dependency vulnerability scanning, force-push prevention to protected branches
- **CI/CD:** Automated security scanning on every push and pull request (gitleaks, pip-audit/npm audit, SAST patterns)
- **Dependabot:** Automated dependency update monitoring

## Secrets Management

- No credentials, API keys, or tokens are stored in this repository
- Secrets are managed via environment variables (`.env` files, gitignored)
- See `.env.example` for required environment variable names

## Dependency Policy

- All dependencies pinned to exact versions
- Prohibited licenses: AGPL-3.0, SSPL-1.0, BSL-1.1
- Weekly automated vulnerability scanning via Dependabot and CI

## Branch Protection

- Force-push to main/master is blocked (local pre-push hook)
- All changes should go through pull requests
- CI must pass before merge (by convention — GitHub Free plan)
