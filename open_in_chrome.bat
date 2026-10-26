@echo off
REM ============================================================================
REM CIVICCHAIN // E-VOTING BLOCKCHAIN — 1-CLICK GOOGLE CHROME LAUNCHER (WINDOWS)
REM Architect: Ateeq Bin Mubarak Wahlan (Roll No: 160920733003)
REM ============================================================================
cd /d "%~dp0"
start chrome "%~dp0index.html" 2>nul || start "" "%~dp0index.html"
