#!/bin/bash

echo ""
echo "===================================================="
echo "  🩺 MEDICAL ASSISTANT - FRONTEND ONLY"
echo "===================================================="
echo ""

# Check if Node is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js from https://nodejs.org/"
    exit 1
fi

echo "✅ Node.js found"
echo ""

cd client

echo "Checking React dependencies..."
if [ ! -d "node_modules" ]; then
    echo "Installing React dependencies (this may take a minute)..."
    npm install
else
    echo "✅ React dependencies already installed"
fi

echo ""
echo "===================================================="
echo "Starting React development server..."
echo "App will open at http://localhost:3000"
echo ""
npm run dev
