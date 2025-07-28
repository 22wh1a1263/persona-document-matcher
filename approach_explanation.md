# Approach Explanation

Our system aims to extract the most relevant content from a collection of PDFs based on a defined persona and job-to-be-done.

## 1. PDF Processing
We use PyMuPDF to extract page-wise text from each PDF. This gives us a structured view of the entire document.

## 2. Persona and Job Understanding
The persona and job description are combined into a query which defines the user’s information need.

## 3. Embedding and Matching
We use the "intfloat/e5-small-v2" sentence transformer model to convert both the user query and PDF page contents into embeddings. Cosine similarity is used to compare how relevant each page is to the user query.

## 4. Section Ranking
We rank the pages based on similarity and select the top N most relevant pages as the extracted sections.

## 5. Subsection Extraction
From the top-ranked pages, we extract the most relevant 2–3 sentences to create a refined summary, which helps in giving granular insight to the user.

## 6. Constraints Handling
The solution is designed to:
- Run on CPU
- Finish within 60 seconds for small PDF collections
- Use a lightweight model under 1GB
- Work offline inside Docker

This generic pipeline is adaptable to any persona and task with diverse document types.
