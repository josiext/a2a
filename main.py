from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel
from src.model import get_model_response
from src.agent import get_agent_response
from src.a2a import get_a2a_response

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"docs": "/docs"}

@app.post("/model")
def get_response(request: PromptRequest):
    response = get_model_response(request.prompt)
    return {"model": str(response)}

@app.post("/agent")
def agent_endpoint(request: PromptRequest):
    response = get_agent_response(request.prompt)
    return {"agent": str(response)}

@app.post("/a2a")
def a2a_endpoint(request: PromptRequest):
    response = get_a2a_response(request.prompt)
    return {"a2a": str(response)}