# KnowYourDocs – RAG-Based Question Answering System

A **fully local Retrieval-Augmented Generation (RAG) Question Answering system** built with **FastAPI**, **FAISS**, **Sentence Transformers**, and a **local open-source LLM (FLAN-T5)**.
Users can upload documents (PDF/TXT) and ask questions that are answered **only using the uploaded content**.

This project is **Windows-friendly**, **cost-free**.

---

## 🚀 Features

* Upload **PDF** and **TXT** documents
* Background document ingestion
* Text chunking with overlap
* Embedding generation using Sentence Transformers
* Vector storage using **FAISS (local)**
* Semantic similarity search
* Answer generation using **local FLAN-T5 model** (no OpenAI, no Ollama)
* FastAPI backend with Swagger docs
* Rate limiting (SlowAPI)
* Simple HTML UI for testing
* CORS enabled for browser access

---

## 🛠 Tech Stack

* **Backend:** FastAPI
* **Embeddings:** Sentence-Transformers (`all-MiniLM-L6-v2`)
* **Vector Store:** FAISS (CPU)
* **LLM:** Google FLAN-T5 (local, Hugging Face)
* **UI:** HTML + CSS + JavaScript
* **Language:** Python 3.10+

---

## 📁 Project Structure

```
KnowYourDocs-RAG/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   ├── upload.py
│   │   └── query.py
│   ├── services/
│   │   ├── loader.py
│   │   ├── chunker.py
│   │   ├── embedder.py
│   │   ├── vector_store.py
│   │   └── llm.py
│   └── models/
│       └── schemas.py
│
├── data/
│   ├── documents/
│   └── faiss_index/
│
├── ui/
│   └── index.html
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions (Windows)

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd KnowYourDocs-RAG
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
uvicorn app.main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🖥 Using the UI

1. Open `ui/index.html` in a browser (Chrome recommended)
2. Upload a **PDF or TXT** document
3. Ask questions related to the document
4. View AI-generated answers

> ⚠️ Backend must be running before using the UI

---

## 🔌 API Endpoints

### Upload Document

```
POST /upload/
```

* Accepts: PDF, TXT
* Processes documents in background

### Ask Question

```
POST /ask/
```

Request body:

```json
{
  "question": "What is this document about?",
  "top_k": 3
}
```

---

## 🧠 How It Works (RAG Flow)

1. User uploads a document
2. Document is parsed and chunked
3. Chunks are embedded and stored in FAISS
4. User question is embedded
5. Top-K relevant chunks are retrieved
6. LLM generates an answer using retrieved context

---

## 🧪 Example Interview Explanation

> "I built a RAG-based QA system using FastAPI where documents are ingested asynchronously, chunked, embedded using Sentence Transformers, stored in FAISS, and queried via semantic similarity. Answers are generated using a fully local FLAN-T5 model with rate limiting and request validation."

---

## 🔮 Future Improvements

* Multi-document namespaces
* Streaming responses
* UI enhancements (show retrieved chunks)
* GPU acceleration
* Docker support
* LangChain integration

---

## ✅ Status

✔ Fully working on Windows
✔ No paid APIs

---

## 👤 Author

**Priyanka Gattu**
Full Stack Developer | Applied AI Enthusiast

---

⭐ If you find this useful, give it a star on GitHub!
