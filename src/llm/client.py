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

Sua tarefa é responder à pergunta do usuário utilizando
EXCLUSIVAMENTE as informações presentes no CONTEXTO.

REGRAS:

1. Não utilize conhecimento externo.
2. Não invente informações.
3. Identifique no CONTEXTO as informações que respondem
   diretamente à pergunta.
4. Ignore informações que não sejam relevantes para a pergunta.
5. Combine informações de diferentes partes do CONTEXTO
   quando necessário.
6. Responda de forma objetiva e clara.
7. Se o CONTEXTO não possuir informação suficiente para
   responder, informe que não há informação suficiente
   nos documentos.

A resposta deve ser baseada somente nas evidências
presentes no CONTEXTO.
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