"""
Round 1B: Persona-Driven Document Intelligence
Adobe India Hackathon 2025

This script processes multiple PDFs, extracts content, and ranks sections/sub-sections
based on a specific persona and job-to-be-done.
"""

import json
import os
import glob
import datetime
from typing import List, Dict, Any
from outline_extractor import extract_outline_from_pdf
from content_extractor import extract_content_from_pdf_with_outline
from relevance_ranker import rank_content_for_persona

class Round1BSolution:
    def __init__(self, input_dir: str = "input", output_dir: str = "output"):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.persona_data = None
        
    def load_persona_data(self, persona_file: str = "persona_job_input.json") -> Dict[str, Any]:
        persona_path = os.path.join(self.input_dir, persona_file)
        
        if os.path.exists(persona_path):
            with open(persona_path, "r", encoding="utf-8") as f:
                self.persona_data = json.load(f)
        else:
            self.persona_data = {
                "persona": "PhD Researcher in Computational Biology",
                "job_to_be_done": "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks",
                "focus_areas": ["research", "methodology", "data", "analysis"],
                "expertise_level": "expert",
                "domain": "academic_research"
            }
        
        return self.persona_data
    
    def get_pdf_files(self) -> List[str]:
        pdf_pattern = os.path.join(self.input_dir, "*.pdf")
        return glob.glob(pdf_pattern)
    
    def process_single_pdf(self, pdf_path: str) -> Dict[str, Any]:
        print(f"Processing: {os.path.basename(pdf_path)}")
        
        outline_data = extract_outline_from_pdf(pdf_path)
        content_data = extract_content_from_pdf_with_outline(pdf_path, outline_data)
        ranked_sections, sub_section_analysis = rank_content_for_persona(
            content_data, self.persona_data
        )
        
        return {
            "outline": outline_data,
            "content": content_data,
            "ranked_sections": ranked_sections,
            "sub_section_analysis": sub_section_analysis
        }
    
    def process_all_pdfs(self) -> List[Dict[str, Any]]:
        pdf_files = self.get_pdf_files()
        results = []
        
        for pdf_path in pdf_files:
            try:
                result = self.process_single_pdf(pdf_path)
                results.append({
                    "pdf_path": pdf_path,
                    "pdf_name": os.path.basename(pdf_path),
                    **result
                })
            except Exception as e:
                print(f"Error processing {pdf_path}: {e}")
                continue
        
        return results
    
    def generate_final_output(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        all_ranked_sections = []
        all_sub_section_analysis = []
        
        for result in results:
            all_ranked_sections.extend(result["ranked_sections"])
            all_sub_section_analysis.extend(result["sub_section_analysis"])
        
        all_ranked_sections.sort(key=lambda x: x["importance_rank"], reverse=True)
        all_sub_section_analysis.sort(key=lambda x: x["importance_rank"], reverse=True)
        
        input_documents = [os.path.basename(result["pdf_path"]) for result in results]
        
        final_output = {
            "metadata": {
                "input_documents": input_documents,
                "persona": self.persona_data["persona"],
                "job_to_be_done": self.persona_data["job_to_be_done"],
                "processing_timestamp": datetime.datetime.now().isoformat(),
                "total_documents_processed": len(results),
                "total_sections_found": len(all_ranked_sections),
                "total_sub_sections_analyzed": len(all_sub_section_analysis)
            },
            "extracted_sections": all_ranked_sections[:50],
            "sub_section_analysis": all_sub_section_analysis[:30]
        }
        
        return final_output
    
    def save_output(self, output_data: Dict[str, Any], filename: str = "round1b_output.json"):
        os.makedirs(self.output_dir, exist_ok=True)
        output_path = os.path.join(self.output_dir, filename)
        
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        
        print(f"Output saved to: {output_path}")
        return output_path
    
    def run(self):
        print("=== Round 1B: Persona-Driven Document Intelligence ===")
        print(f"Input directory: {self.input_dir}")
        print(f"Output directory: {self.output_dir}")
        
        persona_data = self.load_persona_data()
        print(f"Persona: {persona_data['persona']}")
        print(f"Job: {persona_data['job_to_be_done']}")
        
        results = self.process_all_pdfs()
        print(f"Processed {len(results)} PDFs")
        
        final_output = self.generate_final_output(results)
        output_path = self.save_output(final_output)
        
        print("=== Processing Complete ===")
        print(f"Total sections ranked: {len(final_output['extracted_sections'])}")
        print(f"Total sub-sections analyzed: {len(final_output['sub_section_analysis'])}")
        
        return output_path

def main():
    solution = Round1BSolution()
    solution.run()

if __name__ == "__main__":
    main() 