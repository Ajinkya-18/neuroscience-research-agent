import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import ast

load_dotenv()

from agents.agent import agent


st.set_page_config(page_title="Neuroscience Research Agent", layout='centered')
st.title("Neuroscience Research Assistant")
st.caption("A research assistant powered by Gemini and Tavily Search")

@st.cache_resource
def load_agent():
    """Uses streamlit's cache to load the agent only once. It calls the imported function."""
    return agent

try:
    agent = load_agent()

except Exception as e:
    st.error(f"Failed to load agent: {e}. Check API keys and permissions.")
    st.stop()


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if user_prompt := st.chat_input("Ask a question..."):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    history_messages = []

    def stream_response(prompt):
        for chunk in agent.stream(
            input={"messages": history_messages + [HumanMessage(prompt)]}, 
            stream_mode='messages', 
            version="v2",
        ):
            if chunk["type"] == "messages":
                token, metadata = chunk["data"]
                if len(token.content_blocks) > 0:
                    if token.content_blocks[0]['type'] == 'text' and not token.content_blocks[0]["text"].startswith('{"query":'):
                        yield token.content_blocks[0]["text"]
                
                else:
                    continue
    

    for msg in st.session_state.messages[:-1]:
        if msg["role"] == "user":
            history_messages.append(HumanMessage(content=msg["content"]))
        elif msg["role"] == "assistant":
            history_messages.append(AIMessage(content=msg["content"]))

    with st.spinner("Searching..."):
        try:
            with st.chat_message("assistant"):
                ai_response = st.write_stream(stream_response(user_prompt))
                st.session_state.messages.append({"role": "assistant", "content": ai_response})


        except Exception as e:
            st.error(f"An error occurred: {e}")

