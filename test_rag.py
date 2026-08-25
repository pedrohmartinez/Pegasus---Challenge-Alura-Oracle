from src.rag.rag import answer_question
from src.retrieval.retriever import retrieve
from src.rag.context import build_context
from src.rag.prompt import build_prompt
from src.llm.client import generate_response

question = (
    "Quais mecanismos de segurança são utilizados na comunicação entre microsserviços?"
)

answer = answer_question(
    question
)
results = retrieve(question)

print("\n================ RETRIEVAL ================\n")

for result in results:
    print("DOCUMENTO:")
    print(result["document"])

    print("\nMETADATA:")
    print(result["metadata"])

    print("\nDISTANCE:")
    print(result["distance"])

    print("\n============================================\n")
    
print("\n================ RESPOSTA ================\n")

print(answer)

# Como os domínios se integram?
# Quem é o CEO da Santo Pegasus Soluciones?
# Quais mecanismos de segurança são utilizados na comunicação entre microsserviços?
