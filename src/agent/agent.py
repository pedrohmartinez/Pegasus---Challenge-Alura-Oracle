import json

from langchain_core.messages import(
    SystemMessage,
    HumanMessage,
    ToolMessage
)


from src.agent.llm import get_agent_llm
from src.agent.tools import search_documents

SYSTEM_PROMPT = """
Você é um assistente da Santo Pegasus Soluciones.

Sua função é responder perguntas utilizando EXCLUSIVAMENTE
informações presentes nos documentos corporativos da empresa.

REGRAS OBRIGATÓRIAS:

1. Não use conhecimento externo.

2. Não invente informações.

3. Não suponha informações que não estejam explicitamente
   presentes nos documentos.

4. Quando precisar de informações dos documentos,
   utilize a ferramenta search_documents.

5. Uma informação somente pode ser apresentada como fato
   quando houver evidência explícita no resultado da ferramenta.

6. Não transforme uma informação parcialmente relacionada
   em uma informação que não foi declarada.

7. Não complete lacunas usando lógica, conhecimento geral,
   associação semântica ou inferência.

8. Informações como nome, endereço, telefone, email, valor,
   quantidade, data, cargo, salário ou qualquer outro dado factual
   não devem ser deduzidas.

9. Se o resultado da ferramenta não possuir evidência suficiente
   para responder exatamente à pergunta, não tente completar
   a informação.

10. Se não houver evidência suficiente, responda SOMENTE:

"Não encontrei informação suficiente nos documentos fornecidos."

11. Combine informações de diferentes resultados somente quando,
    em conjunto, fornecerem evidência suficiente.

12. Responda de forma objetiva e clara.
"""

def run_agent(question: str):
   llm = get_agent_llm()
   
   messages = [
      SystemMessage(content=SYSTEM_PROMPT),
      HumanMessage(content=question)
   ]
   
   while True:
      
      response =llm.invoke(messages)
      
      print("\n===== RESPONSE =====")
      print(response)

      print("\n===== TOOL CALLS =====")
      print(response.tool_calls)
      
      messages.append(response)
      
      # --------------------------------
      # Caso 1: LLM respondeu diretamente
      # --------------------------------

      if not response.tool_calls:
         
         return response.content
      
      # --------------------------------
      # Caso 2: LLM solicitou uma Tool
      # --------------------------------
      
      for tool_call in response.tool_calls:
         
         tool_name = tool_call["name"]
         tool_args = tool_call["args"]
         tool_call_id = tool_call["id"]
         
         if tool_name == "search_documents":
            tool_result = search_documents.invoke(
               tool_args
            )
            
            tool_message = ToolMessage(
               content=json.dumps(
                  tool_result,
                  ensure_ascii=False
               ),
               tool_call_id=tool_call_id
            )
            
            messages.append(tool_message)
            
         else:
            raise ValueError(f"Tool desconhecida: {tool_name}")























































































































































































































































