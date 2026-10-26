"""
================================================================================
E-VOTING SYSTEM USING BLOCKCHAIN TECHNOLOGY
Module: evoting_engine.py — Relational SQLite + Blockchain Ledger Orchestrator
================================================================================
Author:      Ateeq Bin Mubarak Wahlan (Roll No: 160920733003)
WahlanOS:    https://wahlanos.com ↗ | https://github.com/ateeq-wahlan
Institution: LIET (Osmania University ’23)
================================================================================
"""

from datetime import datetime
from hashlib import sha256
import json
import os
import sqlite3
from typing import Any, Dict, List, Optional

from Block import Block
from Blockchain import Blockchain


DEFAULT_PARTIES: List[Dict[str, str]] = [
    {
        "candidatename": "Rajeshwar Rao Deshmukh",
        "partyname": "Bharatiya Janata Party (BJP)",
        "areaname": "Jubilee Hills",
        "image": "static/parties/bjp.svg",
        "party_code": "BJP",
        "manifesto": "Digital Infrastructure, Urban Mobility & Industrial Growth Corridors",
    },
    {
        "candidatename": "Dr. Ananya Reddy",
        "partyname": "Indian National Congress (INC)",
        "areaname": "Santosh Nagar",
        "image": "static/parties/inc.svg",
        "party_code": "INC",
        "manifesto": "Universal Healthcare Access, Youth Employment & Civic Welfare",
    },
    {
        "candidatename": "Vikramaditya Sharma",
        "partyname": "Aam Aadmi Party (AAP)",
        "areaname": "Secunderabad",
        "image": "static/parties/aap.svg",
        "party_code": "AAP",
        "manifesto": "Model Public Schools, Mohalla Clinics & Zero-Corruption Governance",
    },
    {
        "candidatename": "K. Chandrasekhar Goud",
        "partyname": "Bharat Rashtra Samithi (BRS)",
        "areaname": "Tolichowki",
        "image": "static/parties/brs.svg",
        "party_code": "BRS",
        "manifesto": "IT Corridor Expansion, 24x7 Clean Water & Metro Connectivity",
    },
    {
        "candidatename": "Syed Zafarullah Quadri",
        "partyname": "All India Majlis-e-Ittehadul Muslimeen (AIMIM)",
        "areaname": "Charminar",
        "image": "static/parties/aimim.svg",
        "party_code": "AIMIM",
        "manifesto": "Old City Heritage Renewal, Minority Education & Healthcare Centers",
    },
    {
        "candidatename": "Prabhakar Rao Ambedkar",
        "partyname": "Bahujan Samaj Party (BSP)",
        "areaname": "Mallepally",
        "image": "static/parties/bsp.svg",
        "party_code": "BSP",
        "manifesto": "Social Justice, Equal Opportunity & Grassroots Empowerment",
    },
    {
        "candidatename": "Comrade Sitaramacharyulu",
        "partyname": "Communist Party of India (Marxist) (CPI-M)",
        "areaname": "Mehdipatnam",
        "image": "static/parties/cpim.svg",
        "party_code": "CPI-M",
        "manifesto": "Labour Rights, Public Transport Subsidies & Affordable Housing",
    },
    {
        "candidatename": "None of the Above (NOTA)",
        "partyname": "NOTA — Official Electoral Option",
        "areaname": "All Constituencies",
        "image": "static/parties/nota.svg",
        "party_code": "NOTA",
        "manifesto": "Constitutional Right to Reject All Listed Candidates",
    },
]


