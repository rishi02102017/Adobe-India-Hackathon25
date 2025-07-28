# Multilingual PDF Outline Extractor

This repository contains a Python-based solution for extracting the **hierarchical structure (Title, H1, H2, H3)** from multilingual PDF documents using OCR and robust heuristics. This solution is designed for the Adobe India Hackathon Round 1A and is fully hackathon-compliant.

---

## 🚀 Problem Statement (Adobe India Hackathon Round 1A)

Given a PDF (up to 50 pages, any language), extract a structured outline including:
- Document Title
- Headings and subheadings (H1, H2, H3)
- Page numbers

The output must be a valid JSON file in the format:
```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Heading", "page": 1 },
    { "level": "H2", "text": "Subheading", "page": 2 },
    { "level": "H3", "text": "Subsubheading", "page": 3 }
  ]
}
```

---

## 🗂 Project Structure

```
multilingual_outline_extractor/
│
├── input/                        # Input folder for PDF files (any language)
├── output/                       # Output folder for extracted outlines
├── multilingual_outline_extractor.py # Main extraction script (multilingual)
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Containerization for hackathon
└── README.md                     # This file
```

---

## ⚙️ System & Docker Requirements

- **CPU-only** (amd64, no GPU)
- **No network/internet calls**
- **Model size ≤ 200MB**
- **All dependencies installed in the container**
- **Docker AMD64 compatible**

### Tesseract Language Packs Used
- English (`eng`)
- Chinese Simplified (`chi_sim`)
- Italian (`ita`)
- Assamese (`asm`)

---

## 📦 Python Setup (for local testing)

Install dependencies using pip:
```bash
pip install -r requirements.txt
```

---

## 🐳 How to Build and Run (Docker)

### 1. Build the Docker image:
```bash
docker build --platform linux/amd64 -t mysolutionname:somerandomidentifier .
```

### 2. Run the solution:
```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none mysolutionname:somerandomidentifier
```

- All PDFs in `/app/input` will be processed.
- For each `filename.pdf`, a `filename.json` will be created in `/app/output`.

---

## 🧠 Approach & Methodology

1. **PDF to Images**:  
   Uses `pdf2image` to convert every page of each PDF into images. **DPI is set to 120 for speed**.

2. **OCR with Tesseract**:  
   Each page image is processed using `pytesseract` with the appropriate language pack (auto-detected from filename or content).

3. **Parallel Processing**:  
   **OCR is run in parallel across pages** using Python's `ThreadPoolExecutor` for maximum speed and to meet the 10-second/50-page requirement.

4. **Heading Detection**:  
   For each OCR-extracted line, robust heuristics are applied:
   - Short lines, numbering patterns, and language-specific tweaks
   - No reliance on font size (per hackathon pro tips)
   - Language-agnostic, but with special handling for Chinese, Italian, Assamese, and English

5. **Heading Level Classification**:  
   - Based on word/character count and numbering
   - Assigns H1, H2, or H3

6. **Output**:  
   - For each PDF, a JSON file is created in the required format
   - Title is the filename (without extension)

7. **Performance**:  
   - Optimized for ≤10 seconds on a 50-page PDF (lower DPI, parallel processing)
   - No network calls, no file-specific logic, no hardcoding

8. **Robustness**:  
   - Handles errors gracefully, logs progress, and validates input/output

---

## 📁 Sample Output (Excerpt)

```json
{
  "title": "Zini+Weyland+2025+Atti+SIPED+Perugia",
  "outline": [
    { "level": "H1", "text": "Introduzione", "page": 1 },
    { "level": "H2", "text": "Contesto Storico", "page": 2 },
    { "level": "H3", "text": "Dettagli", "page": 3 }
  ]
}
```

---

## 📋 Submission Checklist
- [x] Processes all PDFs in `/app/input`, outputs to `/app/output`
- [x] Multilingual: English, Chinese, Italian, Assamese
- [x] No hardcoded logic, no network calls, CPU-only
- [x] Dockerfile AMD64, all dependencies included
- [x] README.md with approach, models/libraries, build/run instructions

---

## 🔗 Libraries Used
- `pytesseract` (OCR)
- `pdf2image` (PDF to image conversion)
- `Pillow` (Image handling)
- `tesseract-ocr` (with language packs)

---

## 🏆 Scoring Criteria Addressed
- **Heading Detection Accuracy**: Robust heuristics, language-specific tweaks
- **Performance**: Fast, efficient, Dockerized, parallelized
- **Multilingual**: Bonus points for supporting multiple languages

---

## ❗ What Not to Do (Compliant)
- No hardcoded headings or file-specific logic
- No API or web calls
- No exceeding runtime/model size constraints

---

## 👨‍💻 Authors
- Team: Jyotishman, Suvadip and Mehul
