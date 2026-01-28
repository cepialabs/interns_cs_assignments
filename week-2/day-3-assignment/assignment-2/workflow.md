# Pentester Workflow Simulation
## Target: Metasploitable2 (Local Vulnerable Machine)

---

## Step 1: Observe

The target machine was deployed in a local lab environment using VMware.
Both Kali Linux (attacker) and Metasploitable2 (target) were configured on the same network.

To confirm reachability, a basic Nmap scan was performed.

### Command used:
```bash
nmap 192.168.57.159

Observation:

The host was online and responding to requests, indicating it was reachable and ready for testing.

Step 2: Identify Risk Areas

The Nmap scan revealed multiple open ports and services, indicating a large attack surface.

Open services identified:

FTP (21)

SSH (22)

Telnet (23)

SMTP (25)

HTTP (80)

SMB (445)

MySQL (3306)

PostgreSQL (5432)

VNC (5900)

And several other legacy services

The presence of many exposed and legacy services suggested that the system was intentionally vulnerable.
FTP (port 21) was selected as the initial risk area due to its common misconfigurations
and history of weak authentication issues.

Step 3: Analyze Traffic / Service Behavior

The FTP service was manually tested to verify authentication and access control.

FTP connection command:
ftp 192.168.57.159

Credentials used:
Username: msfadmin
Password: msfadmin

Result:

Login was successful

FTP service allowed directory listing

Sensitive files were visible

Commands executed inside FTP:
ls
ls -la

Findings:

User home directory was accessible

Sensitive files such as .bash_history, .mysql_history,
.ssh, and .sudo_as_admin_successful were visible

This indicated weak access controls and insecure service configuration

The FTP service exposed sensitive information that could assist in further attacks
such as credential reuse or privilege escalation.

Step 4: Document Finding
Vulnerability Identified:

Insecure FTP service with valid credentials

Exposure of sensitive system files

Impact:

An attacker can gain unauthorized access to the system,
read sensitive files, and potentially escalate privileges.
This could lead to full system compromise.

Severity:

High

Recommendation:

Disable FTP if not required

Use secure alternatives like SFTP

Enforce strong authentication

Restrict access to sensitive files

Apply proper service hardening