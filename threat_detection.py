class ThreatDetector:
    def __init__(self, failed_logins, ip_requests):
        self.failed_logins = failed_logins
        self.ip_requests = ip_requests

    def detect_bruteforce(self, threshold=3):
        alerts = []

        for ip, count in self.failed_logins.items():
            if count > threshold:
                alerts.append((ip, count))

        return alerts

    def calculate_threat_score(self):
        scores = {}

        for ip in self.ip_requests:
            score = 0

            # Failed login weight
            score += self.failed_logins.get(ip, 0) * 10

            # Activity weight
            score += self.ip_requests.get(ip, 0) * 2

            scores[ip] = min(score, 100)

        return scores
