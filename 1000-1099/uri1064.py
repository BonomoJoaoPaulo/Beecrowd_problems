count = 0
lista_valores = []

while count != 6:
    valor = float(input())
    lista_valores.append(valor)
    count += 1

positivos = 0
lista_positivos = []

for num in lista_valores:
    if num > 0:
        lista_positivos.append(num)
        positivos += 1

print(f'{positivos} valores positivos\n'
    f'{sum(lista_positivos)/len(lista_positivos):.1f}')
