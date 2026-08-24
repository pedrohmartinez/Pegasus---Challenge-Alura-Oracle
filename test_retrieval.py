from src.retrieval.retriever import retrieve

results = retrieve(
    "Como funciona a comunicação entre microsserviços?"
)

for i, result in enumerate(results):
    
    print(f"\nRESULTADO {i + 1}")
    
    print("-" * 50)
    
    print(f"DISTÂNCIA: {result['distance']}")
    
    print("METADATA:")
    print(result["metadata"])
        
    print("\nDOCUMENTO:\n")
    print(result["document"])
    
    
    