from pydantic import BaseModel
from fastapi import FastAPI
from typing import List
from src.helper import getresponse
import uvicorn
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

class RequestState(BaseModel):
    model_name : str
    provider : str
    prompt : str
    query : List[str]
    allow_search : bool

ALLOWED_MODEL_NAMES =["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "gemini-2.5-flash"] 
app = FastAPI(title = "Langgraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):

    
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return "Error Model doesn't exists"
    
    llm_id = request.model_name
    provider = request.provider
    prompt = request.prompt
    query = request.query
    allowed_search = request.allow_search

    response = getresponse(llm_id, provider, prompt, query, allowed_search)
    return response


