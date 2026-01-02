import re

LOG_PATTERNS = [
    # Full timestamped logs
    re.compile(
        r'(?P<timestamp>\d{4}-\d{2}-\d{2} [\d:]+)\s+\[(?P<level>INFO|WARNING|ERROR|CRITICAL)\]\s+(?P<message>.+)'
    ),
    # Simple logs: [LEVEL] message
    re.compile(
        r'\[(?P<level>INFO|WARNING|ERROR|CRITICAL)\]\s+(?P<message>.+)'
    ),
    # Plain logs: LEVEL message
    re.compile(
        r'(?P<level>INFO|WARNING|ERROR|CRITICAL)\s+(?P<message>.+)'
    )
]


def parse_log_line(line: str):
    for pattern in LOG_PATTERNS:
        match = pattern.search(line)
        if match:
            data = match.groupdict()
            data.setdefault("timestamp", "")
            return data
    return None
