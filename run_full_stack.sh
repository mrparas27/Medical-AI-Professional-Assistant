#!/bin/bash

echo ""
echo "===================================================="
echo "  🩺 MEDICAL ASSISTANT - FULL STACK STARTUP"
echo "===================================================="
echo ""

# Check if Node is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js from https://nodejs.org/"
    exit 1
fi

echo "✅ Node.js found"
echo ""

# Check if Python virtual environment exists
if [ ! -d "server/.venv" ]; then
    echo "Creating Python virtual environment..."
    python -m venv server/.venv
fi

# Activate Python environment
if [ -d "server/.venv" ]; then
    source server/.venv/bin/activate
fi

# Start Backend Server
echo "Starting backend server..."
echo ""
(python -m uvicorn server.main:app --host 127.0.0.1 --port 8000 --reload) &
BACKEND_PID=$!

# Wait for backend to start
echo "Waiting 3 seconds for backend to initialize..."
sleep 3

# Install React dependencies if needed
echo ""
echo "Checking React dependencies..."
cd client
if [ ! -d "node_modules" ]; then
    echo "Installing React dependencies..."
    npm install
else
    echo "✅ React dependencies already installed"
fi

echo ""
echo "===================================================="
echo "Starting React development server..."
echo ""
npm run dev

# Cleanup on exit
trap "kill $BACKEND_PID" EXIT
