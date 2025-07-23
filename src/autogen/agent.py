from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import StructuredMessage
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo
from src.utils import MODEL_NAME
import os

async def web_search(query: str) -> str:
    """Find information on the web"""
    return "AutoGen is a programming framework for building multi-agent applications."

model_client = OpenAIChatCompletionClient(
    model=MODEL_NAME,
    model_info=ModelInfo(vision=True, function_calling=True, json_output=True, family="unknown", structured_output=True),
    api_key=os.environ.get("GOOGLE_API_KEY"),
)

agent = AssistantAgent(
    name="assistant",
    model_client=model_client,
    tools=[web_search],
    system_message="Use tools to solve tasks.",
)

async def get_autogen_agent_response(prompt: str):
    result = await agent.run(task=prompt)
    return result.messages[-1].content
