from log_analyzer import LogAnalyzer
from threat_detection import ThreatDetector
from utils import generate_report

def main():
    analyzer = LogAnalyzer("sample.log")
    analyzer.parse_logs()

    detector = ThreatDetector(analyzer.failed_logins, analyzer.ip_requests)

    alerts = detector.detect_bruteforce()
    threat_scores = detector.calculate_threat_score()

    generate_report(analyzer.ip_requests, analyzer.failed_logins, alerts, threat_scores)

if __name__ == "__main__":
    main()
