import faiss
from app.embeddings import get_embeddings

import google.generativeai as genai

# Gemini API key 
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# Load Gemini model
model = genai.GenerativeModel("gemini/gemini-2.5-flash")


class RAG:
    def __init__(self, docs):
        self.docs = docs
        
        # Create embeddings
        self.embeddings = get_embeddings(docs)
        
        # Create FAISS index
        dimension = len(self.embeddings[0])
        self.index = faiss.IndexFlatL2(dimension)
        
        # Add embeddings
        self.index.add(self.embeddings)

    def query(self, question, k=2):
        # Convert question to embedding
        query_vector = get_embeddings([question])
        
        # Search similar chunks
        _, indices = self.index.search(query_vector, k)
        
        # Get context
        context = " ".join([self.docs[i] for i in indices[0]])
        
        # Prompt for Gemini
        prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{question}

Answer:
"""
        
        # Generate response
        response = model.generate_content(prompt)
        
        return response.text