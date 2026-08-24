from src.retrieval.retriever import retrieve

results = retrieve(
    "Como funciona a comunicação entre microsserviços?"
)

print("IDS:")
print(results["ids"])

print("\n---------------------------------")

print("DISTÂNCIAS:")
print(results["distances"])