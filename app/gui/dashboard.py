import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter.scrolledtext import ScrolledText
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from utils.constants import LOG_LEVELS

# Updated for a more professional palette
LOG_COLORS = {
    "INFO": "#2ecc71",      # Emerald Green
    "WARNING": "#f1c40f",   # Sunflower Yellow
    "ERROR": "#e74c3c",     # Alizarin Red
    "CRITICAL": "#9b59b6",  # Amethyst Purple
}

class Dashboard(ttk.Frame):
    def __init__(self, master, on_pause, on_resume, on_filter_change):
        super().__init__(master, padding=20)
        self.pack(fill=BOTH, expand=True)

        self.on_pause = on_pause
        self.on_resume = on_resume
        self.on_filter_change = on_filter_change
        self.paused = False

        # --- Layout Containers ---
        self.top_row = ttk.Frame(self)
        self.top_row.pack(fill=X, pady=(0, 10))
        
        # Split top row into Left (Filters/Controls) and Right (Metrics)
        self.left_panel = ttk.Frame(self.top_row)
        self.left_panel.pack(side=LEFT, fill=BOTH, expand=True)
        
        self.right_panel = ttk.Frame(self.top_row)
        self.right_panel.pack(side=RIGHT, fill=BOTH)

        self._init_filters()
        self._init_controls() # Integrated into filter area
        self._init_counters()
        self._init_chart()
        self._init_log_viewer()
        self._init_status()

    # ───────────────── Filters & Controls ───────────────── #

    def _init_filters(self):
        self.filters = {lvl: ttk.BooleanVar(value=True) for lvl in LOG_LEVELS}
        
        filter_frame = ttk.Labelframe(self.left_panel, text=" Global Controls ", padding=15)
        filter_frame.pack(fill=BOTH, expand=True, padx=(0, 10))

        # Checkbuttons
        check_container = ttk.Frame(filter_frame)
        check_container.pack(fill=X, side=TOP)
        
        for level in LOG_LEVELS:
            ttk.Checkbutton(
                check_container,
                text=level,
                variable=self.filters[level],
                bootstyle="round-toggle",
                command=self.on_filter_change
            ).pack(side=LEFT, padx=10)

    def _init_controls(self):
        # Pause Button moved to a more prominent location
        self.pause_btn = ttk.Button(
            self.left_panel,
            text="Pause Stream",
            bootstyle="warning-outline",
            width=15,
            command=self.toggle_pause
        )
        self.pause_btn.pack(side=BOTTOM, anchor=W, pady=(10, 0))

    def should_display(self, level):
        return self.filters[level].get()

    # ───────────────── Counters (Metric Cards) ───────────────── #

    def _init_counters(self):
        self.count_vars = {lvl: ttk.StringVar(value="0") for lvl in LOG_LEVELS}
        
        card_frame = ttk.Frame(self.right_panel)
        card_frame.pack(fill=BOTH)

        for level in LOG_LEVELS:
            # Create a "Card" look
            container = ttk.Frame(card_frame, bootstyle="secondary", padding=1)
            container.pack(side=LEFT, padx=5)
            
            inner = ttk.Frame(container, bootstyle="default", padding=10)
            inner.pack()
            
            ttk.Label(inner, text=level, font=("Helvetica", 8, "bold")).pack()
            ttk.Label(
                inner, 
                textvariable=self.count_vars[level],
                font=("Helvetica", 16, "bold"),
                bootstyle="info"
            ).pack()

    def update_count(self, level, value):
        self.count_vars[level].set(str(value))

    # ───────────────── Logic Passthrough ───────────────── #

    def toggle_pause(self):
        if self.paused:
            self.on_resume()
            self._set_status("Monitoring resumed", "success")
            self.pause_btn.config(text="Pause Stream", bootstyle="warning-outline")
        else:
            self.on_pause()
            self._set_status("Monitoring paused", "warning")
            self.pause_btn.config(text="Resume Stream", bootstyle="success-outline")
        self.paused = not self.paused

    # ───────────────── Chart (Visual Polish) ───────────────── #

    def _init_chart(self):
        frame = ttk.Labelframe(self, text=" Analytics ", padding=10)
        frame.pack(fill=X, pady=10)

        # Matplotlib theme integration
        self.figure = Figure(figsize=(6, 2.5), dpi=100, facecolor='#2b2b2b')
        self.ax = self.figure.add_subplot(111)
        self.ax.set_facecolor('#2b2b2b')
        self.ax.tick_params(colors='white', labelsize=8)
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)
        self.ax.spines['left'].set_color('white')

        self.canvas = FigureCanvasTkAgg(self.figure, frame)
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=True)

    def update_chart(self, counts):
        self.ax.clear()
        levels = list(counts.keys())
        values = list(counts.values())
        colors = [LOG_COLORS.get(lvl, "#ffffff") for lvl in levels]

        bars = self.ax.bar(levels, values, color=colors, width=0.6)
        self.ax.set_title("Log Frequency", color='white', pad=15, fontdict={'fontsize': 10, 'fontweight': 'bold'})
        
        # Add value labels on top of bars
        for bar in bars:
            height = bar.get_height()
            self.ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                        f'{int(height)}', ha='center', va='bottom', color='white', fontsize=8)

        self.canvas.draw_idle()

    # ───────────────── Log Viewer (Modern Console) ───────────────── #

    def _init_log_viewer(self):
        # Darker background for the log area for a modern developer look
        self.log_area = ScrolledText(
            self, 
            height=12, 
            font=("Consolas", 10),
            bg="#1e1e1e", 
            fg="#d4d4d4",
            padx=10,
            pady=10,
            borderwidth=0
        )
        self.log_area.pack(fill=BOTH, expand=True, pady=10)

        for level, color in LOG_COLORS.items():
            self.log_area.tag_config(
                level,
                foreground=color,
                font=("Consolas", 10, "bold")
            )

    def refresh_logs(self, logs):
        self.log_area.config(state=NORMAL)
        self.log_area.delete("1.0", END)
        for line, level in logs:
            if self.should_display(level):
                self.log_area.insert(END, f"[{level}] ", level)
                self.log_area.insert(END, f"{line}\n")
        self.log_area.see(END)
        self.log_area.config(state=DISABLED) # Keep logs read-only

    # ───────────────── Status ───────────────── #

    def _init_status(self):
        self.status_frame = ttk.Frame(self, bootstyle="secondary")
        self.status_frame.pack(fill=X, side=BOTTOM, pady=(5, 0))
        
        self.status = ttk.Label(
            self.status_frame,
            text="● Waiting for log file...",
            bootstyle="inverse-secondary",
            font=("Helvetica", 9)
        )
        self.status.pack(side=LEFT, padx=10, pady=2)

    def _set_status(self, text, style):
        self.status.config(text=f"● {text}", bootstyle=f"inverse-{style}")

    def show_alert(self, message):
        self._set_status(message, "danger")

    def reset_status(self):
        self.paused = False
        self.pause_btn.config(text="Pause Stream", bootstyle="warning-outline")
        self._set_status("Monitoring System Active", "success")