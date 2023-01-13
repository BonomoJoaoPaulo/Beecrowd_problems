
while True:
    M, N = input().split()
    if M and N == "0":
        break
    else:
        M = M.replace('0', "")
        N = N.replace('0', "")
        soma = int(M) + int(N)
        soma = str(soma)
        soma = soma.replace('0', "")
        soma = int(soma)
    print(soma)
