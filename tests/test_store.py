from src.ingestion.loader import load_all_pdfs
from src.chunking.splitter import split_documents
from src.embeddings.embedder import generate_embeddings
from src.vectorstore.chroma_store import store_chunks


documents = load_all_pdfs(
    "data/pdfs"
)

chunks = split_documents(
    documents
)

texts = [
    chunk.page_content
    for chunk in chunks
]

embeddings = generate_embeddings(
    texts
)

store_chunks(
    chunks,
    embeddings
)

print("Indexação concluída")