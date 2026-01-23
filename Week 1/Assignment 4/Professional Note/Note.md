## TITLE
Security Misconfiguration (Public FTP Directory Exposure)
## TARGET
Website: http://localhost:3000

Affected Path: /ftp/

## OWASP Mapping
OWASP Top 10 Category:
A05:2021 – Security Misconfiguration

#### Servertiy- HIGH

## SCOPE
The scope of this assessment was limited:

- Only access to the /ftp directory was checked.

- No exploitation, deletion, or modification was attempted.

- Testing was non-destructive and for educational purposes.

## Vulnerability Description
Security misconfiguration a situation where an information system, application, server, or network is not properly
configured from a security prespective making it vulnerable to unauthorized access or attacks. The impact of this vulernability
leading to data breaches, priviliges escalation, service disruption or complete system compromise.

The FTP directory is publicly accessible without any authentication.

If a user visits the /ftp/ path, the server allows directory listing and the stored files become publicly visible.

This indicates improper access control and security misconfiguration, which could expose sensitive data to unauthorized users.

## Observation
During testing, the following was observed:

- The /ftp/ URL was accessible without login. Directory listing was enabled.

- Multiple files and folders were publicly visible. No access restriction or authentication was being used.

## Question
- Why is the FTP directory allowed for public access?

- Do the exposed files contain sensitive or confidential data?

- Is proper authentication and access control configured on the server?

- Is directory listing disabled in the production environment?

## Learning
This vulnerability provides important lessons:

- Sensitive directories should never be left open to public access.

- Server-side access control and authentication should be properly configured.

- Disabling directory listings is a basic security best practice.

- Security misconfiguration is a common but high-risk weakness.

- Regular security audits can prevent such issues.
