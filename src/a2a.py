from typing import Annotated

from langchain.chat_models import init_chat_model
from langchain_tavily import TavilySearch
from langchain_core.messages import BaseMessage
from typing_extensions import TypedDict
from langchain.chat_models import init_chat_model

from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import HumanMessage, SystemMessage

class State(TypedDict):
    messages: Annotated[list, add_messages]

graph_builder = StateGraph(State)

tool = TavilySearch(max_results=2)
tools = [tool]

llm = init_chat_model("gemini-2.5-flash-lite-preview-06-17", model_provider="google_genai")
llm_with_tools = llm.bind_tools(tools)

def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)

tool_node = ToolNode(tools=[tool])
graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
graph_builder.add_edge("tools", "chatbot")
graph_builder.set_entry_point("chatbot")
memory = InMemorySaver()
graph = graph_builder.compile(checkpointer=memory)

def get_a2a_response(prompt: str, thread_id: str = None):
    config = {"configurable": {"thread_id": thread_id}}
    messages = [
        SystemMessage(content="Eres un modelo de IA que responde preguntas de manera clara y concisa. Tu nombre es Jarvis."),
        HumanMessage(content=prompt)
    ]

    response = graph.invoke({"messages": messages}, config)
    return response["messages"][-1].content
