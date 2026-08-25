from src.retrieval.retriever import retrieve
from src.rag.context import build_context
from src.rag.prompt import build_prompt
from src.llm.client import generate_response

def answer_question(
    question: str
) -> str:
    
    results = retrieve(question)
    
    context = build_context(results)
    
    prompt = build_prompt(
        context,
        question
    )
    
    answer = generate_response(
        prompt
    )
    
    return answer