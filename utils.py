import json
from datetime import datetime

def generate_report(ip_requests, failed_logins, alerts, threat_scores):
    print("\n🔍 SOC ANALYSIS REPORT")
    print("-" * 40)

    print("\nIP Activity:")
    for ip, count in ip_requests.items():
        print(f"{ip} → {count} requests")

    print("\nFailed Logins:")
    for ip, count in failed_logins.items():
        print(f"{ip} → {count} failed attempts")

    print("\n🚨 Suspicious Activity:")
    if alerts:
        for ip, count in alerts:
            print(f"[CRITICAL] {ip} → {count} failed logins")
    else:
        print("No threats detected")

    print("\n📊 Threat Scores:")
    for ip, score in threat_scores.items():
        print(f"{ip} → {score}/100")

    # 🔥 JSON REPORT
    report = {
        "timestamp": datetime.now().isoformat(),
        "ip_activity": ip_requests,
        "failed_logins": failed_logins,
        "alerts": [{"ip": ip, "attempts": count} for ip, count in alerts],
        "threat_scores": threat_scores
    }

    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("\n📁 Report saved as report.json")
