def build_prompt(
    context: str,
    question: str
) -> str:
    
    prompt = f"""
Você é um asssitente da Santo Pegasus Soluciones.

Responda á pergunta utilizando exclusivamente as
informações presente no contexto fornecido.

Se a informação necessária não estiver presente
no contexto fornecido, responda exatamente:

"Não encontrei informação suficiente nos
documentos fornecidos."

================ CONTEXTO ================

{context}

================ PERGUNTA ================

{question}

================ RESPOSTA ================
"""
    
    return prompt
    