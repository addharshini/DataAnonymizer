# config.py
import re

# Custom regex patterns for sensitive data
CUSTOM_PATTERNS = {
    "ssn": r"\b\d{3}-\d{2}-\d{4}\b",  # Match SSNs like 123-45-6789
    "credit_card": r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b",  # Match credit card numbers
    "name": r"\b[A-Z][a-z]*\b",  # Match capitalized words (simple approach)
    "address": r"\b\d+\s[A-Za-z]+\s[A-Za-z]+\b",  # Match simple address-like patterns
    "date": r"\b\d{4}-\d{2}-\d{2}\b",  # Match dates like 2021-01-01
}
