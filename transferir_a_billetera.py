import hashlib, json

# Simulación de semilla BIP39 y derivación de dirección GUARECOIN™
semilla_bip39 = "ritual fuego cosmos verdad soberania krillin infinito mito universo"
direccion_guarecoin = hashlib.sha256(semilla_bip39.encode()).hexdigest()[:40]

# Leer consolidación
total_guarecoins = 0
archivos = ["registro_mineria_sha256.json", "registro_mineria_sha3.json"]
dificultad = 4

def verificar_hash(texto, algoritmo):
    if algoritmo == "SHA-256":
        return hashlib.sha256(texto.encode()).hexdigest()
    elif algoritmo == "SHA-3":
        return hashlib.sha3_256(texto.encode()).hexdigest()
    return None

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

# Transferencia ritualizada
transferencia = {
    "direccion_guarecoin": direccion_guarecoin,
    "guarecoins_transferidos": total_guarecoins
}

print("🔐 Dirección GUARECOIN™:", direccion_guarecoin)
print(f"✅ {total_guarecoins} GUARECOINS™ transferidos a tu billetera multimoneda")

with open("transferencia_soberana.json", "w") as f:
    json.dump(transferencia, f, indent=2)