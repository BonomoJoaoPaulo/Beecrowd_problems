count = 0
lista_valores = []

while count != 100:
    valor = int(input())
    lista_valores.append(valor)
    count += 1

for x in lista_valores:
    if x == max(lista_valores):
        print(f'{x}\n'
        f'{lista_valores.index(x) + 1}')
