count = 0
lista_valores = []

while count != 5:
    valor = int(input())
    lista_valores.append(valor)
    count += 1

positivos = 0
negativos = 0
pares = 0
impares = 0

for num in lista_valores:
    if num > 0:
        positivos += 1
    if num < 0:
        negativos += 1
    if num % 2 == 0:
        pares += 1
    if num % 2 != 0:
        impares += 1    

print(f'{pares} valor(es) par(es)\n'
    f'{impares} valor(es) impar(es)\n'
    f'{positivos} valor(es) positivo(s)\n'
    f'{negativos} valor(es) negativo(s)')
