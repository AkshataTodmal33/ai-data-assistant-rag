from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from groq import Groq

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔑 API Key
import os
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 📄 Load data
df = pd.read_csv("data.csv")
documents = df.astype(str).apply(lambda row: " ".join(row), axis=1).tolist()

# 🧠 Embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(documents)

# 📦 FAISS
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Request format
class Query(BaseModel):
    question: str

# 🔍 Search
def search(query):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=2)
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