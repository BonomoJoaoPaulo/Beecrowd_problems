N = int(input())
C = 0
E = 0
casa = 0
escrit = 0
if 1 <= N <= 1000:
    for i in range(N):
        ida, volta = input().split()
        if ida == 'chuva':
            if casa >= 1:
                escrit += 1
                casa -= 1
            else:
                escrit += 1
                C += 1
        if volta == 'chuva':
            if escrit >= 1:
                casa += 1
                escrit -= 1
            else:
                casa += 1
                E += 1

    print(f'{C} {E}')