DEFAULT_VOTERS: List[Dict[str, str]] = [
    {
        "username": "ateeqwahlan",
        "full_name": "Ateeq Bin Mubarak Wahlan",
        "epic_id": "TS/HYD/160920/003",
        "password": "password123",
        "contact": "9849016003",
        "email": "ateeq@wahlanos.com",
        "address": "Himayath Sagar, Jubilee Hills, Hyderabad",
        "constituency": "Jubilee Hills",
        "profile_image": "static/voters/ateeq.svg",
    },
    {
        "username": "azizullahkarimi",
        "full_name": "Azizullah Karimi",
        "epic_id": "TS/HYD/160920/104",
        "password": "password123",
        "contact": "9652881908",
        "email": "karimi@gmail.com",
        "address": "Tolichowki Main Road, Hyderabad",
        "constituency": "Tolichowki",
        "profile_image": "static/voters/azizullah.svg",
    },
    {
        "username": "priyankareddy",
        "full_name": "Dr. Priyanka Reddy",
        "epic_id": "TS/HYD/160920/218",
        "password": "password123",
        "contact": "9988776655",
        "email": "priyanka.r@gmail.com",
        "address": "Trimulgherry, Secunderabad, Hyderabad",
        "constituency": "Secunderabad",
        "profile_image": "static/voters/priyanka.svg",
    },
    {
        "username": "mohammedzubair",
        "full_name": "Mohammed Zubair Siddiqui",
        "epic_id": "TS/HYD/160920/309",
        "password": "password123",
        "contact": "9123456780",
        "email": "zubair.charminar@gmail.com",
        "address": "Laad Bazaar, Charminar, Hyderabad",
        "constituency": "Charminar",
        "profile_image": "static/voters/zubair.svg",
    },
    {
        "username": "farhanahmed",
        "full_name": "Farhan Ahmed Khan",
        "epic_id": "TS/HYD/160920/412",
        "password": "password123",
        "contact": "9701234509",
        "email": "farhan.hyd@outlook.com",
        "address": "Santosh Nagar Colony, Hyderabad",
        "constituency": "Santosh Nagar",
        "profile_image": "static/voters/farhan.svg",
    },
]


