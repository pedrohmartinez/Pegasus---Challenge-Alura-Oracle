def build_prompt(
    context: str,
    question: str
) -> str:
    
    prompt = f"""
    Você é um asssitente da Santo Pegasus Soluciones.
    
    Responda á pergunta utilizando exclusivamente as
    informações presente no contexto fornecido.
    
    Se o contexto não possuir informação suficiente 
    para responder á pergunta, informe que não encontrou 
    informação suficiente nos documentos fornecidos.
    
    ================ CONTEXTO ================

    {context}

    ================ PERGUNTA ================

    {question}

    ================ RESPOSTA ================
    """
    
    return prompt
    