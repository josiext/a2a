from langchain_core.messages import HumanMessage, SystemMessage
from src.utils import SYSTEM_PROMPT, MODEL_NAME, MODEL_PROVIDER
from langchain.chat_models import init_chat_model

model = init_chat_model(MODEL_NAME, model_provider=MODEL_PROVIDER)

def get_model_response(prompt: str, thread_id: str = None):
    config = {"configurable": {"thread_id": thread_id}}
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=prompt)
    ]

    response = model.invoke(messages, config)
    return str(response)
