from src.rag.rag import answer_question
from src.retrieval.retriever import retrieve

question = (
    "Quantos funcionários a empresa possui?"
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

    # print("\nDISTANCE:")
    # print(result["distance"])

    print("\n============================================\n")
    
print("\n================ RESPOSTA ================\n")

print(answer)

print("\n============================================\n")

# Testes padrão
# Como os domínios se integram?
# Quem é o CEO da Santo Pegasus Soluciones?
# Quais mecanismos de segurança são utilizados na comunicação entre microsserviços?
