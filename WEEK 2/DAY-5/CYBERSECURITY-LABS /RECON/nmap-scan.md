# Nmap Scan Report

## Command Used
```bash
nmap -A -T4 testphp.vulnweb.com
Host Information
IP Address: 44.228.249.3

Reverse DNS: ec2-44-228-249-3.us-west-2.compute.amazonaws.com

Latency: 0.021s

Network Distance: 2 hops

Open Ports & Services
Port	State	Service	Version
80	Open	HTTP	nginx 1.19.0
Service Detection
Web server running nginx 1.19.0

Website title: Home of Acunetix Art

OS Detection
Operating System: Linux Kernel 4.x / 5.x (Estimated)

Observations
Only HTTP service exposed

No unnecessary ports open

Server is hosted on AWS cloud

Security Implication
Web service is the main attack vector

Vulnerabilities likely exist in web application layer
