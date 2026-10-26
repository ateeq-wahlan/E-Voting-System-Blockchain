@echo off
REM ============================================================================
REM E-VOTING SYSTEM USING BLOCKCHAIN TECHNOLOGY // WINDOWS ONE-CLICK LAUNCHER
REM Architect: Ateeq Bin Mubarak Wahlan (Roll No: 160920733003)
REM Web: https://wahlanos.com | GitHub: https://github.com/ateeq-wahlan
REM ============================================================================
cd /d "%~dp0"
echo Starting E-Voting Blockchain Server on http://127.0.0.1:5070 ...
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python app.py
) else (
    start "" "%~dp0index.html"
)
