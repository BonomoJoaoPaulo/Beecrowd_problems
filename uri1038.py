
dicionario_precos = {1: 4, 2: 4.5, 3: 5, 4: 2, 5: 1.5}

C, Q = [int(x) for x in input().split()]

print(f'Total: R$ {(dicionario_precos[C] * Q):.2f}')
