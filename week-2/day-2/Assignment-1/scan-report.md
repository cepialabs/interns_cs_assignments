# Vulnerability Scanning Report – Metasploitable

## Objective
- To perform a network scan on a local vulnerable machine (Metasploitable)
- To identify open ports, running services, and potential vulnerable services
- To understand real-world reconnaissance techniques used during penetration testing

---

## Target Details
- Target Machine: Metasploitable
- Target IP Address: 192.168.0.123
- Attacking Machine: Kali Linux
- Network Type: Local virtual network (VirtualBox)

---

## Scan Methodology
- Tool Used: Nmap
- Scan Command Executed:
  - `nmap -sS -sV -O 192.168.0.123`
- Scan Type:
  - TCP SYN (Stealth) scan
  - Service version detection
  - Operating system detection

![metasploit-scan](nmap-scan.png)

---

## Scan Summary
- Host status: Up and reachable
- Network latency: Approximately 0.002 seconds
- Closed ports: 977 TCP ports
- Multiple services exposed with outdated versions
- Operating system detected: Linux Kernel 2.6.x

---

## Identified Open Ports and Services
- Port 21 (FTP): vsftpd 2.3.4
- Port 22 (SSH): OpenSSH 4.7p1
- Port 23 (Telnet): Linux telnetd
- Port 25 (SMTP): Postfix smtpd
- Port 53 (DNS): ISC BIND 9.4.2
- Port 80 (HTTP): Apache httpd 2.2.8
- Port 111 (RPC): rpcbind service
- Port 139 (SMB): Samba smbd 3.x–4.x
- Port 445 (SMB): Samba smbd 3.x–4.x
- Port 512 (exec): Remote command execution service
- Port 513 (login): rlogin service
- Port 514 (shell): rsh service
- Port 1099 (Java RMI): GNU Classpath grmiregistry
- Port 1524 (bindshell): Metasploitable root shell
- Port 2049 (NFS): Network File System
- Port 2121 (FTP): ProFTPD 1.3.1
- Port 3306 (MySQL): MySQL 5.0.51a
- Port 5432 (PostgreSQL): PostgreSQL 8.3.x
- Port 5900 (VNC): VNC protocol 3.3
- Port 6000 (X11): X Window System
- Port 6667 (IRC): UnrealIRCd
- Port 8009 (AJP): Apache JServ Protocol
- Port 8180 (HTTP): Apache Tomcat

---

## Potentially Vulnerable Services
- vsftpd 2.3.4:
  - Known backdoor vulnerability
  - Can allow unauthorized shell access
- Telnet service:
  - Sends credentials in plaintext
  - Vulnerable to sniffing and brute-force attacks
- Samba services:
  - Outdated versions vulnerable to remote code execution
- Bind shell on port 1524:
  - Direct root-level access exposed
- MySQL service:
  - Outdated version
  - Often misconfigured with weak credentials
- Java RMI service:
  - Susceptible to remote code execution attacks
- UnrealIRCd:
  - Known backdoored version
  - Allows arbitrary command execution
- Apache Tomcat:
  - May expose default credentials and management interfaces

---

## Operating System Information
- Detected OS: Linux
- Kernel version range: 2.6.9 – 2.6.33
- Device type: General purpose system
- MAC Address: 08:00:27:5E:38:61 (VirtualBox virtual NIC)

---

- The target system exposes numerous unnecessary and outdated services
- Several high-risk vulnerabilities were identified during reconnaissance
- This scan demonstrates how attackers can gather critical information during the initial phase of an attack
- Proper hardening, patch management, and service minimization are essential to secure systems
