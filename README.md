# 🚀 RAG-Based Question Answering System

An end-to-end Retrieval-Augmented Generation (RAG) system that allows users to upload documents and ask questions. The system retrieves relevant context and generates accurate answers using LLMs.

---

## 🔥 Features

* 📄 Upload custom text documents
* 🔍 Semantic search using FAISS
* 🤖 Context-aware answers using Gemini API
* ⚡ FastAPI backend for real-time responses
* 🐳 Dockerized for deployment

---

## 🧠 Tech Stack

* Python
* FastAPI
* FAISS
* Sentence Transformers
* Google Gemini API
* Docker

---

## 🏗️ Architecture

1. Convert documents into embeddings
2. Store embeddings in FAISS vector database
3. Retrieve relevant chunks based on user query
4. Send context + query to LLM
5. Generate final answer

---

## 🚀 Installation

```bash
git clone https://github.com/AnjaliGupta2568/Customer-Churn-Prediction-project.git
cd rag-qa-system
pip install -r requirements.txt
```

---

## ▶️ Run Locally

```bash
uvicorn app.main:app --reload
```

Open:

```
http://localhost:8000/docs
```

---

## 🐳 Run with Docker

```bash
docker build -t rag-api .
docker run -p 8000:8000 -e GEMINI_API_KEY=your_key rag-api
```

---

## 📌 API Usage

### Ask Question

```
GET /ask?q=your_question
```

---

## 📸 Demo

(Add screenshots here)

---

## 🎯 Use Cases

* Document-based Q&A system
* Customer support automation
* Knowledge base assistant

---

## 🚀 Future Improvements

* Streamlit UI
* Chat history
* Multi-document support
* Cloud deployment (AWS/GCP)

---

## 👩‍💻 Author

**Anjali Gupta**
Aspiring AI/ML Engineer

---

## ⭐ If you like this project, give it a star!
