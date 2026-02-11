# Tool User vs Skill Builder Analysis
## Action: Directory Enumeration (Dirsearch)

---

## 1. What I understood WITHOUT relying on tools (Skill Builder Mindset)

Before using any automated tool, I manually observed the target web application.

### Manual Observation Steps:
- Opened the website in browser
- Checked URLs and page structure
- Used browser DevTools to inspect network requests
- Tried common paths manually

### Manual checks performed:
```bash
https://target.com/admin
https://target.com/login
https://target.com/api
https://target.com/uploads

What I learned manually:

If the server returns 403, the directory likely exists but access is restricted

If it returns 301/302, the directory exists and redirects

If it returns 404, the directory likely does not exist

By understanding HTTP status codes and URL patterns, I could logically guess
which directories might be sensitive or interesting from a security perspective.

This step helped me think like an attacker instead of blindly running tools.

2. What the tool ONLY made faster (Tool User Mindset)

After forming assumptions manually, I used Dirsearch to speed up the enumeration process.

Command used:
1. dirsearch -u https://target.com

2. dirsearch -u https://target.com -x 404 -e php,html,js
	
What Dirsearch did:

Automatically tested hundreds of directory names

Identified valid paths based on response codes

Saved time compared to manual testing

However, the tool did not understand which directory was risky.
It only executed requests faster.
All decisions and analysis were still done by me.

3. Example from practice

During a scan, Dirsearch returned the following result:

/admin   (Status: 403)
/uploads (Status: 200)

Analysis:

/admin → exists but restricted → possible access control issue

/uploads → accessible → potential file upload vulnerability