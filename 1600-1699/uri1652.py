while True:
    L, N = [int(x) for x in input().split()]
    if ((0 <= L <= 20) and (1 <= N <= 100)):
        break
    else:
        L, N = [int(x) for x in input().split()]


count_L = L
count_N = N
plural_irregular = {}
lista_pal = []

while count_L != 0:
    irregular = [str(z) for z in input().split()]
    plural_irregular[irregular[0]] = irregular[1]
    count_L -= 1

while count_N != 0:
    singular = str(input())
    lista_pal.append(singular)
    count_N -= 1


def teste_irregular(palavra):
    global plural_irregular
    global irregularidade
    global plural
    if palavra in plural_irregular.keys():
        irregularidade = True
    plural = plural_irregular.get(palavra)

saida = []
irregularidade = False
vogal = ['a','e','i','o','u']

for n in range(len(lista_pal)):
    irregularidade = False
    teste = teste_irregular(lista_pal[n])
    if irregularidade:
        saida.append(plural)
    elif not irregularidade:
        if ((lista_pal[n])[-1] == 'y' and ((lista_pal[n])[-2] not in vogal)):
            plural = (lista_pal[n])[:-1] + 'ies'
            saida.append(plural)
        elif (((lista_pal[n])[-1] == 'o') or ((lista_pal[n])[-1] == 's') or ((lista_pal[n])[-1] == 'x')):
            plural = (lista_pal[n]) + 'es'
            saida.append(plural)
        elif (((lista_pal[n])[-1] == 'h') and (((lista_pal[n])[-2] == 's') or ((lista_pal[n])[-2] == 'c'))):
            plural = (lista_pal[n]) + 'es'
            saida.append(plural)
        else:
            plural = (lista_pal[n]) + 's'
            saida.append(plural)


for y in range(len(saida)):
    print(saida[y])
