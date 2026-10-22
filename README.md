# E-Voting System Using Blockchain Technology

<div align="center">

[![Live Interactive Demo](https://img.shields.io/badge/%F0%9F%9A%80_LIVE_INTERACTIVE_DEMO-LAUNCH_IN_BROWSER-2238FF?style=for-the-badge&logoColor=white)](https://ateeq-wahlan.github.io/E-Voting-System-Blockchain/)
[![GitHub Codespaces](https://img.shields.io/badge/%E2%98%81%EF%B8%8F_GITHUB_CODESPACES-RUN_PYTHON_BACKEND-14161B?style=for-the-badge&logo=github&logoColor=white)](https://codespaces.new/ateeq-wahlan/E-Voting-System-Blockchain)
[![Academic Monograph](https://img.shields.io/badge/%F0%9F%93%94_PROJECT_MONOGRAPH-9_CHAPTER_REPORT-059669?style=for-the-badge)](https://ateeq-wahlan.github.io/E-Voting-System-Blockchain/PROJECT_MONOGRAPH.html)
[![Portfolio](https://img.shields.io/badge/PORTFOLIO-WAHLANOS.COM-2238FF?style=for-the-badge)](https://wahlanos.com)

**Engineering trust. Securing democracy.**  
*A Decentralized Electronic Voting Platform powered by SHA-256 Proof-of-Work Blockchain, Additive Homomorphic Ballot Commitments, Zero-Knowledge Voter Nullifiers, and 320×240 Webcam Biometric Verification.*

</div>

---

## ⚡ Run Instantly Without Cloning

You can explore the complete **E-Voting Blockchain Platform** right now in your browser—no local installation or database setup required:

1. **🌐 Zero-Install Interactive Web App (GitHub Pages):**  
   👉 **[Launch Live E-Voting Blockchain Platform (`index.html`)](https://ateeq-wahlan.github.io/E-Voting-System-Blockchain/)**  
   *(Includes the 8-Party National & Regional Ballot Roster, Admin Party Registration Console, Voter Signup, 320×240 Biometric Webcam Booth, Live Proof-of-Work Block Mining, Double-Vote Prevention, and Cryptographic Tamper Simulator).*
2. **📑 Printable 9-Chapter Major Project Monograph:**  
   👉 **[View / Print Complete Academic Monograph (`PROJECT_MONOGRAPH.html`)](https://ateeq-wahlan.github.io/E-Voting-System-Blockchain/PROJECT_MONOGRAPH.html)**
3. **☁️ One-Click Cloud Python Environment (GitHub Codespaces):**  
   👉 **[Open in GitHub Codespaces](https://codespaces.new/ateeq-wahlan/E-Voting-System-Blockchain)** to run the Python backend (`app.py` / `manage.py`), SQLite database (`evoting.db`), and pickled blockchain ledger (`blockchain_ledger.pkl`) in a live cloud container.

---

## 🏛️ Academic & Author Attribution

| Attribute | Details |
| :--- | :--- |
| **Project Title** | **E-Voting System Using Blockchain Technology** |
| **Author / Architect** | **Ateeq Bin Mubarak Wahlan** |
| **University Roll No.** | **`160920733003`** |
| **Degree & Branch** | Bachelor of Engineering (B.E.) — Computer Science and Engineering |
| **Internal Guide** | **Ms. Gazala Begum** (Assistant Professor, Dept. of CSE) |
| **Head of Department** | **Dr. T K Shaik Shavali** (Professor & HOD - CSE) |
| **Institution** | **Lords Institute of Engineering & Technology** (Affiliated to Osmania University, Hyderabad – 500 091) |
| **Portfolio & GitHub** | **[wahlanos.com](https://wahlanos.com)** • **[github.com/ateeq-wahlan](https://github.com/ateeq-wahlan)** |

---

## ✨ Key Architectural Highlights

- **Cryptographic SHA-256 Proof-of-Work Engine (`Block.py` & `Blockchain.py`):** Every cast vote is encapsulated into a transaction, linked to the `previous_hash` of the preceding block, and mined at `difficulty = 2` (requiring a leading `'00'` SHA-256 digest prefix).
- **Zero-Knowledge Voter Nullifiers & Homomorphic Commitments (`BallotCipher`):** Voter identities (`username`) are converted via `PBKDF2-HMAC-SHA256` into deterministic one-way nullifiers (`zk_nullifier_...`). This prevents double voting while keeping voter choices confidential via additive homomorphic commitment hashes (`0x...`).
- **320×240 Webcam Biometric Verification Booth:** Integrates HTML5 `getUserMedia` live webcam capture (with an automatic biometric landmark simulator fallback) that verifies the voter's facial signature (`User Validated as <username>`) before unlocking the ballot sheet.
- **Expanded Multi-Party National & Regional Roster (`addparty`):** Pre-loaded with 8 major ballot options and crisp vector party emblems (`static/parties/*.svg`):
  - **Bharatiya Janata Party (BJP)** — *Lotus Symbol* (`Jubilee Hills`)
  - **Indian National Congress (INC)** — *Hand Symbol* (`Santosh Nagar`)
  - **Aam Aadmi Party (AAP)** — *Broom Symbol* (`Secunderabad`)
  - **Bharat Rashtra Samithi (BRS)** — *Car Symbol* (`Tolichowki`)
  - **All India Majlis-e-Ittehadul Muslimeen (AIMIM)** — *Kite Symbol* (`Charminar`)
  - **Bahujan Samaj Party (BSP)** — *Elephant Symbol* (`Mallepally`)
  - **Communist Party of India (Marxist) (CPI-M)** — *Civic Star Symbol* (`Mehdipatnam`)
  - **NOTA (None of the Above)** — *Official Ballot Cross Emblem* (`All Constituencies`)
- **Dual Relational Schema (`database.sql` & `evoting.db`):** Implements both the original implementation tables (`register`, `addparty`) and the 3NF normalized schema (`Voter`, `Election`, `Ballot`, `Voting`).

---

## 📂 Repository Structure

```text
EVoting/
├── index.html                      # Standalone + Backend-connected 5-Tab Interactive Web App
├── PROJECT_MONOGRAPH.html          # Complete 9-Chapter Printable Academic Report
├── WORKFLOW_DOCUMENTATION.md       # End-to-End Architecture & Viva Walkthrough Guide
├── Block.py                        # Core SHA-256 Block Structure & compute_hash()
├── Blockchain.py                   # Proof-of-Work Ledger, BallotCipher & Chain Integrity Audit
├── evoting_engine.py               # SQLite + Blockchain Ledger Orchestrator
├── app.py                          # Zero-Dependency Python HTTP & REST JSON Server (Port 5070)
├── manage.py                       # CLI Wrapper (`python manage.py runserver` / `migrate`)
├── database.sql                    # Full MySQL / SQLite Schema (register, addparty & 3NF tables)
├── test_evoting.py                 # Automated Verification Test Suite (PoW, Double-Vote, Tamper)
├── Run_EVoting.command             # One-Click macOS Native Launcher
├── run.bat                         # One-Click Windows Launcher
├── requirements.txt                # Zero external dependencies required (Python 3 stdlib)
├── .devcontainer/devcontainer.json # One-Click GitHub Codespaces Cloud Configuration
└── static/
    ├── wahlanos_evoting.css        # WahlanOS Design System (Editorial Ivory & Electric Cobalt)
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
  <sub>Architected by <strong>Ateeq Bin Mubarak Wahlan (160920733003)</strong> • <a href="https://wahlanos.com">wahlanos.com</a> • <a href="https://github.com/ateeq-wahlan">github.com/ateeq-wahlan</a></sub>
</div>
