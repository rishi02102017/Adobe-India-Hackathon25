# Adobe India Hackathon 2025 - "Connecting the Dots Through Docs"
## Complete Solution: Round 1A + Round 1B

This repository contains a comprehensive solution for the Adobe India Hackathon 2025, implementing both Round 1A (PDF Outline Extraction) and Round 1B (Persona-Driven Document Intelligence) challenges. Our solution demonstrates advanced document processing capabilities with robust multilingual support and intelligent content analysis.

---

## 🎯 Challenge Overview

### Round 1A: Understand Your Document
**Theme**: Connecting the Dots Through Docs

Extract structured outlines from PDF documents with:
- Document Title extraction
- Hierarchical heading detection (H1, H2, H3)
- Page number mapping
- Multilingual support (Assamese, Chinese, English, Italian)

### Round 1B: Persona-Driven Document Intelligence  
**Theme**: Connect What Matters — For the User Who Matters

Build an intelligent document analyst that:
- Processes 3-10 related PDFs simultaneously
- Extracts and prioritizes relevant sections based on persona
- Performs granular sub-section analysis
- Delivers personalized content recommendations

---

## 🏗️ Complete Solution Architecture

```
Challenge_1A/
├── input/                                    # Input directory containing PDF documents
│   ├── e01_978-3-499-55628-9_01_006298746.pdf  # English PDF document
│   ├── file02.pdf                             # Additional PDF document
│   ├── Zini+Weyland+2025+Atti+SIPED+Perugia.pdf # Italian PDF document
│   └── 科技期刊与预印本平台协同发展路径与策略研究.pdf # Chinese PDF document
├── output/                                  # Output directory for extracted outlines
│   ├── e01_978-3-499-55628-9_01_006298746.json # JSON outline for English PDF
│   ├── file02.json                            # JSON outline for file02.pdf
│   ├── Zini+Weyland+2025+Atti+SIPED+Perugia.json # JSON outline for Italian PDF
│   └── 科技期刊与预印本平台协同发展路径与策略研究.json # JSON outline for Chinese PDF
├── multilingual_outline_extractor.py        # Main Python script for outline extraction
├── requirements.txt                         # Python dependencies
├── Dockerfile                              # Container configuration
├── .gitignore                              # Git ignore file
└── README.md                               # Project documentation

Challenge_1b/
├── input/                                    # Input directory
│   ├── *.pdf                                # PDF documents (any language)
│   ├── persona_job_input.json              # Persona configuration (Round 1B)
│   └── ankuran_outline.json                # Pre-existing outline (optional)
├── output/                                  # Output directory
│   ├── *.json                              # Round 1A: Individual PDF outlines
│   └── round1b_output.json                 # Round 1B: Complete analysis
├── round1a_main.py                         # Round 1A: Main execution script
├── round1b_main.py                         # Round 1B: Main execution script
├── outline_extractor.py                    # PDF outline extraction (Round 1A)
├── content_extractor.py                    # Content mapping (Round 1B)
├── relevance_ranker.py                     # Persona-driven ranking (Round 1B)
├── requirements.txt                        # Python dependencies
├── Dockerfile                              # Container configuration
├── approach_explanation.md                 # Round 1B methodology
└── README.md                               # This comprehensive guide
```

---

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.9+
- Docker (for containerized execution)
- 8GB RAM, 8 CPUs (as per hackathon specs)

### Local Development Setup

```bash
# Clone the repository
git clone <repository-url>
cd Challenge_1B

# Install dependencies
pip install -r requirements.txt

# Run Round 1A (Single PDF Outline Extraction)
python3 round1a_main.py

# Run Round 1B (Multi-PDF Persona Analysis)
python3 round1b_main.py
```

### Docker Execution (Hackathon Submission)

```bash
# Build the Docker image
docker build --platform linux/amd64 -t adobe-hackathon-2025:latest .

# Run Round 1A
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  adobe-hackathon-2025:latest python3 round1a_main.py

# Run Round 1B
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  adobe-hackathon-2025:latest python3 round1b_main.py
```

---

## 📋 Round 1A: PDF Outline Extraction

### Problem Statement
Extract structured outlines from PDF documents (up to 50 pages) with:
- Document title identification
- Hierarchical heading detection (H1, H2, H3)
- Page number mapping
- Multilingual support

### Technical Implementation

#### Core Components
1. **PDF Processing**: PyMuPDF for text extraction
2. **Heading Detection**: Advanced regex patterns for H1, H2, H3 classification
3. **Multilingual Support**: Language-agnostic processing pipeline
4. **Quality Filtering**: Publisher name and author filtering

#### Key Features
- **Generic Design**: No hardcoded headings or file-specific logic
- **Robust Detection**: Advanced regex patterns with comprehensive filtering
- **Performance Optimized**: ≤10 seconds for 50-page documents
- **Error Handling**: Graceful handling of malformed PDFs

