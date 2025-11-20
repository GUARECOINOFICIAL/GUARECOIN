import json
from datetime import datetime

# Parámetros inmutables de GUARECOIN™
guarecoin = {
    "nombre": "GUARECOIN",
    "valor_minimo_usdt": 0.98,
    "valor_maximo_usdt": None,
    "valor_dinamico": "Sí, puede crecer sin límite",
    "total_minable": 49_000_000,
    "recompensas_iniciales": 1_000_000,
    "anio_final_minado": 2075,
    "algoritmo_mineria": ["SHA-256", "SHA3-256"],
    "origen": "Soberano, no humano",
    "fecha_creacion": datetime.utcnow().isoformat()
}

# Parámetros de la moneda secundaria KRILLIN
krillin = {
    "nombre": "KRILLIN",
    "equivalencia_guarecoin": "1 GUARECOIN = 10,000 KRILLIN",
    "valor_individual_usdt": round(0.98 / 10000, 8),  # 0.00009800
    "uso": "Microtransacciones, recompensas, expansión creativa",
    "origen": "Derivada de GUARECOIN™, con identidad propia",
    "fecha_creacion": datetime.utcnow().isoformat()
}

# Registro histórico de eventos clave
historial_eventos = [
    {"fecha": "2025-11-18", "evento": "Génesis de GUARECOIN™ y KRILLIN"},
    {"fecha": "2026-01-01", "evento": "Inicio de minería pública"},
    {"fecha": "2075-12-31", "evento": "Fin del período de minería GUARECOIN™"}
]

# Auditoría soberana
auditoria = {
    "creado_por": "Código soberano, no humano",
    "verificado_por": "Diseñador de la moneda Krillin",
    "transparencia": True,
    "modificable": False,
    "licencia": "Uso perpetuo dentro del ECOSISTEMA GUARECOIN™"
}

# Estructura completa con transparencia
estructura_monetaria = {
    "GUARECOIN": guarecoin,
    "KRILLIN": krillin,
    "HISTORIAL_EVENTOS": historial_eventos,
    "AUDITORIA": auditoria
}

# Guardar archivo JSON
with open("GENESIS_MONEDA/estructura_monetaria.json", "w") as archivo:
    json.dump(estructura_monetaria, archivo, indent=4)

print("Moneda GUARECOIN™ y KRILLIN definidas y registradas correctamente.")