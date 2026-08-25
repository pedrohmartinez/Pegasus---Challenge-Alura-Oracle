from src.rag.rag import answer_question

question = (
    "Como os domínios se integram?"
)

answer = answer_question(
    question
)

print("\n================ RESPOSTA ================\n")

print(answer)

# Como os domínios se integram?
# Quem é o CEO da Santo Pegasus Soluciones?
# Quais mecanismos de segurança são utilizados na comunicação entre microsserviços?
