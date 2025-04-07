# file_handlers.py
import os
import pandas as pd
import docx
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

def handle_file(file_path, anonymize_fn):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
        anonymized = anonymize_fn(text, file_path)
        with open(f"anonymized_{os.path.basename(file_path)}", "w", encoding="utf-8") as f:
            f.write(anonymized)

    elif ext in [".xls", ".xlsx"]:
        df = pd.read_excel(file_path)
        for col in df.select_dtypes(include=["object"]):
            df[col] = df[col].astype(str).apply(lambda x: anonymize_fn(x, file_path))
        df.to_excel(f"anonymized_{os.path.basename(file_path)}", index=False)

    elif ext == ".pdf":
        reader = PdfReader(file_path)
        text = "\n".join([page.extract_text() or "" for page in reader.pages])
        anonymized = anonymize_fn(text, file_path)
        with open(f"anonymized_{os.path.basename(file_path)}.txt", "w", encoding="utf-8") as f:
            f.write(anonymized)

    elif ext == ".docx":
        doc = docx.Document(file_path)
        full_text = "\n".join([para.text for para in doc.paragraphs])
        anonymized = anonymize_fn(full_text, file_path)
        with open(f"anonymized_{os.path.basename(file_path)}.txt", "w", encoding="utf-8") as f:
            f.write(anonymized)

    elif ext == ".html":
        with open(file_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
        text = soup.get_text()
        anonymized = anonymize_fn(text, file_path)
        with open(f"anonymized_{os.path.basename(file_path)}.txt", "w", encoding="utf-8") as f:
            f.write(anonymized)

    else:
        raise ValueError(f"Unsupported file type: {ext}")
