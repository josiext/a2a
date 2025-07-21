import os
from langchain_core.messages import HumanMessage, SystemMessage

if not os.environ.get("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in environment variables. Please check your .env file.")

from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.5-flash-lite-preview-06-17", model_provider="google_genai")

def get_model_response(prompt: str):
    messages = [
        SystemMessage(content="Eres un modelo de IA que responde preguntas de manera clara y concisa. Tu nombre es Jarvis."),
        HumanMessage(content=prompt)
    ]

    print(messages)
    response = model.invoke(messages)
    return str(response)