#### Sample Output (Round 1A)
```json
{
  "title": "Research Paper on Neural Networks",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "Background", "page": 2 },
    { "level": "H3", "text": "Previous Work", "page": 3 },
    { "level": "H2", "text": "Methodology", "page": 4 },
    { "level": "H3", "text": "Data Collection", "page": 5 }
  ]
}
```

---

## 🧠 Round 1B: Persona-Driven Document Intelligence

### Problem Statement
Build an intelligent document analyst that processes multiple PDFs and extracts relevant content based on:
- Persona definition (e.g., "PhD Researcher in Computational Biology")
- Job-to-be-done (e.g., "Prepare comprehensive literature review")
- Document collection (3-10 related PDFs)

### Technical Implementation

#### Core Components
1. **OutlineExtractor**: Extracts document structure from multiple PDFs
2. **ContentExtractor**: Maps headings to full content sections
3. **RelevanceRanker**: Persona-driven content ranking and analysis
4. **Round1BSolution**: Complete pipeline orchestration

#### Advanced Features
- **Multi-PDF Processing**: Simultaneous processing of 3-10 documents
- **Persona-Driven Analysis**: Customizable relevance scoring
- **Sub-Section Analysis**: Granular content breakdown
- **Domain-Specific Keywords**: Academic, business, and education domains
- **Quality Assessment**: Content filtering and validation

#### Sample Output (Round 1B)
```json
{
  "metadata": {
    "input_documents": ["research1.pdf", "research2.pdf", "research3.pdf"],
    "persona": "PhD Researcher in Computational Biology",
    "job_to_be_done": "Prepare comprehensive literature review focusing on methodologies",
    "processing_timestamp": "2025-01-XX...",
    "total_documents_processed": 3,
    "total_sections_found": 45,
    "total_sub_sections_analyzed": 120
  },
  "extracted_sections": [
    {
      "document": "Neural Networks for Drug Discovery",
      "page_number": 5,
      "section_title": "Methodology",
      "importance_rank": 8.5,
      "level": "H2",
      "content": "Our approach utilizes graph neural networks..."
    }
  ],
  "sub_section_analysis": [
    {
      "document": "Neural Networks for Drug Discovery",
      "page_number": 5,
      "refined_text": "The graph neural network architecture consists of...",
      "importance_rank": 7.2,
      "parent_section": "Methodology"
    }
  ]
}
```

---

## 🌍 Multilingual Support

Our solution demonstrates exceptional multilingual capability:

### Supported Languages
- **Assamese**: Educational textbook content (85MB, complex structure)
- **Chinese**: Research papers on academic publishing (1.0MB, 9 pages)
- **English**: Academic research documents (162KB, 7 pages)
- **Italian**: Academic conference proceedings (2.8MB, 10 pages)

### Language-Agnostic Processing
- **Generic Regex Patterns**: Work across different scripts and languages
- **Unicode Support**: Full UTF-8 encoding support
- **Cultural Adaptation**: Language-specific heading patterns
- **Quality Filtering**: Publisher and author name detection across languages

---

## ⚡ Performance & Compliance

### Round 1A Constraints
- ✅ **Execution Time**: ≤10 seconds for 50-page documents
- ✅ **Model Size**: ≤200MB (PyMuPDF only)
- ✅ **Network**: No internet access required
- ✅ **Architecture**: CPU-only (amd64)

### Round 1B Constraints
- ✅ **Execution Time**: ≤60 seconds for 3-5 documents
- ✅ **Model Size**: ≤1GB (minimal dependencies)
- ✅ **Network**: No internet access required
- ✅ **Architecture**: CPU-only (amd64)

### Performance Optimizations
- **Parallel Processing**: Multi-threaded PDF processing
- **Memory Management**: Efficient text extraction and filtering
- **Caching**: Optimized regex pattern matching
- **Error Recovery**: Graceful handling of corrupted PDFs

---

## 🎯 Scoring Criteria Excellence

### Round 1A Scoring (45 points max)
- **Heading Detection Accuracy (25 points)**: Advanced regex patterns with comprehensive filtering
- **Performance Compliance (10 points)**: Optimized for speed and resource usage
- **Multilingual Bonus (10 points)**: Support for 4+ languages with cultural adaptation

### Round 1B Scoring (100 points max)
- **Section Relevance (60 points)**: Sophisticated keyword matching and domain-specific analysis
- **Sub-Section Relevance (40 points)**: Granular content analysis with refined text extraction

---

## 🔧 Technical Deep Dive

### Dependencies
```txt
PyMuPDF==1.23.21          # PDF processing and text extraction
```

### Key Algorithms

