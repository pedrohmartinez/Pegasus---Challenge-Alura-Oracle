from src.llm.client import generate_response

response = generate_response(
    "Explique em uma frase o que é um microsserviço"
)

print("\nResposta:")
print(response)