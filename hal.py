import random

def temperatura():
    return random.uniform(-15, 49.9)

def aquecedor(estado: str):
    if estado == 'ligado':
        print('AQUECEDOR LIGADO!')
    else:
        print('AQUECEDOR DESLIGADO!')

def rele(estado: str):
    if estado == 'ligado':
        print('RELÉ LIGADO!')
    else:
        print('RELÉ DESLIGADO!')
    aquecedor(estado)
    print('========================================')