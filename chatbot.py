from groq import Groq

import os
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 🧠 System + memory
messages = [
    {
        "role": "system",
        "content": "You are an AI assistant specialized in AWS and Data Engineering. You give clear, short, and professional answers."
    }
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    bot_reply = response.choices[0].message.content

    print("Bot:", bot_reply)

    messages.append({"role": "assistant", "content": bot_reply})