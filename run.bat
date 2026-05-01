@echo off
REM Medical Assistant - Windows Run Script
REM This script activates the virtual environment and runs the application

echo.
echo ============================================================
echo  Starting Medical Assistant - AI-Powered Chatbot
echo ============================================================
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Install requirements if needed
echo Installing/updating dependencies...
pip install -q -r server/requirements.txt

REM Start the application
echo.
echo Starting FastAPI server...
echo Server will be available at: http://127.0.0.1:8000
echo.
echo Press Ctrl+C to stop the server
echo.

cd server
python -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload

pause
