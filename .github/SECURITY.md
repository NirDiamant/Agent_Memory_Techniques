# Security Policy

This repository hosts educational notebooks. It does not run services or accept user input at scale. Still, we take security seriously for contributors and readers.

## Reporting a vulnerability

Please do not open public issues for security-sensitive reports.

Send details to the maintainer through GitHub (open a private security advisory: https://github.com/NirDiamant/Agent_Memory_Techniques/security/advisories/new) or by direct message on any of the channels listed in the README under "Stay Updated".

We will acknowledge within 7 days and aim to respond with a fix or mitigation plan within 30 days.

## Scope

Examples of issues we care about:

- Notebook code that leaks API keys or user data
- Instructions that lead readers to unsafe patterns in production
- Dependencies with known CVEs that are installed by our `requirements.txt`
- Tutorial examples that could be misused for credential harvesting or scraping at harmful scale

Out of scope:

- Third-party service behavior (report to the service directly)
- Personal API keys checked into forks (the fork owner should rotate the key)
