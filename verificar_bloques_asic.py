import json, hashlib

dificultad = 4
archivos = ["registro_mineria_sha256.json", "registro_mineria_sha3.json"]

def verificar_hash_sha256(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

def verificar_hash_sha3(texto):
    return hashlib.sha3_256(texto.encode()).hexdigest()

def verificar_bloques():
    for archivo in archivos:
        print(f"\n🔍 Verificando bloques en {archivo}...")
        try:
            with open(archivo, "r") as f:
                bloques = json.load(f)
        except:
            print("⚠️ Archivo no encontrado o vacío.")
            continue

        for i, bloque in enumerate(bloques, 1):
            algoritmo = bloque.get("algoritmo")
            usuario = bloque.get("usuario")
            timestamp = bloque.get("timestamp")
            nonce = bloque.get("nonce")
            hash_guardado = bloque.get("hash")

            base = usuario + timestamp + str(nonce)

            if algoritmo == "SHA-256":
                hash_calculado = verificar_hash_sha256(base)
            elif algoritmo == "SHA-3":
                hash_calculado = verificar_hash_sha3(base)
            else:
                print(f"❌ Bloque {i}: Algoritmo no permitido → {algoritmo}")
                continue

            if not hash_calculado.startswith("0" * dificultad):
                print(f"❌ Bloque {i}: Hash inválido → {hash_calculado}")
                continue

            if hash_calculado != hash_guardado:
                print(f"❌ Bloque {i}: Hash no coincide con el registrado")
                continue

            print(f"✅ Bloque {i} válido ({algoritmo})")

verificar_bloques()