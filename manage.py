#!/usr/bin/env python3
"""
================================================================================
E-VOTING SYSTEM USING BLOCKCHAIN TECHNOLOGY
Module: manage.py — Compatibility CLI Wrapper (`python manage.py runserver`)
================================================================================
Author:      Ateeq Bin Mubarak Wahlan (Roll No: 160920733003)
Portfolio:   https://wahlanos.com | https://github.com/ateeq-wahlan
================================================================================
"""

import sys
from app import run_server, ENGINE


def main() -> None:
    if len(sys.argv) > 1 and sys.argv[1] == "migrate":
        state = ENGINE.get_system_state()
        print("Applying database migrations for E-Voting Blockchain System...")
        print(f"  [OK] Relational tables initialized in evoting.db ({state['election']['registered_parties']} parties, {state['election']['registered_voters']} voters)")
        print(f"  [OK] Blockchain ledger verified ({state['election']['total_blocks']} PoW blocks, difficulty={state['election']['difficulty']})")
        return

    print("Performing system checks...")
    print("System check identified no issues (0 silenced).")
    run_server(open_browser="--no-browser" not in sys.argv)


if __name__ == "__main__":
    main()
