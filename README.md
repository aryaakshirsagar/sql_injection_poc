# SQL Injection Detector (PoC)

## Overview
This is a beginner-friendly **Proof-of-Concept** tool for detecting **possible SQL Injection vulnerabilities** in web applications.
** Ethical Use Only** – test only on systems you own or have permission for (e.g., DVWA, Juice Shop).

---

##  Requirements
- Python 3.x
- Install dependencies:
```bash
pip install requests beautifulsoup4
```

---

##  How to Run
1. Save the script as `sql_injection_detector.py`
2. Open a terminal in the script folder.
3. Run:
```bash
python sql_injection_detector.py
```
4. Enter a target URL with a GET parameter:
```
http://127.0.0.1/dvwa/vulnerabilities/sqli/?id=1
```
5. The tool will:
   - Send **classic**, **union-based**, and **time-based** SQLi payloads
   - Check for **error messages**, **unexpected output**, or **response delays**
   - Show a summary of possible vulnerabilities

---

## Example Output
```
[+] Testing target: http://127.0.0.1/dvwa/vulnerabilities/sqli/?id=1

[>] Testing payload: ' OR '1'='1' --
[!] Vulnerable indicator found: ['Possible SQL error in response']

=== Summary of Potential Vulnerabilities ===
Payload: ' OR '1'='1' --
URL: http://127.0.0.1/dvwa/vulnerabilities/sqli/?id=' OR '1'='1' --
Indicators: ['Possible SQL error in response']
Response time: 0.34s
----------------------------------------
```

---

## Prevention Tips
- Always use **parameterized queries** / **prepared statements**
- Validate & sanitize user input
- Use ORM frameworks instead of raw SQL
- Restrict database error messages in production
