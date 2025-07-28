# Persona-Driven Document Matcher

This project was built for **Adobe India Hackathon 2025 – Round 1B**.  
It is a **persona-aware intelligent document matcher** that evaluates how well a document (e.g., résumé, proposal, report) aligns with a given persona and job description.

---

## 🚀 Features

- 🔍 PDF parsing with semantic understanding
- 🧠 Persona and job profiling
- 🤖 AI-based document matching using Sentence Transformers
- 📄 Outputs relevance score and reasoning in `output.json`

---

## 🧠 How it Works

1. Load the **persona** and **job description** from `persona_job.json`
2. Parse and extract text from all PDFs in `pdfs/`
3. Use SentenceTransformer embeddings to compute similarity
4. Output best matches and explanations in `output.json`

---

## 📁 Project Structure
```plaintext
persona-document-matcher/
│
├── main.py                    # Main script to run the document-persona matcher
├── utils.py                   # Utility functions for similarity checking
├── requirements.txt           # List of Python dependencies
├── Dockerfile                 # Docker configuration for containerization
├── persona_job.json           # Sample persona/job description JSON file
├── output.json                # Output file with similarity scores
├── approach_explanation.md    # Explanation of the matching approach
├── pdfs/                      # Folder containing test PDF documents
│   └── test_document.pdf
├── __pycache__/               # Python bytecode cache (auto-generated)
└── README.md                  # Project documentation (this file)
