N = int(input())

def nome_dificil(nome):
    vogais = ['a','e','i','o','u']
    count = 0
    for car in nome.lower():
        if count == 3:
            return True
        if car not in vogais:
            count += 1
        else:
            count = 0
    if count == 3:
        return True
    else:
        return False


while N > 0:
    sobrenome = input().title()
    if nome_dificil(sobrenome):
        print(f'{sobrenome} nao eh facil')
    else:
        print(f'{sobrenome} eh facil')
    N -= 1
