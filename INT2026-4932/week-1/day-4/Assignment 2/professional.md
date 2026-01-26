# Title 
Weak Session Managemnet Using DVWA

# Scope
The scope of these notes is to study and understand weak session management vulnerabilities using the DVWA.  
The focus is on identifying how predictable session identifiers can introduce security risks and how such issues can be mitigated.

# Target
The target application is Damn Vulnerable Web Application (DVWA), specifically the Weak Session IDs vulnerability module at low security level.

# Observations
- The application generates a session cookie named 'dvwaSession'.
- The session ID value increases sequentially 1, 2, 3 on every POST request.
- The session identifier is predictable and not random.
- No security flags such as HttpOnly or Secure are applied to the cookie.
- An attacker can guess or manipulate the session ID to access another user’s session.

# Questions
- Why is using a simple or predictable session ID unsafe?
- What can happen if an attacker guesses a user’s session ID?
- Why should cookies have security flags like HttpOnly and Secure?
- How does PHP automatically create safer session IDs?

# Learning
- Session IDs should be random and not easy to guess.
- Weak session handling can allow attackers to take over user sessions.
- Cookies should use security options like HttpOnly, Secure, and SameSite.
- It is safer to use built-in session features instead of writing custom code.
- Good session management is important to keep web applications secure.