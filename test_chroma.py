from src.vectorstore.chroma_store import (
    get_collection
)


collection = get_collection()

print(collection.name)