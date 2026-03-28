import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from groq import Groq

# 🔑 Groq API
import os
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 📄 Load CSV
df = pd.read_csv("data.csv")

# Convert rows to text
documents = df.astype(str).apply(lambda row: " ".join(row), axis=1).tolist()

# 🧠 Create embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(documents)

# 📦 Store in FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# 🔍 Search function
def search(query):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=2)
    return [documents[i] for i in I[0]]

# 💬 Chat loop
messages = [
    {"role": "system", "content": "You are a data assistant. Answer ONLY from the given data. Give short and direct answers."}
]

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    # 🔍 Retrieve relevant data
    results = search(user_input)
    context = "\n".join([f"Data: {r}" for r in results])

    # Add context + question
    messages.append({
        "role": "user",
        "content": f"Context:\n{context}\n\nQuestion: {user_input}"
    })

    # 🤖 LLM call
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    bot_reply = response.choices[0].message.content
    print("Bot:", bot_reply)

    messages.append({"role": "assistant", "content": bot_reply})