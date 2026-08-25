from src.llm.client import generate_response

prompt = """
Você é um assistente da Santo Pegasus Soluciones.

Responda exclusivamente utilizando as informações
presentes no contexto.

================ CONTEXTO ================

Os domínios da arquitetura se integram exclusivamente
por meio de APIs ou mensageria.

================ PERGUNTA ================

Como os domínios se integram?

================ RESPOSTA ================
"""


response = generate_response(prompt)

print("\n================ RESPOSTA ================\n")
print(response)