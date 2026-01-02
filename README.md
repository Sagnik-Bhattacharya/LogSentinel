# LogSentinel 🛡️

A **real-time log monitoring & alerting desktop application** built with Python. LogSentinel watches log files live, detects severity patterns, raises alerts, stores incidents, and visualizes trends — all through a clean GUI.

This project is designed to be **resume-ready**, demonstrating GUI development, multithreading, log parsing, alerting logic, persistence, and data visualization.

---

## 🚀 Features

* 📡 **Real-time log monitoring** (tail-style)
* 🎚️ **Severity-based filtering** (INFO, WARNING, ERROR, CRITICAL)
* 🚨 **Threshold-based alerts**
* ⏸️ **Pause / Resume monitoring**
* 💾 **SQLite persistence** for alerts
* 📊 **Live charts** for log severity distribution
* 🧱 **Clean modular architecture**

---

## 🧰 Tech Stack

* Python 3
* Tkinter + ttkbootstrap (GUI)
* SQLite (Persistence)
* Matplotlib (Charts)
* Regex (Log parsing)
* Threading (Non-blocking monitoring)

---

## 📁 Project Structure

```
logsentinel/
├── app/
│   ├── gui/
│   │   ├── dashboard.py
│   │   └── file_selector.py
│   ├── core/
│   │   ├── monitor.py
│   │   ├── parser.py
│   │   └── detector.py
│   ├── storage/
│   │   └── database.py
│   ├── utils/
│   │   └── constants.py
│   └── main.py
├── sample_logs/
│   └── app.log
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🖥️ Screenshots

> Add screenshots here before uploading to GitHub

* Dashboard overview
* Log filtering
* Alert triggered state
* Severity chart

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/logsentinel.git
cd logsentinel
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python app/main.py
```

---

## 🧪 How to Test LogSentinel

### ✅ Basic Manual Testing

1. Launch the app
2. Click **Select Log File**
3. Choose `sample_logs/app.log`
4. Open the same log file in a text editor
5. Append new log lines like:

```
2026-01-02 18:20:01 [ERROR] Payment service unavailable
2026-01-02 18:20:05 [CRITICAL] Disk space exhausted
```

6. Save the file
7. Observe:

   * New logs appear instantly
   * Counters increase
   * Alerts trigger at thresholds
   * Chart updates automatically

---

### ⏸️ Pause / Resume Test

* Click **Pause** → logs stop updating
* Append logs to the file
* Click **Resume** → logs continue from last position

---

### 🎚️ Filter Test

* Uncheck INFO or WARNING
* Only selected severities appear
* Counters & alerts still work correctly

---

### 💾 Database Test

* Trigger ERROR / CRITICAL alerts
* Close the app
* Verify `logsentinel.db` exists
* Open using DB Browser for SQLite
* Check the `alerts` table

---

## 🧠 Design Highlights (For Interviews)

* Decoupled **GUI / core / storage layers**
* Thread-safe log monitoring
* UI-only filtering (no data loss)
* Periodic chart updates for performance
* Single-responsibility modules

---

## 🔮 Future Enhancements

* Export alerts to CSV
* Pattern-based custom rules
* System tray notifications
* EXE packaging with PyInstaller

---

## 📜 License

MIT License

---

⭐ If you found this project useful, consider giving it a star!
