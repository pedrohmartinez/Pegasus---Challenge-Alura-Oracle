import os
from dotenv import load_dotenv

import requests

load_dotenv()

LM_STUDIO_URL = os.getenv("LM_STUDIO_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

def generate_response(
    prompt: str,
) -> str:
    
    payload = {
        "model": MODEL_NAME,
        "messages" : [
            {
                "role": "system",
                "content": (
                    """
Você é um assistente da Santo Pegasus Soluciones.

Responda à pergunta do usuário usando EXCLUSIVAMENTE
as informações presentes no CONTEXTO fornecido.

REGRAS OBRIGATÓRIAS:

1. Não use conhecimento externo.

2. Não invente informações.

3. Não suponha informações que não estejam explicitamente
   presentes no CONTEXTO.

4. Não transforme uma informação parcialmente relacionada
   em uma informação que não foi declarada.

5. Uma informação somente pode ser apresentada como fato
   quando houver evidência explícita no CONTEXTO que a sustente.

6. Não complete lacunas usando lógica, conhecimento geral,
   associação semântica ou inferência.

7. Se a pergunta solicitar uma informação específica,
   verifique se essa informação específica está explicitamente
   presente no CONTEXTO.

8. Informações como nome, endereço, telefone, email, valor,
   quantidade, data, cargo, salário ou qualquer outro dado factual
   não devem ser deduzidas a partir de informações relacionadas.

9. Se o CONTEXTO contiver apenas informações relacionadas,
   mas não suficientes para responder exatamente à pergunta,
   NÃO tente completar a resposta.

10. Se não houver evidência suficiente no CONTEXTO,
    responda SOMENTE:

"Não encontrei informação suficiente nos documentos fornecidos."

11. Combine informações de diferentes partes do CONTEXTO
    somente quando essas informações, em conjunto,
    fornecerem evidência suficiente para responder à pergunta.

12. Responda de forma objetiva e clara.

"""
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2,
        "max_tokens": 500
    }
    
    response = requests.post(
        LM_STUDIO_URL,
        json=payload
    )
    
    response.raise_for_status()
    
    data = response.json()
    
    answer = data["choices"][0]["message"]["content"]
    
    return answer