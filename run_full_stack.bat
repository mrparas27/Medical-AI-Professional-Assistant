@echo off
setlocal enabledelayedexpansion

echo.
echo ====================================================
echo   🩺 MEDICAL ASSISTANT - FULL STACK STARTUP
echo ====================================================
echo.

REM Check if Node is installed
where node >nul 2>nul
if !errorlevel! neq 0 (
    echo ❌ Node.js not found. Please install Node.js from https://nodejs.org/
    pause
    exit /b 1
)

echo ✅ Node.js found
echo.

REM Start Backend Server
echo Starting backend server...
echo.
start cmd /k "python -m uvicorn server.main:app --host 127.0.0.1 --port 8000 --reload"

REM Wait for backend to start
echo Waiting 3 seconds for backend to initialize...
timeout /t 3 /nobreak

REM Install React dependencies if needed
echo.
echo Checking React dependencies...
cd client
if not exist "node_modules" (
    echo Installing React dependencies...
    call npm install
) else (
    echo ✅ React dependencies already installed
)

echo.
echo ====================================================
echo Starting React development server...
echo.
call npm run dev

echo.
pause
