# Wrong Answer 5%

N = int(input())
nome_ling = ""
lista_palavras = []
while N != 0:
    M = input()
    palavra = ''
    count = 0
    try:
        count = int(M)
    except ValueError:
        pass
    while count != 0:
        livro = input()
        palavra += livro[0].lower()
        if str(count) == M:
            nome_ling += livro[0].upper()
        count -= 1
    lista_palavras.append(palavra)
    N -= 1


lista_vogais = ['a', 'e', 'i', 'o', 'u']
vogais = 0
consoantes = 0
string_final = ''
contados = []

for word in lista_palavras:
    string_final += word

for car in string_final:
    if car in lista_vogais and car not in contados:
        vogais += 1
        contados.append(car)     
    elif car not in lista_vogais and car not in contados:
        consoantes += 1
        contados.append(car)

tempo = (vogais * 2 + consoantes)/consoantes


print(f'Nome da Linguagem: {nome_ling}\n'
    'Lista de Palavras:')

for word in lista_palavras:
    print(word)

print(f'Numero de Vogais: {vogais}\n'
    f'Numero de Consoantes: {consoantes}\n'
    f'Numero Total de Letras: {vogais + consoantes}')

if consoantes != 0:
    print(f'Tempo para aprender: {tempo:.1f} horas')
else:
    print('Linguagem Ruim')
