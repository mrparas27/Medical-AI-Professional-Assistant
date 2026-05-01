#!/usr/bin/env python
"""
🩺 MEDICAL ASSISTANT - FULL STACK LAUNCHER
Complete application startup script
"""

import os
import sys
import time
import subprocess
import webbrowser
import atexit
from pathlib import Path

# ============================================================
# CONFIGURATION
# ============================================================
ROOT_DIR = Path(__file__).resolve().parent
SERVER_DIR = ROOT_DIR / "server"
CLIENT_DIR = ROOT_DIR / "client"

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8000
SERVER_URL = f"http://{SERVER_HOST}:{SERVER_PORT}"

CLIENT_PORT = 8501

# ============================================================
# COLORS (Terminal Output)
# ============================================================
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

def print_banner():
    """Print startup banner"""
    banner = f"""
{Colors.BOLD}{Colors.OKCYAN}
{'='*60}
🩺  MEDICAL ASSISTANT - AI-POWERED CHATBOT
{'='*60}
{Colors.ENDC}

📂 Project Root: {ROOT_DIR}
📂 Server Dir: {SERVER_DIR}
📂 Client Dir: {CLIENT_DIR}

🌐 Server URL: {SERVER_URL}
💻 Streamlit URL: http://localhost:{CLIENT_PORT}

Press Ctrl+C to stop all services
{Colors.OKCYAN}{'='*60}{Colors.ENDC}
    """
    print(banner)

def start_server():
    """Start FastAPI server"""
    print(f"\n{Colors.BOLD}⏳ Starting FastAPI Server...{Colors.ENDC}")
    try:
        server_process = subprocess.Popen(
            [
                sys.executable, "-m", "uvicorn",
                "server.main:app",
                "--host", SERVER_HOST,
                "--port", str(SERVER_PORT),
                "--log-level", "info"
            ],
            cwd=ROOT_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"{Colors.OKGREEN}✅ FastAPI Server started (PID: {server_process.pid}){Colors.ENDC}")
        return server_process
    except Exception as e:
        print(f"{Colors.FAIL}❌ Failed to start server: {str(e)}{Colors.ENDC}")
        sys.exit(1)

def wait_for_server(timeout=30):
    """Wait for server to be ready"""
    import socket
    start_time = time.time()
    
    print(f"\n{Colors.BOLD}⏳ Waiting for server to start...{Colors.ENDC}")
    
    while time.time() - start_time < timeout:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((SERVER_HOST, SERVER_PORT))
            sock.close()
            
            if result == 0:
                print(f"{Colors.OKGREEN}✅ Server is ready!{Colors.ENDC}")
                return True
        except:
            pass
        
        time.sleep(0.5)
    
    print(f"{Colors.FAIL}❌ Server did not start within {timeout} seconds{Colors.ENDC}")
    return False

def start_client():
    """Start Streamlit client"""
    print(f"\n{Colors.BOLD}⏳ Starting Streamlit Client...{Colors.ENDC}")
    try:
        client_process = subprocess.Popen(
            [
                sys.executable, "-m", "streamlit", "run",
                str(CLIENT_DIR / "app.py"),
                "--logger.level=warning"
            ],
            cwd=CLIENT_DIR,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"{Colors.OKGREEN}✅ Streamlit Client started (PID: {client_process.pid}){Colors.ENDC}")
        return client_process
    except Exception as e:
        print(f"{Colors.FAIL}❌ Failed to start client: {str(e)}{Colors.ENDC}")
        return None

def open_browser():
    """Open web browser to client"""
    time.sleep(3)
    print(f"\n{Colors.BOLD}🌐 Opening browser...{Colors.ENDC}")
    try:
        webbrowser.open(f"http://localhost:{CLIENT_PORT}")
        print(f"{Colors.OKGREEN}✅ Browser opened{Colors.ENDC}")
    except Exception as e:
        print(f"{Colors.WARNING}⚠️  Could not open browser: {str(e)}{Colors.ENDC}")

def cleanup(server_process, client_process):
    """Cleanup on exit"""
    print(f"\n\n{Colors.WARNING}{'='*60}")
    print("🛑 Shutting down services...{Colors.ENDC}")
    
    try:
        if server_process and server_process.poll() is None:
            print("Stopping FastAPI server...")
            server_process.terminate()
            server_process.wait(timeout=5)
            print(f"{Colors.OKGREEN}✅ Server stopped{Colors.ENDC}")
    except:
        if server_process:
            server_process.kill()
    
    try:
        if client_process and client_process.poll() is None:
            print("Stopping Streamlit client...")
            client_process.terminate()
            client_process.wait(timeout=5)
            print(f"{Colors.OKGREEN}✅ Client stopped{Colors.ENDC}")
    except:
        if client_process:
            client_process.kill()
    
    print(f"{Colors.OKGREEN}✅ All services stopped{Colors.ENDC}")
    print(f"{Colors.WARNING}{'='*60}{Colors.ENDC}\n")

def main():
    """Main entry point"""
    print_banner()
    
    # Start server
    server_process = start_server()
    
    # Wait for server
    if not wait_for_server():
        server_process.kill()
        sys.exit(1)
    
    # Start client
    client_process = start_client()
    
    # Register cleanup
    def on_exit():
        cleanup(server_process, client_process)
    
    atexit.register(on_exit)
    
    # Open browser
    open_browser()
    
    print(f"\n{Colors.OKGREEN}{'='*60}")
    print("🚀 MEDICAL ASSISTANT IS READY!")
    print(f"{Colors.ENDC}")
    print(f"Server: {SERVER_URL}")
    print(f"Client: http://localhost:{CLIENT_PORT}")
    print(f"{Colors.OKGREEN}{'='*60}{Colors.ENDC}\n")
    
    # Keep running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()
