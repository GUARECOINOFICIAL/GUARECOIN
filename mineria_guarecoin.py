import hashlib
import time
import json
from datetime import datetime

# 🧱 Parámetros inmutables de GUARECOIN™
VALOR_MONEDA = 0.98  # USDT
TOTAL_MINABLE = 49_000_000
RECOMPENSAS_INICIALES = 1_000_000
AÑO_FINAL_MINADO = 2075
ALGORITMO = "SHA-256 + SHA3-256"

# 🔄 Estado inicial del sistema
bloques = []
monedas_minadas = 0

# 🔐 Función para generar hash dual
def generar_hash_bloque(datos, nonce):
    sha256 = hashlib.sha256((datos + str(nonce)).encode()).hexdigest()
    sha3 = hashlib.sha3_256(sha256.encode()).hexdigest()
    return sha3

# ⚙️ Función de minería soberana
def minar_bloque(usuario_id):
    global monedas_minadas
    if monedas_minadas >= TOTAL_MINABLE:
        print("Límite de monedas minadas alcanzado.")
        return None

    datos = f"GUARECOIN_MINING_{usuario_id}_{time.time()}"
    nonce = 0
    hash_valido = ""

    # 🔁 Bucle de prueba de trabajo
    while not hash_valido.startswith("0000"):  # Dificultad ajustable
        hash_valido = generar_hash_bloque(datos, nonce)
        nonce += 1

    monedas_minadas += 1
    bloque = {
        "usuario": usuario_id,
        "hash": hash_valido,
        "nonce": nonce,
        "timestamp": datetime.utcnow().isoformat(),
        "moneda_generada": VALOR_MONEDA,
        "algoritmo": ALGORITMO,
        "transparencia": True,
        "auditable": True
    }
    bloques.append(bloque)
    return bloque

# 🧪 Simulación de minería
usuario_demo = "KRILLIN_USER_001"
bloque_generado = minar_bloque(usuario_demo)

# 💾 Guardar bloque en archivo JSON
if bloque_generado:
    with open("MINERIA_SOBERANA/bloque_demo.json", "w") as archivo:
        json.dump(bloque_generado, archivo, indent=4)
    print("✅ Bloque GUARECOIN™ minado y registrado correctamente.")