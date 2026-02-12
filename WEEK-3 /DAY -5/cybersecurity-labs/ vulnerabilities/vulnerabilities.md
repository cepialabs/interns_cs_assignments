# Mini Project: Vulnerability Assessment Report  
Target Application: OWASP Juice Shop  
Test Environment: Kali Linux (VirtualBox)  
Assessed by: Zubair Wani  
Date: Feb 2026  

---

## Objective
The objective of this project is to perform vulnerability assessment on a deliberately vulnerable web application (OWASP Juice Shop) in order to identify, validate, and prioritize security weaknesses using manual testing techniques.

---

## Scope
- Application: OWASP Juice Shop (Express v4.21.0)
- Type: Web Application Security Testing
- Testing Method: Black-box & Grey-box testing
- Tools Used:
  - Kali Linux
  - Firefox Browser
  - Burp Suite (basic interception)
  - Manual payload testing

---

## Methodology
1. Application Reconnaissance  
2. Identification of Input Points  
3. Manual Vulnerability Testing  
4. Validation of Findings  
5. Evidence Collection  
6. Risk Prioritization  

---

# Identified Vulnerabilities

---

## 1. Security Misconfiguration – Open FTP Directory (High)

**URL:**  
http://localhost:3000/ftp  

**Description:**  
The FTP directory is publicly accessible without authentication, allowing attackers to browse and download sensitive internal files.

**Evidence:**  
Accessible files:
- acquisitions.md  
- incident-support.kdbx  
- suspicious_errors.yml  
- legal.md  
- package.json.bak  

**Impact:**  
- Sensitive information disclosure  
- Credential leakage  
- Internal system exposure  

**Severity:** High  

---

## 2. Improper API Handling / Error Disclosure (Medium)

**URL:**  
http://localhost:3000/api  

**Description:**  
The application throws a detailed server error revealing internal backend stack trace, file paths, and application framework details.

**Impact:**  
- Information leakage  
- Application structure exposure  
- Easier exploitation  

**Severity:** Medium  

---

## 3. Broken Authentication & Access Control (High)

**Description:**  
The application allows weak authentication mechanisms and improper access control which can lead to unauthorized access.

**Impact:**  
- Unauthorized account access  
- Privilege escalation  

**Severity:** High  

---

## 4. Sensitive Data Exposure (Medium)

**Description:**  
Sensitive system files and application backups are exposed via open FTP directories.

**Impact:**  
- Data leakage  
- Privacy breach  
- Credential exposure  

**Severity:** Medium  

---

## Conclusion
During this vulnerability assessment, multiple critical and high-risk vulnerabilities were discovered including security misconfiguration, sensitive data exposure, and broken authentication. These vulnerabilities can lead to severe data breaches and system compromise if exploited in real-world environments.

Immediate remediation is recommended to secure exposed directories, sanitize error handling, and strengthen authentication mechanisms.

---

## Learning Outcome
This project improved hands-on skills in:
- Manual vulnerability discovery
- Web application security testing
- Practical exploitation understanding
- Professional security documentation
