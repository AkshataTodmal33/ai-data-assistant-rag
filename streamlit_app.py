import streamlit as st
import requests

st.title("🤖 AI Data Assistant")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    st.write(f"{msg['role']}: {msg['content']}")

# User input
user_input = st.text_input("Ask a question")

if st.button("Send"):
    if user_input:
        # Call FastAPI
        response = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"question": user_input}
        )

        answer = response.json()["answer"]

        # Save messages
        st.session_state.messages.append({"role": "You", "content": user_input})
        st.session_state.messages.append({"role": "Bot", "content": answer})

        st.write(f"You: {user_input}")
        st.write(f"Bot: {answer}")