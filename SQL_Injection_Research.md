# SQL Injection Research & Proof-of-Concept

## 1. Overview
**SQL Injection (SQLi)** is a web vulnerability where malicious SQL code is inserted into a query to manipulate a database.

### Types
- **Classic/Inline** – Modify query directly (`' OR '1'='1' --`)
- **Union-based** – Use `UNION SELECT` to fetch other data
- **Blind** – Use delays (`SLEEP()`) or yes/no queries when no errors are shown

---

## 2. Real-World Examples
### CVE-2023-25136 – MySQL Auth Bypass
A logic flaw allowed attackers to bypass authentication by sending crafted packets.

### CVE-2022-21661 – WordPress SQL Injection
Improper query preparation in WP core functions allowed attackers to run arbitrary queries.

### CVE-2019-11043 – PHP-FPM Remote Code Execution
Specially crafted requests with SQLi vectors led to arbitrary code execution on certain PHP-FPM configs.

---

## 3. Proof-of-Concept Tool Methodology
1. **Payload Injection** – Append known SQLi payloads to target parameter
2. **Response Analysis** – Look for:
   - SQL error keywords
   - Unexpected SQL-related output
   - Delayed responses (blind SQLi)
3. **Logging** – Store payloads and indicators for review

---

## 4. Prevention Recommendations
- **Parameterized queries** (Prepared Statements)
- **Input validation** – Allow only expected characters
- **ORM frameworks** – Avoid raw SQL
- **Least privilege** – Limit DB account permissions
- **Web Application Firewall (WAF)** – Block known SQLi patterns

---

## 5. Ethical Considerations
- Only test on **authorized targets**
- Avoid destructive payloads
- Follow **responsible disclosure** if vulnerabilities are found
