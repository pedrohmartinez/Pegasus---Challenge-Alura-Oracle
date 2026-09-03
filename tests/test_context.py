from src.retrieval.retriever import retrieve
from src.rag.context import build_context

question = "Como funciona a comunicação entre microsserviços?"

results = retrieve(question)

context = build_context(results)

print("\n================ CONTEXTO ================\n")

print(context)