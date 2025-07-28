# Use official Python image
FROM --platform=linux/amd64 python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies for OCR and PDF handling
RUN apt-get update && apt-get install -y \
    poppler-utils \
    tesseract-ocr \
    tesseract-ocr-eng \
    tesseract-ocr-chi-sim \
    tesseract-ocr-ita \
    tesseract-ocr-asm \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set Tesseract language path
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata

# Command to run
CMD ["python3", "multilingual_outline_extractor.py"]
