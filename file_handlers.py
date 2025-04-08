import PyPDF2
import docx

def handle_file(file_path, anonymizer_func):
    """
    Process and anonymize text from a .txt file.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    
    # Anonymize the text
    anonymized_text = anonymizer_func(text, file_path)
    
    # Write the anonymized content to a new file
    output_file_path = "anonymized_" + file_path
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(anonymized_text)

def handle_pdf(file, anonymizer_func):
    """
    Extract text from a PDF and anonymize it.
    """
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    # Anonymize the text
    return anonymizer_func(text, file.name)

def handle_docx(file, anonymizer_func):
    """
    Extract text from a DOCX file and anonymize it.
    """
    doc = docx.Document(file)
    text = "\n".join([para.text for para in doc.paragraphs])
    
    # Anonymize the text
    return anonymizer_func(text, file.name)
