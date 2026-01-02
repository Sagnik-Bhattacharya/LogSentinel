# app/gui/dashboard.py
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter.scrolledtext import ScrolledText
from utils.constants import LOG_LEVELS

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Map log levels to colors
LOG_COLORS = {
    "INFO": "green",
    "WARNING": "orange",
    "ERROR": "red",
    "CRITICAL": "red"
}


class Dashboard(ttk.Frame):
    def __init__(self, master, on_pause, on_resume, on_filter_change):
        super().__init__(master)
        self.on_filter_change = on_filter_change
        self.pack(fill=BOTH, expand=True, padx=10, pady=10)

        self.on_pause = on_pause
        self.on_resume = on_resume
        self.paused = False

        # ===== Filters =====
        self.filters = {
            level: ttk.BooleanVar(value=True) for level in LOG_LEVELS
        }

        filter_frame = ttk.Labelframe(self, text="Log Filters")
        filter_frame.pack(fill=X, pady=5)

        for level in LOG_LEVELS:
            ttk.Checkbutton(
                filter_frame,
                text=level,
                variable=self.filters[level],
                bootstyle="round-toggle",
                command=self.on_filter_change   # ✅ NO master usage
            ).pack(side=LEFT, padx=5)



        # ===== Counters =====
        self.count_vars = {
            level: ttk.StringVar(value="0") for level in LOG_LEVELS
        }

        counter_frame = ttk.Frame(self)
        counter_frame.pack(fill=X, pady=5)

        for level in LOG_LEVELS:
            ttk.Label(counter_frame, text=level).pack(side=LEFT, padx=5)
            ttk.Label(
                counter_frame,
                textvariable=self.count_vars[level],
                bootstyle="info"
            ).pack(side=LEFT, padx=5)

        # ===== Controls =====
        control_frame = ttk.Frame(self)
        control_frame.pack(fill=X, pady=5)

        self.pause_btn = ttk.Button(
            control_frame,
            text="Pause",
            bootstyle="warning",
            command=self.toggle_pause
        )
        self.pause_btn.pack(side=LEFT)

        # ===== Chart =====
        chart_frame = ttk.Labelframe(self, text="Log Severity Chart")
        chart_frame.pack(fill=BOTH, expand=False, pady=10)

        self.figure = Figure(figsize=(6, 3), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_title("Log Events Count")
        self.ax.set_ylabel("Count")

        self.canvas = FigureCanvasTkAgg(self.figure, chart_frame)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)

        # ===== Log Viewer =====
        self.log_area = ScrolledText(self, height=12)
        self.log_area.pack(fill=BOTH, expand=True, pady=10)

        # Setup color tags
        for level, color in LOG_COLORS.items():
            self.log_area.tag_config(level, foreground=color, font=("TkDefaultFont", 10, "bold"))

        # ===== Status =====
        self.status = ttk.Label(
            self,
            text="Waiting for log file...",
            bootstyle="secondary"
        )
        self.status.pack(fill=X)
    
    def refresh_logs(self, all_lines):
        self.log_area.delete("1.0", "end")
        for line, level in all_lines:
            if self.should_display(level):
                self.log_area.insert("end", line + "\n")
        self.log_area.see("end")

        
    def toggle_pause(self):
        if not self.paused:
            self.on_pause()
            self.pause_btn.config(text="Resume", bootstyle="success")
            self.status.config(text="Monitoring paused", bootstyle="warning")
        else:
            self.on_resume()
            self.pause_btn.config(text="Pause", bootstyle="warning")
            self.status.config(text="Monitoring resumed", bootstyle="success")

        self.paused = not self.paused

    def should_display(self, level):
        return self.filters.get(level, False).get()

    def add_log(self, line, level):
        if self.should_display(level):
            # Insert colored log
            self.log_area.insert("end", line + "\n", level)
            self.log_area.see("end")

    def update_count(self, level, value):
        if level in self.count_vars:
            self.count_vars[level].set(str(value))

    def update_chart(self, counts: dict):
        self.ax.clear()
        levels = list(counts.keys())
        values = list(counts.values())

        # Optional: color bars by severity
        colors = [LOG_COLORS.get(lvl, "blue") for lvl in levels]
        self.ax.bar(levels, values, color=colors)
        self.ax.set_title("Log Severity Distribution")
        self.ax.set_ylabel("Count")

        self.canvas.draw_idle()

    def show_alert(self, message):
        self.status.config(text=message, bootstyle="danger")

    def reset_status(self):
        self.status.config(text="Monitoring...", bootstyle="success")
        self.paused = False
        self.pause_btn.config(text="Pause", bootstyle="warning")
