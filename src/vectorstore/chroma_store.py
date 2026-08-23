from chromadb import PersistentClient

COLLECTION_NAME = "pegasus_docs"

def get_chroma_client():
    client = PersistentClient(
        path="data/chroma"
    )
    
    return client

def get_collection():
    
    client = get_chroma_client()
    
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME
    )
    
    return collection