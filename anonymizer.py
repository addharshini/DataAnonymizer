import re
from faker import Faker
from config import CUSTOM_PATTERNS
from logger import log_change
from file_handlers import handle_file, handle_pdf, handle_docx
import sys

# Initialize Faker
fake = Faker()

# Function to replace matched text with fake data
def replace_with_fake(match, label):
    """
    Replace the matched text with corresponding fake data.
    """
    if label == "ssn":
        return fake.ssn()
    elif label == "credit_card":
        return fake.credit_card_number()
    elif label == "name":
        return fake.name()
    elif label == "address":
        return fake.address()
    elif label == "date":
        return fake.date()
    else:
        return match.group(0)  # Return the original match if no rule matches

# Anonymize text while maintaining structure
def anonymize_text(text, file):
    """
    Anonymize sensitive data in the text while maintaining the structure.
    """
    # For each type of sensitive data (defined in CUSTOM_PATTERNS)
    for label, pattern in CUSTOM_PATTERNS.items():
        # Iterate through all matches of the pattern in the text
        for match in re.finditer(pattern, text):
            # Replace the matched text with fake data
            replacement = replace_with_fake(match, label)
            # Log the replacement
            log_change(file, match.group(0), replacement, label)
            # Replace the match in the text
            text = text.replace(match.group(0), replacement)
    return text

# CLI or Streamlit
if __name__ == "__main__":
    if len(sys.argv) > 1:
        # CLI mode
        file_path = sys.argv[1]
        print(f"🔍 Processing {file_path}...")

        # Handle different file types based on extension
        if file_path.lower().endswith(".pdf"):
            handle_pdf(file_path, anonymize_text)
        elif file_path.lower().endswith(".docx"):
            handle_docx(file_path, anonymize_text)
        elif file_path.lower().endswith(".txt"):
            handle_file(file_path, anonymize_text)
        else:
            print("❌ Unsupported file type. Please upload a .txt, .pdf, or .docx file.")
            sys.exit(1)
        
        print("✅ Anonymization complete. Check output folder and anonymization_log.txt.")
    else:
        # Streamlit mode
        import streamlit as st

        st.title("🛡️ Data Anonymizer")

        option = st.radio("Choose input method:", ("Upload .txt file", "Upload .pdf file", "Upload .docx file", "Enter text manually"))

        input_text = ""
        source_label = "user_input"

        if option == "Upload .txt file":
            uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])
            if uploaded_file is not None:
                input_text = uploaded_file.read().decode("utf-8")
                source_label = uploaded_file.name
        elif option == "Upload .pdf file":
            uploaded_file = st.file_uploader("Upload a .pdf file", type=["pdf"])
            if uploaded_file is not None:
                input_text = handle_pdf(uploaded_file, anonymize_text)  # Passing anonymizer_func here
                source_label = uploaded_file.name
        elif option == "Upload .docx file":
            uploaded_file = st.file_uploader("Upload a .docx file", type=["docx"])
            if uploaded_file is not None:
                input_text = handle_docx(uploaded_file, anonymize_text)  # Passing anonymizer_func here
                source_label = uploaded_file.name
        else:
            input_text = st.text_area("Enter text to anonymize")

        if input_text:
            st.subheader("🔐 Anonymized Output")
            anonymized = anonymize_text(input_text, source_label)
            st.text_area("Output", anonymized, height=300)
            st.download_button("💾 Download Anonymized Text", data=anonymized, file_name="anonymized.txt")
