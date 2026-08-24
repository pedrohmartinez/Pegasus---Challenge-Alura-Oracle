from src.retrieval.retriever import retrieve

results = retrieve(
    "Como funciona a comunicação entre microsserviços?"
)

print(results.keys())