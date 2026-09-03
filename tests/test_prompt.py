from src.retrieval.retriever import retrieve
from src.rag.context import build_context
from src.rag.prompt import build_prompt

question = "Como funciona a comunicação entre microsserviços?"

results =  retrieve(question)

context = build_context(results)

prompt = build_prompt(
    context,
    question
)

print("\n================ PROMPT ================\n")

print(prompt)