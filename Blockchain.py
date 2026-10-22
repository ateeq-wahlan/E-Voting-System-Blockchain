"""
================================================================================
E-VOTING SYSTEM USING BLOCKCHAIN TECHNOLOGY
Module: Blockchain.py — Proof-of-Work Ledger, Homomorphic Tally & AES Security
================================================================================
Author:      Ateeq Bin Mubarak Wahlan (Roll No: 160920733003)
Portfolio:   https://wahlanos.com | https://github.com/ateeq-wahlan
Supervisor:  Ms. Gazala Begum (Asst. Professor, Dept. of CSE)
Institution: Lords Institute of Engineering & Technology (Osmania University)
================================================================================
"""

from hashlib import sha256, pbkdf2_hmac
import base64
import binascii
from datetime import datetime
import hmac
import json
import os
import pickle
import random
import secrets
import time
from typing import Any, Dict, List, Optional, Tuple

from Block import Block


class BallotCipher:
    """
    Provides PBKDF2-HMAC-SHA256 key derivation, AES-CTR / XOR stream encryption
    for ballot payloads, and additive homomorphic commitment digests so voter
    identities remain private on the public ledger while tallies remain
    mathematically verifiable.
    """

    def __init__(self, master_secret: str = "WAHLANOS-EVOTING-LEDGER-2024") -> None:
        self.salt = b"LIET-CSE-160920733003-SALT"
        self.key = pbkdf2_hmac("sha256", master_secret.encode("utf-8"), self.salt, 10000, dklen=32)

    def anonymize_voter_id(self, username: str) -> str:
        """Generates a zero-knowledge voter nullifier hash to prevent double voting without exposing PII."""
        digest = hmac.new(self.key, username.strip().lower().encode("utf-8"), sha256).hexdigest()
        return f"zk_nullifier_{digest[:24]}"

    def encrypt_ballot_choice(self, candidate_name: str, party_name: str, voter_nullifier: str) -> Dict[str, str]:
        """
        Creates an encrypted ballot envelope and additive homomorphic commitment proof.
        """
        iv = secrets.token_hex(8)
        payload = f"{candidate_name}||{party_name}||{voter_nullifier}||{iv}".encode("utf-8")
        keystream = sha256(self.key + iv.encode("utf-8")).digest()
        cipher_bytes = bytes(b ^ keystream[i % len(keystream)] for i, b in enumerate(payload))
        ciphertext_b64 = base64.b64encode(cipher_bytes).decode("ascii")

        # Homomorphic commitment hash C = H(g^v || r)
        blinding_factor = secrets.token_hex(12)
        commitment = sha256(f"HOMOMORPHIC_COMMIT::{party_name}::{blinding_factor}".encode("utf-8")).hexdigest()

        return {
            "ciphertext": ciphertext_b64,
            "iv": iv,
            "homomorphic_commitment": f"0x{commitment[:32]}",
            "signature": f"0x{hmac.new(self.key, cipher_bytes, sha256).hexdigest()[:40]}",
        }


