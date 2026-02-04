# Attack Surface Analysis

## Objective
The objective of this section is to analyze and summarize the overall attack surface of the target based on findings from network scanning, subdomain discovery, and OSINT activities. This helps in understanding potential entry points that could be abused by an attacker.

## Target Information
- **Target Type:** Public-facing Web Application (Intentionally Vulnerable)
- **IP Address:** 137.74.187.104
- **Domain Name:** hackthissite.org
- **Assessment Purpose:** Internship Task

---

## Attack Surface Overview
The attack surface represents all externally exposed points through which an attacker could attempt to gain unauthorized access or information. These include network services, web applications, subdomains, and publicly available information.

---

## 1. Network-Level Attack Surface

### Identified Components
- Open Ports: 22 (SSH), 80 (HTTP), 443 (HTTPS)
- Services accessible directly from the internet

### Potential Risks
- SSH service may be targeted for unauthorized access if misconfigured.
- Web services increase exposure to application-layer attacks.
- Multiple open ports expand the network footprint.

---

## 2. Application-Level Attack Surface

### Identified Components
- Web application accessible over HTTP and HTTPS
- Publicly reachable login and user interaction pages
- Input points such as URLs, forms, and parameters

### Potential Risks
- Web vulnerabilities such as SQL Injection, XSS, or authentication issues
- Misconfigurations in web server or application logic
- Improper access control on sensitive endpoints

---

## 3. Subdomain-Based Attack Surface

### Identified Components
- Multiple publicly accessible subdomains discovered through OSINT tools
- Subdomains potentially hosting different services or environments

### Potential Risks
- Legacy or less-maintained subdomains may have weaker security
- Inconsistent security controls across subdomains
- Additional applications increase reconnaissance opportunities for attackers

---

## 4. OSINT-Based Attack Surface

### Identified Components
- Publicly indexed pages and resources
- Exposed documents (e.g., PDF files)
- Login pages and authentication endpoints
- Possible directory listing indicators

### Potential Risks
- Information disclosure aiding targeted attacks
- Metadata leakage from public documents
- Increased likelihood of credential-based attacks on login pages

---

## Overall Risk Assessment
**Medium Risk**

The overall risk is assessed as medium due to the presence of multiple exposed services, publicly accessible subdomains, and information disclosure through OSINT. Although no active exploitation was performed, these factors collectively increase the potential attack surface.

---

## Recommendations
- Reduce exposed network services to the minimum required.
- Harden SSH access using key-based authentication and access restrictions.
- Apply consistent security configurations across all subdomains.
- Limit public exposure of sensitive information and documents.
- Disable directory listing and unnecessary indexing.
- Perform regular vulnerability assessments and security reviews.

---

## Conclusion
The attack surface analysis highlights multiple externally exposed components associated with the target system. While the assessment was limited to non-intrusive techniques, the findings indicate that continuous monitoring, proper hardening, and regular security assessments are essential to reduce potential security risks.
