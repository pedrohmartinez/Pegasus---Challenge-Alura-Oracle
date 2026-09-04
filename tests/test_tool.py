from src.agent.tools import search_documents

print(f"Nome: {search_documents.name}")

print("\nDescrição:")
print(search_documents.description)

print("\nSchema:")
print(search_documents.args_schema.model_json_schema())