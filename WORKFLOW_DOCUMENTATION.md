# CivicChain // E-Voting System Using Blockchain Technology (2023–2024) — Architecture & Workflow Guide

**Architect:** Ateeq Bin Mubarak Wahlan (Roll No: `160920733003`)  
**Institution:** LIET (Osmania University), Hyderabad  
**Academic Year:** 2023–2024 (B.E. Computer Science & Engineering)  
**Portfolio:** [wahlanos.com](https://wahlanos.com) • **GitHub:** [github.com/ateeq-wahlan](https://github.com/ateeq-wahlan)

---

## 1. Executive Summary

**CivicChain // E-Voting System Using Blockchain Technology (2023–2024)** is a decentralized, cryptographically verifiable electronic voting platform that eliminates single-point-of-failure vulnerabilities in traditional paper ballots and centralized database voting machines.

Once an election is initialized on the ledger, no central administrator can alter, delete, or forge cast ballots. Every vote is authenticated via an interactive **320×240 Human Face Biometric Scan Popup**, anonymized with a **Zero-Knowledge Voter Nullifier (`zk_nullifier_...`)**, sealed inside an **Additive Homomorphic Commitment (`0x...`)**, and mined into a **SHA-256 Proof-of-Work (`difficulty = 2`)** block.

---

## 2. System Architecture & 7-Stage Pipeline

```
+-----------------------------------------------------------------------------------+
|STAGE 1: Citizen Electoral Enrollment (`Form-6` / `register` Table)                |
|  Citizen enrolls Full Name, EPIC ID, Constituency Address & Human Face Portrait   |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|STAGE 2: Cryptographic Identity & Nullifier Derivation (`BallotCipher`)            |
|  PBKDF2-HMAC-SHA256 derives 256-bit Face Signature + `zk_nullifier_<24_hex>`      |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|STAGE 3: Role-Based Electoral Commission Governance (`Form-2A` & `Form-2B`)        |
|  Admin (`admin`/`admin`) gazettes Parties (`Form-2A`) or revokes mandates (`2B`)  |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|STAGE 4: Interactive Human Biometric Scan Popup (`/CastVote.html` & `/ValidateUser`)|
|  Click any Voter Card -> Human Portrait Popup -> `Take Snapshot` -> Laser Scan    |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|STAGE 5: Double-Vote Lock & Homomorphic Ballot Encryption                          |
|  Verifies `zk_nullifier` is unspent -> Encrypts choice + Homomorphic Commitment   |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|STAGE 6: Proof-of-Work Mining Node (`Block.py` & `Blockchain.py`)                  |
|  Increments `block.nonce` until `SHA-256(block_json)` starts with `'00'`          |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|STAGE 7: Immutable Receipt, ZK Proof Lookup & Form-7 Roll Delisting (`/ViewVotes`) |
|  Outputs `Previous Hash`, `Block No`, `Current Hash` + Tamper Lab & Form-7 Purge  |
+-----------------------------------------------------------------------------------+
```

---

## 3. Core Modules & File Inventory

| File / Directory | Role in Architecture |
| :--- | :--- |
| `Block.py` | Implements the `Block(index, transactions, timestamp, previous_hash, nonce)` class and deterministic `compute_hash()` SHA-256 digest function. |
| `Blockchain.py` | Implements `Blockchain` (`difficulty = 2`, `create_genesis_block()`, `proof_of_work()`, `add_block()`, `is_valid_proof()`, `mine()`, `save_object()`, `verify_chain_integrity()`) and `BallotCipher`. |
| `evoting_engine.py` | Orchestrates SQLite (`evoting.db`) and the pickled blockchain (`blockchain_ledger.pkl`), supporting `add_party` (`Form-2A`), `delete_party` (`Form-2B`), `register_voter` (`Form-6`), `delete_voter` (`Form-7`), `validate_biometric_snapshot`, and `reset_demo_state`. |
| `database.sql` | Complete SQL script containing both the `register` and `addparty` tables and the 3NF normalized `Voter`, `Election`, `Ballot`, and `Voting` tables. |
| `app.py` & `manage.py` | Zero-dependency Python HTTP/JSON server on Port `5070` supporting `python3 app.py` and `python3 manage.py runserver`. |
| `index.html` | Self-contained 5-tab interactive Web Application styled in the independent **CivicChain Electoral Design System** (`Space Grotesk`, `DM Sans`, `IBM Plex Mono`, Sovereign Emerald-Teal `#0D9488` & Constitutional Navy `#0B1528`). |
| `static/evoting_logo.svg` | Custom 3D isometric ballot-box & blockchain emblem designed specifically for the E-Voting platform. |
| `static/parties/*.svg` | High-resolution vector symbols for **BJP (Lotus)**, **INC (Hand)**, **AAP (Broom)**, **BRS (Car)**, **AIMIM (Kite)**, **BSP (Elephant)**, **CPI-M (Star)**, and **NOTA**. |

---

## 4. Step-by-Step Verification & Viva Walkthrough

1. **Inspect the Interactive Moving Atomic Consensus Core (Homepage Hero)**:
   - Observe the 4 orbiting cryptographic atoms (**`CV BIOMETRICS`**, **`SHA-256 POW`**, **`ZK NULLIFIER`**, **`HOMOMORPHIC ZKP`**) smoothly revolving around the central ballot nucleus. Click any orbiting node or pill button to inspect its live telemetry.
2. **Test Role-Based Access Control (`Public Viewer` vs. `EC Admin Authority`)**:
   - By default, the app runs in **Public Viewer Mode** (voter phone numbers and emails are masked, and administrative deletion/registration actions are locked).
   - Click **`SCOPE: PUBLIC VIEWER (UNLOCK ADMIN 🔒)`** in the top header and log in with `admin` / `admin` to unlock **EC Admin Authority Scope**.
3. **Execute Party Registration (`Form-2A`) & Party Mandate Revocation (`Form-2B`) (`02. Admin Party Console`)**:
   - Gazette a new political candidate using **Form-2A**, or revoke an existing candidate's electoral mandate using **Form-2B (`Revoke Mandate`)** with statutory Election Commission grounds.
4. **Execute Voter Enrollment (`Form-6`) & Electoral Roll Delisting (`Form-7`) (`03. Voter Roll & Form-7 Delisting`)**:
   - Enroll a new citizen with a human portrait preset (**Form-6**), or delist an existing voter (**Form-7**) and observe how their off-chain polling credential is revoked while any historical anonymous ballot (`zk_nullifier_...`) remains immutable on-chain.
5. **Open the Human Face Biometric Scan Popup (`04. Biometric Voting Booth`)**:
   - Click any citizen card (including voters who have **Already Voted** like `Azizullah Karimi` or `Dr. Priyanka Reddy`, or eligible voter `Ateeq Bin Mubarak Wahlan`) to launch the **Biometric Identity & Optical Landmark Scanner Popup**.
   - Click **`📸 1. Take Snapshot & Run Biometric Scan`** inside the popup to watch the laser landmark scan validate their human portrait (`99.68% Match Confidence`).
   - If the voter has already voted, inspect their **Mined Blockchain Receipt (`Block #`, `ZK Nullifier`, `Homomorphic Commitment`)** inside the popup; if eligible, click **`Proceed to Ballot Sheet →`** to cast an encrypted vote and mine a new Proof-of-Work block!
