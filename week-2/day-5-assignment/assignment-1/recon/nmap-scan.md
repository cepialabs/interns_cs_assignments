Starting Nmap 7.97 ( https://nmap.org ) at 2026-02-03 10:57 +0530
NSE: Loaded 158 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 10:57
Completed NSE at 10:57, 0.02s elapsed
Initiating NSE at 10:57
Completed NSE at 10:57, 0.00s elapsed
Initiating NSE at 10:57
Completed NSE at 10:57, 0.00s elapsed
Initiating Parallel DNS resolution of 1 host. at 10:57
Completed Parallel DNS resolution of 1 host. at 10:57, 0.18s elapsed
Initiating Ping Scan at 10:57
Scanning www.alibaba.com (23.218.230.46) [4 ports]
Completed Ping Scan at 10:57, 0.14s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 10:57
Completed Parallel DNS resolution of 1 host. at 10:57, 0.05s elapsed
Initiating SYN Stealth Scan at 10:57
Scanning www.alibaba.com (23.218.230.46) [1000 ports]
Discovered open port 443/tcp on 23.218.230.46
Discovered open port 80/tcp on 23.218.230.46
Completed SYN Stealth Scan at 10:58, 27.66s elapsed (1000 total ports)
Initiating Service scan at 10:58
Scanning 2 services on www.alibaba.com (23.218.230.46)
Completed Service scan at 10:58, 12.47s elapsed (2 services on 1 host)
Initiating OS detection (try #1) against www.alibaba.com (23.218.230.46)
Retrying OS detection (try #2) against www.alibaba.com (23.218.230.46)
Initiating Traceroute at 10:58
Completed Traceroute at 10:58, 3.09s elapsed
Initiating Parallel DNS resolution of 7 hosts. at 10:58
Completed Parallel DNS resolution of 7 hosts. at 10:58, 0.08s elapsed
NSE: Script scanning 23.218.230.46.
Initiating NSE at 10:58
Completed NSE at 10:58, 5.45s elapsed
Initiating NSE at 10:58
NSOCK ERROR [64.8110s] poll_loop(): nsock_loop error 10022: An invalid argument was supplied. 
NSE: Script Engine Scan Aborted.
An error was thrown by the engine: F:\New folder/nse_main.lua:1078: a fatal error occurred in nsock_loop
stack traceback:
	[C]: in function 'nmap.socket.loop'
	F:\New folder/nse_main.lua:1078: in upvalue 'run'
	F:\New folder/nse_main.lua:1488: in function <F:\New folder/nse_main.lua:1435>
	[C]: in ?
Nmap scan report for www.alibaba.com (23.218.230.46)
Host is up (0.036s latency).
rDNS record for 23.218.230.46: a23-218-230-46.deploy.static.akamaitechnologies.com
Not shown: 998 filtered tcp ports (no-response)
PORT    STATE SERVICE  VERSION
80/tcp  open  http     AkamaiGHost (Akamai's HTTP Acceleration/Mirror service)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-title: Did not follow redirect to https://www.alibaba.com/?from_http=1
443/tcp open  ssl/http AkamaiGHost (Akamai's HTTP Acceleration/Mirror service)
| tls-alpn: 
|   http/1.1
|_  http/1.0
| tls-nextprotoneg: 
|   http/1.1
|_  http/1.0
| ssl-cert: Subject: commonName=air.alibaba.com/organizationName=Alibaba Cloud Computing Ltd./stateOrProvinceName=\xE6\xB5\x99\xE6\xB1\x9F\xE7\x9C\x81/countryName=CN
| Subject Alternative Name: DNS:air.alibaba.com, DNS:activity.alibaba.com, DNS:air.alibaba.co.uk, DNS:alibaba.com, DNS:amdc-detect-de-ak.alibaba.com, DNS:amdc-detect-sg-ak.alibaba.com, DNS:amdc-detect-us-ak.alibaba.com, DNS:app.alibaba.com, DNS:arabic.alibaba.com, DNS:biz.alibaba.com, DNS:buyer.alimebot.alibaba.com, DNS:buyeragent.alibaba.com, DNS:carp.alibaba.com, DNS:cashier.alibaba.com, DNS:data.alibaba.com, DNS:dsp.alibaba.com, DNS:dutch.alibaba.com, DNS:error.alibaba.com, DNS:french.alibaba.com, DNS:german.alibaba.com, DNS:hebrew.alibaba.com, DNS:hindi.alibaba.com, DNS:hz-productposting.alibaba.com, DNS:i.alibaba.com, DNS:i.alibabausercontent.com, DNS:img.alibaba.com, DNS:indonesian.alibaba.com, DNS:insights.alibaba.com, DNS:italian.alibaba.com, DNS:japanese.alibaba.com, DNS:korean.alibaba.com, DNS:lang.alicdn.com, DNS:login.alibaba.com, DNS:logistics.alibaba.com, DNS:m-sale.alibaba.com, DNS:m.alibaba.com, DNS:m.arabic.alibaba.com, DNS:m.chinese.alibaba.com, DNS:m.dutch.alibaba.com, DNS:m.french.alibaba.com, DNS:m.german.alibaba.com, DNS:m.hebrew.alibaba.com, DNS:m.hindi.alibaba.com, DNS:m.indonesian.alibaba.com, DNS:m.italian.alibaba.com, DNS:m.japanese.alibaba.com, DNS:m.korean.alibaba.com, DNS:m.portuguese.alibaba.com, DNS:m.ppc.alibaba.com, DNS:m.russian.alibaba.com, DNS:m.spanish.alibaba.com, DNS:m.thai.alibaba.com, DNS:m.turkish.alibaba.com, DNS:m.vietnamese.alibaba.com, DNS:message.alibaba.com, DNS:myconnections.alibaba.com, DNS:ocean-gw.alibaba.com, DNS:offer.alibaba.com, DNS:onetalk.alibaba.com, DNS:portuguese.alibaba.com, DNS:post.alibaba.com, DNS:productcenter.alibaba.com, DNS:reads.alibaba.com, DNS:rfq.alibaba.com, DNS:russian.alibaba.com, DNS:s.alicdn.com, DNS:sale.alibaba.com, DNS:select-pages.alibaba.com, DNS:select.alibaba.com, DNS:seller.alibaba.com, DNS:sg-akamai.alibaba.com, DNS:simple.m.alibaba.com, DNS:siteadmin.alibaba.com, DNS:sourcing.alibaba.com, DNS:spanish.alibaba.com, DNS:support.alibaba.com, DNS:template.alibaba.com, DNS:thai.alibaba.com, DNS:tradeassurance.alibaba.com, DNS:turkey.alibaba.com, DNS:turkish.alibaba.com, DNS:turkiye.alibaba.com, DNS:us-akamai.alibaba.com, DNS:us-productposting.alibaba.com, DNS:video.alibaba.com, DNS:video01.alibaba.com, DNS:vietnamese.alibaba.com, DNS:watch.alibaba.com, DNS:wss-imakamai.alibaba.com, DNS:www.alibaba.com
| Issuer: commonName=DigiCert Global G3 TLS ECC SHA384 2020 CA1/organizationName=DigiCert Inc/countryName=US
| Public Key type: ec
| Public Key bits: 256
| Signature Algorithm: ecdsa-with-SHA384
| Not valid before: 2025-12-24T00:00:00
| Not valid after:  2026-07-07T23:59:59
| MD5:     9de4 56ba b7a8 27a3 0052 2f47 c332 c259
| SHA-1:   389e 3e7d a0c9 5620 0474 0bed d065 03a0 4a25 313f
|_SHA-256: 616b ed3f 3bb9 178b ba66 4711 0f3a e8a8 9794 9df8 196d ea25 3579 0f36 11bf 6624
| http-robots.txt: 43 disallowed entries (15 shown)
| /bin/ /apps/ /buy/ /memberhome/ /minisite/ 
| /corporations/ /buyers/ /trade/ /product/ /catalogs/corporations/ 
| /rss/*/*.rss /activities/ /productshowimg/ 
|_/member/*/contactinfo.html /member/*/company_profile.html
|_http-title: Alibaba.com: Manufacturers, Suppliers, Exporters & Importers f...
| http-methods: 
|_  Supported Methods: GET HEAD
|_http-favicon: Unknown favicon MD5: 7B7CE9977E05D1236F1997397A679C93
|_http-trane-info: Problem with XML parsing of /evox/about
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|router|specialized|storage-misc
Running (JUST GUESSING): Linux 4.X|5.X|2.6.X|3.X (91%), MikroTik RouterOS 7.X (90%), Crestron 2-Series (86%), HP embedded (85%)
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5 cpe:/o:mikrotik:routeros:7 cpe:/o:linux:linux_kernel:5.6.3 cpe:/o:crestron:2_series cpe:/o:linux:linux_kernel:2.6 cpe:/o:linux:linux_kernel:3 cpe:/h:hp:p2000_g3
Aggressive OS guesses: Linux 4.15 - 5.19 (91%), Linux 5.0 - 5.14 (91%), MikroTik RouterOS 7.2 - 7.5 (Linux 5.6.3) (90%), Crestron XPanel control system (86%), Linux 2.6.32 - 3.13 (86%), Linux 3.10 - 4.11 (86%), Linux 3.2 - 4.14 (86%), Linux 3.4 - 3.10 (86%), Linux 3.8 (86%), Linux 4.12 (86%)
No exact OS matches for host (test conditions non-ideal).
Uptime guess: 0.000 days (since Tue Feb  3 10:58:36 2026)
Network Distance: 9 hops
TCP Sequence Prediction: Difficulty=254 (Good luck!)
IP ID Sequence Generation: All zeros

TRACEROUTE (using port 443/tcp)
HOP RTT      ADDRESS
1   13.00 ms gpon.net (192.168.1.1)
2   8.00 ms  103.154.9.42
3   ...
4   27.00 ms reverse.anonet.in (103.43.33.1)
5   27.00 ms 121.240.111.145.static-delhi.vsnl.net.in (121.240.111.145)
6   29.00 ms 172.31.155.74 (172.31.155.74)
7   31.00 ms 115.110.210.66.static-Delhi.vsnl.net.in (115.110.210.66)
8   31.00 ms 116.119.109.16
9   34.00 ms a23-218-230-46.deploy.static.akamaitechnologies.com (23.218.230.46)

NSE: Script Post-scanning.
Initiating NSE at 10:58
NSOCK ERROR [64.8650s] poll_loop(): nsock_loop error 10022: An invalid argument was supplied. 
NSE: Script Engine Scan Aborted.
An error was thrown by the engine: F:\New folder/nse_main.lua:1078: a fatal error occurred in nsock_loop
stack traceback:
	[C]: in function 'nmap.socket.loop'
	F:\New folder/nse_main.lua:1078: in upvalue 'run'
	F:\New folder/nse_main.lua:1488: in function <F:\New folder/nse_main.lua:1435>
	[C]: in ?
Read data files from: F:\New folder
OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 64.87 seconds
           Raw packets sent: 2102 (96.076KB) | Rcvd: 404 (32.003KB)
