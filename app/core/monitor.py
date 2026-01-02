# # app/core/monitor.py
# import time
# from utils.constants import POLL_INTERVAL

# class LogMonitor:
#     def __init__(self, filepath, on_new_line):
#         self.filepath = filepath
#         self.on_new_line = on_new_line
#         self.running = False
#         self.paused = False

#     def start(self):
#         self.running = True
#         with open(self.filepath, "r") as file:
#             file.seek(0, 2)  # move to end of file

#             while self.running:
#                 if self.paused:
#                     time.sleep(POLL_INTERVAL)
#                     continue

#                 line = file.readline()
#                 if line:
#                     self.on_new_line(line.strip())
#                 else:
#                     time.sleep(POLL_INTERVAL)

#     def pause(self):
#         self.paused = True

#     def resume(self):
#         self.paused = False

#     def stop(self):
#         self.running = False

import time


class LogMonitor:
    def __init__(self, filepath, callback):
        self.filepath = filepath
        self.callback = callback
        self.running = True
        self.paused = False

    def stop(self):
        self.running = False

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def start(self):
        with open(self.filepath, "r") as file:

            # Load last 50 lines (history)
            lines = file.readlines()
            for line in lines[-50:]:
                self.callback(line.strip())

            # Follow file for new logs
            while self.running:
                if self.paused:
                    time.sleep(0.5)
                    continue

                line = file.readline()
                if not line:
                    time.sleep(0.3)
                    continue

                self.callback(line.strip())
