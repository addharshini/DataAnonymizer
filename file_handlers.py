# file_handlers.py
import os
import pandas as pd
import json
from docx import Document
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup

def handle_file(file_path, anonymize_func):
    ext = file_path.split('.')[-1].lower()
    if ext == 'csv':
        df = pd.read_csv(file_path)
        anonymized_data = df.applymap(lambda x: anonymize_func(str(x), file_path))
        df.to_csv(file_path, index=False)
    elif ext == 'xlsx':
        df = pd.read_excel(file_path)
        anonymized_data = df.applymap(lambda x: anonymize_func(str(x), file_path))
        df.to_excel(file_path, index=False)
    elif ext == 'json':
        with open(file_path, 'r') as f:
            data = json.load(f)
        anonymized_data = {k: anonymize_func(str(v), file_path) for k, v in data.items()}
        with open(file_path, 'w') as f:
            json.dump(anonymized_data, f, indent=4)
    elif ext == 'txt':
        with open(file_path, 'r') as f:
            text = f.read()
        anonymized_text = anonymize_func(text, file_path)
        with open(file_path, 'w') as f:
            f.write(anonymized_text)
    elif ext == 'pdf':
        with open(file_path, 'rb') as f:
            reader = PdfReader(f)
            text = ''.join([page.extract_text() for page in reader.pages])
        anonymized_text = anonymize_func(text, file_path)
        # Re-save PDF here after modifying text (complex)
    elif ext == 'docx':
        doc = Document(file_path)
        text = ''.join([para.text for para in doc.paragraphs])
        anonymized_text = anonymize_func(text, file_path)
        # Modify docx text here and re-save it
    elif ext == 'html':
        with open(file_path, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
        text = soup.get_text()
        anonymized_text = anonymize_func(text, file_path)
        # Re-save HTML here
    else:
        print(f"Unsupported file type: {ext}")
