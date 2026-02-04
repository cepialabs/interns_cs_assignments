# Subdomain Discovery

## Objective
The objective of this activity is to identify publicly accessible subdomains associated with the target domain using passive reconnaissance techniques. Discovering subdomains helps in expanding the attack surface and identifying additional assets that may be less secured.

## Target Information
- **Domain Name:** hackthissite.org
- **Associated IP Address:** 137.74.187.104
- **Assessment Purpose:** Internship Task
- **Reconnaissance Type:** Passive (OSINT-based)

---

## Tools Used
- Online Subdomain Finder (subdomainfinder.c99.nl)
- theHarvester

---

## Methodology
Subdomain enumeration was performed using publicly available OSINT tools and search-based techniques. No active scanning or intrusive interaction with the target infrastructure was conducted.

---

## 1. Subdomain Enumeration using subdomainfinder.c99.nl

### Tool Used
- **Website:** subdomainfinder.c99.nl
  
![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%202/Mini%20Project/Cybersecurity-Labs/Images/subdomain.png?raw=true)

### Technique
- Online passive subdomain enumeration
- Search engine and DNS-based data sources

### Purpose
- Identify known subdomains indexed in public sources
- Quickly map external domain footprint

### Observation
- Multiple subdomains related to the target domain were identified.
- The results indicate the presence of additional publicly accessible assets.

---

## 2. Subdomain Enumeration using theHarvester

### Tool Used
- **theHarvester**

![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%202/Mini%20Project/Cybersecurity-Labs/Images/harvester%20subdomain.png?raw=true)

### Command Used
```bash

theHarvester -d hackthissite.org -b google,bing,duckduckgo
```
### Findings Summary
| Tool Used              | Result                         |
| ---------------------- | ------------------------------ |
| subdomainfinder.c99.nl | Multiple subdomains identified |
| theHarvester           | Multiple subdomains identified |

### Security Impact

- Each discovered subdomain represents an additional attack surface.
- Some subdomains may host legacy, testing, or staging environments.
- Inconsistent security configurations across subdomains may introduce risk.
