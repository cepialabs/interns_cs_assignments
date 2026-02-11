# Nikto Scan Report – DVWA

## 1. Scan Overview

- **Target Application:** Damn Vulnerable Web Application (DVWA)
- **Target URL:** http://127.0.0.1/DVWA
- **Tool Used:** Nikto v2.5.0
- **Scan Type:** Web server vulnerability and misconfiguration scan
- **Environment:** Localhost (Lab environment – intentionally vulnerable)

Nikto was used to identify common web server issues such as insecure headers, outdated components, and potential misconfigurations. Since DVWA is an intentionally vulnerable application, findings must be interpreted carefully.

---

## 2. Dangerous / Suspicious Findings

### 2.1 PHP Backdoor File Manager Detected

**Nikto Output:**

![nikto-dvwa-output](nikto_dvwa_output.png)


**Nikto Interpretation:**
- Nikto flagged these URLs as **PHP backdoor file manager locations**
- The `filesrc=/etc/hosts` parameter is commonly used by web shells to read server files

**Security Impact (If Real):**
- Would allow an attacker to:
  - Read sensitive server files
  - Execute commands remotely
  - Fully compromise the web server

**Important Interpretation:**
- DVWA **does not ship with WordPress by default**
- These paths are **generic Nikto signatures**
- Nikto reports *potential* issues based on known patterns, not confirmed exploits

**Conclusion:**
**Likely a false positive**  
Manual verification is required to confirm whether these files actually exist and are accessible.

---

## 3. Outdated or Vulnerable Components

### 3.1 Generic WordPress Path Detection

Nikto attempted to detect:
- `/wordpress/`
- `/wp-content/`
- `/wp-includes/`

**Interpretation:**
- Nikto assumes WordPress may be installed and checks for known vulnerable paths
- DVWA itself is **not WordPress-based**
- No confirmed WordPress installation was verified during the scan

**Conclusion:**
**Unconfirmed / assumed component detection**  
This highlights Nikto’s signature-based nature and the need for manual validation.

---

## 4. Potential Misconfigurations

### 4.1 Exposure of Sensitive Files (Theoretical)

The scan attempted access to:
- `/etc/hosts`

**Interpretation:**
- This would indicate a serious misconfiguration if accessible
- However, Nikto only tested for the presence of known exploit patterns
- It does not confirm successful file access unless explicitly stated

**Conclusion:**
**Potential misconfiguration, not confirmed**
Manual testing (browser or curl) is required to validate exploitability.

---

## 5. Dangerous or Missing HTTP Headers

**Note:**  
The provided output does not explicitly list HTTP security headers.

However, based on DVWA’s known insecure setup, the following headers are typically **missing or misconfigured**:

- `Content-Security-Policy`
- `X-Frame-Options`
- `X-Content-Type-Options`
- `Strict-Transport-Security`

**Security Impact:**
- Missing headers can lead to:
  - Clickjacking
  - MIME-type sniffing
  - XSS attacks
  - Man-in-the-middle attacks

**Interpretation:**
This aligns with DVWA’s purpose as a deliberately insecure application.

---

## 6. Why Nikto Output Should Not Be Blindly Trusted

- Nikto uses **signature-based detection**
- It reports **possible vulnerabilities**, not confirmed exploits
- Many findings require:
  - Manual file existence checks
  - Version validation
  - Exploit verification

In this scan:
- Several findings are **generic WordPress checks**
- DVWA is intentionally vulnerable, which can amplify alerts
- No confirmed exploitation was demonstrated

---

## 7. Final Conclusion

- Nikto successfully identified **potential security risks and misconfigurations**
- Some findings appear to be **false positives**
- Manual verification is essential before labeling issues as real vulnerabilities
- This scan demonstrates why automated tools should be used as **assistive tools**, not absolute truth

---