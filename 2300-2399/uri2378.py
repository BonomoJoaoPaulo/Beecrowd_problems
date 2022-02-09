while True:
    N, C = input().split()
    N = int(N)
    C = int(C)
    if (1 <= N <= 1000) and (1 <= C <= 1000):
        break

ultrapassou = 'N'
def viagens(passageiros,capacidade):
    if passageiros > capacidade:
        global ultrapassou
        ultrapassou = 'S'

total = 0
for x in range(N):
    S,E = input().split()
    S = int(S)
    E = int(E)
    total = total - S
    total = total + E
    viagens(total, C)

print(ultrapassou)
