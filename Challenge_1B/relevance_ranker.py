import json
import re
from typing import List, Dict, Any, Tuple
from collections import Counter

class RelevanceRanker:
    def __init__(self, persona_data: Dict[str, Any]):
        self.persona = persona_data.get("persona", "")
        self.job = persona_data.get("job_to_be_done", "")
        self.focus_areas = persona_data.get("focus_areas", [])
        self.expertise_level = persona_data.get("expertise_level", "intermediate")
        self.domain = persona_data.get("domain", "general")
        
        self.domain_keywords = self._get_domain_keywords()
        self.keywords = self._extract_keywords()
        
    def _extract_keywords(self) -> List[str]:
        keywords = []
        
        keywords.extend(self.focus_areas)
        
        persona_words = re.findall(r'\b\w+\b', self.persona.lower())
        keywords.extend([word for word in persona_words if len(word) > 3])
        
        job_words = re.findall(r'\b\w+\b', self.job.lower())
        keywords.extend([word for word in job_words if len(word) > 3])
        
        keywords.extend(self.domain_keywords)
        
        return list(set(keywords))
    
    def _get_domain_keywords(self) -> List[str]:
        if self.domain == "academic_research":
            return [
                "research", "study", "analysis", "methodology", "results", "conclusion",
                "data", "dataset", "benchmark", "performance", "evaluation", "experiment",
                "method", "approach", "technique", "algorithm", "model", "framework",
                "literature", "review", "survey", "comparison", "assessment", "validation"
            ]
        elif self.domain == "business":
            return [
                "business", "market", "strategy", "financial", "revenue", "investment",
                "analysis", "report", "performance", "growth", "trend", "forecast"
            ]
        elif self.domain == "education":
            return [
                "learning", "education", "study", "concept", "theory", "practice",
                "curriculum", "teaching", "pedagogy", "assessment", "evaluation"
            ]
        else:
            return ["analysis", "study", "research", "method", "approach"]
    
    def _calculate_text_quality(self, text: str) -> float:
        if not text:
            return 0.0
        
        words = text.split()
        if len(words) < 10:
            return 0.1
        
        sentences = re.split(r'[.!?]+', text)
        avg_sentence_length = len(words) / len(sentences) if sentences else 0
        
        if avg_sentence_length < 5 or avg_sentence_length > 50:
            return 0.3
        
        return 1.0
    
    def _calculate_keyword_density(self, text: str, heading: str = "") -> float:
        if not text:
            return 0.0
        
        text_lower = text.lower()
        heading_lower = heading.lower()
        
        keyword_matches = 0
        total_keywords = len(self.keywords)
        
        for keyword in self.keywords:
            if keyword.lower() in text_lower:
                keyword_matches += 1
            if keyword.lower() in heading_lower:
                keyword_matches += 2
        
        return keyword_matches / total_keywords if total_keywords > 0 else 0.0
    
    def _calculate_content_relevance(self, text: str, heading: str = "") -> float:
        if not text:
            return 0.0
        
        keyword_density = self._calculate_keyword_density(text, heading)
        text_quality = self._calculate_text_quality(text)
        
        heading_bonus = 0.0
        if heading:
            heading_keywords = sum(1 for kw in self.keywords if kw.lower() in heading.lower())
            heading_bonus = min(heading_keywords * 0.5, 2.0)
        
        relevance_score = (keyword_density * 5.0 + text_quality * 2.0 + heading_bonus)
        
        return min(relevance_score, 10.0)
    
    def calculate_relevance_score(self, text: str, heading: str = "") -> float:
        return self._calculate_content_relevance(text, heading)
    
    def rank_sections(self, content_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        ranked_sections = []
        
        for section in content_data.get("content", []):
            content = section.get("content", "")
            heading = section.get("heading", "")
            
            if not content or len(content.strip()) < 50:
                continue
            
            relevance_score = self.calculate_relevance_score(content, heading)
            
            if relevance_score > 0.01:
                ranked_sections.append({
                    "document": content_data.get("title", ""),
                    "page_number": section.get("page", 0),
                    "section_title": heading,
                    "importance_rank": relevance_score,
                    "level": section.get("level", ""),
                    "content": content
                })
        
        ranked_sections.sort(key=lambda x: x["importance_rank"], reverse=True)
        
        return ranked_sections
    
    def extract_sub_sections(self, content: str, max_length: int = 300) -> List[str]:
        if not content:
            return []
        
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
        
        sub_sections = []
        current_section = ""
        
        for paragraph in paragraphs:
            if len(paragraph) < 20:
                continue
                
            if len(current_section + paragraph) < max_length:
                current_section += paragraph + "\n\n"
            else:
                if current_section and len(current_section.strip()) > 50:
                    sub_sections.append(current_section.strip())
                current_section = paragraph + "\n\n"
        
        if current_section and len(current_section.strip()) > 50:
            sub_sections.append(current_section.strip())
        
        return sub_sections
    
    def analyze_sub_sections(self, ranked_sections: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        sub_section_analysis = []
        
        for section in ranked_sections[:15]:
            content = section.get("content", "")
            sub_sections = self.extract_sub_sections(content)
            
            for i, sub_section in enumerate(sub_sections):
                relevance_score = self.calculate_relevance_score(sub_section)
                
                if relevance_score > 0.01:
                    sub_section_analysis.append({
                        "document": section.get("document", ""),
                        "page_number": section.get("page_number", 0),
                        "refined_text": sub_section[:200] + "..." if len(sub_section) > 200 else sub_section,
                        "importance_rank": relevance_score,
                        "parent_section": section.get("section_title", "")
                    })
        
        sub_section_analysis.sort(key=lambda x: x["importance_rank"], reverse=True)
        
        return sub_section_analysis[:25]

def rank_content_for_persona(content_data: Dict[str, Any], persona_data: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    ranker = RelevanceRanker(persona_data)
    
    ranked_sections = ranker.rank_sections(content_data)
    sub_section_analysis = ranker.analyze_sub_sections(ranked_sections)
    
    return ranked_sections, sub_section_analysis 