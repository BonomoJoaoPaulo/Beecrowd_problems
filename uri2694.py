
N = int(input())

while N > 0:
    entrada = input()
    valor1 = int(entrada[2:4])
    valor2 = int(entrada[5:8])
    valor3 = int(entrada[11:13])
    soma = valor1 + valor2 + valor3
    print(soma)
    N -= 1
