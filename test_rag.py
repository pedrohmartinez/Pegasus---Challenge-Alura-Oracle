from src.rag.rag import answer_question
from src.retrieval.retriever import retrieve

# Lista das questions do benchmark de testes do RAG
questions = [
    "Qual é o principal produto da empresa?",
    "Qual é a missão tecnológica da empresa?",
    "Quantos funcionários a empresa possui?",
    "Quais bancos de dados são utilizados?",
    "Como os domínios se integram?",
    "Quais mecanismos de segurança são utilizados na comunicação entre microsserviços?",
    "Qual é o salário do CEO?",
    "Qual é o faturamento anual da empresa?",
    "Quem é o CEO da Santo Pegasus Soluciones?",
    "Qual é o endereço físico da sede da empresa?",
    "Qual é a capital do Brasil?",
    "Explique como funciona o sistema operacional Windows."
    ]

for i, question in enumerate(questions):
    answer = answer_question(
        question
    )
    results = retrieve(question)

    print(f"\n================ PERGUNTA {i} ================\n")
    print(question)
    
    print("\n================ RETRIEVAL ================\n")

    for result in results:
        print("DOCUMENTO:")
        print(result["document"])

        print("\nDISTANCE:")
        print(result["distance"])
        
    print(f"\n================ RESPOSTA {i} ================\n")

    print(answer)

    print("\n============================================\n")
