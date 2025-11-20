import json
import uuid
from datetime import datetime
import random

# Simulación de billeteras anónimas
billeteras = [f"0xBILLETERA_{str(i).zfill(4)}" for i in range(1000)]

# Función para generar transacción pública
def generar_transaccion(origen, destino, cantidad):
    return {
        "tx_id": str(uuid.uuid4()),
        "origen": origen,
        "destino": destino,
        "cantidad_guarecoin": cantidad,
        "valor_usdt": round(cantidad * 0.98, 2),
        "fecha": datetime.utcnow().isoformat(),
        "visible": True,
        "anonimo": True,
        "verificado_por": "IA soberana GUARECOIN™"
    }

# Simulación de 10 transacciones entre billeteras anónimas
transacciones = []
for _ in range(10):
    origen, destino = random.sample(billeteras, 2)
    cantidad = random.randint(100, 10000)
    transacciones.append(generar_transaccion(origen, destino, cantidad))

# Guardar archivo JSON
with open("TRANSACCIONES_PUBLICAS/transacciones_demo.json", "w") as archivo:
    json.dump(transacciones, archivo, indent=4)

print("✅ Transacciones públicas registradas correctamente entre billeteras anónimas.")