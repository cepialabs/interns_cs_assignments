# Pentester Workflow Simulation

## Target Application
testphp.vulnweb.com  
testhtml5.vulnweb.com  

---

## Objective

To simulate a **real penetration testing workflow** by following structured steps:

Observe → Identify Risk → Analyze Traffic → Document Findings

---

# Step 1: Observation Phase

### Actions:
- Browsed the web application manually.
- Explored links, parameters, input fields, and page behavior.
- Inspected page source and application structure.

### Findings:
- Input parameters visible in URL.
- Dynamic parameters passed in requests.
- Reflected user input observed.

---

# Step 2: Risk Identification Phase

### Actions:
- Identified suspicious parameters.
- Tested basic payloads:
  - `' OR '1'='1`
  - `<script>alert(1)</script>`

### Findings:
- Application reflects unsanitized user input.
- High probability of:
  - SQL Injection
  - Cross-Site Scripting (XSS)

---

# Step 3: Traffic Analysis Phase

### Tools Used:
- Browser Developer Tools (Network Tab)
- Nikto Web Scanner

---

### DevTools Findings:

- Analyzed:
  - Request headers
  - Response headers
  - Parameters
  - Cookies
- Found:
  - Missing security headers
  - Reflected parameters
  - Weak client-side filtering

---

### Nikto Scan Findings:

```bash
nikto -h http://testphp.vulnweb.com
