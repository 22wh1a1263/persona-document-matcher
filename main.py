import os
from utils import (
    extract_text_by_page,
    load_persona_job,
    load_embedding_model,
    compute_similarities
)
from datetime import datetime
import json

def main():
    # Step 1: Load persona and job
    persona, job = load_persona_job()
    persona_job_text = f"{persona} needs to: {job}"

    # Step 2: Read PDFs
    pdf_folder = "pdfs"
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

    all_pages = []
    for pdf in pdf_files:
        full_path = os.path.join(pdf_folder, pdf)
        pages = extract_text_by_page(full_path)
        for page in pages:
            all_pages.append({
                "document": pdf,
                "page_number": page["page_number"],
                "text": page["text"]
            })

    # Step 3: Load embedding model
    model = load_embedding_model()

    # Step 4: Compute similarity and sort
    ranked_pages = compute_similarities(persona_job_text, all_pages, model)

    # Step 5: Take top 5 pages
    top_n = 5
    extracted_sections = []
    subsection_analysis = []

    for rank, page in enumerate(ranked_pages[:top_n]):
        extracted_sections.append({
            "document": page["document"],
            "page_number": page["page_number"],
            "section_title": "Auto-selected section",
            "importance_rank": rank + 1
        })

        # For subsection analysis - extract top 3 sentences
        top_sentences = sorted(
            page["text"].split(". "),
            key=lambda s: len(s),  # simple scoring by length (can improve)
            reverse=True
        )[:3]

        refined_text = ". ".join(top_sentences)

        subsection_analysis.append({
            "document": page["document"],
            "page_number": page["page_number"],
            "refined_text": refined_text.strip()
        })

    # Step 6: Create output JSON
    output = {
        "metadata": {
            "input_documents": pdf_files,
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    with open("output.json", "w") as f:
        json.dump(output, f, indent=4)

    print("✅ All done! Output saved to output.json")

if __name__ == "__main__":
    main()
