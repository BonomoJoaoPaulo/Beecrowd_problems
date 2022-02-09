rodada = 1
while True:
    R = int(input())
    soma_A = 0
    soma_B = 0
    rapelou = ''
    if R == 0:
        break
    for i in range(R):
        A, B = input().split()
        A = int(A)
        B = int(B)
        soma_A += A
        soma_B += B
    if soma_A > soma_B:
        rapelou = 'Aldo'
    elif soma_A < soma_B:
        rapelou = 'Beto'

    print('Teste {}\n'
          '{}\n'
          ''.format(rodada, rapelou))
    rodada += 1
