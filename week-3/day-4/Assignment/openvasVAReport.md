# OpenVAS (Greenbone) Vulnerability Assessment Report

## 1. Environment Setup

- Scanner: OpenVAS / Greenbone Community Edition
- Target 1: Metasploitable 2 (192.168.56.102)
- Target 2: DVWA hosted on Kali Linux (192.168.56.101)
- Scan Type: Full and Fast Scan
- Network Mode: VirtualBox Host-Only Adapter

---

# 2. Scan Results – Metasploitable 2

Metasploitable is intentionally vulnerable and contains multiple exploitable services.

## High Severity Findings

### 1. VSFTPD 2.3.4 Backdoor Vulnerability
- Port: 21
- CVSS Score: 10.0
- Description: VSFTPD 2.3.4 contains a backdoor allowing remote command execution.
- Impact: Attacker can gain remote shell access.
- Remediation: Upgrade or remove vulnerable FTP service.

### 2. UnrealIRCd Backdoor Command Execution
- Port: 6667
- CVSS Score: 10.0
- Description: UnrealIRCd shipped with a malicious backdoor.
- Impact: Remote attacker can execute arbitrary commands as root.
- Remediation: Replace with trusted version.

### 3. Samba Remote Code Execution (CVE-2007-2447)
- Port: 445
- CVSS Score: 9.3
- Description: Samba username map script vulnerability allows command injection.
- Impact: Remote root compromise possible.
- Remediation: Upgrade Samba to secure version.

---

## Medium Severity Findings

### 1. MySQL Service Exposed
- Port: 3306
- Description: MySQL allows remote connections.
- Impact: Database enumeration and brute-force attempts.
- Remediation: Restrict access and enforce strong authentication.

### 2. Outdated Apache HTTP Server (2.2.x)
- Port: 80
- Description: Detected outdated Apache version with known vulnerabilities.
- Impact: Information disclosure and possible exploitation.
- Remediation: Update to latest stable release.

---

## 🔵 Informational Findings

- OpenSSH 4.7p1 detected on port 22
- Multiple RPC services enabled
- Linux Kernel 2.6.x identified
- Multiple open TCP ports discovered
- Service banner information exposed

---

# 3. Scan Results – DVWA

DVWA is intentionally insecure and contains multiple web application vulnerabilities.

## High Severity Findings

### 1. PHP-CGI Argument Injection Vulnerability
- Port: 80
- Description: PHP-CGI vulnerability allows command execution.
- Impact: Remote code execution on web server.
- Remediation: Upgrade PHP to patched version.

### 2. Directory Listing Enabled
- Port: 80
- Description: Apache directory indexing enabled.
- Impact: Sensitive file exposure.
- Remediation: Disable directory listing in Apache configuration.

---

## Medium Severity Findings

### 1. SQL Injection Vulnerability
- Description: Input parameters vulnerable to SQL Injection.
- Impact: Authentication bypass and database extraction.
- Remediation: Use parameterized queries and prepared statements.

### 2. Cross-Site Scripting (Reflected XSS)
- Description: User input not properly sanitized.
- Impact: Session hijacking and client-side attacks.
- Remediation: Implement input validation and output encoding.

### 3. Missing Security Headers
- X-Frame-Options not set
- X-Content-Type-Options not set
- Content-Security-Policy missing
- Impact: Increased exposure to clickjacking and injection attacks
- Remediation: Configure proper HTTP security headers

---

## Informational Findings

- Apache HTTP Server detected
- PHP version disclosure
- Cookies missing HttpOnly flag
- Server banner information exposed

---

- Metasploitable contains multiple critical remote code execution vulnerabilities.
- DVWA contains common web application vulnerabilities such as SQL Injection and XSS.
- Both systems demonstrate how outdated software and misconfigurations increase attack surface.
- Regular vulnerability scanning and patch management are essential for securing production environments.
