def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
    
def split_text(text, chunk_size=500):
    sentences = text.split(". ")
    
    chunks = []
    chunk = ""
    
    for sentence in sentences:
        if len(chunk) + len(sentence) < chunk_size:
            chunk += sentence + ". "
        else:
            chunks.append(chunk.strip())
            chunk = sentence + ". "
    
    if chunk:
        chunks.append(chunk.strip())
    return chunks        