from src.embeddings.embedder import generate_embeddings
from src.chunking.splitter import split_documents
from src.ingestion.loader import load_all_pdfs

all_documents = load_all_pdfs("data/pdfs")
        
chunks = split_documents(all_documents)

texts = [chunk.page_content for chunk in chunks]

embeddings = generate_embeddings(texts)

print(f"quantidade de embeddings: {len(embeddings)}")
print("\n------------------")
print(f"tipo dos embeddings: {type(embeddings)}")
print("\n------------------")
print(f"dimensionalidade: {len(embeddings[0])}")