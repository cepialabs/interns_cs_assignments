# OSINT Findings Report

## Target Overview
- Target Domain: singhgad.edu
- Organization: Sinhgad Institutes
- Reconnaissance Type: Passive OSINT
- Purpose: Educational and academic reconnaissance only

---

## 1. Domain & DNS Information

### DNS Lookup
- Domain Name: singhgad.edu
- IPv4 Address: 123.63.148.72
- IPv6 Address: 64:ff9b::7b3f:9448
- DNS Server Used: 10.19.181.191

This indicates the domain resolves to both IPv4 and IPv6 addresses and is actively hosted.

---

## 2. Subdomain Enumeration

### Tool Used
- Sublist3r

### Results Summary
- Total Unique Subdomains Found: 147+

### Notable Subdomains Identified
- admissions.singhgad.edu
- dashboard.admissions.singhgad.edu
- alumni.singhgad.edu
- cms.singhgad.edu
- app.singhgad.edu
- cpanel.app.singhgad.edu
- mail.app.singhgad.edu
- cloud.singhgad.edu
- simca.singhgad.edu
- sscosr.singhgad.edu
- sdpds.singhgad.edu

## 3. Publicly Accessible Documents (Google Dorking)

### Google Dork Used
site:singhgad.edu filetype:pdf "alumni"


### Findings
- Alumni association reports
- Policy documents
- Institutional reports
- Event and academic documents


## 4. Interesting URLs Identified

- https://www.singhgad.edu/
- https://admissions.singhgad.edu/
- https://essportal.singhgad.edu/
- https://essportal.singhgad.edu/SaralESS
- https://registrations.springfestival.singhgad.edu/tt-07-ws-036
- https://sbcs.singhgad.edu/
- https://sscosr.singhgad.edu/
- https://sdch.singhgad.edu/
- https://simca.singhgad.edu/
- https://sdpds.singhgad.edu/

These portals may host authentication systems and sensitive student or staff data.

## 5. IP Address Enumeration

### IPs Found
- 115.113.155.115
- 123.63.148.72
- 166.62.30.157
- 169.148.148.76
- 185.20.209.52

Multiple IP addresses suggest distributed hosting infrastructure.

## 6. Email Address Discovery

### Emails Identified
- directormca_siom@singhgad.edu
- principal.scoe@singhgad.edu
- principal.scop@singhgad.edu