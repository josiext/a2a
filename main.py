from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from src.model import model

app = FastAPI()

@app.get("/")
def read_root():
    return {"docs": "/docs"}

@app.get("/model")
def get_model_response():
    response = model.invoke("Eres un modelo razonador?")
    return {"model": str(response)}