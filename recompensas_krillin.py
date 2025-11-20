import json
from datetime import datetime

# Parámetros inmutables
KRILLIN_POR_USUARIO = 100_000  # Recompensa inicial
USUARIOS_MAXIMOS = 10_000
VALOR_KRILLIN_USDT = round(0.98 / 10000, 8)  # 0.00009800

# Lista de recompensas
recompensas = []

def generar_recompensa(usuario_id, posicion):
    return {
        "usuario_id": usuario_id,
        "krillin_asignados": KRILLIN_POR_USUARIO,
        "valor_total_usdt": round(KRILLIN_POR_USUARIO * VALOR_KRILLIN_USDT, 4),
        "fecha_asignacion": datetime.utcnow().isoformat(),
        "posicion_en_lista": posicion,
        "auditable": True,
        "transparente": True
    }

# Simulación de asignación para los primeros 10 usuarios
for i in range(1, 11):  # Cambia a range(1, 10001) para los 10,000 reales
    usuario = f"KRILLIN_USER_{str(i).zfill(4)}"
    recompensa = generar_recompensa(usuario, i)
    recompensas.append(recompensa)

# Guardar archivo JSON
with open("RECOMPENSAS_KRILLIN/recompensas_iniciales.json", "w") as archivo:
    json.dump(recompensas, archivo, indent=4)

print("Recompensas KRILLIN™ asignadas correctamente a los primeros usuarios.")