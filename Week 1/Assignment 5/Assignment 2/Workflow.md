## Target: DVWA

## Observation:
The application was accessed via a web browser to analyze its structure.Modules and input points available were analyzed without aggressively interacting with them.It is a resource for security professionals to test their skills and tools in a legal environment, assists web developers in understanding the processes of securing web applications, and assists students & teachers in understanding web application security in a controlled classroom environment. DVWA offers various levels of vulnerability difficulty, making it ideal for beginners as well as advanced security professionals.

## Risk Area:
The OWASP Top 10 risks derive their respective positions from research or vulnerable code submissions contributed by project members, security consulting firms, bug bounty hunters, and other cybersecurity professionals.
DVWA has vulnerabilities such as XSS, CSRF, SQL injection, file injection, upload vulnerabilities, and so on, which is excellent for learning purposes to teach others about these vulnerabilities. Researchers can also use their tools to capture packets, brute force, and so on in DVWA.

. Brute Force
. Broken Acess Control
. Inhection

## Analyze Traffic
During the traffic analysis process, the SQL Injection module of DVWA was analyzed by entering carefully crafted input values into the User ID field. The Developer Tools Network tab of the browser was utilized to analyze the HTTP requests that were created after the form was submitted.

Multiple HTTP GET requests were noted, as the DVWA SQL Injection module sends user input through the HTTP GET protocol. Among the HTTP GET requests, the request with the injected payload in the URL query parameters was identified. The injected payload was directly visible in the request, as user input was sent to the server without proper sanitization.

Also added the screenshot (Analyze Traffic 1, Analyze Traffic Response) you can check.

## Document Finding
During the testing phase, the specially crafted SQL payloads were entered into the application using the input field. The application's behavior altered after the injection, signifying that the execution of the backend queries had been impacted. Network traffic analysis revealed that the injected payload was sent to the server using HTTP GET requests.

**Vulnerability Identified**

**Name:** SQL Injection

**Location:** DVWA → Vulnerabilities → SQL Injection

**Parameter Affected:** User ID

**Request Method:** GET

**Risk Level**

**High**

**Impact**

An attacker can use this vulnerability to manipulate database queries to bypass authentication, fetch sensitive information, or alter database contents. This vulnerability can result in the complete compromise of the database if exploited in a production environment.

**Recommendation**

Input validation and parameterized queries (prepared statements) should be used. User inputs should be sanitized before being processed by backend queries to avoid SQL Injection attacks.
