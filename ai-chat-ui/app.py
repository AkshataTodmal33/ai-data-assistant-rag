import streamlit as st
import requests

st.title("🤖 AI Data Assistant")

user_input = st.text_input("Ask a question:")

if st.button("Ask"):
    response = requests.post(
        "https://ai-data-assistant-rag.onrender.com/chat",
        json={"question": user_input}
    )

    if response.status_code == 200:
        st.write("🧠 Answer:")
        st.success(response.json()["answer"])
    else:
        st.error("Something went wrong")