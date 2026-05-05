from fastapi import FastAPI, UploadFile, File
from app.rag_pipeline import RAG
from app.utils import split_text

app = FastAPI()

# Default data (initial)
docs = [
    "AI is transforming the world",
    "Machine learning is a subset of AI",
    "FastAPI is used for building APIs"
]

rag = RAG(docs)


@app.get("/")
def home():
    return {"message": "RAG API is running"}


@app.get("/ask")
def ask_question(q: str):
    answer = rag.query(q)
    return {"question": q, "answer": answer}


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    
    text = content.decode("utf-8", errors="ignore")
    chunks = split_text(text)
    
    global rag
    rag = RAG(chunks)
    
    return {"message": "File uploaded and processed", "chunks": len(chunks)}