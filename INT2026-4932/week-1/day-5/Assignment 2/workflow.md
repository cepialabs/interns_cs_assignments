# Pentester Workflow Simulation – DVWA (SQL Injection)
# Step 1: Observation
First, I explored DVWA like a normal user.
- Logged into DVWA dashboard.
- Opened the SQL Injection module.
- Observed an input box asking for a User ID.
- Noticed that the application returns user details based on the input.
This indicated that the input might be directly used in a database query.

## Step 2: Identify Risky Area
The User ID input field was identified as a risky area.
- User input is sent directly to the backend database.
- No client-side validation was visible.
- SQL Injection is a common risk when input is not sanitized.

This made the SQL Injection module a suitable target.
# Step 3: Analyze Traffic
To understand how the application processes input:
- Entered a normal value (e.g., `1`) and observed the output.
- Entered a special input (`1' OR '1'='1`) in the User ID field.
- The application returned multiple user records.
This confirmed that:
- User input is directly included in SQL queries.
- The database is executing injected SQL commands.
- Input is not properly filtered.

# Step 4: Document Finding
# Vulnerability Identified
SQL Injection
