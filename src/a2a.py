from typing import Annotated

from typing_extensions import TypedDict
from IPython.display import Image, display

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage

class State(TypedDict):
    # Messages have the type "list". The `add_messages` function
    # in the annotation defines how this state key should be updated
    # (in this case, it appends messages to the list, rather than overwriting them)
    messages: Annotated[list, add_messages]

llm = init_chat_model("gemini-2.5-flash-lite-preview-06-17", model_provider="google_genai")

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()

display(Image(graph.get_graph().draw_mermaid_png()))

def get_a2a_response(prompt: str, thread_id: str = None):
    config = {"configurable": {"thread_id": thread_id}}
    messages = [
        SystemMessage(content="Eres un modelo de IA que responde preguntas de manera clara y concisa. Tu nombre es Jarvis."),
        HumanMessage(content=prompt)
    ]
    for event in graph.stream({"messages": messages}, config):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)
            return value["messages"][-1].content