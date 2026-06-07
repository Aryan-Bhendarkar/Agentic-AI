from backend import chatbot
from langchain_core.messages import HumanMessage
import streamlit as st

CONFIG = {"configurable": {"thread_id": "thread-1"}}

if 'message_history' in st.session_state:
    st.session_state['message_history'] = []

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message["content"])