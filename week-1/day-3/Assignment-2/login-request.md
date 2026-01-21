# Chrome DevTools – HTTP Request Capture

## Login Request

![Login Request](request-screenshots/login-request.png)

- **URL:** http://localhost/DVWA/login.php
- **Method:** GET
- **Parameters:**
  - username
  - password
  - Login
- **Observation:**
  - Login data is sent using the GET method.
  - Server responds with HTTP 200 and returns an HTML page.
  - Successful authentication results in a session being created using a PHP session ID cookie.
