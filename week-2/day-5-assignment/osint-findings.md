# OSINT Reconnaissance Report – Alibaba.com

## Objective
To collect and analyze publicly available intelligence related to the domain
alibaba.com using OSINT techniques such as WHOIS, DNS analysis, and Shodan data,
without performing any active exploitation.

---

## Domain Overview
- Domain Name: alibaba.com
- Registrar: Alibaba Cloud Computing (Beijing) Co., Ltd.
- Registrar IANA ID: 420
- Whois Server: grs-whois.hichina.com
- Domain Age: ~26 years (Created on 1999-04-15)
- Expiry Date: 2030-05-23

---

## Domain Status & Security Controls
- clientTransferProhibited
- serverDeleteProhibited
- serverTransferProhibited
- serverUpdateProhibited

These protections indicate strong domain-level security and protection against
unauthorized ownership changes.

---

## DNS & Nameserver Information
- NS1.ALIBABADNS.COM
- NS2.ALIBABADNS.COM

Observations:
- Custom Alibaba DNS infrastructure is used
- DNSSEC is currently unsigned
- Long-term stable DNS setup with minimal nameserver changes

---

## IP & Hosting Information
- Current IP Address: 184.28.10.189
- Hosting Provider: Akamai Technologies Inc.
- ASN: AS16625 (AKAMAI-AS)
- IP Location: United States – Seattle
- IP History: 578 IP changes over 21 years

Observation:
- Heavy use of CDN (Akamai) effectively hides origin servers
- Frequent IP rotation reduces direct infrastructure exposure

---

## Shodan Intelligence Summary
- Total Shodan Results: 149

### Geographic Distribution
- China: 121
- Singapore: 11
- United States: 6
- Germany: 3
- Hong Kong: 2

### Organizations Observed
- Aliyun Computing Co., LTD
- Alibaba Cloud LLC
- Huawei Public Cloud Services
- Tencent Cloud Computing

---

## Open Ports Observed (Public Exposure)
- 443/tcp (HTTPS)
- 80/tcp (HTTP)
- 3000/tcp
- 3001/tcp
- 3002/tcp

Observation:
- Majority of services are exposed via standard web ports
- Higher ports may be used for internal dashboards or application services

---

## Web Servers & Technologies
- Nginx
- Tengine
- OpenResty
- Microsoft IIS (limited instances)

### Web Security Headers & Tech
- HSTS enabled
- Alibaba Cloud CDN
- jQuery detected on some services

---

## SSL / TLS & Fingerprinting
- TLS Versions Supported:
  - TLSv1.2
  - TLSv1.3
- Multiple JARM and JA3S fingerprints observed
- SSL termination handled via CDN infrastructure

---

## HTTP Insights
Common page titles observed:
- Welcome to Tengine!
- HTTP Server Test Page
- Alibaba Cloud IDaaS Error Page
- Qwen Chat

Observation:
- Presence of default/test pages may indicate staging or misconfigured services
  if publicly accessible.

---

## Vulnerability Information
- No known vulnerabilities reported via Shodan
- No CVEs directly associated with exposed services

---

## Security Assessment Summary
- Strong use of CDN and cloud infrastructure
- Minimal direct IP exposure
- Mature DNS and registrar-level protections
- Large distributed attack surface due to global infrastructure
- Potential risk exists if test or default pages are unintentionally exposed

---

## Limitations
- Findings are based only on publicly available OSINT data
- No active scanning or exploitation was performed
- Results may vary over time due to dynamic infrastructure
