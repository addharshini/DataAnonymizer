# Privacy Anonymizer

This project is a Python-based tool for anonymizing sensitive information in text, PDF, DOCX, and plain text files. It uses regular expressions to identify and replace sensitive data (e.g., SSNs, credit card numbers, names, and addresses) with fake data generated using the Faker library.

## Features

- Anonymize sensitive data in text files (.txt, .pdf, .docx).
- Replace real information like SSNs, credit card numbers, and names with randomly generated fake data.
- Support both CLI (Command Line Interface) and Streamlit Web App for interactive use.
- Log all changes made to files for auditing and reporting.

## Pre-requisites

Make sure you have Python 3.6+ installed. The following Python libraries are required:

- `PyPDF2`: For reading and extracting text from PDF files.
- `python-docx`: For reading DOCX files.
- `Faker`: For generating fake data.
- `streamlit`: For creating the web interface.

## Installation

To install the necessary dependencies, use the `requirements.txt` file:

1. Clone the repository:

    ```bash
    git clone https://github.com/addharshini/PrivacyAnonymizer.git
    cd DataAnonymizer
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

* * *

### 🖼️ UI Preview

<img width="782" height="836" alt="Screenshot 2025-07-16 133446" src="https://github.com/user-attachments/assets/2d1b0325-33a6-4a52-a882-e03a864169d3" />

## Usage

### CLI Mode

1. To anonymize a file via CLI, run the following command:

    ```bash
    python3 anonymizer.py sample.txt
    ```

    Replace `sample.txt` with the path to your file. The anonymized text will be saved in a new file with the prefix `anonymized_`.

2. The changes made during anonymization will be logged in the `anonymization_log.txt` file.

### Streamlit Mode

1. To start the Streamlit application, use the following command:

    ```bash
    python -m streamlit run anonymizer.py
    ```

2. Once the app is running, you can:

    - Upload a `.txt`, `.pdf`, or `.docx` file.
    - Or enter text manually into the app.
    - Anonymized content will be displayed and can be downloaded as a new file.

## How It Works

1. **Text Extraction**: The tool reads the content of the uploaded file (or the manually entered text).
2. **Anonymization**: It applies predefined regular expression patterns to find sensitive data (e.g., SSNs, credit cards, names) and replaces them with fake data.
3. **Logging**: All changes are logged with timestamps to provide an audit trail.
4. **Output**: The anonymized text is displayed in the Streamlit interface or saved as a new file in the case of CLI.

## Supported File Types

- `.txt`
- `.pdf`
- `.docx`

## Dependencies

The following Python libraries are required:

- `PyPDF2`: For PDF text extraction.
- `python-docx`: For DOCX file text extraction.
- `Faker`: For generating fake data.
- `streamlit`: For the web app interface.
* * *


### 📄 License

MIT License © 2025 Divya Dharshini

* * *

### 🤝 Contributions

Pull requests are welcome! For major changes, please open an issue first.

* * *

