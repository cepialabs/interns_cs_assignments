# Linux Commands

## 1. ip a
Displays network interfaces and IP addresses.
Used to identify system network configuration.
![ip a output](images/ip-a.png)

## 2. ip route
Shows the routing table.
Used to understand how packets leave the system.
![ip route output](images/ip-route.png)

## 3. ss -tulnp
Lists all listening ports and services.
Used to identify open ports and running services.
![ss output](images/ss-tulnp.png)

## 4. netstat -tulnp
Shows active connections and listening services.
Helpful for detecting unauthorized services.
![netstat output](images/netstat-tulnp.png)

## 5. ps aux
Displays all running processes.
Used to identify suspicious or malicious processes.
![ps output](images/ps-aux.png)

## 6. top
Shows real-time system resource usage.
Used to monitor abnormal CPU or memory usage.
![top output](images/top.png)

## 7. whoami
Displays the current user.
Used to verify privilege level.
![whoami output](images/whoami.png)

## 8. id
Shows user ID and group memberships.
Used to check permission and access levels.
![id output](images/id.png)

## 9. sudo -l
Lists commands the user can run with sudo.
Used during privilege escalation checks.
![sudo output](images/sudo.png)

## 10. chmod
Changes file permissions.
Used to secure or exploit file access.
![chmod output](images/chmod.png)

## 11. chown
Changes file ownership.
Used to control access to sensitive files.
![chown output](images/chown.png)

## 12. find / -perm -4000 2>/dev/null
Finds SUID binaries on the system.
Used for privilege escalation analysis.
![suid output](images/find.png)

## 13. grep
Searches for specific patterns in files.
Used to find credentials or logs.
![grep output](images/grep.png)

## 14. journalctl
Displays system logs.
Used for incident response and log analysis.
![journalctl output](images/journalctl.png)

## 15. tcpdump
Captures network packets.
Used for traffic analysis and investigation.
![tcpdump output](images/tcpdump.png)