#### Heading Detection (Round 1A)
```python
# Advanced regex patterns for H1, H2, H3 classification
heading_patterns = {
    'h1': [r'^(?:\d+\.)?\s*([A-Z][A-Z\s]{3,50})$'],
    'h2': [r'^(?:\d+\.\d+)?\s*([A-Z][A-Z\s]{3,50})$'],
    'h3': [r'^(?:\d+\.\d+\.\d+)?\s*([A-Z][A-Z\s]{3,50})$']
}
```

#### Relevance Ranking (Round 1B)
```python
# Persona-driven scoring algorithm
relevance_score = (keyword_density * 5.0 + text_quality * 2.0 + heading_bonus)
```

### Architecture Benefits
- **Modular Design**: Easy to extend and maintain
- **Scalable**: Handles varying document sizes and counts
- **Robust**: Comprehensive error handling and validation
- **Efficient**: Optimized for hackathon constraints

---

## 📊 Usage Examples

### Academic Research Persona
```json
{
  "persona": "PhD Researcher in Computational Biology",
  "job_to_be_done": "Prepare comprehensive literature review focusing on methodologies, datasets, and performance benchmarks",
  "focus_areas": ["research", "methodology", "data", "analysis"],
  "expertise_level": "expert",
  "domain": "academic_research"
}
```

### Business Analysis Persona
```json
{
  "persona": "Investment Analyst",
  "job_to_be_done": "Analyze revenue trends, R&D investments, and market positioning strategies",
  "focus_areas": ["financial", "market", "strategy", "analysis"],
  "expertise_level": "expert",
  "domain": "business"
}
```

### Educational Persona
```json
{
  "persona": "Undergraduate Chemistry Student",
  "job_to_be_done": "Identify key concepts and mechanisms for exam preparation on reaction kinetics",
  "focus_areas": ["learning", "concepts", "mechanisms", "preparation"],
  "expertise_level": "beginner",
  "domain": "education"
}
```

---

## 🏆 Innovation Highlights

### Technical Innovations
1. **Generic Multilingual Processing**: Language-agnostic pipeline that works across scripts
2. **Advanced Content Filtering**: Publisher and author name detection to improve accuracy
3. **Persona-Driven Intelligence**: Context-aware relevance scoring with domain-specific keywords
4. **Granular Analysis**: Both high-level section ranking and detailed sub-section extraction
5. **Performance Optimization**: Parallel processing and efficient memory management

### Business Value
1. **Scalable Solution**: Works across diverse document types and domains
2. **User-Centric Design**: Personalized content extraction based on specific needs
3. **Multilingual Reach**: Global applicability across different languages and cultures
4. **Production Ready**: Robust error handling and comprehensive validation

---

## 🔍 Testing & Validation

### Test Cases Covered
1. **Academic Research**: 4 research papers on "Graph Neural Networks for Drug Discovery"
2. **Business Analysis**: 3 annual reports from competing tech companies
3. **Educational Content**: 5 chapters from organic chemistry textbooks

### Quality Metrics
- **Accuracy**: High precision and recall in heading detection
- **Performance**: Consistently meets time and memory constraints
- **Robustness**: Handles edge cases and malformed documents
- **Scalability**: Processes varying document sizes efficiently

---

## 📝 Submission Requirements

### Files Included
- ✅ **Dockerfile**: AMD64 compatible with all dependencies
- ✅ **requirements.txt**: Minimal, optimized dependencies
- ✅ **README.md**: Comprehensive documentation (this file)
- ✅ **approach_explanation.md**: Detailed methodology for Round 1B
- ✅ **Source Code**: Complete implementation for both rounds
- ✅ **Sample Outputs**: Example results for validation

### Compliance Checklist
- ✅ **No Network Calls**: Fully offline operation
- ✅ **CPU Only**: No GPU dependencies
- ✅ **Size Constraints**: Model size within limits
- ✅ **Time Constraints**: Execution within specified timeframes
- ✅ **Multilingual**: Bonus points for language support
- ✅ **Generic Design**: No hardcoded or file-specific logic

---

## 👥 Team Information

**Team Members**: Jyotishman, Suvadip and Mehul

**Hackathon**: Adobe India Hackathon 2025
**Track**: Document Intelligence
**Challenge**: "Connecting the Dots Through Docs"

---

## 🚀 Future Enhancements

### Potential Extensions
1. **Additional Languages**: Support for more scripts and languages
2. **Advanced NLP**: Integration with language models for better understanding
3. **Real-time Processing**: Stream processing for large document collections
4. **API Integration**: RESTful API for cloud deployment
5. **User Interface**: Web-based interface for persona configuration

### Scalability Improvements
1. **Distributed Processing**: Multi-node document processing
2. **Caching Layer**: Redis integration for performance optimization
3. **Database Integration**: Persistent storage for analysis results
4. **Monitoring**: Comprehensive logging and performance metrics

---

## 📄 License

This project is developed for the Adobe India Hackathon 2025. All rights reserved.

---

*Ready to connect the dots and build the future of document intelligence!* 🚀 
