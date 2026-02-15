## Target: DVWA
The DVWA (Damn Vulnerable Web Application) is a web application that is intentionally insecure and is used for educational 
purposes, specifically for penetration testing and ethical hacking. In this project, different common web vulnerabilities were 
tested at different security levels (Low, Medium, and High) by utilizing the DVWA web application. The objective was to focus on 
different vulnerabilities at different attack vectors according to the OWASP guidelines, and also to understand the vulnerabilities
and how they can be exploited along with mitigation techniques.

![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%203/Assignment%203/Images/DVWA.png?raw=true)
### Tool: Nikto (Web Server Scanner)
Nikto is an open-source web server vulnerability scanner that uses the command-line interface and is designed to quickly identify 
security concerns, misconfigurations, and outdated software. Nikto is developed using the Perl language and checks against over 6,700 
malicious files/CGIs and 1,200 outdated server versions, making it an essential and fast vulnerability scanner.
#### Scan Command
```
nikto -h http://localhost:8080
```
![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%203/Assignment%203/Images/NIKTO.png?raw=true)

### Dangerous Headers
![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%203/Assignment%203/Images/Dangerous%20Header.png?raw=true)
#### Missing X-Frame-Options
- The X-Frame-Options header is missing in the application.
- Risk: Clickjacking attacks may occur.
- An attacker can embed your site in malicious iframes.
- Recommendation: Enable X-Frame-Options: DENY or SAMEORIGIN.
 #### Missing X-Content-Type-Options
- Header is not set.
- Risk: Browser may perform MIME sniffing.
- This can lead to content-type confusion attacks.
- Recommendation: Add X-Content-Type-Options: nosniff.

### Outdated Components
![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%203/Assignment%203/Images/outdated%20comp.png?raw=true)

#### Outdated Web Server Version
``` Sercer: Apache/2.4.25 (Debian) ```
- An old version of Apache was detected.
- Older versions may have known CVEs.
- An attacker can search for exploits based on the version.
##### Recommendation
- Upgrade to the latest stable version of Apache.
- Disable ServerTokens and ServerSignature.

### Potential Misconfiguration
![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%203/Assignment%203/Images/mis.png?raw=true)

##### Directory Indexing Enabled
- It is listing the files inside the server folder.
- The attacker can see sensitive files (backup, config, logs).
- The risk of information disclosure increases.

#### Exposed phpinfo.php
- The phpinfo page shows server configuration details.
- PHP version, modules, and file paths are revealed.
- An attacker can use this in the reconnaissance phase.

#### Risk
- Targeted exploit planning becomes easier.

### Interpret Output Instead of Blindly Trusting It

#### Automated tools can give false positives
Nikto flags every finding as a potential vulnerability, but not every result is a real exploit.
#### Manual validation is necessary
Every finding should be verified using a browser, curl, or additional testing.
#### Outdated version ≠ automatically vulnerable
Having an old software version doesn't mean an exploit is confirmed; it's important to check CVEs and exploit availability.
####  Context and environment matter
Missing headers might be normal in a lab environment, but in production, they can pose a serious risk.
#### Evaluate risk based on business impact
Severity is not determined solely by the tool's output, but by exploitability and impact.
