N = int(input())
lista_entradas = []

while N > 0:
    entrada = [x for x in input().split()]
    lista_entradas.append(entrada)
    N -= 1


def MDC(x, y):
    div_x = []
    mdc = 1
    if x < 0:
        x = -x

    for n in range(1, x+1):
        if x % n == 0:
            div_x.append(n)
    for n in div_x:
        if y % n == 0:
            mdc = n
    return mdc


def soma(lista_e):
    n_result = (int(lista_e[0]) * int(lista_e[6]) + int(lista_e[4]) * int(lista_e[2]))
    d_result = (int(lista_e[2]) * int(lista_e[6]))

    return f'{n_result}/{d_result} = {int(n_result / MDC(n_result, d_result))}/{int(d_result / MDC(n_result, d_result))}'


def subtrai(lista_e):
    n_result = (int(lista_e[0]) * int(lista_e[6]) - int(lista_e[4]) * int(lista_e[2]))
    d_result = (int(lista_e[2]) * int(lista_e[6]))

    return f'{n_result}/{d_result} = {int(n_result / MDC(n_result, d_result))}/{int(d_result / MDC(n_result, d_result))}'


def multiplica(lista_e):
    n_result = (int(lista_e[0]) * int(lista_e[4]))
    d_result = (int(lista_e[2]) * int(lista_e[6]))

    return f'{n_result}/{d_result} = {int(n_result / MDC(n_result, d_result))}/{int(d_result / MDC(n_result, d_result))}'


def divide(lista_e):
    n_result = (int(lista_e[0]) * int(lista_e[6]))
    d_result = (int(lista_e[4]) * int(lista_e[2]))

    return f'{n_result}/{d_result} = {int(n_result / MDC(n_result, d_result))}/{int(d_result / MDC(n_result, d_result))}'


for e in lista_entradas:
    if e[3] == '+':
        print(soma(e))
    elif e[3] == '-':
        print(subtrai(e))
    if e[3] == '*':
        print(multiplica(e))
    if e[3] == '/':
        print(divide(e))
