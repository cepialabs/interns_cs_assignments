# Vulnerability Report: SQL Injection

- **Target Application:** DVWA (Damn Vulnerable Web Application)
- **Vulnerability Type:** SQL Injection (In-band/Error-Based)
- **Severity:** High
- **Researcher:** [Zubair Wani]
 
 ## 🔍 Description
The "User ID" search functionality in the application is vulnerable to **SQL Injection (SQLi)**.
This occurs because the application takes user input and includes it directly i
n a database query without proper validation or sanitization.

By entering specific SQL characters, 
an attacker can break out of the intended logic and execute unauthorized commands directly on the backend database.

## ⚡ Impact
If exploited, this vulnerability allows an attacker to:
* **Exfiltrate Data:** Access the entire user database, including sensitive information like usernames and hashed passwords.
* **Bypass Authentication:** Log in as an administrator or any other user without a valid password.
* **Data Manipulation:** Depending on database permissions, an attacker could modify, insert, or delete records.

---

## 🛠️ Proof of Concept (Evidence)

1. **Step 1:** Navigate to the **SQL Injection** tab in DVWA.
2. **Step 2:** In the User ID input field, enter the following payload:
   ```sql
   %' OR '1'='1



 ## step 3: Click "Submit."

 ##  Observation:
Instead of showing the details for a single ID, 
the application returns the names and surnames of every user in the database.

Why it works: The backend query likely looks like this:

SELECT first_name, last_name FROM users WHERE user_id = '$id';

When we input %' OR '1'='1, the query becomes:

SELECT first_name, last_name FROM users WHERE user_id = '%' OR '1'='1';

Since '1'='1' is always true, the database returns all rows.

✅ Recommendation (Fix)
-- Secure Example (PHP/PDO)
$stmt = $pdo->prepare('SELECT first_name, last_name FROM users WHERE user_id = :id');
$stmt->execute(['id' => $user_input]);
