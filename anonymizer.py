# anonymizer.py
import re
from faker import Faker
from config import CUSTOM_PATTERNS
from logger import log_change
from file_handlers import handle_file
import sys

# Initialize Faker
fake = Faker()

# Anonymization function
def anonymize_text(text, file):
    # Replace sensitive data based on custom regex patterns
    for label, pattern in CUSTOM_PATTERNS.items():
        matches = re.findall(pattern, text)
        for match in matches:
            replacement = fake.ssn() if label == "ssn" else fake.credit_card_number()
            text = text.replace(match, replacement)
            log_change(file, match, replacement, label)

    # Replace entities without using spaCy (basic pattern replacement)
    text = re.sub(r"\b[A-Z][a-z]*\b", lambda x: fake.name(), text)  # Random name replacement
    text = re.sub(r"\b[0-9]{4}-[0-9]{2}-[0-9]{2}\b", lambda x: fake.date(), text)  # Random date replacement
    text = re.sub(r"\b[A-Za-z]+\b", lambda x: fake.city(), text)  # Replace city names

    return text

# CLI or Streamlit
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # CLI mode
        file_path = sys.argv[1]
        print(f"🔍 Processing {file_path}...")
        handle_file(file_path, anonymize_text)
        print("✅ Anonymization complete. Check output folder and anonymization_log.txt.")
    else:
        # Streamlit mode
        import streamlit as st

        st.title("🛡️ Data Anonymizer")

        option = st.radio("Choose input method:", ("Upload .txt file", "Enter text manually"))

        input_text = ""
        source_label = "user_input"

        if option == "Upload .txt file":
            uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
            if uploaded_file is not None:
                input_text = uploaded_file.read().decode("utf-8")
                source_label = uploaded_file.name
        else:
            input_text = st.text_area("Enter text to anonymize")

        if input_text:
            st.subheader("🔐 Anonymized Output")
            anonymized = anonymize_text(input_text, source_label)
            st.text_area("Output", anonymized, height=300)
            st.download_button("💾 Download Anonymized Text", data=anonymized, file_name="anonymized.txt")
