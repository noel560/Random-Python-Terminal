@echo off
title Downloading and Installing Requirements
color 0A

echo Checking if Python is installed...
python --version >nul 2>&1
if errorlevel 1 (
    color 0C
    echo ERROR: Python is not installed or not in PATH!
    pause
    exit /b
)

echo Checking if pip is installed...
pip --version >nul 2>&1
if errorlevel 1 (
    color 0C
    echo ERROR: pip is not installed or not in PATH!
    pause
    exit /b
)

echo.
echo Downloading and installing requirements...
pip install -r requirements.txt

if errorlevel 1 (
    color 0C
    echo ERROR: Failed to install requirements!
) else (
    color 0A
    echo Successfully installed requirements!
)

echo.
pause
