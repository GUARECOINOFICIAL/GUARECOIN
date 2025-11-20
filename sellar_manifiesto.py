from web3 import Web3
import json

# Conexión a red pública (ej. Polygon, Arbitrum, Ethereum)
w3 = Web3(Web3.HTTPProvider("https://rpc.ankr.com/polygon"))  # Puedes cambiar la red

# Dirección soberana del fundador (reemplaza con tu wallet)
direccion_fundador = "0xTU_DIRECCION_PUBLICA"

# Clave privada para firmar (solo en máquina local, nunca compartas)
clave_privada = "TU_CLAVE_PRIVADA"

# Manifiesto soberano
with open("manifiesto_soberano.txt", "r", encoding="utf-8") as f:
    manifiesto = f.read()

# Preparar transacción
tx = {
    'nonce': w3.eth.get_transaction_count(direccion_fundador),
    'to': direccion_fundador,  # Transacción sin valor, solo para inscribir
    'value': 0,
    'gas': 200000,
    'gasPrice': w3.to_wei('30', 'gwei'),
    'data': manifiesto.encode('utf-8')
}

# Firmar y enviar
signed_tx = w3.eth.account.sign_transaction(tx, clave_privada)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

# Confirmación ritual
print(f"🔥 Manifiesto sellado en la blockchain. TX Hash: {w3.to_hex(tx_hash)}")