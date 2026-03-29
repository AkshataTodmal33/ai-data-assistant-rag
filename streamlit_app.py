import streamlit as st
import requests

st.title("🤖 AI Data Assistant")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat
for msg in st.session_state.messages:
    st.write(f"{msg['role']}: {msg['content']}")

# Input
user_input = st.text_input("Ask a question")

if st.button("Send"):
    if user_input:
        try:
            with st.spinner("Thinking... please wait ⏳"):
                response = requests.post(
                    "https://ai-data-assistant-rag.onrender.com/chat",
                    json={"question": user_input},
                    timeout=60
                )

            if response.status_code == 200:
                answer = response.json().get("answer", "No response")

                # Save messages
                st.session_state.messages.append({"role": "You", "content": user_input})
                st.session_state.messages.append({"role": "Bot", "content": answer})

                st.write(f"You: {user_input}")
                st.write(f"Bot: {answer}")
            else:
                st.error("API returned error")

        except Exception as e:
            st.error(f"Error: {e}")