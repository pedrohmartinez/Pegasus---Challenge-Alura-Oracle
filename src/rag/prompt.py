def build_prompt(
    context: str,
    question: str
) -> str:
    
    prompt = f"""
================ CONTEXTO ================

{context}

================ PERGUNTA ================

{question}

================ RESPOSTA ================
"""
    
    return prompt
    