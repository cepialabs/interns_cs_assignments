VULN-01: SQL Injection (Authentication Bypass)
Vulnerability Name: SQL Injection on Login Page

Location: http://testphp.vulnweb.com/login.php

Payload Used: ' OR 1=1 --

Steps to Reproduce:

Login page par jao.

Username field mein ' OR 1=1 -- enter karo.

Password field mein kuch bhi dalo.

Submit karne par system authentication bypass karke login kar dega.

Impact: Attacker bina valid password ke kisi bhi user ka account access kar sakta hai.

Evidence: evidence/image_9560c6.png

VULN-02: Reflected XSS (Cross-Site Scripting)
VULN-02: Reflected XSS (Cross-Site Scripting)
Vulnerability Name: Reflected XSS in Search Parameter

Location: http://testphp.vulnweb.com/search.php?test=query

Payload Used: <script>alert(document.cookie)</script>

Steps to Reproduce:

Search box mein script payload enter karein.

Page load hote hi browser script execute karega aur alert box show karega.

Impact: Attacker users ki session cookies chura sakta hai (Session Hijacking).

Evidence: evidence/image_9564c3.png