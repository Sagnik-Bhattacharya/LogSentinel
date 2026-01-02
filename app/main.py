# app/main.py
import threading
import ttkbootstrap as ttk
import time
from gui.dashboard import Dashboard
from gui.file_selector import FileSelector
from core.monitor import LogMonitor
from core.parser import parse_log_line
from core.detector import Detector
from storage.database import AlertDatabase
from utils.constants import LOG_LEVELS


class LogSentinelApp:
    def __init__(self, root):
        self.root = root
        self.monitor = None
        self.thread = None
        self.last_chart_update = time.time()
        self.chart_interval = 1.0  # seconds
        self.detector = Detector()
        self.database = AlertDatabase()
        self.all_logs = []
        self.level_counts = {level: 0 for level in LOG_LEVELS}

        self.dashboard = Dashboard(
            root,
            on_pause=self.pause_monitoring,
            on_resume=self.resume_monitoring,
            on_filter_change=self.refresh_filtered_logs
        )

        self.file_selector = FileSelector(root, self.start_monitoring)
        
    def start_monitoring(self, filepath):
        if self.monitor:
            self.monitor.stop()

        self.detector.reset()
        self.level_counts = {level: 0 for level in LOG_LEVELS}
        self.dashboard.reset_status()

        # CREATE MONITOR
        self.monitor = LogMonitor(
            filepath=filepath,
            callback=self.schedule_log_update  # IMPORTANT
        )

        # START IN BACKGROUND THREAD
        self.thread = threading.Thread(
            target=self.monitor.start,
            daemon=True
        )
        self.thread.start()
        
    def schedule_log_update(self, line):
        # Ensure GUI updates run on main thread
        self.root.after(0, self.on_new_line, line)

    def on_new_line(self, line):
        parsed = parse_log_line(line)
        if not parsed:
            return

        level = parsed["level"]

        # store every log line
        self.all_logs.append((line, level))

        if level in self.level_counts:
            self.level_counts[level] += 1
            self.dashboard.update_count(level, self.level_counts[level])

        # add log if filter allows
        self.dashboard.add_log(line, level)

        # update chart periodically
        self.dashboard.update_chart(self.level_counts)
    
    def refresh_filtered_logs(self):
        self.dashboard.refresh_logs(self.all_logs)

        
    def pause_monitoring(self):
        if self.monitor:
            self.monitor.pause()

    def resume_monitoring(self):
        if self.monitor:
            self.monitor.resume()

def main():
    root = ttk.Window(
        title="LogSentinel",
        themename="darkly",
        size=(900, 600)
    )
    LogSentinelApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
