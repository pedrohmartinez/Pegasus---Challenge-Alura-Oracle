from src.agent.tools import search_documents

results = search_documents(
    "Qual é o principal produto da empresa?"
)

for result in results:
    print(result)