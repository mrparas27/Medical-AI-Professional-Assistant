#!/bin/bash

# Medical Assistant - Unix/Mac Run Script
# This script activates the virtual environment and runs the application

echo ""
echo "============================================================"
echo "  Starting Medical Assistant - AI-Powered Chatbot"
echo "============================================================"
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install requirements if needed
echo "Installing/updating dependencies..."
pip install -q -r server/requirements.txt

# Start the application
echo ""
echo "Starting FastAPI server..."
echo "Server will be available at: http://127.0.0.1:8000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

cd server
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
