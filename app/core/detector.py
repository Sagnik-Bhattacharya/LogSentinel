# app/core/detector.py
from utils.constants import ALERT_THRESHOLDS

class Detector:
    def __init__(self):
        self.reset()

    def reset(self):
        self.counts = {level: 0 for level in ALERT_THRESHOLDS}

    def process(self, level: str):
        if level in self.counts:
            self.counts[level] += 1

            if self.counts[level] >= ALERT_THRESHOLDS[level]:
                return {
                    "level": level,
                    "count": self.counts[level],
                    "message": f"{level} threshold exceeded"
                }
        return None
