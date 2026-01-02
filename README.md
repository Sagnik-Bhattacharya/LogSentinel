# LogSentinel 🛡️

**LogSentinel** is a real-time log monitoring, filtering, and visualization tool built with Python and Tkinter. It helps developers and system engineers observe application behavior, detect critical issues early, and analyze log trends through an interactive GUI dashboard.

This project is inspired by real-world observability tools like **ELK Stack, Datadog, and Splunk**, implemented as a lightweight, local, and beginner-to-intermediate friendly system.

---

## 🚀 Features

- 📡 **Real-time Log Monitoring** – Watches log files as they update
- 🔎 **Severity-based Filtering** – INFO / WARNING / ERROR / CRITICAL
- 📊 **Live Error Frequency Chart** – Visualize system health instantly
- 🧠 **Smart Log Parsing** – Handles mixed log formats
- 🖥️ **Interactive GUI Dashboard** – Built with Tkinter + ttkbootstrap
- 🧵 **Non-blocking Monitoring** – Uses background threads
- 🗂️ **Sample Logs Included** – Test instantly

---

## 🧠 Why LogSentinel?

Logs are the backbone of debugging and production monitoring. Raw log files quickly become unmanageable as systems grow. LogSentinel turns plain-text logs into actionable insights by:

- Reducing noise via filters
- Highlighting critical failures
- Tracking error trends visually
- Speeding up debugging and incident response

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
│   │   └── detector.py   # Severity detection
│   ├── storage/          # Persistence layer
│   │   └── database.py
│   ├── utils/
│   │   └── constants.py
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
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
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

1. Select a log file (try `sample_logs/app.log`)
2. Start monitoring
3. Apply severity filters
4. Observe live logs and chart updates

---

## 🧪 Testing the System

### Manual Testing

- Add new lines to the log file while monitoring
- Try different severity levels
- Apply filters and observe chart updates

### Example Test Logs

```
[INFO] App started
WARNING Disk almost full
2026-01-02 18:40:01 [ERROR] Database down
CRITICAL Kernel panic
```

---

## 📈 Real-World Use Cases

- 🔧 Local development debugging
- 🚨 Production incident monitoring
- 📊 System health visualization
- 🔍 Root-cause analysis
- 🛡️ Security & audit log review

---

## 🧩 Future Enhancements (Planned)

- Alert popups & sound notifications
- Regex-based filters
- Save filter presets
- Export error reports
- Multi-file monitoring

---

## 💼 Resume Description

> Built a real-time log monitoring and visualization system with Python, featuring live file watching, severity-based filtering, and GUI dashboards inspired by production observability tools.

---

⭐ If you find this project useful, consider starring the repository!
