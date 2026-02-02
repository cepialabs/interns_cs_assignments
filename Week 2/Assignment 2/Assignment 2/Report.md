# Metasploit Documentation

## How Many Ports Are Open?
| Port     | State | Service    | Version                      |
| -------- | ----- | ---------- | ---------------------------- |
| 21/tcp   | Open  | FTP        | vsftpd 2.3.4                 |
| 22/tcp   | Open  | SSH        | OpenSSH 4.7p1 (protocol 2.0) |
| 23/tcp   | Open  | Telnet     | Linux telnetd                |
| 25/tcp   | Open  | SMTP       | Postfix smtpd                |
| 53/tcp   | Open  | DNS        | ISC BIND 9.4.2               |
| 80/tcp   | Open  | HTTP       | Apache httpd 2.2.8 (Ubuntu)  |
| 111/tcp  | Open  | RPCBind    | RPC #100000                  |
| 139/tcp  | Open  | NetBIOS    | Samba smbd 3.X–4.X           |
| 445/tcp  | Open  | NetBIOS    | Samba smbd 3.X–4.X           |
| 512/tcp  | Open  | RSH        | netkit-rsh rexecd            |
| 513/tcp  | Open  | Rlogin     | rlogind                      |
| 514/tcp  | Open  | TCPWrapped | —                            |
| 1099/tcp | Open  | Java RMI   | GNU Classpath grmiregistry   |
| 1524/tcp | Open  | Bind Shell | Metasploitable root shell    |
| 2049/tcp | Open  | NFS        | v2–v4                        |
| 2121/tcp | Open  | FTP        | ProFTPD 1.3.1                |
| 3306/tcp | Open  | MySQL      | MySQL 5.0.51a                |
| 5432/tcp | Open  | PostgreSQL | 8.3.x                        |
| 5900/tcp | Open  | VNC        | Protocol 3.3                 |
| 6000/tcp | Open  | X11        | Access Denied                |
| 6667/tcp | Open  | IRC        | UnrealIRCd                   |
| 8009/tcp | Open  | AJP13      | Apache JServ v1.3            |
| 8180/tcp | Open  | HTTP       | Apache Tomcat/Coyote 1.1     |

## Which Services Look Risky?

- FTP : Backdoor vulnerabilities in File Transfer Protocol (FTP) servers are a severe security risk with high criticality, where malicious code is embedded directly into the server software to enable unauthorized remote attackers to gain full control (root access) of the system. 
The most famous and historically important example of a backdoor vulnerability is the vsFTPd 2.3.4 backdoor (CVE-2011-2523), which remains a classic case study in cybersecurity.
- Telnet : The main security concern with Telnet is that it sends all the data from the session in plaintext form without encryption. This means that anyone with access to the network can easily intercept the data and steal the credentials. It is considered insecure and obsolete and is very susceptible to sniffing and lateral movement attacks.
- SMB : Remote Code Execution (RCE) attacks in Server Message Block (SMB) protocols enable attackers to execute malicious code on a target system from a remote location, which often results in full system compromise, ransomware attacks (such as WannaCry), and lateral movement attacks. Such vulnerabilities, such as CVE-2020-0796 (SMBGhost) or CVE-2017-0144 (EternalBlue), do not require authentication to be exploited.
- RMI : The unauthenticated access to the Java Remote Method Invocation (RMI) interface is a severe security concern, which may lead to the Remote Code Execution (RCE), execution of arbitrary OS commands with high privileges, and unauthorized modification of data. The exposed RMI/JMX interface is commonly exploited via the deserialization of untrusted data.
- NFS : Unauthenticated access to files in Network File Systems (NFS) can result in serious threats such as data theft, unauthorized modification, and privilege escalation. An attacker can take advantage of an improperly exported directory (e.g., no_root_squash) to read/write sensitive files or gain root access to the server.

## What Version Are Outdated?
| Service | Version | Status      |latest version     |
| ------- | ------- | ----------- | ------------      |
| vsftpd  | 2.3.4   | Backdoored  | 3.0.5+            | 
| Apache  | 2.2.8   | End-of-Life | 2.4.66            |
| OpenSSH | 4.7p1   | Outdated    | 9.x (Latest Stable)|
| MySQL   | 5.0.51a | Deprecated  | 8.0.x              |
| Samba   | 3.0.20  | Exploitable | 4.19+              |
| PHP     | 5.2.x   | Unsupported | 8.2 / 8.3          |
