from src.retrieval.retriever import retrieve

results = retrieve(
    "Como funciona a comunicação entre microsserviços?"
)

for i in range(3):
    
    print(f"\nRESULTADO {i + 1}")
    
    print("-" * 50)
    
    print(
        f"ID: {results['ids'][0][i]}"
    )
    
    print(
        f"DISTÂNCIA: {results['distances'][0][i]}"
    )
    
    print("\nDOCUMENTO:\n")
    
    print(
        results["documents"][0][i]
    )
    
    print("\n")
    