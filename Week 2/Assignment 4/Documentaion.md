## Objective
The objective of this activity was to use search engine queries to identify whether any publicly accessible 
sensitive resources (files, directories, login pages) are exposed on the internet.
### Query Used
#### a) Public Files Identification Query
`Cybersecurity filetype:pdf`

Description:
This query was used to search for publicly available PDF documents related to the keyword “cybersecurity.” 
This technique can identify sensitive documentssuch as reports, whitepapers, internal documents, or training materials that
may have been accidentally made public.

#### b) Exposed Directories Identification Query
`intitle:"index of" cybersecurity`

Description:
This query is used to locate directories where directory listing is enabled."Index of" means that the server is publicly 
exposing its folder structure, allowing multiple files to be accessed without authentication.

#### c) Login Pages Identification Query
`inurl:login`

Description:
This query is used to identify login pages for websites. Login pages are attractive to attackers because they are the entry
point for authentication mechanisms.

### 2. Type of Information That Could Be Exposed

#### a) Information Exposed from Public Files (PDFs)
The following sensitive information can be exposed through public PDF files:

- Internal cybersecurity reports
- Company policies & procedures
- Employee names and roles
- Security architecture details

#### b) Exposed Directories se Exposed Information
This data can be publicly accessible when Directory listing is enabled:

- Backup files (.zip, .bak, .old)
- configuration files
- log files
- Uploaded documents
- Source code files

Exposed directories indicate serious security misconfiguration.

#### c) Login Pages se Security Risks
The following risks are incurred through publicly discoverable login pages:

- Brute-force attacks
- Credential stuffing attacks
- Username enumeration
- Exploitation of weak password policies

If there are no controls like CAPTCHA, rate limiting, or account lockout on the login page, then there is a risk of 
system compromise.


### observation

- Sensitive resources can be easily discovered through search engine queries.
- Public files and open directories show weak security posture of the organization.
- Login pages provide a direct attack surface for attackers.

### Conclusion
Public files, exposed directories, and openly accessible login pages are high-risk security issues for an organization. 
To mitigate these risks, it is important to remove sensitive files from public indexing, disable directory listing, and 
implement strong security mechanisms on login pages.
