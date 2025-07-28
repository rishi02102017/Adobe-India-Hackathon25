import json
import fitz
import re
import os
from typing import List, Dict, Any

class OutlineExtractor:
    def __init__(self):
        self.publisher_names = {
            'wiley', 'elsevier', 'springer', 'taylor', 'francis', 'sage', 'emerald', 
            'blackwell', 'oxford', 'cambridge', 'mit', 'ieee', 'acm', 'ssrn', 'arxiv',
            'biorxiv', 'medrxiv', 'chemrxiv', 'authorea', 'research square', 'sciety',
            'prereview', 'review commons', 'asapbio', 'elife', 'reseach square'
        }
        
        self.author_indicators = [
            'liu jingyi', 'yang heng', 'chu jingli', 'andrea zini', 'beate weyland',
            'uwe flick', 'ernst von kardorff', 'ines steinke', 'werner meinefeld',
            'jo reichertz', 'hans merkens', 'udo kelle', 'christian erzberger',
            'stephan wolff', 'christel hopf', 'hubert knoblauch', 'alessia bartolini',
            'federico batini', 'mina de santis', 'marco milella', 'pierluigi malavasi'
        ]
        
        self.heading_patterns = {
            'h1': [
                r'^(?:\d+\.)?\s*([A-Z][A-Z\s]{3,50})$',
                r'^(?:\d+\.)?\s*([A-Z][a-z\s]{4,100})$',
                r'^(?:Chapter|Section|Part)\s+\d+[:\s]+([A-Z][A-Za-z\s]{4,100})$',
                r'^([A-Z][A-Za-z\s]{4,100})\s*$'
            ],
            'h2': [
                r'^(?:\d+\.\d+)?\s*([A-Z][A-Z\s]{3,50})$',
                r'^(?:\d+\.\d+)?\s*([A-Z][a-z\s]{4,100})$',
                r'^(?:Subsection|Subchapter)\s+\d+[:\s]+([A-Z][A-Za-z\s]{4,100})$'
            ],
            'h3': [
                r'^(?:\d+\.\d+\.\d+)?\s*([A-Z][A-Z\s]{3,50})$',
                r'^(?:\d+\.\d+\.\d+)?\s*([A-Z][a-z\s]{4,100})$'
            ]
        }
        
    def _is_publisher_name(self, text: str) -> bool:
        text_lower = text.lower().strip()
        return text_lower in self.publisher_names
    
    def _is_author_name(self, text: str) -> bool:
        text_lower = text.lower().strip()
        for author in self.author_indicators:
            if author in text_lower or text_lower in author:
                return True
        return False
    
    def _is_valid_heading(self, text: str) -> bool:
        if not text or len(text) < 4:
            return False
            
        if self._is_publisher_name(text):
            return False
            
        if self._is_author_name(text):
            return False
            
        if len(text) > 150:
            return False
            
        if re.match(r'^\d+$', text):
            return False
            
        if re.match(r'^[A-Z\s]{2,}$', text) and len(text) < 8:
            return False
            
        if re.match(r'^[A-Z][a-z]+\s+[A-Z][a-z]+$', text):
            return False
            
        return True
    
    def _classify_heading(self, line: str) -> str:
        line = line.strip()
        
        if not self._is_valid_heading(line):
            return None
        
        for level, patterns in self.heading_patterns.items():
            for pattern in patterns:
                if re.match(pattern, line):
                    return level.upper()
        
        return None
    
    def extract_outline(self, pdf_path: str) -> Dict[str, Any]:
        doc = fitz.open(pdf_path)
        outline = []
        
        title = doc.metadata.get('title', '')
        if not title:
            title = os.path.basename(pdf_path).replace('.pdf', '')
        
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text()
            lines = text.split('\n')
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                    
                heading_level = self._classify_heading(line)
                if heading_level:
                    outline.append({
                        "level": heading_level,
                        "text": line,
                        "page": page_num + 1
                    })
        
        doc.close()
        
        return {
            "title": title,
            "outline": outline
        }

def extract_outline_from_pdf(pdf_path: str) -> Dict[str, Any]:
    extractor = OutlineExtractor()
    return extractor.extract_outline(pdf_path)

if __name__ == "__main__":
    pdf_path = "input/e01_978-3-499-55628-9_01_006298746.pdf"
    if os.path.exists(pdf_path):
        outline = extract_outline_from_pdf(pdf_path)
        print(json.dumps(outline, indent=2, ensure_ascii=False)) 