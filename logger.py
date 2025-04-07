# logger.py
import os
from datetime import datetime

LOG_FILE = "anonymization_log.txt"

def log_change(file_name, original, replacement, label):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] File: {file_name} | Type: {label} | Replaced: '{original}' -> '{replacement}'\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(log_entry)
