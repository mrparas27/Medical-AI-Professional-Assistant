@echo off
setlocal enabledelayedexpansion

echo.
echo ====================================================
echo   🩺 MEDICAL ASSISTANT - FRONTEND (REACT)
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

cd client

echo Checking React dependencies...
if not exist "node_modules" (
    echo Installing React dependencies (this may take a minute^)...
    call npm install
) else (
    echo ✅ React dependencies already installed
)

echo.
echo ====================================================
echo Starting React development server...
echo App will open at http://localhost:3000
echo.
call npm run dev

pause