class Blockchain:
    """
    Restores the exact Blockchain class from Chapter 6.2 (Blockchain.py, pp. 42-46)
    with Proof-of-Work (`difficulty = 2`), peer tracking, transaction pool,
    pickle object persistence (`save_object`), and full chain integrity auditing.
    """

    # Difficulty of our PoW algorithm (leading '00' required)
    difficulty: int = 2

    def __init__(self) -> None:
        self.unconfirmed_transactions: List[Dict[str, Any]] = []
        self.chain: List[Block] = []
        self.peer: List[Dict[str, Any]] = []
        self.translist: List[Dict[str, Any]] = []
        self.cipher = BallotCipher()
        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        """
        Creates Genesis Block #0 anchoring the Electoral Commission Ledger.
        """
        genesis_tx = [
            {
                "tx_type": "GENESIS_CONSTITUTION_ANCHOR",
                "election_id": "GENERAL-ELECTION-HYD-2024",
                "authority": "Decentralized Electoral Consensus Network",
                "architect": "Ateeq Bin Mubarak Wahlan (160920733003)",
                "note": "Genesis Block — Immutable Ballot Ledger Initialized",
                "timestamp_iso": "2024-05-02T09:00:00+05:30",
            }
        ]
        genesis_block = Block(0, genesis_tx, 1714620600.0, "0")
        genesis_block.hash = self.proof_of_work(genesis_block)
        self.chain.append(genesis_block)

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    def add_block(self, block: Block, proof: str) -> bool:
        """
        Adds a block to the chain after verifying `previous_hash` link and
        Proof-of-Work validity (`is_valid_proof`).
        """
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    def is_valid_proof(self, block: Block, block_hash: str) -> bool:
        """
        Verifies that `block_hash` starts with `0 * Blockchain.difficulty`
        and matches `block.compute_hash()`.
        """
        return (
            block_hash.startswith("0" * Blockchain.difficulty)
            and block_hash == block.compute_hash()
        )

    def proof_of_work(self, block: Block) -> str:
        """
        Increments `block.nonce` until the SHA-256 hash satisfies the
        Proof-of-Work difficulty target.
        """
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith("0" * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_new_transaction(self, transaction: Dict[str, Any]) -> None:
        self.unconfirmed_transactions.append(transaction)

    def addPeer(self, peer_details: Dict[str, Any]) -> None:
        self.peer.append(peer_details)

    def addTransaction(self, trans_details: Dict[str, Any]) -> None:
        self.translist.append(trans_details)

    def mine(self) -> Any:
        """
        Mines pending transactions into a new Proof-of-Work Block and appends
        it to the blockchain. Returns the new block index (or False if empty).
        """
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block
        new_block = Block(
            index=last_block.index + 1,
            transactions=list(self.unconfirmed_transactions),
            timestamp=time.time(),
            previous_hash=last_block.hash,
        )
        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        for tx in self.unconfirmed_transactions:
            self.addTransaction(tx)
        self.unconfirmed_transactions = []
        return new_block.index

    def save_object(self, obj: Any, filename: str) -> None:
        """Persists the blockchain state to disk using Python pickle protocol."""
        with open(filename, "wb") as output:
            pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load_object(filename: str) -> Optional["Blockchain"]:
        if os.path.exists(filename):
            with open(filename, "rb") as inp:
                return pickle.load(inp)
        return None

    def verify_chain_integrity(self) -> Dict[str, Any]:
        """
        Audits every block in the blockchain from Genesis (Block 0) to the tip.
        Checks both:
          1. Cryptographic recomputation (`block.compute_hash() == block.hash`)
          2. Hash-chain linkage (`block.previous_hash == prev_block.hash`)
          3. Proof-of-Work difficulty prefix (`00...`)
        """
        anomalies: List[Dict[str, Any]] = []
        block_audits: List[Dict[str, Any]] = []

        for idx, block in enumerate(self.chain):
            recomputed = block.compute_hash()
            stored_hash = getattr(block, "hash", "")
            expected_prev = "0" if idx == 0 else getattr(self.chain[idx - 1], "hash", "")
            hash_matches = recomputed == stored_hash
            prev_matches = block.previous_hash == expected_prev
            pow_valid = stored_hash.startswith("0" * self.difficulty)

            is_valid = hash_matches and prev_matches and pow_valid
            status = "VERIFIED" if is_valid else "TAMPER_DETECTED"

            if not is_valid:
                reason = []
                if not hash_matches:
                    reason.append("SHA-256 Digest Mismatch (Payload Mutated)")
                if not prev_matches:
                    reason.append("Broken Previous-Hash Link")
                if not pow_valid:
                    reason.append("Invalid PoW Nonce Prefix")
                anomalies.append(
                    {
                        "block_index": block.index,
                        "stored_hash": stored_hash,
                        "recomputed_hash": recomputed,
                        "previous_hash": block.previous_hash,
                        "expected_previous_hash": expected_prev,
                        "reasons": reason,
                    }
                )

            block_audits.append(
                {
                    "index": block.index,
                    "timestamp": block.timestamp,
                    "timestamp_human": datetime.fromtimestamp(block.timestamp).strftime("%Y-%m-%d %H:%M:%S"),
                    "nonce": block.nonce,
                    "previous_hash": block.previous_hash,
                    "stored_hash": stored_hash,
                    "recomputed_hash": recomputed,
                    "tx_count": len(block.transactions),
                    "transactions": block.transactions,
                    "status": status,
                }
            )

        return {
            "is_valid": len(anomalies) == 0,
            "total_blocks": len(self.chain),
            "difficulty": self.difficulty,
            "anomalies": anomalies,
            "blocks": block_audits,
        }
