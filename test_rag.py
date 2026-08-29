from src.rag.rag import answer_question
from src.retrieval.retriever import retrieve

question = (
    "Explique como funciona o Windows."
)

answer = answer_question(
    question
)
results = retrieve(question)

print("\n================ RETRIEVAL ================\n")

for result in results:
    print("DOCUMENTO:")
    print(result["document"])

    # print("\nMETADATA:")
    # print(result["metadata"])

    print("\nDISTANCE:")
    print(result["distance"])

    print("\n============================================\n")
    
print("\n================ RESPOSTA ================\n")

print(answer)

print("\n============================================\n")
