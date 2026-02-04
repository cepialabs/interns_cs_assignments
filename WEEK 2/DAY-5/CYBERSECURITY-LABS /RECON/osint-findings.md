
---

# 📄 osint-findings.md  (From YOUR Google Dorking)

```md
# OSINT Findings Report

## Techniques Used
- Google Dorking
- Search Engine Reconnaissance

## Google Dork Queries Used

site:testphp.vulnweb.com filetype:pdf "confidential"  
site:testphp.vulnweb.com inurl:admin login  

## Discovered Information

### Public Documents
- Public vulnerability scan report PDF indexed by Google

### Exposed Directories
- /admin/ directory listing enabled

### Sensitive Files Found
- create.sql database script publicly accessible

## Example Findings
- Index of /admin/
- create.sql database structure file exposed

## Security Impact
- Directory indexing exposes sensitive internal files
- Database scripts can reveal table structure
- Public vulnerability reports reveal system weaknesses

## Risk Level
**High – Sensitive internal information publicly accessible**
