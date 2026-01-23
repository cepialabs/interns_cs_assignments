Title:
Improper Access Control Leading to Public FTP Directory Access.
Description:
The /ftp path on the target website is publicly accessible without any authentication.
Accessing this endpoint openly lists files and folders in the FTP directory.
This issue indicates improper access control and security misconfiguration, which could expose sensitive files to unauthorized users.
Impact:
Through this vulnerability, an attacker can:
. Download sensitive files (backups, configuration, documents)
. Access credentials, internal data, or database dumps
. Plan further attacks (Privilege Escalation, Data Breach)
. If the exposed files are sensitive, they can have a high impact.

Evidence:
By accessing the URL, publicly directory listing was observed:
http://localhost:3000/ftp/
Multiple files/folders inside the directory are visible without login, which confirms unauthorized access.

