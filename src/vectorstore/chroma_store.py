from chromadb import PersistentClient

COLLECTION_NAME = "pegasus_docs"

def get_chroma_client():
    client = PersistentClient(
        path="data/chroma"
    )
    
    return client

def get_collection():
    
    client = get_chroma_client()
    
    return client.get_or_create_collection(
        name=COLLECTION_NAME
    )
    
def store_chunks(
    chunks,
    embeddings
):
    collection = get_collection()
    
    documents = [
        chunk.page_content 
        for chunk in chunks
    ]
    
    metadatas = [
        chunk.metadata 
        for chunk in chunks
    ]
    
    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]
    
    collection.add(
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings.tolist(),
        ids=ids
    )