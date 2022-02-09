N = int(input())
contagem = 0
total = 0

def funcao(acionamento):
    global fim
    global total
    if acionamento < fim:
        total += (acionamento + 10 - fim)
    else:
        total += 10
    return(total)


while True:
    for x in range(N):
        acionamento = int(input())
        if x == 0:
            fim = (acionamento+10)
            total += 10
        funcao(acionamento)
        fim = (acionamento + 10)
        contagem += 1
    if contagem == N:
        break

print(total)
