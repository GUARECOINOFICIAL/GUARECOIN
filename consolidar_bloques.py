import json, hashlib

dificultad = 4
archivos = ["registro_mineria_sha256.json", "registro_mineria_sha3.json"]
total_guarecoins = 0

def verificar_hash(texto, algoritmo):
    if algoritmo == "SHA-256":
        return hashlib.sha256(texto.encode()).hexdigest()
    elif algoritmo == "SHA-3":
        return hashlib.sha3_256(texto.encode()).hexdigest()
    return None

def consolidar_bloques():
    global total_guarecoins
    for archivo in archivos:
        try:
            with open(archivo, "r") as f:
                bloques = json.load(f)
        except:
            continue

        for bloque in bloques:
            algoritmo = bloque.get("algoritmo")
            usuario = bloque.get("usuario")
            timestamp = bloque.get("timestamp")
            nonce = bloque.get("nonce")
            hash_guardado = bloque.get("hash")
            recompensa = bloque.get("recompensa_total", 0)

            base = usuario + timestamp + str(nonce)
            hash_calculado = verificar_hash(base, algoritmo)

            if not hash_calculado or not hash_calculado.startswith("0" * dificultad):
                continue
            if hash_calculado != hash_guardado:
                continue

            total_guarecoins += recompensa

    print(f"✅ Consolidación completa: {total_guarecoins} GUARECOINS™ acreditados a tu billetera multimoneda")

consolidar_bloques()