# 📘 PDF Chatter

**PDF Chatter** is a lightweight tool inspired by [Google NotebookLM](https://notebooklm.google/), designed to help you **chat with your PDFs**, especially in Vietnamese. It's your personal document assistant — ask questions, take notes, and get instant answers, all in one place.

---

## ✨ Features

- 💬 **Chat with PDFs**: Ask questions and get accurate answers from your uploaded PDF documents — optimized for Vietnamese.
- 📝 **Note-Taking**: Write your own notes, or let the AI generate helpful summaries and insights for you.
- 🔍 **Semantic Search**: Find relevant information quickly with advanced vector search technology.
- 🧠 **RAG Architecture**: Uses Retrieval Augmented Generation for more accurate and contextual responses.

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/vuminhoang/chat-with-pdf-v2.git
cd chat-with-pdf-v2

# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn main:app --reload
```

## 📁 Project Structure

```
chat-with-pdf-v2/ 
├── main.py                      # FastAPI app (entrypoint)
├── api/                        
│   └── routes.py                # Upload PDF, Q&A endpoints
├── core/                       
│   ├── pdf_reader.py            # Extract text from PDFs
│   ├── chunker.py               # Split text into chunks
│   ├── embedder.py              # Use sentence-transformers/OpenAI for embeddings
│   ├── vectordb.py              # FAISS or Chroma vector database
│   └── qa_pipeline.py           # RAG: retrieve + generate
├── models/                      # Schema input/output models
├── data/                        # Store processed PDFs
├── vector_store/                # Store FAISS/Chroma indices
└── requirements.txt             # Project dependencies
```

## 🔧 Usage

1. Start the server with `uvicorn main:app --reload`
2. Access the API at `http://localhost:8000`
3. Upload PDFs via the `/upload-pdf` endpoint
4. Ask questions about your PDFs via the `/ask` endpoint

## 🛠️ API Endpoints

- `POST /upload-pdf`: Upload a PDF file for processing
- `POST /ask`: Ask a question about the uploaded PDF(s)
