# config.py
CUSTOM_PATTERNS = {
    "ssn": r"\d{3}-\d{2}-\d{4}",  # Simple regex for SSNs
    "credit_card": r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b",  # Simple regex for credit cards
    # Add more custom patterns if needed
}
