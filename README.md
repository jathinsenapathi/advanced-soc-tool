# 🛡️ Advanced Security Log Analyzer (Mini SOC Tool)

A Python-based security log analyzer that detects suspicious activity such as brute force attacks by analyzing server logs.

---

## 🚀 Features

* Log parsing using regex
* Detection of failed login attempts (401)
* Brute force attack detection
* Threat scoring for each IP
* JSON report generation
* Modular architecture (multi-file project)

---

## 📂 Project Structure

* `main.py` → Controls the workflow
* `log_analyzer.py` → Parses logs and extracts data
* `threat_detection.py` → Detects attacks and calculates threat scores
* `utils.py` → Generates reports (console + JSON)
* `sample.log` → Sample log file for testing

---

## ▶️ How to Run

```bash
git clone https://github.com/jathinsenapathi/advanced-soc-tool.git
cd advanced-soc-tool
python3 main.py
```

---

## 📊 Example Output

```
[CRITICAL] 203.0.113.5 → 6 failed logins
Threat Score: 72/100
```

---

## 📁 Output

* `report.json` → Structured threat analysis report

---

## 🎯 Use Case

* Detect brute force attacks
* Analyze suspicious IP activity
* Generate security reports

---

## ⚠️ Disclaimer

This project is for educational purposes and authorized security testing only.
