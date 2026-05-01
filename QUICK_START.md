# 🩺 Medical Assistant - AI-Powered Chatbot

A full-stack medical document AI assistant built with FastAPI, Streamlit, Pinecone, and LLM (Groq).

## ✨ Features

- **🔍 RAG System** - Retrieval Augmented Generation using Pinecone vector database
- **📄 PDF Upload** - Upload and process medical documents instantly  
- **💬 AI Chat** - Conversational chat with medical documents
- **🎤 Voice I/O** - Voice input/output (with mic recorder and TTS)
- **🌍 Multi-language** - Auto-translation via deep-translator
- **📊 Chat History** - Save and export conversations
- **🎨 ChatGPT-like UI** - Modern, responsive Streamlit interface

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Pinecone API Key  
- Groq API Key
- `.env` file with configuration

### Installation

1. **Clone or navigate to project**
```bash
cd "C:\Users\Mr Paras Sharma\OneDrive\Desktop\MEDICAL ASSISTANT"
```

2. **Create virtual environment** (if not already done)
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. **Install dependencies**
```bash
pip install -r server/requirements.txt
pip install -r client/requirements.txt
```

### Configuration

Create `.env` file in the root directory:

```env
# Pinecone
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_INDEX_NAME=medicalindex
PINECONE_ENV=us-east-1

# Groq (LLM)
GROQ_API_KEY=your_groq_api_key_here
```

---

## ▶️ Running the Application

### Option 1: Run Full Stack (Recommended)

```bash
python run_full_stack.py
```

This starts both the server and client automatically and opens your browser.

### Option 2: Run Manually

**Terminal 1 - Start FastAPI Server:**
```bash
cd "C:\Users\Mr Paras Sharma\OneDrive\Desktop\MEDICAL ASSISTANT"
python -m uvicorn server.main:app --host 127.0.0.1 --port 8000
```

**Terminal 2 - Start Streamlit Client:**
```bash
cd "C:\Users\Mr Paras Sharma\OneDrive\Desktop\MEDICAL ASSISTANT\client"
streamlit run app.py
```

### Access the Application

- **Backend API**: http://127.0.0.1:8000
- **API Docs**: http://127.0.0.1:8000/docs
- **Streamlit UI**: http://localhost:8501 (or next available port)

---

## 📂 Project Structure

```
MEDICAL ASSISTANT/
├── server/                          # FastAPI Backend
│   ├── main.py                     # App entry point
│   ├── logger.py                   # Logging configuration
│   ├── modules/
│   │   ├── llm.py                 # LLM chain (Groq + LangChain)
│   │   ├── load_vectorstore.py    # PDF processing & Pinecone
│   │   ├── query_handers.py       # Query execution
│   │   └── pdf_handlers.py        # PDF utilities
│   └── routes/
│       ├── upload_pdfs.py         # PDF upload endpoint
│       └── ask_question.py        # Query endpoint
│
├── client/                          # Streamlit Frontend
│   ├── app.py                      # Main UI
│   ├── components/
│   │   ├── chatUI.py              # Chat component
│   │   ├── upload.py              # Upload component
│   │   └── history_download.py    # History export
│   └── utils/
│       ├── api.py                 # API client
│       └── config.py              # Config
│
├── run_full_stack.py               # Full-stack launcher
├── requirements.txt                # Root dependencies
└── .env                            # Configuration (create this)
```

---

## 🔌 API Endpoints

### Upload Documents
```bash
POST /api/upload_pdfs/
Content-Type: multipart/form-data

Request:
files: [PDF file(s)]

Response:
{
  "success": true,
  "message": "Files processed and vectorstore updated",
  "files_count": 1
}
```

### Ask Question
```bash
POST /api/ask/
Content-Type: application/x-www-form-urlencoded

Request:
question=What is diabetes?

Response:
{
  "response": "Based on the medical documents...",
  "confidence": 0.92,
  "sources": ["DIABETES.pdf"]
}
```

---

## 🛠️ Technologies

| Component | Technology |
|-----------|-----------|
| Backend | FastAPI, Python 3.10+ |
| Frontend | Streamlit |
| LLM | Groq (llama-3.1-8b-instant) |
| Vector DB | Pinecone |
| Embeddings | SentenceTransformers (all-MiniLM-L6-v2) |
| PDF Processing | PyPDF2 |
| RAG Framework | LangChain |
| Translation | deep-translator |
| TTS | gTTS |
| Voice Input | streamlit-mic-recorder |

---

## ⚙️ Configuration

### Environment Variables

```env
# Required
PINECONE_API_KEY=<your_api_key>
GROQ_API_KEY=<your_api_key>

# Optional (defaults provided)
PINECONE_INDEX_NAME=medicalindex
PINECONE_ENV=us-east-1
LOG_LEVEL=INFO
```

---

## 🧪 Testing

### Health Check
```bash
curl http://127.0.0.1:8000/
```

### Upload Test
```bash
curl -X POST -F "files=@sample.pdf" http://127.0.0.1:8000/api/upload_pdfs/
```

### Query Test
```bash
curl -X POST -d "question=What is diabetes?" http://127.0.0.1:8000/api/ask/
```

---

## 🐛 Troubleshooting

### Server won't start
- ✅ Check if port 8000 is in use: `netstat -ano | findstr :8000`
- ✅ Kill process: `taskkill /PID <pid> /F`
- ✅ Verify Pinecone credentials in `.env`

### Slow imports
- ✅ Heavy libraries (SentenceTransformers, Pinecone) are lazy-loaded
- ✅ First query will be slower (~15-30s for model loading)
- ✅ Subsequent queries are faster

### Template errors
- ✅ Root endpoint serves JSON, not HTML
- ✅ Streamlit app handles the UI

### Streamlit port conflicts
- ✅ Streamlit auto-selects next available port (8501, 8502, etc.)
- ✅ Check terminal output for actual port

---

## 📈 Performance Tips

1. **Embeddings Caching** - Model is cached after first use
2. **Pinecone Connection Pool** - Reuses connections
3. **Lazy Imports** - Heavy libraries load only when needed
4. **Vector Compression** - Dimension: 384 (all-MiniLM-L6-v2)

---

## 🔐 Security Notes

⚠️ **Development Only** - This setup is for development/demo

- Store API keys in `.env` (never commit!)
- Use environment-specific configs
- Validate user inputs on backend
- Sanitize PDF uploads

---

## 📝 License

Medical Assistant - AI Educational Project

---

## 👨‍💻 Development

### Creating __init__.py files (Python packages)
```
server/__init__.py
server/routes/__init__.py
server/modules/__init__.py
server/middleware/__init__.py
```

### Key Optimizations
- ✅ Relative imports for subpackages
- ✅ Lazy loading of heavy libraries
- ✅ CORS enabled for frontend
- ✅ Structured error handling

---

## 🎯 Next Steps

1. Upload medical PDFs via Streamlit UI
2. Ask questions about the documents
3. Listen to AI responses with TTS
4. Export chat history as JSON

---

**Happy Chatting! 🚀**
