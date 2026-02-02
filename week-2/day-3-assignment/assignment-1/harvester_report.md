Target Domain
adobe.com

Tool Used

theHarvester

Purpose: OSINT (Open Source Intelligence) and public asset discovery

Command Executed
theHarvester -d adobe.com -b crtsh,duckduckgo,bing -l 500 -f adobe_osint

Command Description

-d adobe.com → Target domain

-b crtsh,duckduckgo,bing → Public data sources used

-l 500 → Limit of search results

-f adobe_osint → Output saved in XML and JSON format

Output Files Generated
adobe_osint.json
adobe_osint.xml

Discovered Subdomains / Hosts

blog.adobe.com

blogs.adobe.com

community.adobe.com

genuine.adobe.com

helpx.adobe.com

mail.adobe.com

max.adobe.com

news.adobe.com

reg.adobe.com

www.adobe.com

Discovered Email Addresses
mail@mail.adobe.com

Discovered IP Addresses (Sample)

104.71.60.72

151.101.3.10

18.66.78.117

107.23.154.8

192.243.228.1

Observations

theHarvester successfully identified multiple public-facing subdomains related to the target domain.

Certificate Transparency logs (crt.sh) revealed additional assets through SSL certificates.

Search engines such as Bing and DuckDuckGo provided indexed public information.

Some data sources returned rate-limit or connection reset errors, which is common during OSINT enumeration.

Very limited email addresses were found because large organizations usually protect email exposure.

Results were saved in structured XML and JSON formats for further analysis.