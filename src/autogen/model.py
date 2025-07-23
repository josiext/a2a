from autogen_core.models import UserMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo
from src.utils import MODEL_NAME
import os

# ❌ gemini-2.5-flash-lite is not supported by default so we need to add model_info

model_client = OpenAIChatCompletionClient(
    model=MODEL_NAME,
    model_info=ModelInfo(vision=True, function_calling=True, json_output=True, family="unknown", structured_output=True),
    api_key=os.environ.get("GOOGLE_API_KEY"),
)

async def get_autogen_model_response(prompt: str):
    response = await model_client.create([UserMessage(content=prompt, source="user")])
    return response.content
