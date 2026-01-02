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
        self.monitors = []
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
        
    # def start_monitoring(self, filepaths):
    #     if self.monitor:
    #         self.monitor.stop()

    #     self.detector.reset()
    #     self.level_counts = {level: 0 for level in LOG_LEVELS}
    #     self.dashboard.reset_status()

    #     # CREATE MONITOR
    #     self.monitor = LogMonitor(
    #         filepath=filepath,
    #         callback=self.schedule_log_update  # IMPORTANT
    #     )

    #     # START IN BACKGROUND THREAD
    #     self.thread = threading.Thread(
    #         target=self.monitor.start,
    #         daemon=True
    #     )
    #     self.thread.start()
      
    def start_monitoring(self, filepaths):
        # Stop existing monitors
        for monitor in self.monitors:
            monitor.stop()

        self.monitors.clear()
        self.all_logs.clear()

        self.detector.reset()
        self.level_counts = {level: 0 for level in LOG_LEVELS}
        self.dashboard.reset_status()

        for path in filepaths:
            monitor = LogMonitor(
                filepath=path,
                callback=lambda line, p=path: self.schedule_log_update(line, p)
            )
            self.monitors.append(monitor)

            thread = threading.Thread(
                target=monitor.start,
                daemon=True
            )
            thread.start()
    
    def schedule_log_update(self, line, filepath):
        self.root.after(0, self.on_new_line, line, filepath)


    def on_new_line(self, line, filepath):
        parsed = parse_log_line(line)
        if not parsed:
            return

        level = parsed["level"]

        # store log
        filename = filepath.split("/")[-1]
        display_line = f"{filename} | {line}"
        self.all_logs.append((display_line, level))

        # update counts
        if level in self.level_counts:
            self.level_counts[level] += 1
            self.dashboard.update_count(level, self.level_counts[level])

        # 🚨 PROCESS ALERT LOGIC
        alert = self.detector.process(level)
        if alert:
            self.dashboard.show_alert(alert["message"])
            self.dashboard.show_popup_alert(
                title=f"{alert['level']} Alert",
                message=f"{alert['message']}\nCount: {alert['count']}"
            )

        # refresh UI
        self.refresh_filtered_logs()
    
    
    def refresh_filtered_logs(self):
        self.dashboard.refresh_logs(self.all_logs)

        filtered_counts = {lvl: 0 for lvl in LOG_LEVELS}
        for _, level in self.all_logs:
            if self.dashboard.should_display(level):
                filtered_counts[level] += 1

        self.dashboard.update_chart(filtered_counts)


        
    def pause_monitoring(self):
        for monitor in self.monitors:
            monitor.pause()

    def resume_monitoring(self):
        for monitor in self.monitors:
            monitor.resume()


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
