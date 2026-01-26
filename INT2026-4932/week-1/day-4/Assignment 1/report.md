\# Weak Session ID Vulnerability in DVWA



\## Description

The Weak Session IDs vulnerability was observed in the DVWA under the "Weak Session IDs" module at the low security level.  

The application generates a session identifier using a predictable and incremental value stored in a session variable and sets it as a cookie (dvwaSession) after every POST request.



The session ID is increased sequentially (e.g 1, 2, 3) This behavior makes the session ID easy to guess or manipulate.



\## Impact

Because the session ID is easy to predict, an attacker can guess another user’s session ID and access their account without permission.  

This may allow the attacker to act as that user, view their data, or perform actions on their behalf, which can lead to data misuse and security risks.



\## Evidence

The source code of the vulnerable functionality clearly shows that the session ID and also after refreshing page value increment is incremented sequentially and assigned directly to a cookie:



```php

if ($\_SERVER\['REQUEST\_METHOD'] == "POST") {

&nbsp;   if (!isset($\_SESSION\['last\_session\_id'])) {

&nbsp;       $\_SESSION\['last\_session\_id'] = 0;

&nbsp;   }

&nbsp;   $\_SESSION\['last\_session\_id']++;

&nbsp;   $cookie\_value = $\_SESSION\['last\_session\_id'];

&nbsp;   setcookie("dvwaSession", $cookie\_value);

}



