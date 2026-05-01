#!/usr/bin/env python
"""
Medical Assistant - Full Stack Application Launcher (UPGRADED)
Starts FastAPI backend + opens browser automatically
"""

import os
import sys
import subprocess
import webbrowser
from pathlib import Path
import time
import threading


def install_dependencies():
    """Install required packages if missing"""
    print("\n📦 Checking dependencies...")

    required_packages = [
        "fastapi",
        "uvicorn",
        "langchain",
        "pinecone",
        "sentence-transformers",
        "python-dotenv",
        "PyPDF2"
    ]

    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
        except ImportError:
            print(f"📥 Installing {package}...")
            subprocess.run(
                [sys.executable, "-m", "pip", "install", package],
                check=False
            )


def run_medical_assistant():
    """Start the Medical Assistant application"""

    project_root = Path(__file__).parent
    server_dir = project_root / "server"

    if not server_dir.exists():
        print("❌ Server directory not found!")
        sys.exit(1)

    # Step 1: Install dependencies
    install_dependencies()

    # Step 2: Add server path (IMPORTANT FIX)
    sys.path.append(str(project_root))

    print("\n" + "=" * 60)
    print("🩺  MEDICAL ASSISTANT - AI CHATBOT (UPGRADED)")
    print("=" * 60)
    print(f"\n📂 Project Root: {project_root}")
    print(f"📂 Server Dir: {server_dir}")

    print("\n⏳ Starting FastAPI server...")
    print("🌐 URL: http://127.0.0.1:8000")
    print("\nPress CTRL + C to stop\n")

    try:
        import uvicorn
        from server.main import app  # FIXED IMPORT

        # Auto open browser
        def open_browser():
            time.sleep(2)
            print("\n🌐 Opening browser...")
            webbrowser.open("http://127.0.0.1:8000")

        threading.Thread(target=open_browser, daemon=True).start()

        # Run server
        uvicorn.run(
            app,
            host="127.0.0.1",
            port=8000,
            log_level="info"
        )

    except KeyboardInterrupt:
        print("\n✋ Server stopped by user")

    except Exception as e:
        print("\n❌ Error starting application:")
        print(str(e))
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    run_medical_assistant()