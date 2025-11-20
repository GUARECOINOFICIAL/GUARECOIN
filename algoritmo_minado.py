import hashlib

def doble_hash_soberano(data):
    sha256 = hashlib.sha256(data.encode()).hexdigest()
    sha3_256 = hashlib.sha3_256(sha256.encode()).hexdigest()
    return sha3_256

def minar_bloque(data, dificultad):
    nonce = 0
    while True:
        bloque = f"{data}{nonce}"
        hash_resultado = doble_hash_soberano(bloque)
        if hash_resultado.startswith("0" * dificultad):
            return {
                "bloque": bloque,
                "hash": hash_resultado,
                "nonce": nonce
            }
        nonce += 1