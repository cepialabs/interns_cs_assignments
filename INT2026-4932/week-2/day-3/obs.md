# Subdomain Using theHarvester

# Objective
The objective of this experiment is to perform passive reconnaissance to discover subdomains associated with a target domain using theHarvester tool.

## Tool Used
theHarvester (OSINT-based reconnaissance tool)

## Target Domain
battlegroundsmobileindia.com

# Command
theHarvester -d battlegroundsmobileindia.com -b all

# Results
TheHarvester successfully discovered multiple subdomains associated with the target domain.

Total Hosts Found: 58

## Discovered Subdomains
- esports.battlegroundsmobileindia.com
- apkdownload.battlegroundsmobileindia.com
- help.battlegroundsmobileindia.com
- iosdownload.battlegroundsmobileindia.com
- h5.battlegroundsmobileindia.com
- apm-bom.battlegroundsmobileindia.com
- apm-del.battlegroundsmobileindia.com
- apm-hyd.battlegroundsmobileindia.com

# Emails Found
- No email addresses were found during the scan.

## Observations
- theHarvester successfully identified 58 subdomains using passive OSINT techniques.
- No active scanning or direct interaction with the target server was performed.
- Some subdomains resolved to localhost (127.0.0.1), which may indicate internal or restricted configurations.
- Multiple IP addresses for a single subdomain suggest CDN usage and distributed infrastructure.
- No email addresses were publicly indexed for the target domain.
- Warnings related to missing API keys were observed when using multiple data sources, which is expected behavior.
