N = int(input())


# Euclidean Algorithm
def calcula_mdc(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


count = 0
while count != N:
    F1, F2 = [int(x) for x in input().split()]
    print(calcula_mdc(F1, F2))
    count += 1
