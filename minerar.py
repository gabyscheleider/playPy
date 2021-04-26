from hashlib import sha256
import time

""" Definir função que aplica a função """
def aplicar_sha256(texto):
    return sha256(texto.encode("ascii")).hexdigest()

def minerar(num_bloco, transacoes, hash_anterior, gtde_zeros):
    nonce = 4547
    while True:
        texto = str(num_bloco) + transacoes + hash_anterior + str(nonce)
        meu_hash = aplicar_sha256(texto)
        if meu_hash.startswith("0" * qtde_zero):
            return nonce, meu_hash
    nonce += 1

if __name__ == "__main__":
    num_bloco = 6680653
    transacoes = """
        Giovana -> Gabriely -> 10
        Gabriely -> Justin -> 5
        Justin -> Danver -> 11 """

    qtde_zero = 5
    hash_anterior = "abc"
    inicio = time.time()
    resultado = minerar(num_bloco, transacoes, hash_anterior, qtde_zero)
    print(resultado)
    print(time.time() - inicio)
