import os

if not os.environ.get("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in environment variables. Please check your .env file.")

from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.5-flash-lite-preview-06-17", model_provider="google_genai")

