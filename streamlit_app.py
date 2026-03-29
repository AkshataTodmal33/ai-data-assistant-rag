try:
    with st.spinner("Thinking... please wait ⏳"):
        response = requests.post(
            "https://ai-data-assistant-rag.onrender.com/chat",
            json={"question": user_input},
            timeout=60   # 🔥 increase timeout
        )

    if response.status_code == 200:
        answer = response.json().get("answer", "No response")

        st.session_state.messages.append({"role": "You", "content": user_input})
        st.session_state.messages.append({"role": "Bot", "content": answer})

        st.write(f"You: {user_input}")
        st.write(f"Bot: {answer}")
    else:
        st.error("API returned error")

except Exception as e:
    st.error(f"Error: {e}")