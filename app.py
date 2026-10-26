#!/usr/bin/env python3
"""
================================================================================
E-VOTING SYSTEM USING BLOCKCHAIN TECHNOLOGY
Module: app.py — Zero-Dependency HTTP/JSON & Static Web Application Server
================================================================================
Author:      Ateeq Bin Mubarak Wahlan (Roll No: 160920733003)
WahlanOS:    https://wahlanos.com ↗ | https://github.com/ateeq-wahlan
Institution: LIET (Osmania University ’23)
================================================================================
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import os
import sys
from urllib.parse import urlparse
import webbrowser

from evoting_engine import EVotingEngine

PORT = int(os.environ.get("PORT", 5070))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENGINE = EVotingEngine(BASE_DIR)


class EVotingRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

    def _send_json(self, payload: dict, status_code: int = 200) -> None:
        raw = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
        self.wfile.write(raw)

    def do_OPTIONS(self) -> None:
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        route = parsed.path

        if route == "/api/state":
            self._send_json(ENGINE.get_system_state())
            return
        if route == "/api/parties":
            self._send_json({"parties": ENGINE.list_parties()})
            return
        if route == "/api/voters":
            self._send_json({"voters": ENGINE.list_voters()})
            return
        if route == "/api/audit":
            self._send_json(ENGINE.blockchain.verify_chain_integrity())
            return

        legacy_routes = {
            "/": "/index.html",
            "/index.html": "/index.html",
            "/Admin.html": "/index.html",
            "/AddParty.html": "/index.html",
            "/ViewParty": "/index.html",
            "/Signup": "/index.html",
            "/Login.html": "/index.html",
            "/CastVote.html": "/index.html",
            "/ValidateUser": "/index.html",
            "/ViewVotes": "/index.html",
        }
        if route in legacy_routes:
            self.path = legacy_routes[route]

        return super().do_GET()

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        route = parsed.path
        length = int(self.headers.get("Content-Length", 0))
        body_bytes = self.rfile.read(length) if length > 0 else b"{}"
        try:
            data = json.loads(body_bytes.decode("utf-8"))
        except Exception:
            data = {}

        if route == "/api/admin/login":
            ok = ENGINE.authenticate_admin(data.get("username", ""), data.get("password", ""))
            if ok:
                self._send_json({"status": "success", "message": "Electoral Commission Admin Authority unlocked."})
            else:
                self._send_json({"status": "error", "message": "Invalid Admin credentials (use admin / admin)."}, 401)
            return

        if route == "/api/admin/add-party":
            res = ENGINE.add_party(
                candidatename=data.get("candidatename", ""),
                partyname=data.get("partyname", ""),
                areaname=data.get("areaname", ""),
                image=data.get("image", "static/parties/bjp.svg"),
                party_code=data.get("party_code", "IND"),
                manifesto=data.get("manifesto", "Civic Infrastructure & Transparent Governance"),
            )
            self._send_json({"result": res, "state": ENGINE.get_system_state()})
            return

        if route == "/api/admin/delete-party":
            res = ENGINE.delete_party(
                party_id=int(data.get("party_id", 0)),
                reason=data.get("reason", "EC Form-2B Official Mandate Revocation"),
            )
            code = 200 if res["status"] == "success" else 400
            self._send_json({"result": res, "state": ENGINE.get_system_state()}, code)
            return

        if route == "/api/admin/delete-voter":
            res = ENGINE.delete_voter(
                username=data.get("username", ""),
                reason=data.get("reason", "Form-7 Electoral Roll Delisting & Biometric Revocation"),
            )
            code = 200 if res["status"] == "success" else 400
            self._send_json({"result": res, "state": ENGINE.get_system_state()}, code)
            return

        if route == "/api/admin/reset-demo":
            res = ENGINE.reset_demo_state()
            self._send_json(res)
            return

        if route == "/api/voter/signup":
            res = ENGINE.register_voter(
                username=data.get("username", ""),
                password=data.get("password", ""),
                contact=data.get("contact", ""),
                email=data.get("email", ""),
                address=data.get("address", ""),
                full_name=data.get("full_name", ""),
                profile_image=data.get("profile_image", ""),
            )
            code = 200 if res["status"] == "success" else 400
            self._send_json({"result": res, "state": ENGINE.get_system_state()}, code)
            return

        if route == "/api/voter/register-biometric":
            res = ENGINE.register_biometric_image(
                username=data.get("username", ""),
                image_data=data.get("image_data", ""),
            )
            code = 200 if res["status"] == "success" else 400
            self._send_json({"result": res, "state": ENGINE.get_system_state()}, code)
            return

        if route == "/api/voter/login":
            res = ENGINE.authenticate_voter(data.get("username", ""), data.get("password", ""))
            code = 200 if res["status"] == "success" else 401
            self._send_json(res, code)
            return

        if route == "/api/voter/validate-biometric":
            res = ENGINE.validate_biometric_snapshot(
                username=data.get("username", ""),
                snapshot_data=data.get("snapshot_data", ""),
            )
            code = 200 if res["status"] == "success" else 400
            self._send_json(res, code)
            return

        if route == "/api/voter/cast-vote":
            res = ENGINE.cast_vote(
                username=data.get("username", ""),
                candidatename=data.get("candidatename", ""),
                partyname=data.get("partyname", ""),
                areaname=data.get("areaname", ""),
                party_code=data.get("party_code", ""),
            )
            code = 200 if res["status"] == "success" else 400
            self._send_json({"result": res, "state": ENGINE.get_system_state()}, code)
            return

        if route == "/api/blockchain/simulate-tamper":
            res = ENGINE.simulate_tamper_attack(
                target_block_index=int(data.get("block_index", 1)),
                forged_party=data.get("forged_party", "Unauthorized Tampered Party"),
            )
            self._send_json(res)
            return

        self._send_json({"status": "error", "message": f"Unknown API endpoint: {route}"}, 404)


def run_server(open_browser: bool = True) -> None:
    server_address = ("127.0.0.1", PORT)
    httpd = HTTPServer(server_address, EVotingRequestHandler)
    url = f"http://127.0.0.1:{PORT}/index.html"
    print("=" * 78)
    print("  CIVICCHAIN // E-VOTING SYSTEM USING BLOCKCHAIN TECHNOLOGY")
    print("  Architect: Ateeq Bin Mubarak Wahlan (Roll No: 160920733003)")
    print("  Institution: LIET (Osmania University ’23) | WahlanOS.com")
    print(f"  Server listening at: {url}")
    print("=" * 78)
    if open_browser and os.environ.get("NO_BROWSER") != "1":
        try:
            webbrowser.open(url)
        except Exception:
            pass
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down E-Voting Blockchain Server...")
        httpd.server_close()


if __name__ == "__main__":
    run_server(open_browser="--no-browser" not in sys.argv)
