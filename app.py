import streamlit as st
from chatbot import get_response

# ------------------ Page Configuration ------------------

st.set_page_config(
    page_title="Growfinix AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# ------------------ Sidebar ------------------

with st.sidebar:

    st.title("🤖 Growfinix AI")

    st.write("### Features")

    st.write("✅ AI Chat")
    st.write("✅ Powered by Gemini")
    st.write("✅ Chat History")
    st.write("✅ Fast Responses")

    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ------------------ Main Page ------------------

st.title("🤖 Growfinix AI Assistant")

st.caption("🚀 Built by Tamil Amudhan | Powered by Google Gemini")

# ------------------ Session State ------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# ------------------ Welcome Message ------------------

if len(st.session_state.messages) == 0:
    st.info("👋 Welcome! Ask me anything about AI, Python, Cyber Security, Travel, Programming and more.")

# ------------------ Display Chat ------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ------------------ User Input ------------------

prompt = st.chat_input("Type your message...")

if prompt:

    # User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # AI Response
    with st.chat_message("assistant"):

        with st.spinner("🤖 Thinking..."):

            response = get_response(prompt)

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# ------------------ Footer ------------------

st.divider()

st.caption("© 2026 Anno Joy Shalom | Growfinix AI Internship")
