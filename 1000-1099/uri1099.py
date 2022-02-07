N = int(input())

while N != 0:
    X, Y = [int(x) for x in input().split()]
    soma_impares = 0
    if X > Y:
        for num in range(Y+1, X):
            if num % 2 != 0:
                soma_impares += num
    else:
        for num in range(X+1, Y):
            if num % 2 != 0:
                soma_impares += num
    print(soma_impares)
    N -= 1
