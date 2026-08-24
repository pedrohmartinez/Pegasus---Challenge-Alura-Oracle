from src.embeddings.embedder import generate_embeddings
from src.vectorstore.chroma_store import get_collection

def retrieve(
    question: str,
    top_k: int = 3
):
    
    collection = get_collection()
    
    question_embeddings = generate_embeddings(
        question
    )
    
    results = collection.query(
        query_embeddings=[
            question_embeddings.tolist()
        ],
        n_results=top_k
    )
    
    return results