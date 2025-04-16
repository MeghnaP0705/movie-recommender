# 🎬 AI-Powered Movie Recommender System

A personalized chatbot-powered movie recommender system using **FastAPI**, **Next.js**, **Supabase**, and **Gemini AI**. It tailors movie suggestions based on user preferences using memory and embeddings.

---

## 🔧 Tech Stack

- 🧠 **FastAPI** – Backend REST API
- 💬 **Next.js (React)** – Frontend UI
- 🧬 **Google Gemini API** – Embeddings & NLP processing
- 📦 **Supabase** – User embedding storage
- 🎥 **TMDB API** – Movie data retrieval

---

## ⚙️ Setup Instructions

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### Run server

```bash
uvicorn app:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## 💡 Features

- 🔑 User ID login to track preferences
- 🧠 Memory-powered personalized recommendations
- 🎯 Embedding-based profile generation
- 📡 Real-time chat interface
- 🗃️ Supabase-backed vector storage
- 🎞️ Live movie data via TMDB

