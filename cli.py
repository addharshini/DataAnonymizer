# cli.py
import argparse
import os
import streamlit as st
from anonymizer import anonymize_file

def main():
    parser = argparse.ArgumentParser(description="Data Anonymizer CLI")
    parser.add_argument("--cli", action="store_true", help="Run in CLI mode")
    parser.add_argument("--file", type=str, required=True, help="Path to the file to anonymize")

    args = parser.parse_args()

    if args.cli and args.file:
        file_path = args.file
        if os.path.exists(file_path):
            print(f"Anonymizing file: {file_path}")
            anonymize_file(file_path)
            print(f"Anonymization complete! The file has been saved to: {file_path}")
        else:
            print(f"Error: The file '{file_path}' does not exist.")

def streamlit_app():
    st.title("Data Anonymizer")

    uploaded_file = st.file_uploader("Upload a .txt file", type="txt")
    text_input = st.text_area("Or enter text directly")

    if st.button("Anonymize"):
        if uploaded_file is not None:
            file_content = uploaded_file.read().decode("utf-8")
            st.write("Anonymizing uploaded file...")
            anonymized_content = anonymize_file(file_content)
            st.text_area("Anonymized Text", anonymized_content, height=200)
        elif text_input:
            st.write("Anonymizing entered text...")
            anonymized_content = anonymize_file(text_input)
            st.text_area("Anonymized Text", anonymized_content, height=200)
        else:
            st.error("Please upload a file or enter text to anonymize.")

if __name__ == "__main__":
    mode = st.sidebar.selectbox("Select Mode", ["CLI", "Streamlit"])

    if mode == "CLI":
        main()
    elif mode == "Streamlit":
        streamlit_app()
