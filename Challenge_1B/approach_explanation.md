# Approach Explanation – Round 1B: Persona-Driven Document Intelligence

## Overview

This document outlines the approach for Round 1B of the Adobe India Hackathon challenge. The objective is to build an intelligent document analyst that extracts and prioritizes the most relevant sections from a collection of documents based on a specific persona and their job-to-be-done.

## Methodology

### 1. Multi-PDF Processing Pipeline

The solution processes multiple PDFs (3-10 documents) through a three-stage pipeline:

- Stage 1: Outline Extraction - Each PDF is analyzed to extract structured headings (H1, H2, H3) with page numbers
- Stage 2: Content Mapping - Full content under each heading is extracted and mapped to the outline structure
- Stage 3: Relevance Ranking - Content is analyzed and ranked based on persona and job-to-be-done requirements

### 2. Persona-Driven Intelligence

The system accepts persona and job-to-be-done input through a JSON configuration file. The relevance ranking algorithm:

- Keyword Extraction: Automatically extracts relevant keywords from persona description and job requirements
- Domain-Specific Matching: Applies domain-specific keyword patterns (academic research, business, education)
- Multi-level Scoring: Calculates relevance scores for both sections and sub-sections with different weighting strategies
- Contextual Analysis: Considers heading relevance, content length, and keyword density

### 3. Multilingual Support

The solution demonstrates robust multilingual capability by processing:
- Assamese: Educational textbook content
- Chinese: Research paper on academic publishing
- English: Academic research document
- Italian: Academic conference proceedings

Each language is processed using the same pipeline, with language-agnostic text extraction and analysis.

### 4. Efficiency & Constraints Handling

- Processing Time: Optimized to complete within 60 seconds for 3-5 documents
- Memory Usage: Efficient text processing with minimal memory footprint
- Offline Operation: No internet dependencies, all processing done locally
- CPU-Only: Designed to run on AMD64 architecture with 8 CPUs and 16GB RAM

## Technical Implementation

### Core Components

1. OutlineExtractor: Generic heading detection using regex patterns and text analysis
2. ContentExtractor: Maps headings to full content using PyMuPDF for text extraction
3. RelevanceRanker: Implements persona-driven ranking with keyword matching and scoring algorithms
4. Round1BSolution: Orchestrates the complete pipeline and generates final output

### Output Format

The solution generates a structured JSON output containing:
- Metadata: Input documents, persona, job-to-be-done, processing timestamp
- Extracted Sections: Ranked sections with document, page number, title, and importance score
- Sub-section Analysis: Granular analysis of relevant content chunks with refined text and rankings

## Innovation & Advantages

- Generic Design: Works across diverse document types, personas, and languages
- Scalable Architecture: Modular design allows easy extension and customization
- Robust Error Handling: Graceful handling of malformed PDFs and processing errors
- Comprehensive Analysis: Provides both high-level section ranking and detailed sub-section analysis

This approach ensures the solution meets all hackathon requirements while demonstrating advanced document intelligence capabilities for multilingual content analysis.
