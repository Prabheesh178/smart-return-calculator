@echo off
TITLE Smart Git Uploader
CLS

:: Check if this is a new or existing project
IF EXIST ".git" GOTO UPDATE_EXISTING

:SETUP_NEW
echo ==========================================
echo      SETTING UP NEW REPO
echo ==========================================
echo.

:: 1. Create .gitignore
echo Creating .gitignore file...
echo __pycache__/ > .gitignore
echo *.json >> .gitignore
echo .venv/ >> .gitignore

:: 2. Initialize Git
echo Initializing Git...
git init
git add .
git commit -m "First commit"
git branch -M main

:: 3. Connect to GitHub
echo.
echo PASTE YOUR REPO URL BELOW (Right-Click to Paste):
set /p repo_url="URL: "

echo.
echo Connecting to GitHub...
git remote add origin %repo_url%
git push -u origin main

echo.
echo [SUCCESS] Project is LIVE!
pause
EXIT

:UPDATE_EXISTING
echo ==========================================
echo      UPDATING EXISTING REPO
echo ==========================================
echo.

git add .
set /p commit_msg="Enter commit message: "
git commit -m "%commit_msg%"
git push

echo.
echo [SUCCESS] Changes Uploaded!
pause
EXIT