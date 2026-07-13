@echo off
REM Expense Tracker - Quick Start Script for Windows

echo.
echo ========================================
echo   Expense Tracker with Local LLM
echo   Quick Start Script for Windows
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.13.2+ from https://python.org
    pause
    exit /b 1
)

echo ✓ Python found
echo.

REM Check if virtual environment exists
if not exist venv (
    echo Creating Python virtual environment...
    python -m venv venv
    echo ✓ Virtual environment created
) else (
    echo ✓ Virtual environment already exists
)

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)
echo ✓ Dependencies installed

echo.
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo Before starting the server:
echo.
echo 1. Make sure Ollama is running:
echo    - Download from https://ollama.ai
echo    - Run: ollama pull qwen2.5:3b
echo.
echo 2. Start Ollama service (if not already running)
echo.
echo 3. Start the server:
echo    python main.py
echo.
echo 4. Open browser to:
echo    http://localhost:8000
echo.
pause
