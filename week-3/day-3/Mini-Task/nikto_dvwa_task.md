# Nikto Mini Task – DVWA Scan Findings

## Scan Overview

- **Target:** Damn Vulnerable Web Application (DVWA)
- **URL:** http://127.0.0.1/DVWA
- **Tool:** Nikto
- **Environment:** Local lab setup
- **Purpose:** Identify basic misconfigurations and potentially vulnerable components using automated scanning and manual interpretation.

---

## Identified Misconfigurations

### 1. Missing Security HTTP Headers

**Observation (from Nikto output and DVWA behavior):**
Nikto indicates the absence of commonly recommended HTTP security headers.

**Affected Headers:**
- `X-Frame-Options`
- `X-Content-Type-Options`
- `Content-Security-Policy`
- `Strict-Transport-Security`

**Why this is a misconfiguration:**
- Missing headers can expose the application to:
  - Clickjacking
  - MIME-type sniffing
  - Cross-site scripting (XSS)
  - Man-in-the-middle attacks

**Interpretation:**
DVWA is intentionally insecure, so missing headers are expected. However, in a real-world application, this would be considered a serious configuration weakness.

---

### 2. Exposure to Common Exploit Path Probing

**Nikto Finding:**
Nikto attempted access to multiple well-known paths such as:
```bash
/wordpress/wp-content/
/wordpress/wp-includes/
```


**Why this is a misconfiguration:**
- The web server responds in a way that allows Nikto to probe for common CMS-related paths.
- This increases the attack surface by enabling automated reconnaissance.

**Interpretation:**
Although DVWA does not use WordPress, Nikto’s ability to probe these paths indicates that the server does not restrict or hide unnecessary routes. This is acceptable in a lab environment but unsafe in production.

---

## Potentially Vulnerable Component

### Suspected PHP Backdoor / File Inclusion Pattern

**Nikto Output Example:**
```bash
server.php?filesrc=/etc/hosts
```


**Why this is flagged:**
- The `filesrc` parameter is commonly associated with PHP web shells or file inclusion vulnerabilities.
- If exploitable, this could allow attackers to read sensitive system files.

**Interpretation (Important):**
- Nikto flags this based on known attack signatures.
- DVWA does not include these files by default.
- No confirmed file disclosure was observed during the scan.

**Conclusion:**
This is a **potential vulnerability**, not a confirmed one. Manual verification is required before treating it as a real exploit.

---

## Evidence

A screenshot of the Nikto scan output has been attached to support the findings and confirm tool execution.

---

## Final Notes

- Nikto provides **indicative results**, not proof of exploitation.
- Findings must always be manually validated.
- This task demonstrates the importance of interpreting automated scan results instead of blindly trusting them.

---
