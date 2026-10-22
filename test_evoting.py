#!/usr/bin/env python3
"""
================================================================================
E-VOTING SYSTEM USING BLOCKCHAIN TECHNOLOGY (2023–2024)
Module: test_evoting.py — End-to-End Cryptographic & Functional Test Suite
================================================================================
Author:      Ateeq Bin Mubarak Wahlan (Roll No: 160920733003)
Portfolio:   https://wahlanos.com | https://github.com/ateeq-wahlan
Institution: LIET (Osmania University)
Academic Yr: 2023–2024 (B.E. Computer Science & Engineering)
================================================================================
"""

import tempfile
import unittest

from evoting_engine import EVotingEngine


class TestEVotingBlockchain(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.engine = EVotingEngine(base_dir=self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_01_initial_seed_and_pow_verification(self) -> None:
        state = self.engine.get_system_state()
        self.assertEqual(state["election"]["registered_parties"], 8)
        self.assertEqual(state["election"]["registered_voters"], 5)
        self.assertEqual(state["election"]["total_blocks"], 5)
        self.assertTrue(state["audit"]["is_valid"])
        for blk in state["audit"]["blocks"]:
            self.assertTrue(blk["stored_hash"].startswith("00"))
        # Verify all seeded voters have human portrait URLs and EPIC IDs
        for voter in state["voters"]:
            self.assertTrue(voter["profile_image"].startswith("http"))
            self.assertTrue(voter["epic_id"].startswith("TS/HYD/"))

    def test_02_admin_auth_and_add_delete_party_form2b(self) -> None:
        self.assertTrue(self.engine.authenticate_admin("admin", "admin"))
        self.assertFalse(self.engine.authenticate_admin("admin", "wrong"))
        res = self.engine.add_party(
            candidatename="Dr. Syed Saifullah",
            partyname="Telangana Civic Alliance",
            areaname="Banjara Hills",
            image="static/parties/bjp.svg",
            party_code="TCA",
        )
        self.assertEqual(res["status"], "success")
        self.assertEqual(len(self.engine.list_parties()), 9)

        # Form-2B Party Mandate Revocation (Deletion)
        del_res = self.engine.delete_party(
            party_id=res["party_id"],
            reason="EC Form-2B Candidacy Withdrawal",
        )
        self.assertEqual(del_res["status"], "success")
        self.assertEqual(len(self.engine.list_parties()), 8)

    def test_03_voter_signup_biometric_and_single_vote_enforcement(self) -> None:
        reg = self.engine.register_voter(
            username="newvoter_hyd",
            full_name="Syed Rayyan Ali",
            password="secret",
            contact="9000011111",
            email="newvoter@wahlanos.com",
            address="Jubilee Hills, Hyderabad",
        )
        self.assertEqual(reg["status"], "success")

        bio = self.engine.validate_biometric_snapshot("newvoter_hyd")
        self.assertEqual(bio["status"], "success")
        self.assertEqual(bio["message"], "User Validated as newvoter_hyd")
        self.assertEqual(bio["full_name"], "Syed Rayyan Ali")

        # Cast first vote -> should succeed and mine Block #5
        vote1 = self.engine.cast_vote(
            username="newvoter_hyd",
            candidatename="Rajeshwar Rao Deshmukh",
            partyname="Bharatiya Janata Party (BJP)",
            areaname="Jubilee Hills",
            party_code="BJP",
        )
        self.assertEqual(vote1["status"], "success")
        self.assertEqual(vote1["block_index"], 5)
        self.assertTrue(vote1["current_hash"].startswith("00"))

        # Attempt second vote -> must be rejected by Zero-Knowledge Nullifier check
        vote2 = self.engine.cast_vote(
            username="newvoter_hyd",
            candidatename="Dr. Ananya Reddy",
            partyname="Indian National Congress (INC)",
            areaname="Santosh Nagar",
            party_code="INC",
        )
        self.assertEqual(vote2["status"], "error")
        self.assertEqual(vote2["code"], "DOUBLE_VOTE_REJECTED")

        # Form-7 Voter Delisting -> revokes off-chain roll entry while keeping Block #5 immutable
        del_voter = self.engine.delete_voter("newvoter_hyd", "EC Form-7 Constituency Migration")
        self.assertEqual(del_voter["status"], "success")
        self.assertTrue(del_voter["had_voted"])
        self.assertEqual(len(self.engine.blockchain.chain), 6)

    def test_04_tamper_detection_and_self_healing(self) -> None:
        sim = self.engine.simulate_tamper_attack(target_block_index=1, forged_party="Hacked Party")
        self.assertFalse(sim["tampered_audit"]["is_valid"])
        self.assertGreaterEqual(len(sim["tampered_audit"]["anomalies"]), 1)
        self.assertTrue(sim["consensus_restored"])


if __name__ == "__main__":
    print("Running CivicChain E-Voting Verification Suite (Ateeq Bin Mubarak Wahlan - 160920733003)...")
    unittest.main(verbosity=2)
