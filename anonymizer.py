# anonymizer.py
import re
import os
import spacy
from faker import Faker
from config import CUSTOM_PATTERNS
from logger import log_change

fake = Faker()
nlp = spacy.load("en_core_web_sm")

# Apply regex and NER-based replacements
def anonymize_text(text, file):
    for label, pattern in CUSTOM_PATTERNS.items():
        matches = re.findall(pattern, text)
        for match in matches:
            replacement = fake.ssn() if label == "ssn" else fake.credit_card_number()
            text = text.replace(match, replacement)
            log_change(file, match, replacement, label)

    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "GPE", "ORG", "DATE"]:
            replacement = {
                "PERSON": fake.name(),
                "GPE": fake.city(),
                "ORG": fake.company(),
                "DATE": fake.date()
            }[ent.label_]
            text = text.replace(ent.text, replacement)
            log_change(file, ent.text, replacement, ent.label_)

    return text

# Entry point for any file type
def anonymize_file(file_path):
    from file_handlers import handle_file
    handle_file(file_path, anonymize_text)

# Streamlit support for .txt or text input
if __name__ == "__main__":
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
        st.subheader("Anonymized Output")
        anonymized = anonymize_text(input_text, source_label)
        st.text_area("Output", anonymized, height=300)

        st.download_button("Download Anonymized Text", data=anonymized, file_name="anonymized.txt")
