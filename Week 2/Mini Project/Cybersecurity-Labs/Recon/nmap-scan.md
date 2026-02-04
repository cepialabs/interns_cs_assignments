# Nmap Scan Results

## Objective
The objective of this scan was to identify open ports and exposed services on the target system to understand the network-level attack surface.

## Target Information
- **IP Address:** 137.74.187.104
- **Domain Name:** hackthissite.org
- **Target Type:** Public-facing Web Application (Intentionally Vulnerable)

## Tool Used
- Nmap

## Scan Commands Used

### 1. Basic Port Scan
```
nmap 137.74.187.104

```
#### Observation

- The host is reachable and responding to scan requests.
- Commonly used ports were found open.

### 2. Service Detection Attempt
```
nmap -sV -p 22,80,443 137.74.187.104

```
#### Observation


### Default Safe Scripts
```
nmap -sC -p 22,80,443 137.74.187.104

```



### Scan Resul
| Port | State | Service | Version               |
| ---- | ----- | ------- | --------------------- |
| 22   | Open  | SSH     | Version not disclosed |
| 80   | Open  | HTTP    | Version not disclosed |
| 443  | Open  | HTTPS   | Version not disclosed |

### Observations

- The target system exposes SSH, HTTP, and HTTPS services to the public network.
- Service version information is not disclosed, likely due to security hardening or filtering mechanisms.
- Version hiding reduces information leakage but does not eliminate application-level vulnerabilities.

### Security Impact

- Even without version disclosure, exposed services increase the attack surface.
- Attackers may attempt banner grabbing or application-level fingerprinting techniques.
- Hidden versions may slow down attackers but do not prevent exploitation.

### Risk Level

Medium

The risk is assessed as medium due to multiple exposed services, despite limited information disclosure.

### Recommendation

- Continue using version and banner obfuscation techniques.
- Implement additional monitoring and logging.
- Perform application-layer security testing to identify vulnerabilities beyond service versions.
