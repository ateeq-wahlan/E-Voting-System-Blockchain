"""
================================================================================
E-VOTING SYSTEM USING BLOCKCHAIN TECHNOLOGY
Module: Block.py — Cryptographic Block Structure & SHA-256 Hashing Engine
================================================================================
Author:      Ateeq Bin Mubarak Wahlan (Roll No: 160920733003)
Portfolio:   https://wahlanos.com | https://github.com/ateeq-wahlan
Supervisor:  Ms. Gazala Begum (Asst. Professor, Dept. of CSE)
Institution: Lords Institute of Engineering & Technology (Osmania University)
================================================================================
"""

from hashlib import sha256
import json
import time
from typing import Any, Dict, List, Optional


class Block:
    """
    Represents a single immutable block in the E-Voting Blockchain Ledger.
    Restores the exact specification from Chapter 6.2 (Block.py, p. 42) of the
    Major Project Report while adding deterministic serialization and metadata
    inspection helpers.
    """

    def __init__(
        self,
        index: int,
        transactions: List[Dict[str, Any]],
        timestamp: Optional[float] = None,
        previous_hash: str = "0",
        nonce: int = 0,
    ) -> None:
        self.index: int = index
        self.transactions: List[Dict[str, Any]] = transactions
        self.timestamp: float = timestamp if timestamp is not None else time.time()
        self.previous_hash: str = previous_hash
        self.nonce: int = nonce

    def compute_hash(self) -> str:
        """
        Returns the SHA-256 cryptographic digest of the block contents.
        Excludes any dynamically attached `.hash` attribute during calculation
        so that verification (`block.compute_hash() == block.hash`) is always
        idempotent and deterministic.
        """
        block_dict = {
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
        }
        block_string = json.dumps(block_dict, sort_keys=True)
        return sha256(block_string.encode("utf-8")).hexdigest()

    def to_dict(self) -> Dict[str, Any]:
        """Serializes the block including its finalized Proof-of-Work hash."""
        return {
            "index": self.index,
            "transactions": self.transactions,
            "timestamp": self.timestamp,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
            "hash": getattr(self, "hash", self.compute_hash()),
        }
