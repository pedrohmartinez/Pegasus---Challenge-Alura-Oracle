from src.agent.tools import search_documents

result = search_documents.invoke({
    "query": "Qual é o principal produto da empresa?"
})

print(result)