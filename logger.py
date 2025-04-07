# logger.py
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='anonymization_report.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_change(file, original, replacement, label):
    logging.info(f"File: {file} | {label} | Original: {original} | Replacement: {replacement}")
