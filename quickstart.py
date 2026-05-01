#!/usr/bin/env python
"""
🩺 MEDICAL ASSISTANT - QUICK START GUIDE
"""

print("""
╔════════════════════════════════════════════════════════════════════╗
║          🩺  MEDICAL ASSISTANT - QUICK START GUIDE               ║
╚════════════════════════════════════════════════════════════════════╝

📋 BEFORE RUNNING:
   1. Create .env file with:
      - PINECONE_API_KEY=your_key
      - GROQ_API_KEY=your_key

🚀 RUN FULL STACK (EASIEST):
   python run_full_stack.py

🏃 RUN SEPARATELY:

   Terminal 1 - Backend:
   python -m uvicorn server.main:app --host 127.0.0.1 --port 8000

   Terminal 2 - Frontend:
   cd client
   streamlit run app.py

🌐 ACCESS:
   Backend:  http://127.0.0.1:8000
   API Docs: http://127.0.0.1:8000/docs
   Frontend: http://localhost:8501

✨ FEATURES:
   ✅ Upload medical PDFs
   ✅ Ask AI questions
   ✅ Get voice responses (TTS)
   ✅ Chat history
   ✅ Multi-language support

🔧 TROUBLESHOOTING:
   Port 8000 in use?
   → taskkill /PID <pid> /F
   
   Module import errors?
   → pip install -r server/requirements.txt
   
   Streamlit not found?
   → pip install streamlit

📚 DOCUMENTATION:
   See QUICK_START.md for detailed setup

═══════════════════════════════════════════════════════════════════════

Ready to go! 🚀
""")

if __name__ == "__main__":
    input("Press Enter to continue...")
