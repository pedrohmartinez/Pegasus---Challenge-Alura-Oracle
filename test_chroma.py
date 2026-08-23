from src.vectorstore.chroma_store import (
    get_collection
)


collection = get_collection()

print(f"Nome: {collection.name}")
print(f"Quantidade de registros: {collection.count()}")