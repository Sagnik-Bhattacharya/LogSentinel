# app/storage/database.py
import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path("logsentinel.db")


class AlertDatabase:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self._create_table()

    def _create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                level TEXT NOT NULL,
                message TEXT NOT NULL,
                count INTEGER NOT NULL
            )
        """)
        self.conn.commit()

    def save_alert(self, level: str, message: str, count: int):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO alerts (timestamp, level, message, count)
            VALUES (?, ?, ?, ?)
        """, (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            level,
            message,
            count
        ))
        self.conn.commit()

    def get_alerts(self, limit=100):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT timestamp, level, message, count
            FROM alerts
            ORDER BY id DESC
            LIMIT ?
        """, (limit,))
        return cursor.fetchall()

    def close(self):
        self.conn.close()
