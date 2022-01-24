# Time limited exceeded

def ordena_listas(lista1, lista2):
    string_final = ""
    while len(lista2) != 0:
        menor = min(lista2)
        indice_min = lista2.index(menor)
        pessoas = lista1[indice_min]
        string_formada = f'{pessoas}-{menor} '
        string_final += string_formada
        del(lista1[indice_min])
        del(lista2[indice_min])

    return string_final


contador_cidades = 0
N = 1

while N != 0:

    N = int(input())
    if N == 0:
        break
    else:
        contador_cidades += 1
        count = N
        lista_pessoas = []
        lista_consumo = []
        consumo_total = 0

        while count != 0:
            X, Y = [int(x) for x in input().split()]
            lista_pessoas.append(X)
            lista_consumo.append(int(Y/X))
            consumo_total += Y
            count -= 1

        consumo_medio = (consumo_total/sum(lista_pessoas))
        print(f'Cidade# {contador_cidades}:\n'
        f'{ordena_listas(lista_pessoas, lista_consumo)[:-1]}\n'
        f'Consumo medio: {consumo_medio:.2f} m3.')
