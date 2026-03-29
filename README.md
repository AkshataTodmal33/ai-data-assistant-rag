# 🤖 AI Data Assistant (RAG Chatbot)

An intelligent chatbot that answers questions from structured data using **RAG (Retrieval-Augmented Generation)**.

---

## 🚀 Features
- 🔍 Semantic Search using FAISS
- 🧠 Embeddings with Sentence Transformers
- 💬 Chat UI (React + Streamlit)
- ⚡ FastAPI backend
- ☁️ Ready for deployment
- 📊 Works on CSV data (Flight dataset)

---

## 🛠️ Tech Stack
- Python
- FastAPI
- FAISS
- Sentence Transformers
- Groq LLM
- React (Frontend)
- Streamlit (Optional UI)

---

## 📂 Project Structure
ai-data-assistant-rag/
│
├── api.py                # FastAPI backend
├── streamlit_app.py      # Streamlit frontend UI
├── data.csv              # Dataset
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
│
├── rag_chatbot.py        # RAG logic
├── chatbot.py            # Chat processing
│
└── ai-chat-ui/           # UI components (if used)

---

🚀 Architecture
User → Streamlit UI → FastAPI → FAISS → LLM (Groq) → Response
