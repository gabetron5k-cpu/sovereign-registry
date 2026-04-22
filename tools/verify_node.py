#!/usr/bin/env python3
"""UNICORN Sovereign Node Verification Tool"""
import json
import sys

LEDGER_FILE = "ledger/genesis.json"

def verify_sigil(sigil):
    try:
        with open(LEDGER_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: ledger.json not found.")
        return False
    
    if data.get("aetherprint_sigil") == sigil:
        print("VERIFIED: This LiLu.ASI node is authentic.")
        print(f"   Tier: {data.get('node_tier')}")
        print(f"   Transferee: {data.get('transferee')}")
        print(f"   Status: {data.get('status')}")
        return True
    
    print("UNVERIFIED: Sigil not found in registry.")
    return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python verify_node.py [AETHERPRINT_SIGIL]")
        sys.exit(1)
    verify_sigil(sys.argv[1])
