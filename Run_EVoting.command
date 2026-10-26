#!/bin/bash
# ==============================================================================
# E-VOTING SYSTEM USING BLOCKCHAIN TECHNOLOGY // ONE-CLICK MACOS LAUNCHER
# Architect: Ateeq Bin Mubarak Wahlan (Roll No: 160920733003)
# WahlanOS.com ↗ (https://wahlanos.com) | GitHub: https://github.com/ateeq-wahlan
# ==============================================================================

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$DIR"

echo "=============================================================================="
echo "  E-VOTING SYSTEM USING BLOCKCHAIN TECHNOLOGY // WAHLANOS LEDGER"
echo "  Architect: Ateeq Bin Mubarak Wahlan (Roll No: 160920733003)"
echo "  WahlanOS.com ↗ (https://wahlanos.com) | GitHub: https://github.com/ateeq-wahlan"
echo "=============================================================================="

# Free port 5070 if an older instance is running
lsof -ti:5070 | xargs kill -9 2>/dev/null || true

python3 app.py
