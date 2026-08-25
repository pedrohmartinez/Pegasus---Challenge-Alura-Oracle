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

Sua tarefa é responder perguntas usando somente
as informações presentes no CONTEXTO.

Regras:
1. Não use conhecimento externo.
2. Não invente informações.
3. Se o CONTEXTO não responder à pergunta,
   informe que não há informação suficiente.
4. Responda diretamente à pergunta.
5. Não crie alternativas, questões ou respostas
   de múltipla escolha.
"""
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.2,
        "max_tokens": 300
    }
    
    response = requests.post(
        LM_STUDIO_URL,
        json=payload
    )
    
    response.raise_for_status()
    
    data = response.json()
    
    answer = data["choices"][0]["message"]["content"]
    
    return answer