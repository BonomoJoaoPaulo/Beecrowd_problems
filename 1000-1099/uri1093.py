from math import ceil


def calcula_chance(a, b, c, d):
    lados = 6
    a, b = ceil(a/d), ceil(b/d)
    if c == 3:
        result = a/(a+b)
    else:
        dado = 1 - (lados - c)/lados
        dado = (1 - dado)/dado
        result = (1 - pow(dado, a))/(1 - pow(dado, a + b))

    return result * 100


while True:
    EV1, EV2, AT, D = [int(x) for x in input().split()]
    if not (EV1 or EV2 or AT or D):
        break
    else:
        print(f'{calcula_chance(EV1, EV2, AT, D):.1f}')
