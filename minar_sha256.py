import hashlib, json, time, os

recompensa_total = 10
dificultad = 4
registro = "registro_mineria_sha256.json"

if not os.path.exists(registro):
    with open(registro, "w") as f:
        json.dump([], f, indent=2)

def calcular_hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

def minar_bloque():
    nonce = 0
    timestamp = str(time.time())
    base = "anonimo" + timestamp

    print("⛏️ Minando bloque SHA-256...")

    while True:
        texto = base + str(nonce)
        hash_resultado = calcular_hash(texto)
        if hash_resultado.startswith("0" * dificultad):
            break
        nonce += 1

    bloque = {
        "algoritmo": "SHA-256",
        "usuario": "anonimo",
        "timestamp": timestamp,
        "nonce": nonce,
        "hash": hash_resultado,
        "recompensa_total": recompensa_total
    }

    with open(registro, "r+") as f:
        datos = json.load(f)
        datos.append(bloque)
        f.seek(0)
        json.dump(datos, f, indent=2)

    print(f"✅ ¡Bloque SHA-256 minado! {recompensa_total} GUARECOINS™")

minar_bloque()