# Client-Side User Enumeration via Password Reset Flow

## Title
Client-Side User Enumeration via Password Reset in OWASP Juice Shop

## Description
The password reset functionality in OWASP Juice Shop contains a subtle but critical design flaw that allows user enumeration through **client-side behavior**. Specifically:

- When a **registered/valid email** is entered into the password reset form, additional fields—such as **security question, new password, and confirm password inputs**—become **immediately enabled**.
- When an **invalid or non-existent email** is entered, these fields remain **disabled** and cannot be interacted with.
- This difference occurs **instantly on the client side** without submitting the form or reloading the page.

This behavior effectively allows an attacker to determine which email addresses are registered in the application **without any server-side request or authentication**. This type of vulnerability is often overlooked but can serve as the initial step in targeted attacks such as phishing, account takeover, or credential stuffing.

---

## Impact
The impact of this vulnerability includes:

- **User Enumeration:** Attackers can systematically test email addresses to find valid users.
- **Targeted Attacks:** Identified users can be subjected to phishing or social engineering attacks.
- **Credential Stuffing & Brute Force:** Knowing valid emails reduces the effort required for further attacks on user accounts.
- **Privacy & Reputation Risks:** Exposure of registered users compromises privacy and could harm organizational reputation.

Although the flaw exists in the front-end logic, it is **serious in any realistic scenario**, as it allows attackers to bypass standard protections without triggering server-side defenses.

---

## Evidence
The vulnerability is demonstrated by the following observations:

### Case 1: Valid User
- **Input:** A registered email (e.g., `ketan_patil@gmail.com`)  
- **Behavior Observed:** Security question, new password, and confirm password fields **become enabled immediately**.  
- **Interpretation:** The application confirms the existence of this email account through client-side logic.  

![Password reset fields enabled for valid user](images/valid_email.png)

---

### Case 2: Invalid User
- **Input:** A non-existent email (e.g., `randomuser12345@notreal.com`)  
- **Behavior Observed:** Security question, new password, and confirm password fields **remain disabled** and cannot be edited.  
- **Interpretation:** The difference in UI behavior allows an attacker to distinguish invalid emails from valid ones without submitting the form.  

![Password reset fields disabled for invalid user](images/invalid_email.png)

---

## Summary
This report highlights a **client-side user enumeration flaw** in the OWASP Juice Shop password reset workflow. While the application does not explicitly leak information via messages, the **UI behavior itself serves as a side-channel**, revealing which users are registered.  

Mitigation measures include:
- Removing client-side indicators that differentiate valid from invalid users.
- Implementing server-side rate limiting and uniform responses.
- Adding CAPTCHA or other mechanisms to prevent automated enumeration.

This type of report demonstrates the importance of reviewing not only server-side logic but also **front-end behavior** when assessing security risks.
