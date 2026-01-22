# Security Notes: Web Application Testing

## Scope
This note documents observations and analysis of potential security issues within a web application, focusing on areas where client-side behavior could expose sensitive information or allow unauthorized actions. The goal is to capture relevant findings for review, learning, and future reference.

## Target
- Web application password reset functionality  
- Client-side form behavior  
- Different user account scenarios:
  - **Valid email accounts**  
  - **Invalid/non-existent email accounts**  

## Observations
- Entering a **valid email** immediately enables the following fields:
  - Security question  
  - New password  
  - Confirm password

![Fields enabled for valid user](images/valid_email.png)

- Entering an **invalid email** keeps these fields **disabled**, preventing interaction.

![Fields enabled for valid user](images/invalid_email.png)

- The difference in behavior occurs **instantly on the client side**, without submitting the form.
- No explicit server-side error messages are required to identify valid accounts. The **UI state itself leaks information**, demonstrating a subtle **user enumeration vulnerability**.
- This type of client-side information leakage could be exploited by attackers to:
  - Identify registered users quickly  
  - Launch targeted phishing or social engineering attacks  
  - Prepare for credential stuffing or account takeover attempts

## Questions
- Could this client-side user enumeration be combined with other attack vectors, such as phishing or credential stuffing?  
- Are there other parts of the web application where front-end behavior exposes sensitive information?  
- How could **uniform server responses, rate limiting, or CAPTCHAs** mitigate this vulnerability?  
- What additional steps could be taken to prevent **side-channel leaks** in web applications?  

## Learning
- Client-side behavior can inadvertently **leak sensitive information**, even without server-side error messages.  
- UI state changes (fields enabling/disabling) can serve as a **side channel for user enumeration**.  
- Valid vs invalid account detection can be done **entirely on the client side**, which attackers could automate.  
- Security testing must include **front-end interaction analysis**, not just server responses.  
- Observing how forms react to input gives insight into **logic flaws and potential attack vectors**.
