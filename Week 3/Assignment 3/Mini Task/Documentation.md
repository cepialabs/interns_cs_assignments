## NIKTO Against DVWA

![image](https://github.com/cepialabs/interns_cs_assignments/blob/INT2026-5324/Week%203/Assignment%203/Images/NIKTO.png?raw=true)
### Misconfiguration 1: Directory Indexing Enabled
- Server directory listing is being allowed. 
- This allows the attacker to see the internal file structure. 
- Sensitive files (backup, config, logs) may be exposed. 

#### Risk: Information disclosure. 
#### Recommendation: Disable Directory listing (Options -Indexes). 

## Misconfiguration 2: Exposed phpinfo.php 
- phpinfo page found publicly accessible. 
- Server configuration details, PHP version, modules are being revealed. 
- This can be used in attacker phase reconnaissance. 

#### Risk: Information leakage, targeted attacks. 
#### Recommendation: remove or restrict phpinfo file. 

## Potentially Vulnerable Component: Outdated Apache/PHP Version 

Example: 
```
Server: Apache/2.4.7 
X-Powered-By: PHP/5.6 
```

- Software version outdated detected. 
- Older versions may contain known CVEs. 
- CVE verification is required to confirm exploitation. 

#### Risk: Remote Code Execution or privilege escalation possible (depending on CVE). 
#### Recommendation: Upgrade to latest supported version.
