N, M = [int(x) for x in input().split()]

def teste_primo(x):
    divisores = 0
    for num in range(1, x+1):
        if x % num == 0:
            divisores += 1
    return divisores == 2
        

def encontra_primo(x):
    for num in range(x, 0, -1):
        if teste_primo(num):
            primo = num
            break
    return primo


print(encontra_primo(N) * encontra_primo(M))
