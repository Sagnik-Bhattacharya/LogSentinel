# **LogSentinel 🛡️**

**LogSentinel** is a real-time log monitoring, filtering, and visualization tool built with Python and Tkinter. It helps developers and system engineers observe application behavior, detect critical issues early, and analyze log trends through an interactive GUI dashboard.

> The goal of this project is to explore the core building blocks behind log monitoring tools by implementing them from scratch using Python.

---

## 🚀 Features

* 📡 **Real-time Multi-File Log Monitoring** – Watches one or more log files simultaneously.
* 🔎 **Severity-based Filtering** – Filter logs by INFO / WARNING / ERROR / CRITICAL.
* 📊 **Live Error Frequency Chart** – Visualize system health instantly.
* 🧠 **Smart Log Parsing** – Handles mixed log formats and timestamps.
* 🖥️ **Interactive GUI Dashboard** – Built with Tkinter + ttkbootstrap.
* 🧵 **Non-blocking Monitoring** – Uses background threads to avoid freezing the UI.
* 🛎️ **Popup Alerts** – Threshold-based notifications for critical logs.
* 🗂️ **Export Logs** – Save logs to **CSV** or **JSON** for reporting and analysis.
* 🗃️ **Sample Logs Included** – Test instantly.

---

## 🧠 Why LogSentinel?

Logs are the backbone of debugging and production monitoring. Raw log files quickly become unmanageable as systems grow. LogSentinel turns plain-text logs into actionable insights by:

* Reducing noise via severity filters
* Highlighting critical failures through alerts
* Tracking error trends visually
* Speeding up debugging and incident response

---

## 🏗️ Project Structure

```
logsentinel/
├── app/
│   ├── gui/              # GUI components
│   │   ├── dashboard.py
│   │   └── file_selector.py
│   ├── core/             # Core logic
│   │   ├── monitor.py    # File watcher
│   │   ├── parser.py     # Log parser
│   │   └── detector.py   # Severity detection & alerts
│   ├── storage/          # Persistence layer
│   │   └── database.py
│   ├── utils/
│   │   └── constants.py  # Log levels & thresholds
│   └── main.py           # Application entry point
├── sample_logs/
│   └── app.log
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sagnik-Bhattacharya/LogSentinel.git
cd logsentinel
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python app/main.py
```

1. Select one or more log files (try `sample_logs/app.log`)
2. Start monitoring
3. Apply severity filters
4. Observe live logs, charts, and alerts
5. Export logs to CSV or JSON for reporting

---

## 🧪 Testing the System

### Manual Testing

* Add new lines to log files while monitoring.
* Test different severity levels (INFO, WARNING, ERROR, CRITICAL).
* Apply filters and verify chart updates.
* Trigger alerts by exceeding thresholds.
* Export logs and verify CSV/JSON files.

### Example Test Logs

```
[INFO] App started
WARNING Disk almost full
2026-01-02 18:40:01 [ERROR] Database down
CRITICAL Kernel panic
```

---

## 📈 Real-World Use Cases

* 🔧 Local development debugging
* 🚨 Production incident monitoring
* 📊 System health visualization
* 🔍 Root-cause analysis
* 🛡️ Security & audit log review

---

## 🧩 Future Enhancements (Planned)

* Sound notifications for alerts
* Regex-based filters
* Save filter presets
* Scheduled report exports
* Advanced analytics & trend charts

---

## 💼 Resume Description

> Built a real-time, multi-file log monitoring and visualization system with Python, featuring live file watching, severity-based filtering, popup alerts, GUI dashboards, and export functionality for CSV/JSON reports. Demonstrates skills in Python GUI development, threading, file I/O, and data visualization.

---

⭐ If you find this project useful, consider **starring the repository**!
