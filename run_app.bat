@echo off
REM Medical Assistant - Full Stack Runner (Windows)
REM This script starts both backend and frontend

setlocal enabledelayedexpansion

echo.
echo ============================================================
echo   Medical Assistant - Full Stack Launcher
echo ============================================================
echo.

cd /d "C:\Users\Mr Paras Sharma\OneDrive\Desktop\MEDICAL ASSISTANT"

echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found in PATH
    pause
    exit /b 1
)

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Starting FastAPI Server on http://127.0.0.1:8000...
start "Medical Assistant - Server" cmd /k "python -m uvicorn server.main:app --host 127.0.0.1 --port 8000"

timeout /t 3 /nobreak

echo Starting Streamlit Client on http://localhost:8501...
start "Medical Assistant - Client" cmd /k "cd client && streamlit run app.py"

timeout /t 3 /nobreak

echo.
echo ============================================================
echo Application is starting...
echo.
echo Backend:  http://127.0.0.1:8000
echo Frontend: http://localhost:8501
echo API Docs: http://127.0.0.1:8000/docs
echo.
echo Close these windows to stop the application
echo ============================================================
echo.
