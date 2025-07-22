import os
from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage, SystemMessage


memory = MemorySaver()
model = init_chat_model("gemini-2.5-flash-lite-preview-06-17", model_provider="google_genai")
search = TavilySearch(max_results=2)
tools = [search]
agent_executor = create_react_agent(model, tools, checkpointer=memory)

def get_agent_response(prompt: str):
  config = {"configurable": {"thread_id": None}}
  messages = [
        SystemMessage(content="Eres un modelo de IA que responde preguntas de manera clara y concisa. Tu nombre es Jarvis."),
        HumanMessage(content=prompt)
    ]
  
  response = agent_executor.invoke({"messages": messages}, config)
  return response["messages"][-1].content

def get_agent_response_stream(prompt: str):
    config = {"configurable": {"thread_id": None}}
    messages = [
        SystemMessage(content="Eres un modelo de IA que responde preguntas de manera clara y concisa. Tu nombre es Jarvis."),
        HumanMessage(content=prompt)
      ]
    
    for step in agent_executor.stream(
        {"messages": messages}, config, stream_mode="values"
    ):
        if "messages" in step and step["messages"]:
            step["messages"][-1].pretty_print()
            final_step = step
    
    if final_step and "messages" in final_step and final_step["messages"]:
        return final_step["messages"][-1].content
    else:
        return "I apologize, but I encountered an error while processing your request."
        