def build_prompt(
    context: str,
    question: str
) -> str:
    
    prompt = f"""
Você é um assistente da Santo Pegasus Soluciones.

Responda utilizando exclusivamente as informações
presentes no contexto.

Se a resposta não estiver presente no contexto,
responda exatamente:

"Não encontrei informação suficiente nos documentos fornecidos."

================ CONTEXTO ================

{context}

================ PERGUNTA ================

{question}

================ RESPOSTA ================
"""
    
    return prompt
    