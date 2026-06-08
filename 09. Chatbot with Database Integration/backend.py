from langgraph.graph import StateGraph, START, END
from langchain_openrouter import ChatOpenRouter
from langchain_core.messages import BaseMessage
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from typing import TypedDict, Annotated
import sqlite3

load_dotenv()

llm = ChatOpenRouter(model = "openai/gpt-4o-mini")

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]


def chat_node(state: ChatState):
    messages = state["messages"]
    response = llm.invoke(messages)
    return {"messages": [response]}

conn = sqlite3.connect(database="Chatbot.db", check_same_thread=False)
checkpointer = SqliteSaver(conn)

graph = StateGraph(ChatState)

graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)