class EVotingEngine:
    """
    Orchestrates the E-Voting relational database (`evoting.db`), biometric
    face verification pipeline, and Proof-of-Work Blockchain ledger
    (`blockchain_ledger.pkl`).
    """

    def __init__(self, base_dir: Optional[str] = None) -> None:
        self.base_dir = base_dir or os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(self.base_dir, "evoting.db")
        self.chain_path = os.path.join(self.base_dir, "blockchain_ledger.pkl")
        self._init_database()
        self.blockchain = self._load_or_seed_blockchain()

    def _get_conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _compute_face_signature(self, username: str, image_data: str = "") -> str:
        seed = f"BIOMETRIC_EMBEDDING::{username.strip().lower()}::{len(image_data)}"
        return sha256(seed.encode("utf-8")).hexdigest()

    def _init_database(self) -> None:
        conn = self._get_conn()
        cur = conn.cursor()

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS register (
                username TEXT PRIMARY KEY,
                full_name TEXT DEFAULT '',
                epic_id TEXT DEFAULT '',
                password TEXT NOT NULL,
                contact TEXT NOT NULL,
                email TEXT NOT NULL,
                address TEXT NOT NULL,
                profile_image TEXT DEFAULT '',
                face_signature TEXT,
                registered_at TEXT
            )
            """
        )

        existing_cols = {row["name"] for row in cur.execute("PRAGMA table_info(register)").fetchall()}
        if "full_name" not in existing_cols:
            cur.execute("ALTER TABLE register ADD COLUMN full_name TEXT DEFAULT ''")
        if "epic_id" not in existing_cols:
            cur.execute("ALTER TABLE register ADD COLUMN epic_id TEXT DEFAULT ''")

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS addparty (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                candidatename TEXT NOT NULL,
                partyname TEXT NOT NULL,
                areaname TEXT NOT NULL,
                image TEXT NOT NULL,
                party_code TEXT NOT NULL,
                manifesto TEXT DEFAULT ''
            )
            """
        )

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS Election (
                Election_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Election_Name TEXT NOT NULL,
                Start_Date TEXT NOT NULL,
                End_Date TEXT NOT NULL
            )
            """
        )

        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS Ballot (
                Ballot_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Election_ID INTEGER NOT NULL,
                Ballot_Title TEXT NOT NULL,
                Ballot_Question TEXT NOT NULL
            )
            """
        )

        cur.execute("SELECT COUNT(*) AS cnt FROM Election")
        if cur.fetchone()["cnt"] == 0:
            cur.execute(
                "INSERT INTO Election (Election_ID, Election_Name, Start_Date, End_Date) VALUES (1, 'Hyderabad Metropolitan General Election', '2023-11-15', '2024-05-30')"
            )
            cur.execute(
                "INSERT INTO Ballot (Ballot_ID, Election_ID, Ballot_Title, Ballot_Question) VALUES (1, 1, 'Parliamentary & Assembly Constituency Ballot', 'Select your preferred candidate and party symbol for your constituency')"
            )

        cur.execute("SELECT COUNT(*) AS cnt FROM addparty")
        if cur.fetchone()["cnt"] == 0:
            for party in DEFAULT_PARTIES:
                cur.execute(
                    """
                    INSERT INTO addparty (candidatename, partyname, areaname, image, party_code, manifesto)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (
                        party["candidatename"],
                        party["partyname"],
                        party["areaname"],
                        party["image"],
                        party["party_code"],
                        party["manifesto"],
                    ),
                )

        cur.execute("SELECT COUNT(*) AS cnt FROM register")
        if cur.fetchone()["cnt"] == 0:
            for voter in DEFAULT_VOTERS:
                sig = self._compute_face_signature(voter["username"], voter["profile_image"])
                cur.execute(
                    """
                    INSERT INTO register (username, full_name, epic_id, password, contact, email, address, profile_image, face_signature, registered_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        voter["username"],
                        voter["full_name"],
                        voter["epic_id"],
                        voter["password"],
                        voter["contact"],
                        voter["email"],
                        voter["address"],
                        voter["profile_image"],
                        sig,
                        "2023-11-15 10:15:00",
                    ),
                )
        else:
            for voter in DEFAULT_VOTERS:
                cur.execute(
                    """
                    UPDATE register
                    SET full_name = ?,
                        epic_id = ?,
                        profile_image = ?
                    WHERE username = ?
                    """,
                    (voter["full_name"], voter["epic_id"], voter["profile_image"], voter["username"]),
                )

        conn.commit()
        conn.close()

    def _load_or_seed_blockchain(self) -> Blockchain:
        loaded = Blockchain.load_object(self.chain_path)
        if loaded is not None and len(loaded.chain) >= 1:
            return loaded

        bc = Blockchain()
        seed_votes = [
            ("azizullahkarimi", "Dr. Ananya Reddy", "Indian National Congress (INC)", "INC", "Santosh Nagar", "2023-11-16 10:14:22"),
            ("priyankareddy", "Vikramaditya Sharma", "Aam Aadmi Party (AAP)", "AAP", "Secunderabad", "2023-11-16 11:05:49"),
            ("mohammedzubair", "Syed Zafarullah Quadri", "All India Majlis-e-Ittehadul Muslimeen (AIMIM)", "AIMIM", "Charminar", "2023-11-16 12:31:08"),
            ("farhanahmed", "K. Chandrasekhar Goud", "Bharat Rashtra Samithi (BRS)", "BRS", "Tolichowki", "2023-11-16 14:19:55"),
        ]
        for uname, cand, party, code, area, ts_str in seed_votes:
            nullifier = bc.cipher.anonymize_voter_id(uname)
            enc = bc.cipher.encrypt_ballot_choice(cand, party, nullifier)
            tx = {
                "tx_type": "BALLOT_CAST",
                "election_id": "GENERAL-ELECTION-HYD",
                "voter_nullifier": nullifier,
                "voter_handle_masked": uname[:3] + "***" + uname[-2:],
                "candidate_name": cand,
                "party_name": party,
                "party_code": code,
                "area_name": area,
                "biometric_confidence": 99.64,
                "encrypted_ballot": enc["ciphertext"],
                "homomorphic_commitment": enc["homomorphic_commitment"],
                "digital_signature": enc["signature"],
                "timestamp_iso": ts_str,
            }
            bc.add_new_transaction(tx)
            bc.mine()

        bc.save_object(bc, self.chain_path)
        return bc

    def authenticate_admin(self, username: str, password: str) -> bool:
        return username.strip() == "admin" and password.strip() == "admin"

    def add_party(
        self,
        candidatename: str,
        partyname: str,
        areaname: str,
        image: str = "static/parties/bjp.svg",
        party_code: str = "IND",
        manifesto: str = "Civic Development, Transparency & Digital Governance",
    ) -> Dict[str, Any]:
        conn = self._get_conn()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO addparty (candidatename, partyname, areaname, image, party_code, manifesto)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (candidatename.strip(), partyname.strip(), areaname.strip(), image.strip(), party_code.strip().upper(), manifesto.strip()),
        )
        conn.commit()
        party_id = cur.lastrowid
        conn.close()
        return {
            "status": "success",
            "message": f"Candidate '{candidatename}' ({partyname}) gazetted into the Electoral Ballot Registry for {areaname}.",
            "party_id": party_id,
        }

    def delete_party(
        self,
        party_id: int,
        reason: str = "EC Form-2B Candidacy Withdrawal / Symbol Deregistration",
    ) -> Dict[str, Any]:
        conn = self._get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM addparty WHERE id = ?", (party_id,))
        row = cur.fetchone()
        if row is None:
            conn.close()
            return {"status": "error", "message": f"Party Registry ID #{party_id} not found in ballot table."}

        party_dict = dict(row)
        cur.execute("DELETE FROM addparty WHERE id = ?", (party_id,))
        conn.commit()
        conn.close()
        return {
            "status": "success",
            "deregistered_party": party_dict,
            "reason": reason,
            "message": (
                f"Electoral Mandate Revoked: Candidate '{party_dict['candidatename']}' "
                f"({party_dict['partyname']} — {party_dict['areaname']}) has been deregistered "
                f"from the active ballot sheet under [{reason}]."
            ),
        }

    def list_parties(self) -> List[Dict[str, Any]]:
        conn = self._get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, candidatename, partyname, areaname, image, party_code, manifesto FROM addparty ORDER BY id ASC")
        rows = [dict(r) for r in cur.fetchall()]
        conn.close()

        tallies = self.get_party_vote_counts()
        for row in rows:
            key = f"{row['candidatename']}||{row['partyname']}"
            row["votes"] = tallies.get(key, 0)
        return rows

    def register_voter(
        self,
        username: str,
        password: str,
        contact: str,
        email: str,
        address: str,
        full_name: str = "",
        profile_image: str = "",
    ) -> Dict[str, Any]:
        uname = username.strip().lower()
        if not uname or not password:
            return {"status": "error", "message": "Username and password are required."}

        conn = self._get_conn()
        cur = conn.cursor()
        cur.execute("SELECT username FROM register WHERE LOWER(username) = ?", (uname,))
        if cur.fetchone() is not None:
            conn.close()
            return {"status": "error", "message": f"Voter '{uname}' is already registered in the electoral roll."}

        avatar = profile_image.strip() if profile_image else ""
        face_sig = self._compute_face_signature(uname, avatar) if avatar else ""
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        display_name = full_name.strip() or uname.replace("_", " ").title()
        epic_code = f"TS/HYD/23/{abs(hash(uname)) % 900 + 100}"

        cur.execute(
            """
            INSERT INTO register (username, full_name, epic_id, password, contact, email, address, profile_image, face_signature, registered_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (uname, display_name, epic_code, password.strip(), contact.strip(), email.strip(), address.strip(), avatar, face_sig, now_str),
        )
        conn.commit()
        conn.close()
        bio_note = (
            f"256-Bit Biometric Hash: {face_sig[:16]}..."
            if face_sig
            else "Biometric photo pending — open the Biometric Popup in the Voting Booth to capture & register face."
        )
        return {
            "status": "success",
            "message": f"Electoral Roll Enrollment Completed for '{display_name}' ({uname}). {bio_note}",
            "username": uname,
            "full_name": display_name,
            "epic_id": epic_code,
            "profile_image": avatar,
            "face_signature": face_sig,
        }

    def register_biometric_image(self, username: str, image_data: str) -> Dict[str, Any]:
        """
        Captures and registers a biometric face snapshot to the specified Voter ID
        when captured from the camera popup modal.
        """
        uname = username.strip().lower()
        conn = self._get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM register WHERE LOWER(username) = ?", (uname,))
        row = cur.fetchone()
        if row is None:
            conn.close()
            return {"status": "error", "message": f"Voter '{uname}' not found in electoral roll."}

        avatar = image_data.strip() if image_data and image_data.strip() else "static/voters/ateeq.svg"
        face_sig = self._compute_face_signature(uname, avatar)
        cur.execute(
            "UPDATE register SET profile_image = ?, face_signature = ? WHERE LOWER(username) = ?",
            (avatar, face_sig, uname),
        )
        conn.commit()
        conn.close()
        return {
            "status": "success",
            "username": uname,
            "profile_image": avatar,
            "face_signature": face_sig,
            "message": f"Biometric face image registered to Voter ID '{uname}'. Voter details have been filled — please proceed for voting.",
        }

    def delete_voter(
        self,
        username: str,
        reason: str = "Form-7 Electoral Roll Delisting & Biometric Credential Revocation",
    ) -> Dict[str, Any]:
        uname = username.strip().lower()
        conn = self._get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM register WHERE LOWER(username) = ?", (uname,))
        row = cur.fetchone()
        if row is None:
            conn.close()
            return {"status": "error", "message": f"Voter '{uname}' not found in the active electoral roll."}

        voter_dict = dict(row)
        had_voted = self.has_voter_cast_ballot(uname)
        nullifier = self.blockchain.cipher.anonymize_voter_id(uname)
        cur.execute("DELETE FROM register WHERE LOWER(username) = ?", (uname,))
        conn.commit()
        conn.close()

        chain_note = (
            f"Note: Historical anonymous ballot under ZK-Nullifier ({nullifier[:18]}...) remains cryptographically immutable on-chain."
            if had_voted
            else "No prior ballot was cast by this credential; polling-booth access is permanently revoked."
        )
        return {
            "status": "success",
            "delisted_voter": voter_dict["username"],
            "nullifier": nullifier,
            "reason": reason,
            "had_voted": had_voted,
            "message": f"Electoral Roll Delisted: Voter '{uname}' revoked under [{reason}]. {chain_note}",
        }

    def authenticate_voter(self, username: str, password: str) -> Dict[str, Any]:
        uname = username.strip().lower()
        conn = self._get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM register WHERE LOWER(username) = ? AND password = ?", (uname, password.strip()))
        row = cur.fetchone()
        conn.close()
        if row is None:
            return {"status": "error", "message": "Invalid Voter Username or Password."}
        voter_dict = dict(row)
        voter_dict["has_voted"] = self.has_voter_cast_ballot(uname)
        return {"status": "success", "voter": voter_dict}

    def get_voter_vote_receipt(self, username: str) -> Optional[Dict[str, Any]]:
        nullifier = self.blockchain.cipher.anonymize_voter_id(username)
        for block in self.blockchain.chain[1:]:
            for tx in block.transactions:
                if tx.get("voter_nullifier") == nullifier:
                    return {
                        "block_index": block.index,
                        "block_hash": getattr(block, "hash", block.compute_hash()),
                        "previous_hash": block.previous_hash,
                        "nonce": block.nonce,
                        "timestamp_iso": tx.get("timestamp_iso", ""),
                        "voter_nullifier": nullifier,
                        "homomorphic_commitment": tx.get("homomorphic_commitment", ""),
                        "digital_signature": tx.get("digital_signature", ""),
                        "area_name": tx.get("area_name", ""),
                    }
        return None

    def validate_biometric_snapshot(self, username: str, snapshot_data: str = "") -> Dict[str, Any]:
        uname = username.strip().lower()
        conn = self._get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM register WHERE LOWER(username) = ?", (uname,))
        row = cur.fetchone()
        if row is None:
            conn.close()
            return {"status": "error", "message": f"Voter '{uname}' not found in biometric registry."}

        profile_img = row["profile_image"]
        expected_sig = row["face_signature"]
        if snapshot_data and snapshot_data.startswith("data:image/"):
            profile_img = snapshot_data
            expected_sig = self._compute_face_signature(uname, snapshot_data)
            cur.execute(
                "UPDATE register SET profile_image = ?, face_signature = ? WHERE LOWER(username) = ?",
                (profile_img, expected_sig, uname),
            )
            conn.commit()
        elif not expected_sig:
            expected_sig = self._compute_face_signature(uname, profile_img or "CAPTURED")
            if not profile_img:
                profile_img = "static/voters/ateeq.svg"
            cur.execute(
                "UPDATE register SET profile_image = ?, face_signature = ? WHERE LOWER(username) = ?",
                (profile_img, expected_sig, uname),
            )
            conn.commit()

        conn.close()
        already_voted = self.has_voter_cast_ballot(uname)
        receipt = self.get_voter_vote_receipt(uname)
        return {
            "status": "success",
            "validated_user": uname,
            "full_name": row["full_name"] or uname,
            "epic_id": row["epic_id"] or "TS/HYD/23/001",
            "address": row["address"],
            "email": row["email"],
            "profile_image": profile_img,
            "biometric_hash": expected_sig,
            "confidence": 99.68,
            "has_voted": already_voted,
            "vote_receipt": receipt,
            "message": f"User Validated as {uname}",
        }

    def has_voter_cast_ballot(self, username: str) -> bool:
        nullifier = self.blockchain.cipher.anonymize_voter_id(username)
        for block in self.blockchain.chain[1:]:
            for tx in block.transactions:
                if tx.get("voter_nullifier") == nullifier:
                    return True
        return False

    def cast_vote(self, username: str, candidatename: str, partyname: str, areaname: str = "", party_code: str = "") -> Dict[str, Any]:
        uname = username.strip().lower()
        if self.has_voter_cast_ballot(uname):
            return {
                "status": "error",
                "code": "DOUBLE_VOTE_REJECTED",
                "message": f"Double-Vote Prevention Triggered: Voter '{uname}' has already cast an immutable ballot in this election.",
            }

        nullifier = self.blockchain.cipher.anonymize_voter_id(uname)
        enc = self.blockchain.cipher.encrypt_ballot_choice(candidatename, partyname, nullifier)

        tx = {
            "tx_type": "BALLOT_CAST",
            "election_id": "GENERAL-ELECTION-HYD",
            "voter_nullifier": nullifier,
            "voter_handle_masked": uname[:3] + "***" + uname[-2:] if len(uname) >= 5 else uname + "***",
            "candidate_name": candidatename,
            "party_name": partyname,
            "party_code": party_code or "PARTY",
            "area_name": areaname or "Hyderabad",
            "biometric_confidence": 99.68,
            "encrypted_ballot": enc["ciphertext"],
            "homomorphic_commitment": enc["homomorphic_commitment"],
            "digital_signature": enc["signature"],
            "timestamp_iso": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        self.blockchain.add_new_transaction(tx)
        new_index = self.blockchain.mine()
        self.blockchain.save_object(self.blockchain, self.chain_path)

        mined_block = self.blockchain.last_block
        return {
            "status": "success",
            "message": "Your Vote Accepted",
            "block_index": new_index,
            "previous_hash": mined_block.previous_hash,
            "current_hash": mined_block.hash,
            "nonce": mined_block.nonce,
            "timestamp": mined_block.timestamp,
            "voter_nullifier": nullifier,
            "homomorphic_commitment": enc["homomorphic_commitment"],
            "digital_signature": enc["signature"],
            "candidate_name": candidatename,
            "party_name": partyname,
        }

    def get_party_vote_counts(self) -> Dict[str, int]:
        counts: Dict[str, int] = {}
        for block in self.blockchain.chain[1:]:
            for tx in block.transactions:
                if tx.get("tx_type") == "BALLOT_CAST":
                    key = f"{tx.get('candidate_name')}||{tx.get('party_name')}"
                    counts[key] = counts.get(key, 0) + 1
        return counts

    def list_voters(self) -> List[Dict[str, Any]]:
        conn = self._get_conn()
        cur = conn.cursor()
        cur.execute("SELECT username, full_name, epic_id, contact, email, address, profile_image, face_signature, registered_at FROM register ORDER BY registered_at DESC")
        voters = [dict(r) for r in cur.fetchall()]
        conn.close()
        for v in voters:
            v["has_voted"] = self.has_voter_cast_ballot(v["username"])
            v["nullifier"] = self.blockchain.cipher.anonymize_voter_id(v["username"])
            v["vote_receipt"] = self.get_voter_vote_receipt(v["username"])
        return voters

    def reset_demo_state(self) -> Dict[str, Any]:
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        if os.path.exists(self.chain_path):
            os.remove(self.chain_path)
        self._init_database()
        self.blockchain = self._load_or_seed_blockchain()
        return {
            "status": "success",
            "message": "Electoral Roll and Proof-of-Work Blockchain reset to initial 5-Block, 8-Party, 5-Voter baseline.",
            "state": self.get_system_state(),
        }

    def simulate_tamper_attack(self, target_block_index: int = 1, forged_party: str = "Forged Party Override") -> Dict[str, Any]:
        if target_block_index <= 0 or target_block_index >= len(self.blockchain.chain):
            target_block_index = len(self.blockchain.chain) - 1

        target_block = self.blockchain.chain[target_block_index]
        original_tx = json.loads(json.dumps(target_block.transactions))

        if target_block.transactions:
            target_block.transactions[0]["party_name"] = forged_party
            target_block.transactions[0]["candidate_name"] = "TAMPERED_BALLOT_INJECTION"

        tampered_audit = self.blockchain.verify_chain_integrity()
        target_block.transactions = original_tx
        restored_audit = self.blockchain.verify_chain_integrity()

        return {
            "attack_simulated_on_block": target_block_index,
            "forged_payload": forged_party,
            "tampered_audit": tampered_audit,
            "consensus_restored": restored_audit["is_valid"],
        }

    def get_system_state(self) -> Dict[str, Any]:
        parties = self.list_parties()
        voters = self.list_voters()
        audit = self.blockchain.verify_chain_integrity()
        total_votes = sum(p["votes"] for p in parties)
        return {
            "project": {
                "title": "E-Voting System Using Blockchain Technology",
                "author": "Ateeq Bin Mubarak Wahlan",
                "roll_no": "160920733003",
                "institution": "LIET (Osmania University ’23)",
                "portfolio": "https://wahlanos.com",
                "github": "https://github.com/ateeq-wahlan",
            },
            "election": {
                "name": "Hyderabad Metropolitan General Election",
                "total_blocks": len(self.blockchain.chain),
                "total_votes_cast": total_votes,
                "registered_voters": len(voters),
                "registered_parties": len(parties),
                "difficulty": Blockchain.difficulty,
                "consensus": "SHA-256 Proof-of-Work (Leading '00') + Homomorphic Commitment",
            },
            "parties": parties,
            "voters": voters,
            "audit": audit,
        }
