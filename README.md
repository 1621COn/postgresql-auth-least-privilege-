# postgresql-auth-least-privilege-
A PostgreSQL database and secure Python authentication backend implementing Bcrypt password hashing, parameterized queries to prevent SQL Injection, and Role Isolation via the Principle of Least Privilege.


# Portfolio Project: PostgreSQL Database Hardening & Secure Authentication Backend

## Project Overview
This project demonstrates advanced data security, database hardening, and defensive software development practices. Operating within an **Ubuntu Linux** environment, I deployed a **PostgreSQL** database and developed a secure Python authentication system. The primary objective was to implement defense-in-depth methodologies to protect sensitive user credentials, neutralize injection vectors, and enforce administrative access controls.

---

## Technical Skills Demonstrated
* Database Hardening & Access Control Lists (ACLs)
* Cryptographic Password Hashing & Salting (Bcrypt)
* SQL Injection (SQLi) Mitigation via Parameterized Queries
* The Principle of Least Privilege (PoLP) Role Isolation
* Python Database Integration (`psycopg2`)

---

## Infrastructure & Tools Used
* **Operating System:** Ubuntu Desktop (Virtual Machine)
* **Database Engine:** PostgreSQL
* **Languages & Libraries:** Python 3, Bcrypt, Psycopg2
* **Development Environment:** Python Virtual Environment (`venv`)

---

## Architecture & Security Implementation

### Phase 1: Cryptographic Password Storage (Bcrypt)
Instead of storing user credentials in insecure plain-text format, I built a registration mechanism utilizing the **Bcrypt** algorithm. 
* **Implementation:** The system generates a distinct, random cryptographic salt for each entry and processes the payload through intensive CPU work factor cycles. This ensures that the stored hashes are entirely resilient against pre-computed rainbow table attacks.

### Phase 2: Injection Mitigation (Parameterized Queries)
To defend the system against authentication bypass mechanisms, the query engine was hardened against SQL Injection (SQLi).
* **Implementation:** I utilized parameterized queries (`%s` placeholders) within the Python script execution blocks. This explicitly isolates user-input parameters from the SQL command logic, stripping executable attributes from input data and gracefully neutralizing classic attack strings like `' OR '1'='1`.

### Phase 3: Role Isolation & Least Privilege (PoLP)
To eliminate the severe security risk of running an application database connection using global administrator privileges (`postgres`), I enforced strict network and role boundaries.
* **Implementation:** I created a dedicated account (`low_priv_user`) and completely revoked its default schema access. I then applied targeted Access Control Lists (ACLs) allowing the user to *only* run `SELECT` and `INSERT` commands on the single required table (`user_credentials`). All administrative system commands (like `DROP TABLE`) are blocked at the database engine level.

---

## Defensive Verification Results

### 1. Database Inspection (Obfuscation Verification)
Inspecting the database table verified that user credentials are encrypted via standard cryptographic strings (`$2b$` identifiers):
```text
 user_id | username |                         password_hash                          
---------+----------+----------------------------------------------------------------
       1 | David    | $2b$12$K89sJ...[Sanitized Cryptographic Hash Output]...7h2mKq
```

### 2. Unauthorized Command Simulation (Privilege Testing)
Logging in as the restricted application account and attempting to execute malicious or destructive modifications safely verified the Access Control constraints:
```text
secure_app=> DROP TABLE user_credentials;
ERROR: must be owner of table user_credentials

secure_app=> CREATE TABLE hacker_table (id INT);
ERROR: permission denied for schema public
```

---

## Conclusion
This project demonstrates an enterprise-grade approach to application layer security and database defense. By combining strong cryptographic hashing, strict input parameterization, and isolated user roles, the system successfully minimizes its attack surface and protects sensitive user data against credential theft and access exploits.
