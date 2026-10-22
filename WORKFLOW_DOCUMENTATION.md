# E-Voting System Using Blockchain Technology — End-to-End Architecture & Workflow Guide

**Architect:** Ateeq Bin Mubarak Wahlan (Roll No: `160920733003`)  
**Portfolio:** [wahlanos.com](https://wahlanos.com) • **GitHub:** [github.com/ateeq-wahlan](https://github.com/ateeq-wahlan)  
**Academic Guide:** Ms. Gazala Begum (Asst. Professor, Dept. of CSE)  
**Institution:** Lords Institute of Engineering & Technology (Affiliated to Osmania University, Hyderabad – 500 091)

---

## 1. Executive Summary

The **E-Voting System Using Blockchain Technology** is a decentralized, cryptographically verifiable electronic voting platform that eliminates single-point-of-failure vulnerabilities in traditional paper ballots and centralized database voting machines.

Once an election is initialized on the ledger, no central administrator can alter, delete, or forge cast ballots. Every vote is authenticated via a **320×240 Webcam Biometric Verification Pipeline**, anonymized with a **Zero-Knowledge Voter Nullifier (`zk_nullifier_...`)**, sealed inside an **Additive Homomorphic Commitment (`0x...`)**, and mined into a **SHA-256 Proof-of-Work (`difficulty = 2`)** block.

---

## 2. System Architecture & 7-Stage Pipeline

```
+-----------------------------------------------------------------------------------+
|STAGE 1: Voter Registration (`register` / 1NF `Voter` Table)                       |
|  Citizen enrolls Username, Contact, Constituency Address & Biometric Face Image   |
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
|STAGE 3: Admin Electoral Ballot Registry (`addparty` / 2NF `Election` & 3NF `Ballot`)|
|  Admin registers National & Regional Parties (BJP, INC, AAP, BRS, AIMIM, BSP...)  |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|STAGE 4: Polling Booth Webcam Biometric Verification (`/CastVote.html` -> Fig 28.2)|
|  320x240 Live Snapshot -> `Validate User` -> Confirms `User Validated as <user>`  |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|STAGE 5: Double-Vote Check & Homomorphic Ballot Encryption                         |
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
|STAGE 7: Immutable Receipt & Public Consensus Audit (`/ViewVotes` -> Fig 28.4 & 29)|
|  Outputs `Previous Hash`, `Block No`, `Current Hash` + Live Tamper-Detection Lab  |
+-----------------------------------------------------------------------------------+
```

---

## 3. Core Modules & File Inventory

| File / Directory | Role in Architecture |
| :--- | :--- |
| `Block.py` | Implements the `Block(index, transactions, timestamp, previous_hash, nonce)` class and deterministic `compute_hash()` SHA-256 digest function (Chapter 6.2, p. 42). |
| `Blockchain.py` | Implements `Blockchain` (`difficulty = 2`, `create_genesis_block()`, `proof_of_work()`, `add_block()`, `is_valid_proof()`, `mine()`, `save_object()`, `verify_chain_integrity()`) and `BallotCipher` (Chapter 6.2, pp. 42–46). |
| `evoting_engine.py` | Connects the SQLite relational database (`evoting.db`) and pickled blockchain (`blockchain_ledger.pkl`), seeding 8 National/Regional Parties and 5 registered voters. |
| `database.sql` | Complete SQL script containing both the original `register` and `addparty` tables (Slide 20 / Fig. 22) and the 3NF normalized `Voter`, `Election`, `Ballot`, and `Voting` tables (Chapter 6.1–6.2, pp. 37–41). |
| `app.py` & `manage.py` | Zero-dependency Python HTTP/JSON server on Port `5070` supporting `python app.py` and `python manage.py runserver`. |
| `index.html` | Self-contained 5-tab interactive Web Application styled in the **WahlanOS** design system (`#F7F6F0` ivory, `#2238FF` electric cobalt, `#14161B` ink) that works both with `app.py` and standalone on **GitHub Pages**. |
| `PROJECT_MONOGRAPH.html` | Printable 9-chapter academic project report and UML documentation in Ateeq Bin Mubarak Wahlan's name (`160920733003`). |
| `static/parties/*.svg` | High-resolution vector symbols for **BJP (Lotus)**, **INC (Hand)**, **AAP (Broom)**, **BRS (Car)**, **AIMIM (Kite)**, **BSP (Elephant)**, **CPI-M (Star)**, and **NOTA**. |
| `Run_EVoting.command` / `run.bat` | One-click desktop launchers for macOS and Windows. |

---

## 4. Step-by-Step Verification & Viva Walkthrough

1. **Launch the Application**:
   - **Zero-Clone Browser Mode**: Open `index.html` directly in any browser (or via GitHub Pages).
   - **Full Python Backend Mode**: Double-click `Run_EVoting.command` (macOS) or run `python3 app.py` (opens `http://127.0.0.1:5070/index.html`).
2. **Inspect the National & Regional Party Roster (`01. Overview & Parties`)**:
   - Review all 8 pre-loaded parties (**BJP, INC, AAP, BRS, AIMIM, BSP, CPI-M, NOTA**) with their official constituency symbols and live blockchain tallies.
3. **Register a New Party Candidate (`02. Admin Console`)**:
   - Enter a candidate name, choose a party symbol and constituency area, and click **Add Party Candidate to Blockchain Registry**.
4. **Enroll a New Voter (`03. Voter Signup`)**:
   - Fill out the `New User Signup Screen` (`username`, `password`, `contact`, `email`, `address`, and profile image) to generate a new **Zero-Knowledge Nullifier** (`zk_nullifier_...`).
5. **Authenticate via Webcam & Cast an Encrypted Ballot (`04. Biometric Booth`)**:
   - Select an eligible voter (e.g., `ateeqwahlan`), click **2. Take Snapshot (320×240)** and **3. Validate User ✓**, then click **Click Here to Vote** beside any party candidate.
   - Observe the blue blockchain receipt banner displaying **Previous Hash**, **Block No**, **PoW Nonce**, and **Current Hash** (`00...`).
   - Click vote a second time with the same voter to verify **Double-Vote Prevention**.
6. **Run the Tamper Attack Lab (`05. Blockchain & Results`)**:
   - Click **Simulate Malicious Vote Mutation on Block #1 ⚡** to see how mutating a historical ballot invalidates the SHA-256 hash and triggers immediate consensus rejection.
