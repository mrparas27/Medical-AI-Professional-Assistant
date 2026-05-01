# 🚀 Quick Start Guide - Medical Assistant

## System Requirements
- Python 3.8+
- pip or conda
- 4GB RAM minimum
- Internet connection (for API calls to Groq, Google, and Pinecone)

## ✅ Prerequisites Setup

### 1. Environment Variables
The `.env` file in the `server/` directory should already contain:
```
GOOGLE_API_KEY=your_key
GROQ_API_KEY=your_key
PINECONE_API_KEY=your_key
PINECONE_INDEX_NAME=your_index
```

If not, create it with your API keys from:
- 🔑 GROQ_API_KEY: https://console.groq.com
- 🔑 GOOGLE_API_KEY: https://makersuite.google.com/app/apikey
- 🔑 PINECONE_API_KEY: https://app.pinecone.io

---

## 🎯 Running the Application

### **Option 1: Windows Users (Recommended)**
Simply double-click the batch file in the project root:
```
run.bat
```

Or run in PowerShell:
```powershell
cd "C:\Users\Mr Paras Sharma\OneDrive\Desktop\MEDICAL ASSISTANT"
.\run.bat
```

### **Option 2: Mac/Linux Users**
Make the script executable and run:
```bash
chmod +x run.sh
./run.sh
```

### **Option 3: Manual Python Execution**
From the project root directory:
```bash
# Activate virtual environment
# Windows:
.venv\Scripts\activate

# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r server/requirements.txt

# Start the server
cd server
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

### **Option 4: Using Python Run Script**
```bash
python run.py
```

---

## 🌐 Access the Application

Once the server starts, open your browser and go to:

**👉 http://127.0.0.1:8000**

You should see the Medical Assistant UI with:
- 📄 **Upload Section** (left sidebar)
  - Upload medical PDFs
  - Drag & drop support
  
- 💬 **Chat Section** (main area)
  - Interactive chat interface
  - Real-time responses
  - Source document links

---

## 📋 Usage Instructions

### **Step 1: Upload Documents**
1. Click "📁 Click or drag PDF files here" or drag PDFs into the area
2. Click "Upload PDFs" button
3. Wait for "✓ Uploaded successfully" message

### **Step 2: Ask Questions**
1. Type your medical question in the chat input box
2. Click "Send" or press Enter
3. The AI will search your uploaded documents and provide an answer
4. Sources will be displayed below each response

### **Step 3: View Chat History**
- All messages are displayed in the chat area
- Scroll up to see previous conversations
- Session is cleared when page is refreshed

---

## 🔧 Troubleshooting

### **Problem: "Connection refused" error**
- Ensure the server is running
- Check that port 8000 is not in use: `netstat -an | findstr 8000`
- Try a different port: `python -m uvicorn main:app --port 8001`

### **Problem: "API Key not found"**
- Verify `.env` file exists in `/server` directory
- Check that all required keys are set
- Restart the server after updating `.env`

### **Problem: "Module not found" errors**
- Activate the virtual environment
- Reinstall dependencies: `pip install -r server/requirements.txt`

### **Problem: Slow responses**
- This is normal for the first response (model initialization)
- Subsequent requests will be faster
- Check your internet connection
- Ensure API keys are valid

### **Problem: Files won't upload**
- Ensure files are in PDF format
- Check file size (should be reasonable)
- Try uploading fewer files at once

---

## 📊 Project Structure
```
MEDICAL ASSISTANT/
├── run.py              # Python launcher script
├── run.bat             # Windows batch script
├── run.sh              # Mac/Linux shell script
├── server/
│   ├── main.py         # FastAPI application
│   ├── requirements.txt # Python dependencies
│   ├── .env            # Environment variables
│   ├── routes/         # API endpoints
│   ├── modules/        # Core logic
│   ├── middleware/     # Error handling
│   ├── templates/      # HTML/JavaScript UI
│   └── logger.py       # Logging setup
└── client/
    ├── app.py          # Streamlit alternative UI (optional)
    ├── components/     # UI components
    └── utils/          # API utilities
```

---

## 🛠️ API Endpoints

### Upload PDFs
```bash
POST /upload_pdfs/
Content-Type: multipart/form-data

files: [file1.pdf, file2.pdf, ...]
```

### Ask Question
```bash
POST /ask/
Content-Type: application/x-www-form-urlencoded

question=Your+medical+question+here
```

**Response:**
```json
{
  "response": "AI-generated answer based on your documents",
  "sources": ["source1.pdf", "source2.pdf"]
}
```

---

## 🌟 Features

✅ **Drag & Drop File Upload** - Intuitive PDF upload
✅ **Real-time Chat** - Instant AI responses
✅ **Source Attribution** - Know where answers come from
✅ **Error Handling** - Graceful error messages
✅ **Responsive Design** - Works on desktop and tablet
✅ **Loading States** - Visual feedback during processing
✅ **Auto-scroll Chat** - Latest messages always visible

---

## 📞 Support

For issues or questions:
1. Check the **Troubleshooting** section above
2. Review server logs in the terminal
3. Ensure all API keys are valid
4. Check internet connectivity

---

**Happy Chatting! 🩺💬**

Last Updated: 2024
