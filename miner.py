import json
import hashlib
import time
import socket
from pathlib import Path

GENESIS_FILE = Path("/home/guare/ECOSISTEMA_GUARECOIN/GUARECOIN/repo/data/genesis.json")
MINER_WALLET = "GUARECOIN_WALLET_ADDRESS_AQUI"  # ⚡ Reemplaza con tu dirección real

DIFFICULTY = 4  # número de ceros iniciales requeridos en el hash

def load_genesis():
    with GENESIS_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

def proof_of_work(block):
    block_str = json.dumps(block, sort_keys=True).encode()
    nonce = 0
    while True:
        candidate = block_str + str(nonce).encode()
        hash_result = hashlib.sha256(candidate).hexdigest()
        if hash_result.startswith("0" * DIFFICULTY):
            return nonce, hash_result
        nonce += 1

def mine_block(previous_hash, transactions):
    block = {
        "previous_hash": previous_hash,
        "transactions": transactions,
        "timestamp": time.time(),
        "miner": MINER_WALLET
    }
    nonce, block_hash = proof_of_work(block)
    block["nonce"] = nonce
    block["hash"] = block_hash
    return block

def broadcast_block(block, host="127.0.0.1", port=30303):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(json.dumps(block).encode("utf-8"))
        s.close()
        print(f"📦 Bloque minado enviado al nodo {host}:{port}")
    except Exception as e:
        print(f"⚠️ Error al enviar bloque: {e}")

if __name__ == "__main__":
    genesis = load_genesis()
    prev_hash = genesis["genesis_hash"]

    # Ejemplo de transacción: recompensa al minero
    transactions = [
        {"from": "network", "to": MINER_WALLET, "amount": 50}
    ]

    print("⛏️ Iniciando minería...")
    block = mine_block(prev_hash, transactions)
    print(f"✅ Bloque minado con hash: {block['hash']}")
    broadcast_block(block)