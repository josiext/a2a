from dotenv import load_dotenv

load_dotenv()

import os
from fastapi import FastAPI
from pydantic import BaseModel
from src.langchain.model import get_model_response
from src.langchain.agent import get_agent_response
from src.langchain.a2a import get_a2a_response
from src.autogen.model import get_autogen_model_response 
from src.autogen.agent import get_autogen_agent_response
from src.autogen.a2a import get_autogen_a2a_response

if not os.environ.get("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in environment variables. Please check your .env file.")

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

# LANGCHAIN

@app.get("/")
def read_root():
    return {"docs": "/docs"}

@app.post("/langchain/model")
def get_response(request: PromptRequest):
    response = get_model_response(request.prompt)
    return {"model": str(response)}

@app.post("/langchain/agent")
def agent_endpoint(request: PromptRequest):
    response = get_agent_response(request.prompt)
    return {"agent": str(response)}

@app.post("/langchain/a2a")
def a2a_endpoint(request: PromptRequest):
    response = get_a2a_response(request.prompt)
    return {"a2a": str(response)}

# AUTOGEN

@app.post("/autogen/model")
async def autogen_model_endpoint(request: PromptRequest):
    response = await get_autogen_model_response(request.prompt)
    return {"autogen": str(response)}

@app.post("/autogen/agent")
async def autogen_agent_endpoint(request: PromptRequest):
    response = await get_autogen_agent_response(request.prompt)
    return {"autogen": str(response)}

@app.post("/autogen/a2a")
async def autogen_a2a_endpoint(request: PromptRequest):
    response = await get_autogen_a2a_response(request.prompt)
    return {"autogen": str(response)}