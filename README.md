# CivicChain // E-Voting System Using Blockchain Technology (2023–2024)

<div align="center">

[![Live Interactive Demo](https://img.shields.io/badge/%F0%9F%97%B3%EF%B8%8F_LIVE_INTERACTIVE_DEMO-LAUNCH_IN_BROWSER-0D9488?style=for-the-badge&logoColor=white)](https://ateeq-wahlan.github.io/E-Voting-System-Blockchain/)
[![GitHub Codespaces](https://img.shields.io/badge/%E2%98%81%EF%B8%8F_GITHUB_CODESPACES-RUN_PYTHON_BACKEND-0B1528?style=for-the-badge&logo=github&logoColor=white)](https://codespaces.new/ateeq-wahlan/E-Voting-System-Blockchain)
[![Portfolio](https://img.shields.io/badge/ARCHITECT_PORTFOLIO-WAHLANOS.COM-1D4ED8?style=for-the-badge)](https://wahlanos.com)

**Cryptographic trust. Verifiable civic democracy.**  
*A Decentralized Electronic Voting Platform powered by an Interactive Atomic Consensus Core, SHA-256 Proof-of-Work Blockchain (`difficulty = 2`), Additive Homomorphic Ballot Commitments, Zero-Knowledge Voter Nullifiers, Role-Based Electoral Commission Governance (`Form-2A/2B` & `Form-6/7`), and 320×240 Human Face Biometric Verification.*

</div>

---

## ⚡ Run Instantly Without Cloning

You can explore the complete **CivicChain E-Voting Blockchain Platform** right now in your browser—no local installation or database setup required:

1. **🌐 Zero-Install Interactive Web App (GitHub Pages):**  
   👉 **[Launch Live E-Voting Blockchain Platform (`index.html`)](https://ateeq-wahlan.github.io/E-Voting-System-Blockchain/)**  
   *(Includes the 60fps Interactive Atomic Consensus Reactor, Role-Based Access Control (`Public Viewer` vs. `EC Admin Authority`), Form-2A Party Gazette Registration, Form-2B Party Mandate Revocation, Form-6 Voter Enrollment, Form-7 Electoral Roll Delisting, Interactive Human Face Biometric Scan Popup Modal, Live Proof-of-Work Block Mining, Zero-Knowledge Receipt Verifier, and Tamper Attack Lab).*
2. **☁️ One-Click Cloud Python Environment (GitHub Codespaces):**  
   👉 **[Open in GitHub Codespaces](https://codespaces.new/ateeq-wahlan/E-Voting-System-Blockchain)** to run the Python backend (`app.py` / `manage.py`), SQLite database (`evoting.db`), and pickled blockchain ledger (`blockchain_ledger.pkl`) in a live cloud container.

---

## 🏛️ Academic & Architect Attribution

| Attribute | Details |
| :--- | :--- |
| **Project Title** | **CivicChain // E-Voting System Using Blockchain Technology** |
| **Author / Architect** | **Ateeq Bin Mubarak Wahlan** |
| **University Roll No.** | **`160920733003`** |
| **Degree & Branch** | Bachelor of Engineering (B.E.) — Computer Science and Engineering |
| **Institution** | **LIET (Osmania University)**, Hyderabad |
| **Project Year** | **2023–2024** |
| **Web & GitHub** | **[wahlanos.com](https://wahlanos.com)** • **[github.com/ateeq-wahlan](https://github.com/ateeq-wahlan)** |

---

## ✨ Key Architectural Highlights

- **Interactive 60fps Atomic Consensus Reactor:** Live orbital visualization on the homepage where the central ballot nucleus is orbited by 4 interactive cryptographic subsystems (**`CV BIOMETRICS`**, **`SHA-256 POW`**, **`ZK NULLIFIER`**, and **`HOMOMORPHIC ZKP`**)—click or hover any orbiting node to inspect real-time protocol telemetry.
- **Role-Based Access Control (`Public Viewer Scope` vs. `EC Admin Authority Scope`):**
  - **Public Viewer Mode (Default):** Masks sensitive citizen PII (`contact`, `email`) in the electoral roll while allowing full public verification of blockchain hashes, live tallies, and Zero-Knowledge ballot receipts.
  - **EC Admin Authority Mode (`admin` / `admin`):** Unlocks administrative mutation operations (**Form-2A Party Registration**, **Form-2B Party Mandate Revocation**, **Form-7 Voter Roll Delisting**, and **Election Baseline Reset**) and unmasks full electoral roll records.
- **Statutory Electoral Governance (`Form-2B` Party Deletion & `Form-7` Voter Delisting):**
  - **Form-2B Electoral Mandate Revocation:** Deregisters a political party candidate from the active `addparty` ballot sheet under official statutory grounds (*RP Act Sec. 37 Candidacy Withdrawal*, *MCC Disqualification*, etc.).
  - **Form-7 Electoral Roll Delisting:** Revokes a citizen's off-chain registration and polling-booth biometric credential while preserving on-chain cryptographic immutability for any historical anonymous ballot (`zk_nullifier_...`).
- **Interactive Human Face Biometric Scan Popup Modal:** Clicking any citizen profile (including voters who have **already voted** as well as eligible voters) launches an optical biometric verification modal displaying their real human photograph, EPIC ID (`TS/HYD/160920/...`), animated laser landmark scan (`Take Snapshot (320×240)` → `Validate User`), and—for voters who already cast their ballot—their immutable Proof-of-Work Blockchain Receipt.

---

## 📂 Repository Structure

```text
EVoting/
├── index.html                      # Standalone + Backend-connected 5-Tab Interactive Web App
├── WORKFLOW_DOCUMENTATION.md       # End-to-End Architecture & Viva Walkthrough Guide
├── Block.py                        # Core SHA-256 Block Structure & compute_hash()
├── Blockchain.py                   # Proof-of-Work Ledger, BallotCipher & Chain Integrity Audit
├── evoting_engine.py               # SQLite + Blockchain Ledger Orchestrator (Form-2A/2B & Form-6/7)
├── app.py                          # Zero-Dependency Python HTTP & REST JSON Server (Port 5070)
├── manage.py                       # CLI Wrapper (`python manage.py runserver` / `migrate`)
├── database.sql                    # Full MySQL / SQLite Schema (register, addparty & 3NF tables)
├── test_evoting.py                 # Automated Verification Test Suite (PoW, RBAC, Form-2B/7, Tamper)
├── Run_EVoting.command             # One-Click macOS Native Launcher
├── run.bat                         # One-Click Windows Launcher
├── requirements.txt                # Zero external dependencies required (Python 3 stdlib)
├── .devcontainer/devcontainer.json # One-Click GitHub Codespaces Cloud Configuration
└── static/
    ├── evoting_logo.svg            # Custom Isometric Ballot-Box & Blockchain Vector Emblem
    ├── wahlanos_evoting.css        # CivicChain Electoral Design System (Space Grotesk + IBM Plex Mono)
    └── parties/                    # 8 High-Resolution Party Symbol Vector Emblems (SVG)
```

---

## 🚀 Local Quick Start (macOS, Windows & Linux)

### Option A — Instant Browser Launch (Zero Setup)
Double-click **`index.html`** in Finder or File Explorer to open the interactive application directly in your browser.

### Option B — Full Python Backend + SQLite + Pickle Ledger
```bash
# 1. Verify database migrations & blockchain state
python3 manage.py migrate

# 2. Run the automated cryptographic verification test suite
python3 test_evoting.py

# 3. Launch the E-Voting server on http://127.0.0.1:5070
python3 app.py
```
*(On macOS, you can also simply double-click **`Run_EVoting.command`**; on Windows, double-click **`run.bat`**).*

---

<div align="center">
  <sub>Architected by <strong>Ateeq Bin Mubarak Wahlan (160920733003)</strong> • <strong>LIET (Osmania University) • 2023–2024</strong> • <a href="https://wahlanos.com">wahlanos.com</a> • <a href="https://github.com/ateeq-wahlan">github.com/ateeq-wahlan</a></sub>
</div>
