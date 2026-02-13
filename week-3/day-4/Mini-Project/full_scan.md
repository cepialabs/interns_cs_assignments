# OpenVAS Full Scan Analysis – Metasploitable 2

## 1. Scan Overview

- Scanner Used: OpenVAS (Greenbone Vulnerability Manager)
- Scan Type: Full and Fast Scan
- Target Machine: Metasploitable 2
- Target IP: 192.168.56.102
- Purpose: Identify vulnerabilities and analyze high-risk findings

---

# 2. Selected Vulnerabilities from Full Scan Report

Below are 5 significant vulnerabilities identified during the full scan of Metasploitable 2.

---

## 1. VSFTPD 2.3.4 Backdoor Vulnerability

- Port: 21
- Severity: High
- CVE: CVE-2011-2523

### What It Means

VSFTPD version 2.3.4 contains a malicious backdoor introduced into the source code. When a specially crafted username is used during FTP login, it triggers a hidden backdoor service.

### Why It Is Dangerous

- Allows remote attackers to gain shell access.
- Can lead to full system compromise.
- No authentication required once triggered.

### Real-World Impact

An attacker can gain remote command execution and completely control the server.

---

## 2. Samba Username Map Script Command Injection

- Port: 445
- Severity: High
- CVE: CVE-2007-2447

### What It Means

Samba contains a vulnerability in the username map script feature. Improper input validation allows attackers to inject system commands through crafted usernames.

### Why It Is Dangerous

- Allows remote code execution.
- Can result in root-level access.
- Exploitable without valid credentials.

### Real-World Impact

Attackers can execute arbitrary commands on the target machine.

---

## 3. UnrealIRCd Backdoor Vulnerability

- Port: 6667
- Severity: High

### What It Means

The installed UnrealIRCd version was distributed with a backdoor. Attackers can send specially crafted messages to execute commands.

### Why It Is Dangerous

- Direct remote command execution.
- No authentication required.
- Complete compromise possible.

### Real-World Impact

An attacker can execute system commands remotely and take full control of the server.

---

## 4. MySQL Service Exposed to Remote Connections

- Port: 3306
- Severity: Medium

### What It Means

The MySQL database service is accessible over the network without proper restrictions.

### Why It Is Dangerous

- Enables brute-force attacks.
- Allows database enumeration.
- May expose sensitive data.

### Real-World Impact

Attackers can attempt credential attacks and potentially access confidential database information.

---

## 5. Outdated Apache HTTP Server (2.2.x)

- Port: 80
- Severity: Medium

### What It Means

The Apache version running is outdated and contains multiple known vulnerabilities.

### Why It Is Dangerous

- May allow information disclosure.
- Could be vulnerable to denial-of-service attacks.
- Could be exploited as part of an attack chain.

### Real-World Impact

Attackers can exploit known vulnerabilities in outdated web servers to gain access or disrupt services.

---

# 3. Conclusion

The full OpenVAS scan of Metasploitable 2 identified multiple critical vulnerabilities, especially remote code execution flaws.

Key observations:

- Multiple services allow unauthenticated remote command execution.
- Outdated software significantly increases attack surface.
- Exposed services without proper configuration create security risks.

This exercise demonstrates the importance of:

- Regular vulnerability scanning
- Patch management
- Proper service configuration
- Restricting unnecessary open ports

Metasploitable is intentionally vulnerable for learning purposes, but similar vulnerabilities in production environments could result in severe security breaches.
