def calcula_quadrados(quadrados_lado):
    quadrados_totais = 0
    for x in range(quadrados_lado+1):
        quadrados_totais += x**2
    return quadrados_totais


while True:
    N = int(input())
    if N == 0:
        break
    else:
        print(calcula_quadrados(N))
