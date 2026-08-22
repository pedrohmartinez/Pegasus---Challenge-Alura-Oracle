from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "BAAI/bge-m3"
)

def generate_embedding(text: str):
    embedding = model.encode(text)
    
    return embedding

def generate_embeddings(texts: list[str]):
    embeddings = model.encode(texts)
    
    return embeddings