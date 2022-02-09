D, S = [int(x) for x in input().split()]

dias = D
menor_saldo = S
saldo_total = S

while True:
    valor_dia = int(input())
    saldo_total += valor_dia
    if saldo_total < menor_saldo:
        menor_saldo = saldo_total
        dias -= 1
    else:
        dias -= 1
    if dias == 0:
        print(menor_saldo)
        break
