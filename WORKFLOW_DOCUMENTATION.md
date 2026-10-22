# CivicChain // E-Voting System Using Blockchain Technology — Architecture & Workflow Guide

**Architect:** Ateeq Bin Mubarak Wahlan (Roll No: `160920733003`)  
**Academic Year:** `2023–2024` (B.E. Computer Science & Engineering, Batch `2020–2024`)  
**Institution:** LIET (Osmania University), Hyderabad  
**Portfolio:** [wahlanos.com](https://wahlanos.com) • **GitHub:** [github.com/ateeq-wahlan](https://github.com/ateeq-wahlan)

---

## 1. Executive Summary

**CivicChain** is a decentralized, cryptographically verifiable electronic voting platform that eliminates single-point-of-failure vulnerabilities in traditional paper ballots and centralized database voting machines.

Once an election is initialized on the ledger, no central administrator can alter, delete, or forge cast ballots. Every vote is authenticated via an **Interactive 320×240 Human Portrait Biometric Verification Pipeline**, anonymized with a **Zero-Knowledge Voter Nullifier (`zk_nullifier_...`)**, sealed inside an **Additive Homomorphic Commitment (`0x...`)**, and mined into a **SHA-256 Proof-of-Work (`difficulty = 2`)** block.

---

## 2. System Architecture & 7-Stage Pipeline

```
+-----------------------------------------------------------------------------------+
|STAGE 1: Citizen Biometric Enrollment (`Form-6` -> `register` / 1NF `Voter` Table) |
|  Citizen enrolls Full Name, Username, EPIC ID, Address & Human Portrait Photo     |
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
|STAGE 3: EC Admin Gazette & Mandate Control (`Form-2A` Add / `Form-2B` Revoke)     |
|  Role-locked EC Admin registers or revokes National & Regional Party Mandates     |
+-----------------------------------------+-----------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|STAGE 4: Interactive Human Biometric Optical Scanner Popup (`320x240` Laser Scan)  |
|  Opens human portrait popup -> `Take Snapshot` -> 68-Point CNN Landmark Match     |
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
|STAGE 7: Zero-Knowledge Receipt Verifier & Tamper Attack Lab (`/ViewVotes`)        |
|  Outputs `Previous Hash`, `Block No`, `Current Hash` + ZK Inclusion Proof Lookup  |
+-----------------------------------------------------------------------------------+
```

---

## 3. Role-Based Access Scope (`Public Viewer` vs. `EC Admin Authority`)

| Feature / Capability | `👁️ Public Viewer Scope` (Default) | `🛡️ EC Admin Authority Scope` (`admin` / `admin`) |
| :--- | :--- | :--- |
| **Atomic Consensus Reactor & Party Roster** | Full Interactive Access + Constituency Filter | Full Interactive Access + Constituency Filter |
| **Voter Contact & Email PII (`register`)** | Privacy-Masked (`9849••••03`, `at•••@wahlanos.com`) | Unmasked Full Electoral Roll Audit View |
| **Candidate Gazette Nomination (`Form-2A`)** | 🔒 Locked behind Admin Authority Gate | ✅ Unlocked (`POST /api/admin/add-party`) |
| **Party Mandate Revocation (`Form-2B`)** | 🔒 Locked behind Admin Authority Gate | ✅ Unlocked (`POST /api/admin/delete-party`) |
| **Electoral Roll Delisting (`Form-7`)** | 🔒 Locked behind Admin Authority Gate | ✅ Unlocked (`POST /api/admin/delete-voter`) |
| **Human Biometric Scanner Popup & Voting** | ✅ Enabled for All Registered Voters | ✅ Enabled for All Registered Voters |
| **Zero-Knowledge Receipt Verifier & Audit** | ✅ Publicly Verifiable by Any Citizen | ✅ Publicly Verifiable + Demo Ledger Reset |

---

## 4. Step-by-Step Verification & Viva Walkthrough

1. **Inspect the Animated Atomic Consensus Reactor (Hero Section)**:
   - Observe the 3 orbiting consensus nodes (`CV BIOMETRICS`, `SHA-256 POW`, `HOMOMORPHIC ZKP`) revolving smoothly around the central Ballot Core. Click any orbiting node to read its live cryptographic telemetry, or click **`⏸ PAUSE / ▶ RESUME`**.
2. **Test Public Viewer vs. EC Admin Authority Scope**:
   - In **`02. Admin Console`**, notice that adding or revoking parties is locked in **Public Viewer Mode**.
   - Click **`🔒 Role: Public Viewer (Unlock Admin)`** in the top navigation bar (credentials: `admin` / `admin`) to unlock **EC Admin Authority Mode**.
3. **Register & Revoke a Party Mandate (`02. Admin Console`)**:
   - Gazette a new candidate under **`Form-2A`**, then test **`Form-2B` Electoral Mandate Revocation** by disqualifying/deregistering a candidate and observing the real-time ballot sync.
4. **Enroll & Delist a Voter (`03. Voter Roll & Signup`)**:
   - Enroll a citizen under **`Form-6`**, then test **`Form-7` Electoral Roll Delisting** to see how off-chain biometric credentials are revoked while historical on-chain ballots remain immutable.
5. **Launch the Interactive Human Portrait Biometric Scanner Popup (`04. Biometric Booth`)**:
   - Click any citizen card in the **Electoral Roll Biometric Roster** (try both an unvoted citizen like `ateeqwahlan` and an already-voted citizen like `priyankareddy` or `azizullahkarimi`).
   - Inside the popup showing their real human photograph, click **`📸 1. Take Snapshot & Run Laser Facial Scan`** to watch the CNN laser sweep and 68-point facial landmark mesh, then click **`✓ 2. Validate Voter & Sync to Booth`**.
6. **Verify Zero-Knowledge Ballot Inclusion & Tamper Detection (`05. Blockchain & Audit`)**:
   - Use the **Zero-Knowledge Ballot Inclusion Verifier** to look up any voter's `zk_nullifier_...` or `Block Hash`, and click **`Simulate Malicious Vote Mutation on Block #1 ⚡`** to verify immediate SHA-256 tamper rejection.
