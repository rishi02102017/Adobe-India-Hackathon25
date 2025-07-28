# Round 1B: Persona-Driven Document Intelligence
## Adobe India Hackathon 2025 - "Connecting the Dots Through Docs"

This repository contains a complete solution for Round 1B of the Adobe India Hackathon challenge. The system acts as an intelligent document analyst, extracting and prioritizing the most relevant sections from a collection of documents based on a specific persona and their job-to-be-done.

## What This Solution Does

Given:
- Multiple PDFs (3-10 documents in any language)
- Persona definition (e.g., "PhD Researcher in Computational Biology")
- Job-to-be-done (e.g., "Prepare a comprehensive literature review")

This system:
- Extracts structured outlines from all PDFs
- Maps headings to full content
- Ranks sections and sub-sections by relevance to the persona
- Outputs a comprehensive JSON with metadata, ranked sections, and sub-section analysis

## Multilingual Support

The solution demonstrates robust multilingual capability by processing: 
- Assamese: Educational textbook content
- Chinese: Research paper on academic publishing  
- English: Academic research document
- Italian: Academic conference proceedings

## Project Structure

```
multilingual_content_generator/
├── input/
│   ├── *.pdf                    # PDF documents to process
│   ├── persona_job_input.json   # Persona and job configuration
│   └── ankuran_outline.json     # Existing outline (optional)
├── output/
│   └── round1b_output.json      # Final output
├── round1b_main.py              # Main execution script
├── outline_extractor.py         # PDF outline extraction
├── content_extractor.py         # Content mapping
├── relevance_ranker.py          # Persona-driven ranking
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Container configuration
├── approach_explanation.md      # Methodology explanation
└── README.md                    # This file
```

## Quick Start

### 1. Prepare Input Files

Place your PDFs in the `input/` directory and create a persona configuration:

```json
{
  "persona": "PhD Researcher in Computational Biology",
  "job_to_be_done": "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks",
  "focus_areas": ["research", "methodology", "data", "analysis"],
  "expertise_level": "expert",
  "domain": "academic_research"
}
```

### 2. Run Locally

```bash
# Install dependencies
pip install -r requirements.txt

# Run the solution
python3 round1b_main.py
```

### 3. Run with Docker

```bash
# Build the image
docker build --platform linux/amd64 -t round1b-solution:latest .

# Run the container
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  round1b-solution:latest
```

## Output Format

The solution generates a comprehensive JSON output:

```json
{
  "metadata": {
    "input_documents": ["document1.pdf", "document2.pdf"],
    "persona": "PhD Researcher in Computational Biology",
    "job_to_be_done": "Prepare a comprehensive literature review...",
    "processing_timestamp": "2025-01-XX...",
    "total_documents_processed": 4,
    "total_sections_found": 150,
    "total_sub_sections_analyzed": 300
  },
  "extracted_sections": [
    {
      "document": "Research Paper",
      "page_number": 5,
      "section_title": "Methodology",
      "importance_rank": 8.5,
      "level": "H2",
      "content": "Full section content..."
    }
  ],
  "sub_section_analysis": [
    {
      "document": "Research Paper",
      "page_number": 5,
      "refined_text": "Key methodology details...",
      "importance_rank": 7.2,
      "parent_section": "Methodology"
    }
  ]
}
```

## Technical Features

### Core Components

1. OutlineExtractor: Generic heading detection using regex patterns
2. ContentExtractor: Maps headings to full content using PyMuPDF
3. RelevanceRanker: Persona-driven ranking with keyword matching
4. Round1BSolution: Complete pipeline orchestration

### Key Capabilities

- Multi-PDF Processing: Handles 3-10 documents simultaneously
- Multilingual Support: Works with Assamese, Chinese, English, Italian, and more
- Persona-Driven Analysis: Customizable relevance ranking based on user needs
- Efficient Processing: Completes within 60 seconds for 3-5 documents
- Offline Operation: No internet dependencies
- Robust Error Handling: Graceful handling of malformed PDFs

## Hackathon Compliance

### Requirements Met

- Input: Accepts 3-10 PDFs + persona + job-to-be-done
- Output: JSON with metadata, ranked sections, sub-section analysis
- Constraints: CPU-only, ≤1GB model, ≤60s processing, offline operation
- Multilingual: Bonus points for handling multiple languages
- Docker: AMD64 compatible, volume mounting for input/output

### Scoring Criteria

- Section Relevance (60 points): Advanced keyword matching and domain-specific analysis
- Sub-Section Relevance (40 points): Granular content analysis with refined text extraction
- Multilingual Bonus: Support for 4+ languages (Assamese, Chinese, English, Italian)

## Dependencies

- Python 3.9
- PyMuPDF: PDF text extraction and processing
- Standard Library: JSON, regex, datetime, os, glob

## Usage Examples

### Academic Research Persona
```json
{
  "persona": "PhD Researcher in Computational Biology",
  "job_to_be_done": "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks"
}
```

### Business Analysis Persona
```json
{
  "persona": "Investment Analyst",
  "job_to_be_done": "Analyze revenue trends, R&D investments, and market positioning strategies"
}
```

### Educational Persona
```json
{
  "persona": "Undergraduate Chemistry Student",
  "job_to_be_done": "Identify key concepts and mechanisms for exam preparation on reaction kinetics"
}
```

## Innovation Highlights

- Generic Design: Works across diverse document types and domains
- Scalable Architecture: Modular design for easy extension
- Intelligent Ranking: Context-aware relevance scoring
- Comprehensive Analysis: Both high-level and granular content analysis
- Robust Multilingual Support: Language-agnostic processing pipeline

## Authors

- Jyotishman, Suvadip and Mehul
- Developed for Adobe India Hackathon 2025
- Document Intelligence Track
- "Connecting the Dots Through Docs" Challenge

---

Ready to connect the dots and build the future of document intelligence! 