@echo off
setlocal enabledelayedexpansion

echo.
echo ====================================================
echo   🩺 MEDICAL ASSISTANT - BACKEND SERVER
echo ====================================================
echo.

REM Check if Python is installed
where python >nul 2>nul
if !errorlevel! neq 0 (
    echo ❌ Python not found. Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo ✅ Python found
echo.

REM Check and activate virtual environment
if not exist ".venv" (
    echo Creating Python virtual environment...
    python -m venv .venv
)

echo Activating virtual environment...
call .venv\Scripts\activate.bat

echo.
echo Starting backend server on http://127.0.0.1:8000...
echo.

REM Run with module path (fixes import issues)
python -m uvicorn server.main:app --host 127.0.0.1 --port 8000 --reload

pause
