from src.retrieval.retriever import retrieve
from langchain_core.tools import tool

@tool
def search_documents(query: str) -> list:
    """
    Busca informações relevantes nos documentos corporativos
    da Santo Pegasus Soluciones.
    Use esta ferramenta quando precisar consultar informações
    presentes na base documental da empresa.
    """
    
    return retrieve(
        question=query,
        top_k=3
    )