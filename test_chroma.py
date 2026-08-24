from src.vectorstore.chroma_store import (
    get_collection
)


collection = get_collection()

resultado = collection.get(
    ids=["chunk_0"],
    include=["documents","metadatas","embeddings"]
)

print("DOCUMENTO:")
print(resultado["documents"][0])

print("\n---------------------------------")

print("METADATA:")
print(resultado["metadatas"][0])

print("\n---------------------------------")

print("TIPO DO EMBEDDING:")
print(type(resultado["embeddings"][0]))

print("\n---------------------------------")

print("DIMENSIONALIDADE:")
print(len(resultado["embeddings"][0]))