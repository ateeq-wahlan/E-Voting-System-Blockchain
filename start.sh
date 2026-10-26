#!/bin/bash
# ==============================================================================
# E-VOTING SYSTEM USING BLOCKCHAIN TECHNOLOGY // LINUX & MACOS LAUNCHER
# Architect: Ateeq Bin Mubarak Wahlan (Roll No: 160920733003)
# Web: https://wahlanos.com | GitHub: https://github.com/ateeq-wahlan
# ==============================================================================
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"
lsof -ti:5070 | xargs kill -9 2>/dev/null || true
python3 app.py
