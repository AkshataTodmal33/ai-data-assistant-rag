from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import faiss
import numpy as np
from groq import Groq
import os


app = FastAPI()

# ✅ CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔑 Groq API Key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 📄 Load data
df = pd.read_csv("data.csv")
documents = df.astype(str).apply(lambda row: " ".join(row), axis=1).tolist()

# ✅ Simple lightweight embedding (NO heavy ML)
def simple_embedding(text):
    # convert text → fixed size vector (cheap trick)
    vector = np.zeros(100)
    for i, char in enumerate(text[:100]):
        vector[i] = ord(char) / 1000
    return vector

# 🧠 Generate embeddings
embeddings = np.array([simple_embedding(doc) for doc in documents])

# 📦 FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# 📥 Request format
class Query(BaseModel):
    question: str

# 🔍 Search
def search(query):
    query_embedding = np.array([simple_embedding(query)])
    D, I = index.search(query_embedding, k=2)
    return [documents[i] for i in I[0]]

# 🚀 API endpoint
@app.post("/chat")
def chat(query: Query):
    results = search(query.question)

    context = "\n".join([
        f"Flight: {r.split()[0]}, Delay: {r.split()[1]}, Price: {r.split()[2]}"
        for r in results
    ])

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """You are a data assistant. Use ONLY the given data.
Delay is the second value, price is the third value.
Answer correctly and do not confuse columns.
Give short and exact answers."""
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {query.question}"
            }
        ]
    )

    return {"answer": response.choices[0].message.content}

@app.get("/")
def home():
    return {"message": "AI Data Assistant is running 🚀"}