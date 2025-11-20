from web3 import Web3

# Conexión a red pública (ej. Polygon)
w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/polygon"))

# Hash de la transacción donde se selló el manifiesto
tx_hash = "0xTU_HASH_DE_TRANSACCION"  # ← reemplaza con el hash real

# Obtener y decodificar la transacción
tx = w3.eth.get_transaction(tx_hash)
data_hex = tx.input
manifiesto = bytes.fromhex(data_hex[2:]).decode('utf-8')

# Mostrar el manifiesto sellado
print("📜 MANIFIESTO SELLADO EN LA BLOCKCHAIN:")
print("-" * 60)
print(manifiesto)
print("-" * 60)
print(f"🔗 Verificado en: https://polygonscan.com/tx/{tx_hash}")