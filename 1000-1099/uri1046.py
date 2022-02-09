I, F = (int(x) for x in input().split())

if F > I:
    duracao = (F - I)
elif F < I:
    duracao = (F - I) + 24
else:
    duracao = 24

print(f'O JOGO DUROU {duracao} HORA(S)')
