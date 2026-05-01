#!/bin/bash

echo ""
echo "===================================================="
echo "  🩺 MEDICAL ASSISTANT - BACKEND SERVER (FIXED)"
echo "===================================================="
echo ""

# Check if Python virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Creating Python virtual environment..."
    python -m venv .venv
fi

# Activate Python environment
source .venv/bin/activate

# Install dependencies
echo "Installing backend dependencies..."
cd server
pip install -r requirements.txt > /dev/null 2>&1
cd ..

echo ""
echo "Starting backend server on http://127.0.0.1:8000..."
echo ""

# Run with module path (fixes import issues)
python -m uvicorn server.main:app --host 127.0.0.1 --port 8000 --reload
