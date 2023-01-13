Teste = 1

while True:
    N = int(input())
    pedacos = (1+ 2**N)**2
    if 0 <= N <= 15:
        print('Teste {}\n'
              '{}\n'
              ''.format(Teste, pedacos))
        Teste += 1
    elif N == -1:
        break
