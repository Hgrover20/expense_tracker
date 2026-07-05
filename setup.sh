#!/bin/bash

# Expense Tracker - Quick Start Script for Linux/Mac

echo ""
echo "========================================"
echo "  Expense Tracker with Local LLM"
echo "  Quick Start Script"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.13.2+ from https://python.org"
    exit 1
fi

echo "✓ Python found"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

echo ""
echo "Activating virtual environment..."
source venv/bin/activate

echo ""
echo "Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi
echo "✓ Dependencies installed"

echo ""
echo "========================================"
echo "  Setup Complete!"
echo "========================================"
echo ""
echo "Before starting the server:"
echo ""
echo "1. Make sure Ollama is running:"
echo "   - Download from https://ollama.ai"
echo "   - Run: ollama pull qwen3:8b"
echo ""
echo "2. Start Ollama service (if not already running)"
echo ""
echo "3. Start the server:"
echo "   python main.py"
echo ""
echo "4. Open browser to:"
echo "   http://localhost:8000"
echo ""
