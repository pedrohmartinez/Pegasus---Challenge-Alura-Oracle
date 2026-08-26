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

Sua única fonte de conhecimento é o CONTEXTO fornecido.

Ao responder:

1. Identifique as informações do CONTEXTO que respondem à pergunta.
2. Ignore informações não relacionadas.
3. Combine evidências quando necessário.
4. Não utilize conhecimento externo.

Se o CONTEXTO não possuir informação suficiente para responder, responda exatamente:

"Não encontrei informação suficiente nos documentos fornecidos."
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