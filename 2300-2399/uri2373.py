N = int(input())

quebrados = 0

while N > 0:
    L, C = [int(x) for x in input().split()]
    if L > C:
        quebrados += C
    N -= 1

print(quebrados)
