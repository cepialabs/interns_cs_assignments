🛡️ OWASP Juice Shop – Reconnaissance & Observation Report

Target: https://owasp-juice.shop

Objective: Manual reconnaissance and application observation

1️⃣ Purpose of the Website

OWASP Juice Shop is an intentionally vulnerable web application created by the OWASP Foundation for:

Learning web application security

Practicing penetration testing techniques

Understanding real-world vulnerabilities

Hands-on experience with OWASP Top 10 risks

It simulates a modern e-commerce platform that sells products such as juice, merchandise, and accessories.

2️⃣ Is There a Login Page?

✅ Yes

A login feature is present.

Users can:

Log in using existing credentials

Register as a new user

Login appears to be handled via API requests, indicating a Single Page Application (SPA) architecture.

Observation:

Authentication uses token-based session handling (likely JWT).

3️⃣ Is There an Admin Panel Visible?

❌ No public admin panel is visible

No direct /admin or /administrator link is visible in the UI.

This suggests:

Admin functionality is hidden

Admin endpoints may exist but are not directly exposed

Admin access might be achievable through:

Broken access control

Privilege escalation vulnerabilities

Hidden endpoints

4️⃣ Technologies Used (Guess-Based on Observation)

⚠️ Based on visible behavior and request analysis (educated guess):

Frontend:

Angular (Single Page Application behavior)

HTML, CSS, JavaScript

Bootstrap / Material UI styling

Backend:

Node.js

Express.js framework

RESTful APIs

Database:

SQLite / MySQL (likely relational DB)

Authentication:

JWT (JSON Web Tokens)

5️⃣ Pages and Endpoints Observed
Visible UI Pages:

/

/login

/register

/about

/contact

/basket

/profile

/search

API Endpoints (Observed via DevTools / Burp):

/rest/user/login

/api/Products

/api/Users

/rest/basket/*

6️⃣ Initial Security Observations

Application heavily relies on client-side logic

Uses REST APIs, increasing exposure to:

IDOR

Broken access control

API parameter tampering

JWT tokens are stored client-side → possible:

Token theft

Session hijacking

Admin functionality likely exists but is hidden → high-value attack surface

7️⃣ Conclusion

OWASP Juice Shop closely simulates a real-world modern e-commerce web application and provides an excellent platform for practicing:

Web application penetration testing

API security testing

Authentication and authorization testing

Business logic flaw detection

This observation phase provides the foundation for deeper security testing.
