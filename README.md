## 🤖 AI Data Assistant (RAG Chatbot)

An intelligent chatbot that answers questions from structured data using **Retrieval-Augmented Generation (RAG)**.

---

## 🚀 Features

- 🔍 Semantic search using **FAISS**
- 🧠 Lightweight embeddings (optimized for fast deployment)
- 💬 Interactive chat UI (**Streamlit / React**)
- ⚡ Scalable backend using **FastAPI**
- 📊 Supports CSV-based structured datasets (Flight data)
- ☁️ Fully deployed on cloud (Render + Streamlit Cloud)

---

## 🛠️ Tech Stack

- Python
- FastAPI
- FAISS
- Groq LLM
- Streamlit
- React (Optional UI)

---

## 📂 Project Structure

```bash
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
└── ai-chat-ui/           # UI components (optional)
```

---

## 🚀 Architecture

```
User → Streamlit UI → FastAPI → FAISS → LLM (Groq) → Response
```

---

## 🔗 Live Links

- 🌐 Live App: https://ai-data-assistant-rag-6pyxyvawoj7mu42iqigze9.streamlit.app/  
- 📘 API Docs: https://ai-data-assistant-rag.onrender.com/docs  
- 💻 GitHub Repo: https://github.com/AkshataTodmal33/ai-data-assistant-rag  
