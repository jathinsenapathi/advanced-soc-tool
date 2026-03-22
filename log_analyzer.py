import re
from collections import defaultdict

class LogAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.ip_requests = defaultdict(int)
        self.failed_logins = defaultdict(int)

    def parse_logs(self):
        with open(self.log_file, "r") as file:
            for line in file:
                match = re.search(r'(\d+\.\d+\.\d+\.\d+).*"(GET|POST) (/\S*) .*" (\d+)', line)

                if match:
                    ip, method, endpoint, status = match.groups()

                    # Count total requests per IP
                    self.ip_requests[ip] += 1

                    # Detect failed logins (401)
                    if status == "401":
                        self.failed_logins[ip] += 1
