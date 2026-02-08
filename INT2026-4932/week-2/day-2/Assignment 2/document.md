Target Machine: Metasploitable2
Scanner: Kali Linux
Tool Used: Nmap

 1. Open Ports Identified
The following ports were found open during the Nmap scan:
21/tcp   – FTP
22/tcp   – SSH
23/tcp   – Telnet
25/tcp   – SMTP
53/tcp   – DNS
80/tcp   – HTTP
111/tcp  – RPCBind
139/tcp  – NetBIOS-SSN
445/tcp  – Microsoft-DS (SMB)
512/tcp  – exec (rexecd)
513/tcp  – login (rlogin)
514/tcp  – tcpwrapped
1099/tcp – Java RMI Registry
1524/tcp – Bindshell (Metasploitable root shell)
2049/tcp – NFS (rpcbind)
2121/tcp – FTP (ProFTPD)
3306/tcp – MySQL
5432/tcp – PostgreSQL
5900/tcp – VNC
6000/tcp – X11
6667/tcp – IRC
8009/tcp – AJP13
8180/tcp – HTTP (Unknown service)

2. How Many Ports Are Open?
Total open TCP ports detected: 23

3. Which Services Look Risky?
FTP (vsftpd 2.3.4)
Telnet
rlogin / rexec
SMB (139, 445)
Java RMI
Bindshell (1524)
ProFTPD
MySQL
PostgreSQL
VNC
IRC (UnrealIRCd)

 4. Possible Vulnerable Services
vsftpd 2.3.4 – Known backdoor vulnerability
Telnet – Sends credentials in plain text
SMB – Prone to enumeration and exploits
Java RMI – Remote code execution risk
Bindshell – Direct root access
ProFTPD – Old FTP service
MySQL 5.0.51a – Weak authentication possible
PostgreSQL – Unsecured database access
VNC – Weak/no authentication
UnrealIRCd – Known malicious backdoor