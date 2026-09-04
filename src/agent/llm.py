import os 

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from src.agent.tools import search_documents

load_dotenv()

LM_STUDIO_URL = os.getenv("LM_STUDIO_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

def get_agent_llm():
    
    llm = ChatOpenAI(
        base_url=LM_STUDIO_URL,
        api_key="lm_studio",
        model=MODEL_NAME,
        temperature=0.2,
        max_tokens=500
    )
    
    return llm.bind_tools([
        search_documents
    ])