# app/gui/file_selector.py
import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class FileSelector(ttk.Frame):
    def __init__(self, master, on_file_selected):
        super().__init__(master)
        self.on_file_selected = on_file_selected
        self.pack(fill=X, padx=10, pady=5)

        self.label = ttk.Label(self, text="No file selected", bootstyle="secondary")
        self.label.pack(side=LEFT, padx=5)

        self.button = ttk.Button(
            self,
            text="Select Log File",
            bootstyle="primary",
            command=self.open_file_dialog
        )
        self.button.pack(side=RIGHT)

    def open_file_dialog(self):
        file_paths = filedialog.askopenfilenames(
            title="Select log files",
            filetypes=[("Log files", "*.log"), ("All files", "*.*")]
        )

        if file_paths:
            self.label.config(text=f"{len(file_paths)} files selected")
            self.on_file_selected(file_paths)
