from src.retrieval.retriever import retrieve

def search_documents(
    query: str,
    top_k: int = 3
):
    """
    Busca documentos relevantes na base de conhecimento
    da Santo Pegasus Soluciones.
    """
    
    return retrieve(
        question=query,
        top_k=top_k
    )