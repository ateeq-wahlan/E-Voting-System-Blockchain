# CivicChain // E-Voting System Using Blockchain Technology (2023–2024)

<div align="center">

[![Live Interactive Demo](https://img.shields.io/badge/%F0%9F%97%B3%EF%B8%8F_LIVE_INTERACTIVE_PLATFORM-LAUNCH_IN_BROWSER-0D7C66?style=for-the-badge&logoColor=white)](https://ateeq-wahlan.github.io/E-Voting-System-Blockchain/)
[![GitHub Codespaces](https://img.shields.io/badge/%E2%98%81%EF%B8%8F_GITHUB_CODESPACES-RUN_PYTHON_BACKEND-0B192C?style=for-the-badge&logo=github&logoColor=white)](https://codespaces.new/ateeq-wahlan/E-Voting-System-Blockchain)
[![Portfolio](https://img.shields.io/badge/ARCHITECT_PORTFOLIO-WAHLANOS.COM-0284C7?style=for-the-badge)](https://wahlanos.com)

**Verifiable elections. Zero-trust consensus.**  
*A Decentralized Electronic Voting Platform powered by SHA-256 Proof-of-Work Blockchain, Additive Homomorphic Ballot Commitments, Zero-Knowledge Voter Nullifiers, Role-Based Electoral Authority Controls, and Interactive 320×240 Human Biometric Verification.*

</div>

---

## ⚡ Run Instantly Without Cloning

You can explore the complete **CivicChain E-Voting Blockchain Platform** right now in your browser—no local installation or database setup required:

1. **🌐 Zero-Install Interactive Web App (GitHub Pages):**  
   👉 **[Launch Live CivicChain E-Voting Platform (`index.html`)](https://ateeq-wahlan.github.io/E-Voting-System-Blockchain/)**  
   *(Includes the Interactive Atomic Consensus Reactor, 8-Party National & Regional Ballot Roster, Role-Locked EC Admin Console with `Form-2A` Registration & `Form-2B` Mandate Revocation, `Form-6` Voter Enrollment & `Form-7` Roll Delisting, Interactive Human Portrait Biometric Scanner Popup, Live Proof-of-Work Block Mining, Zero-Knowledge Receipt Verifier, and Cryptographic Tamper Attack Lab).*
2. **☁️ One-Click Cloud Python Environment (GitHub Codespaces):**  
   👉 **[Open in GitHub Codespaces](https://codespaces.new/ateeq-wahlan/E-Voting-System-Blockchain)** to run the Python backend (`app.py` / `manage.py`), SQLite database (`evoting.db`), and pickled blockchain ledger (`blockchain_ledger.pkl`) in a live cloud container.

---

## 🏛️ Academic & Architect Attribution

| Attribute | Details |
| :--- | :--- |
| **Project Title** | **E-Voting System Using Blockchain Technology (`CivicChain`)** |
| **Architect / Author** | **Ateeq Bin Mubarak Wahlan** |
| **University Roll No.** | **`160920733003`** |
| **Degree & Branch** | Bachelor of Engineering (B.E.) — Computer Science and Engineering |
| **Academic Year** | **2023–2024** (Batch 2020–2024) |
| **Institution** | **LIET (Osmania University)**, Hyderabad |
| **Portfolio & GitHub** | **[wahlanos.com](https://wahlanos.com)** • **[github.com/ateeq-wahlan](https://github.com/ateeq-wahlan)** |

---

## ✨ Key Architectural & Functional Highlights

- **Interactive Atomic Consensus Engine:** Real-time 60fps orbital visualization on the homepage showing the three core cryptographic rings (`CV BIOMETRICS`, `SHA-256 POW`, and `HOMOMORPHIC ZKP`) revolving around the zero-trust ballot nucleus with live click-to-inspect telemetry.
- **Role-Based Access Control (`Public Viewer` vs. `EC Admin Authority`):** Distinct data visibility and authority scopes—Public Viewers see privacy-masked voter PII (`9849••••03`) and read-only audit views, while authenticated Electoral Commission Admins (`admin` / `admin`) unlock candidate gazette registration, mandate revocation, voter roll delisting, and full PII inspection.
- **Party Gazette Registration (`Form-2A`) & Mandate Revocation (`Form-2B`):** Full lifecycle management of political parties and constituency candidates (`addparty`), allowing the EC Admin to register new candidates or disqualify/deregister existing party mandates.
- **Voter Enrollment (`Form-6`) & Electoral Roll Delisting (`Form-7`):** Full citizen registration (`register`) and off-chain biometric credential revocation, demonstrating how revoking a voter's off-chain login credential preserves the on-chain immutability of any previously mined anonymous ballot (`zk_nullifier_...`).
- **Interactive Human Portrait Biometric Scanner Popup (`320×240`):** Clicking any voter profile (including voters who have already voted) opens an optical biometric verification modal displaying their real human photograph, animated CNN laser landmark sweep, 99.68% confidence match, and on-chain block receipt.
- **Cryptographic SHA-256 Proof-of-Work Engine (`Block.py` & `Blockchain.py`):** Every cast vote is encapsulated into a transaction, linked to the `previous_hash` of the preceding block, and mined at `difficulty = 2` (requiring a leading `'00'` SHA-256 digest prefix).

---

## 📂 Repository Structure

```text
EVoting/
├── index.html                      # Standalone + Backend-connected 5-Tab Interactive Web App
├── WORKFLOW_DOCUMENTATION.md       # End-to-End Architecture & Viva Walkthrough Guide
├── Block.py                        # Core SHA-256 Block Structure & compute_hash()
├── Blockchain.py                   # Proof-of-Work Ledger, BallotCipher & Chain Integrity Audit
├── evoting_engine.py               # SQLite + Blockchain Ledger Orchestrator (Add/Delete Party & Voter)
├── app.py                          # Zero-Dependency Python HTTP & REST JSON Server (Port 5070)
├── manage.py                       # CLI Wrapper (`python manage.py runserver` / `migrate`)
├── database.sql                    # Full MySQL / SQLite Schema (register, addparty & 3NF tables)
├── test_evoting.py                 # Automated Verification Test Suite (PoW, RBAC, Revocation, Tamper)
├── Run_EVoting.command             # One-Click macOS Native Launcher
├── run.bat                         # One-Click Windows Launcher
├── requirements.txt                # Zero external dependencies required (Python 3 stdlib)
├── .devcontainer/devcontainer.json # One-Click GitHub Codespaces Cloud Configuration
└── static/
    ├── evoting_logo.svg            # Custom Electoral Ballot-Box & Blockchain Cube Emblem
    ├── wahlanos_evoting.css        # CivicChain Design System (Outfit, DM Sans & IBM Plex Mono)
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
  <sub>Architected by <strong>Ateeq Bin Mubarak Wahlan (160920733003)</strong> • <strong>LIET (Osmania University) • 2023–2024</strong> • <a href="https://wahlanos.com">wahlanos.com</a></sub>
</div>
