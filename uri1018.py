while True:
    N = int(input())
    if 0 < N < 1000000:
        break

print(N)

n100 = N / 100
print(f'{int(n100)} nota(s) de R$ 100,00')
N_restante = N % 100

n50 = N_restante / 50
print(f'{int(n50)} nota(s) de R$ 50,00')
N_restante = N_restante % 50

n20 = N_restante / 20
print(f'{int(n20)} nota(s) de R$ 20,00')
N_restante = N_restante % 20

n10 = N_restante / 10
print(f'{int(n10)} nota(s) de R$ 10,00')
N_restante = N_restante % 10

n5 = N_restante / 5
print(f'{int(n5)} nota(s) de R$ 5,00')
N_restante = N_restante % 5

n2 = N_restante / 2
print(f'{int(n2)} nota(s) de R$ 2,00')
N_restante = N_restante % 2

n1 = N_restante / 1
print(f'{int(n1)} nota(s) de R$ 1,00')
