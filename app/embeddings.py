from sentence_transformers import SentenceTransformer

# Load model once(important for performance)
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embeddings(text_chunks):
    return model.encode(text_chunks)

