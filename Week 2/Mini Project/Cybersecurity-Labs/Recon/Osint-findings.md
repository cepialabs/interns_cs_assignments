# OSINT Findings

## Objective
The objective of this activity is to gather publicly available information related to the target domain using Open Source Intelligence (OSINT) techniques. OSINT helps in identifying information leakage that could assist an attacker during reconnaissance.

## Target Information
- **Domain Name:** hackthissite.org
- **Associated IP Address:** 137.74.187.104
- **Assessment Purpose:** Internship Task
- **Reconnaissance Type:** Passive (OSINT)

---

## Tools & Techniques Used
- Search Engine Reconnaissance (Google Dorking)
- Manual browser-based analysis
- Publicly accessible web resources

---

## 1. Search Engine Reconnaissance (Google Dorking)

```text
site:hackthissite.org
```
![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%202/Mini%20Project/Cybersecurity-Labs/Images/site.org.png?raw=true)

```
site:hackthissite.org filetype:pdf
```
![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%202/Mini%20Project/Cybersecurity-Labs/Images/filetype-pdf.png?raw=true)
```
inurl:login site:hackthissite.org
```
![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%202/Mini%20Project/Cybersecurity-Labs/Images/login%20dork%20(2).png?raw=true)

### 2. Information Identified
#### a) Publicly Accessible Pages
- Multiple web pages related to challenges and user interaction were indexed.
- Public pages reveal application structure and functionality.

#### b) Exposed Documents

- PDF files related to site content and documentation were found.
- Such files may contain metadata or sensitive information.

#### c) Directory Listing Indicators

- Search results suggested the possible presence of open directories.
- Directory listings can expose internal files and folder structures.

#### d) Login Pages and Authentication Endpoints

- Multiple login-related URLs were identified.
- These endpoints can be targeted for authentication-based attacks if not secured.

### Finding Summary
| Finding Type  | Description                            |
| ------------- | -------------------------------------- |
| Indexed Pages | Public pages indexed by search engines |
| Documents     | PDF files publicly accessible          |
| Directories   | Possible directory listing exposure    |
| Login Pages   | Authentication endpoints discovered    |

### Security Impact
- Publicly indexed information can help attackers map application structure.
- Exposed documents may leak sensitive metadata.
- Directory listings can expose internal resources.
- Login pages increase the risk of brute-force or credential-based attacks.
