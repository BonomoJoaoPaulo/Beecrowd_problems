X = int(input())

while True:
    Z = int(input())
    if Z > X:
        break

def ultrapassa_Z(x, z):
    count = 1
    soma = x
    while soma <= z:
        x += 1
        soma += x
        count += 1
    return count

print(ultrapassa_Z(X, Z))
