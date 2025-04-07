# Data Anonymizer Tool

## Features
- Anonymize files (CSV, Excel, PDF, DOCX, HTML, TXT, JSON)
- Detects SSNs, credit cards, names, dates, orgs, etc.
- GUI and CLI modes
- Logging with timestamp

## Setup
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

## Run
**GUI Mode**
```bash
python main.py
```

**CLI Mode**
```bash
python main.py --cli --file sample_data/sample.txt
```

## Packaging (optional)
```bash
pyinstaller --onefile --windowed main.py
```
