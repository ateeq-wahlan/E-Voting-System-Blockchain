@echo off
REM ============================================================================
REM 1-CLICK GIT REPOSITORY INITIALIZER (ATEEQ BIN MUBARAK WAHLAN - 160920733003)
REM Double-click this file if GitHub Desktop says "does not appear to be a Git repository"
REM ============================================================================
cd /d "%~dp0"
echo Initializing Git Repository under Ateeq Bin Mubarak Wahlan...
git init -b main
git config user.name "Ateeq Bin Mubarak Wahlan"
git config user.email "ateeq-wahlan@users.noreply.github.com"
git add -A
git commit -m "feat(sec03): launch CivicChain E-Voting Blockchain System (Ateeq Bin Mubarak Wahlan - 160920733003)"
echo.
echo ============================================================================
echo SUCCESS! This folder is now a valid Git repository under Ateeq Wahlan.
echo Go back to GitHub Desktop -> Add Local Repository -> Select this folder!
echo ============================================================================
pause
