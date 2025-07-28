import json
import fitz
import os
import re
from typing import List, Dict, Any

class ContentExtractor:
    def __init__(self):
        pass
    
    def _clean_text(self, text: str) -> str:
        if not text:
            return ""
        
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s\.\,\;\:\!\?\-\(\)\[\]\{\}]', '', text)
        text = text.strip()
        
        return text
    
    def _is_quality_content(self, text: str) -> bool:
        if not text or len(text) < 100:
            return False
        
        words = text.split()
        if len(words) < 20:
            return False
        
        sentences = re.split(r'[.!?]+', text)
        if len(sentences) < 2:
            return False
        
        return True
    
    def extract_content_for_outline(self, pdf_path: str, outline_data: Dict[str, Any]) -> Dict[str, Any]:
        doc = fitz.open(pdf_path)
        pdf_text = []
        
        for page in doc:
            text = page.get_text()
            cleaned_text = self._clean_text(text)
            pdf_text.append(cleaned_text)
        
        doc.close()
        
        final_content = {
            "title": outline_data["title"],
            "content": []
        }
        
        for heading in outline_data["outline"]:
            page_num = heading["page"] - 1
            if page_num < len(pdf_text):
                text = pdf_text[page_num]
                
                if self._is_quality_content(text):
                    final_content["content"].append({
                        "level": heading["level"],
                        "heading": heading["text"],
                        "page": heading["page"],
                        "content": text
                    })
        
        return final_content

def extract_content_from_pdf_with_outline(pdf_path: str, outline_data: Dict[str, Any]) -> Dict[str, Any]:
    extractor = ContentExtractor()
    return extractor.extract_content_for_outline(pdf_path, outline_data)

if __name__ == "__main__":
    pdf_path = "input/Ankuran (Pratham Bhag) (Language (L1))_Class 1_Assamese medium.pdf"
    outline_path = "input/ankuran_outline.json"
    
    if os.path.exists(pdf_path) and os.path.exists(outline_path):
        with open(outline_path, "r", encoding="utf-8") as f:
            outline_data = json.load(f)
        content = extract_content_from_pdf_with_outline(pdf_path, outline_data)
        print(json.dumps(content, indent=2, ensure_ascii=False)) 