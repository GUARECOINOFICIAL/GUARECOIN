import json
import socket
import threading
import argparse
import time
from pathlib import Path

GENESIS_FILE = Path("/home/guare/ECOSISTEMA_GUARECOIN/GUARECOIN/repo/data/genesis.json")
BOOTSTRAP_FILE = Path("/home/guare/ECOSISTEMA_GUARECOIN/GUARECOIN/repo/data/bootstrap.txt")
BLOCKS_FILE = Path("/home/guare/ECOSISTEMA_GUARECOIN/GUARECOIN/repo/data/blocks.json")

DEFAULT_PORT = 30303
CONNECT_TIMEOUT = 3

# Cargar génesis
if not GENESIS_FILE.exists():
    raise FileNotFoundError(f"❌ No se encontró el génesis en: {GENESIS_FILE}")
with GENESIS_FILE.open("r", encoding="utf-8") as f:
    genesis = json.load(f)

print("✅ Nodo GUARECOIN iniciado")
print(f"🔑 Hash génesis: {genesis['genesis_hash']}")
print(f"🧮 Suministro inicial: {genesis['meta']['total_initial_supply']} GUARECOIN")
print(f"📂 Data dir: {GENESIS_FILE.parent}")

# Inicializar cadena de bloques local
if not BLOCKS_FILE.exists():
    with BLOCKS_FILE.open("w", encoding="utf-8") as f:
        json.dump([], f, indent=2)

peers = []

def append_block(block_json_str: str):
    try:
        block = json.loads(block_json_str)
    except Exception as e:
        print(f"⚠️ Bloque inválido (JSON): {e}")
        return

    # Validaciones mínimas
    required_keys = {"previous_hash", "transactions", "timestamp", "miner", "nonce", "hash"}
    if not required_keys.issubset(block.keys()):
        print("⚠️ Bloque inválido (faltan campos requeridos)")
        return

    # Guardar
    try:
        with BLOCKS_FILE.open("r", encoding="utf-8") as f:
            chain = json.load(f)
        chain.append(block)
        with BLOCKS_FILE.open("w", encoding="utf-8") as f:
            json.dump(chain, f, indent=2)
        print(f"✅ Bloque guardado: {block['hash']}")
    except Exception as e:
        print(f"⚠️ Error guardando bloque: {e}")

def handle_client(conn, addr):
    print(f"🔗 Conexión recibida de {addr}")
    try:
        data = conn.recv(65536).decode("utf-8")
        if data:
            print("📦 Bloque recibido, procesando...")
            append_block(data)
            conn.send(b"OK")
        else:
            # Si no envían bloque, devolvemos el génesis como handshake básico
            conn.send(json.dumps(genesis).encode("utf-8"))
    except Exception as e:
        print(f"⚠️ Error en cliente {addr}: {e}")
    finally:
        conn.close()

def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", port))
    server.listen(32)
    print(f"🌍 Nodo escuchando en puerto {port}...")

    while True:
        conn, addr = server.accept()
        peers.append(addr)
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

def load_bootstrap_nodes():
    if not BOOTSTRAP_FILE.exists():
        print(f"⚠️ No se encontró bootstrap.txt en {BOOTSTRAP_FILE}.")
        return []
    with BOOTSTRAP_FILE.open("r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f.readlines()]
    nodes = []
    for ln in lines:
        if not ln or ln.startswith("#"):
            continue
        if ":" not in ln:
            print(f"⚠️ Línea inválida en bootstrap.txt: '{ln}' (ip:puerto)")
            continue
        ip, port = ln.split(":", 1)
        ip, port = ip.strip(), port.strip()
        if not ip or not port.isdigit():
            print(f"⚠️ Línea inválida en bootstrap.txt: '{ln}'")
            continue
        nodes.append((ip, int(port)))
    if nodes:
        print(f"📂 Bootstrap: {len(nodes)} peers cargados")
    else:
        print("⚠️ Bootstrap sin peers válidos")
    return nodes

def connect_bootstrap(self_ip=None, self_port=None):
    nodes = load_bootstrap_nodes()
    for ip, port in nodes:
        if self_ip and self_port and ip == self_ip and port == self_port:
            print(f"ℹ️ Omitiendo conexión a sí mismo {ip}:{port}")
            continue
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(CONNECT_TIMEOUT)
            s.connect((ip, port))
            s.send(b"HELLO")
            print(f"🤝 Conectado bootstrap {ip}:{port}")
            s.close()
        except Exception as e:
            print(f"⚠️ No se pudo conectar a {ip}:{port} ({e})")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Puerto del nodo")
    args = parser.parse_args()

    threading.Thread(target=start_server, args=(args.port,), daemon=True).start()
    connect_bootstrap(self_ip="127.0.0.1", self_port=args.port)

    while True:
        time.sleep(60)