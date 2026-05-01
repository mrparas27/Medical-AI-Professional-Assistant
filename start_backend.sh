#!/bin/bash

echo ""
echo "===================================================="
echo "  🩺 MEDICAL ASSISTANT - BACKEND ONLY"
echo "===================================================="
echo ""

# Check if Python virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Creating Python virtual environment..."
    python -m venv .venv
fi

# Activate Python environment
source .venv/bin/activate

# Start backend server
echo "Starting backend server on http://127.0.0.1:8000..."
echo ""

python -m uvicorn server.main:app --host 127.0.0.1 --port 8000 --reload
