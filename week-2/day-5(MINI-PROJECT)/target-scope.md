# Target Scope 

## Target Domain
- **Primary Domain:** dmce.ac.in
- **Organization:** Datta Meghe College of Engineering
- **Domain Type:** Educational Institution 

## Objective
To perform **passive and limited active reconnaissance** on the target domain to identify publicly exposed assets, services, and information

## Scope of Assessment

### In-Scope Assets
- `dmce.ac.in`
- Publicly accessible subdomains of `dmce.ac.in`
- Public DNS records (A, MX, TXT, NS)
- Public IP addresses associated with the domain
- Web services hosted on standard ports
- Publicly available documents, emails, and metadata

### Out-of-Scope Assets
- Internal systems and intranet services
- Authenticated portals (student, staff, admin panels)
- Any form of exploitation or vulnerability exploitation
- Denial-of-service, brute-force, or intrusive testing
- Third-party services not owned or controlled by the institution

## Allowed Activities
- Passive OSINT techniques (Google dorks, certificate transparency logs)
- Subdomain enumeration using passive tools
- Service and port discovery using **limited Nmap scanning**
- Collection of publicly available information only

## Disallowed Activities
- Exploitation of vulnerabilities
- Password attacks or authentication bypass attempts
- Uploading payloads or executing malicious code
- Any action that may disrupt services or data integrity

No sensitive data is intentionally accessed, stored, or misused.  
All findings are derived from **publicly accessible sources only**.

## Tools Intended for Use
- Nmap (limited port and service detection)
- crt.sh
- theHarvester
- Amass (passive mode)
- Google Dorking

