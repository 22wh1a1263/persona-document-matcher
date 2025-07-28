import fitz  # PyMuPDF
import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text_by_page(pdf_path):
    doc = fitz.open(pdf_path)
    text_by_page = []
    for page_number, page in enumerate(doc, start=1):
        text = page.get_text()
        if text.strip():
            text_by_page.append({
                "page_number": page_number,
                "text": text
            })
    return text_by_page

def load_persona_job(json_path="persona_job.json"):
    with open(json_path, "r") as f:
        data = json.load(f)
    return data["persona"], data["job_to_be_done"]

def load_embedding_model():
    return SentenceTransformer("intfloat/e5-small-v2")

def compute_embedding(text, model):
    return model.encode(text, convert_to_tensor=False)

def compute_similarities(persona_job_text, pages, model):
    pj_embed = compute_embedding(persona_job_text, model)

    for page in pages:
        page_embed = compute_embedding(page["text"], model)
        similarity = cosine_similarity([pj_embed], [page_embed])[0][0]
        page["similarity"] = float(similarity)

    return sorted(pages, key=lambda x: x["similarity"], reverse=True)
