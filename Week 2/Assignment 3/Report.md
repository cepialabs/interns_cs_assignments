## Observation Report – Email & Domain Enumeration
#### Tool Used: theHarvester
#### Target Domain: instagram.com
#### Reconnaissance Type: OSINT (Passive Information Gathering) 
#### Objective:
The objective of this activity was to perform email and domain reconnaissance on the target domain using theHarvester in order to identify publicly available information that could be useful during the reconnaissance phase of a security assessment.

#### Tool Description: theHarvester
heHarvester is an open-source OSINT tool used to gather:
- Email addresses
- Subdomains
- Hosts
from publicly available sources such as search engines and social platforms.

No active attack is performed using this tool.

#### Command:
theHarvester -d (target url) -l (list) -b (search engine) 

#### Observation :
- Publicly available information related to the target domain was successfully retrieved.
- Multiple email patterns associated with the organization were identified.
- Subdomains discovered may reveal additional attack surface.
- Information gathered can be misused for phishing, spoofing, or social engineering if not protected properly.
  
