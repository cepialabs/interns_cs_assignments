## Scanning Metasploitable Using Nmap NSE Scripts
### Introduction

Metasploitable is an intentionally vulnerable virtual machine designed for learning and practicing penetration testing. In this task, Nmap Scripting Engine (NSE) vulnerability scripts were used to identify potential security weaknesses and verify whether they correspond to real, publicly known CVEs.

## Tool and Technique Used
### Tool
- Nmap (Network Mapper)
- Nmap Scripting Engine (NSE)

### Scan Command Used
```bash
 nmap --script vuln <Metasploitable-IP>
```
### Purpose of the command:
``` --script vuln ``` → Run vulnerability detection scripts
## Identified Vulnerabilities and CVE Validation
### 1. CVE-2023-38408
Affected Software

OpenSSH (with agent forwarding enabled)

What is the vulnerability?

CVE-2023-38408 is a vulnerability in OpenSSH agent forwarding. When agent forwarding is enabled, a malicious or compromised remote server can exploit the SSH agent and execute arbitrary commands on the client system.

Impact

Remote Code Execution on the client machine

Attacker can run commands with the user’s privileges

Possible data theft, credential abuse, or lateral movement

Why it matters

This vulnerability breaks the trust model of SSH. Even though SSH is considered secure, enabling agent forwarding can expose the client system if the remote server is compromised.

Severity: High
Key Risk: Client-side compromise through trusted SSH connections

![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%203/Assignment%202/Images/CVE%201.png?raw=true)

### 2. CVE-2016-1908
Affected Software

libssh (SSH library used by multiple applications)

What is the vulnerability?

CVE-2016-1908 is an authentication bypass vulnerability in libssh. Due to improper handling of authentication states, an attacker can bypass authentication and gain access without valid credentials.

Impact

Unauthorized access to SSH services

Attacker can log in without authentication

Full compromise of the affected service or system

Why it matters

Authentication bypass vulnerabilities are extremely dangerous because they allow attackers to skip security controls entirely and gain direct access.

Severity: Critical
Key Risk: Unauthenticated system access
![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%203/Assignment%202/Images/CVE%202.png?raw=true)

### 3. CVE-2011-2523
Affected Software

vsftpd 2.3.4 (FTP server)

What is the vulnerability?

CVE-2011-2523 is a backdoor vulnerability in vsftpd version 2.3.4. A malicious backdoor was inserted into the software, allowing attackers to gain shell access by using a specially crafted username.

Impact

Remote shell access without authentication

Complete system compromise

Attacker can execute arbitrary commands

Why it matters

This vulnerability allows full system takeover with no credentials required and is commonly found in vulnerable systems like Metasploitable.

Severity: Critical
Key Risk: Full remote system control
![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%203/Assignment%202/Images/CVE%203.png?raw=true)

## Summary Table
| CVE ID | Affected Software | Vulnerability Type | Impact | Severity |
|------|------------------|-------------------|--------|----------|
| CVE-2023-38408 | OpenSSH | Agent Forwarding RCE | Client-side code execution | High |
| CVE-2016-1908 | libssh | Authentication Bypass | Unauthorized system access | Critical |
| CVE-2011-2523 | vsftpd 2.3.4 | Backdoor RCE | Full system compromise | Critical |
