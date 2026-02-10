# Vulnerability Assessment Using Nmap on Metasploitable

## 1. Introduction

Vulner scanning is an important phase in penetration testing, which helps in the identification of security vulnerabilities in a specific target system. In this assignment, Nmap Vulnerability Scripts (NSE) are applied with a goal of scanning a Metasploitable virtual machine, which is a vulnerable Linux operating system.

The end goal of the assessment is to establish any possible vulnerabilities, their impact, and the reason for their importance in the context of security.

## 2. About Metasploitable

"Metasploitable" is a virtual machine designed to have weak security, created by the pen-testing company Rapid7. To be clear, it's a virtual machine with outdated services/configurations/vulnerabilities.

It is widely used by:

* Students interested in penetration testing
* Security professionals for practice * Ethical hacking labs and certifications

---

## 3. Tool Used: Nmap with NSE Scripts

**Nmap (Network Mapper)** is an open-source tool used for network discovery and vulnerability scanning.

### Nmap Scripting Engine (NSE)

NSE allows Nmap to run scripts that:

* Detect known vulnerabilities
* Identify misconfigurations
* Perform basic exploitation checks

For this scan, vulnerability-related NSE scripts were used.

---

## 4. Scan Methodology

The following steps were followed to perform the vulnerability assessment:

1. Identify the IP address of the Metasploitable machine
2. Perform a basic port scan to identify open services
3. Run Nmap vulnerability scripts against detected services
4. Analyze results and identify potential vulnerabilities

---

## 5. Nmap Commands Used

### Target
![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%203/Assignment%202/Images/Screenshot%202026-02-10%20222903.png?raw=true)
### 5.1 Basic Port and Service Scan

```bash
nmap -sV <target-ip>
```

This command identifies open ports and the services running on them.
![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%203/Assignment%202/Images/Screenshot%202026-02-10%20223407.png?raw=true)


### 5.2 Vulnerability Scan Using NSE

```bash
nmap -sV --script vuln <target-ip>
```

This command runs multiple vulnerability detection scripts against the target.

---
![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%203/Assignment%202/Images/Screenshot%202026-02-10%20222639.png?raw=true)

![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%203/Assignment%202/Images/Screenshot%202026-02-10%20222703.png?raw=true)

## 6. Vulnerabilities Identified

### 6.1 FTP Backdoor Vulnerability

**Service:** FTP (vsftpd 2.3.4)
**Script Detected:** ftp-vsftpd-backdoor

**Description:**
The vsftpd 2.3.4 service contains a malicious backdoor that allows attackers to gain remote shell access.

**Impact:**

* Unauthorized remote access
* Full system compromise

**Why it matters:**
This vulnerability allows attackers to take complete control of the system without authentication.

---

### 6.2 SMB Vulnerability

**Service:** SMB (Samba)
**Script Detected:** smb-vuln-ms08-067

**Description:**
A critical vulnerability in the SMB service that allows remote code execution.

**Impact:**

* Remote code execution
* System takeover

**Why it matters:**
This vulnerability has been widely exploited by worms and malware in real-world attacks.

---

### 6.3 Outdated Web Server Vulnerability

**Service:** Apache HTTP Server
**Script Detected:** http-vuln-cve scripts

**Description:**
The Apache web server running on Metasploitable is outdated and vulnerable to multiple known CVEs.

**Impact:**

* Information disclosure
* Potential remote code execution

**Why it matters:**
Outdated web services are common entry points for attackers.

---

## 7. Summary Table

| Service            | Port | Vulnerability | Impact                | Severity |
| ------------------ | ---- | ------------- | --------------------- | -------- |
| FTP (vsftpd 2.3.4) | 21   | Backdoor RCE  | Remote shell access   | Critical |
| SMB (Samba)        | 445  | MS08-067      | Remote code execution | Critical |
| Apache HTTP        | 80   | Multiple CVEs | Info disclosure / RCE | High     |

---

## 8. Conclusion

The Nmap vulnerability scan against Metasploitable revealed multiple critical and high-risk vulnerabilities. These weaknesses demonstrate how outdated services and poor security configurations can lead to complete system compromise.

This assessment highlights the importance of:

* Regular vulnerability scanning
* Timely patching and updates
* Proper service hardening

---

## 9. Ethical Considerations

All scans were performed in a controlled lab environment on Metasploitable, which is intentionally vulnerable. No unauthorized systems were scanned during this assessment.

---

## 10. References

* Nmap Official Documentation
* Metasploitable Documentation
* MITRE CVE Database
