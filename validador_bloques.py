import json
import hashlib

# Cargar bloque minado
with open("MINERIA_SOBERANA/bloque_demo.json", "r") as archivo:
    bloque = json.load(archivo)

# Validación de hash
def validar_hash(bloque):
    datos = f"GUARECOIN_MINING_{bloque['usuario']}_{bloque['timestamp']}"
    nonce = bloque["nonce"]
    sha256 = hashlib.sha256((datos + str(nonce)).encode()).hexdigest()
    sha3 = hashlib.sha3_256(sha256.encode()).hexdigest()
    return sha3 == bloque["hash"]

# Validación de estructura
def validar_estructura(bloque):
    claves_requeridas = [
        "usuario", "hash", "nonce", "timestamp",
        "moneda_generada", "algoritmo", "transparencia", "auditable"
    ]
    return all(clave in bloque for clave in claves_requeridas)

# Validación completa
valido_hash = validar_hash(bloque)
valido_estructura = validar_estructura(bloque)

if valido_hash and valido_estructura:
    print("✅ Bloque GUARECOIN™ validado y sincronizado correctamente.")
else:
    print("❌ Bloque inválido. Rechazado por el sistema soberano.")