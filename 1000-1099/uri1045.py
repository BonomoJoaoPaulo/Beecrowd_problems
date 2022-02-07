A, B, C = [float(x) for x in input().split()]

while A != max(A, B, C):
    if B > A:
        intermedio = A
        A = B
        B = intermedio
    if C > A:
        intermedio = A
        A = C
        C = intermedio

if A >= B + C:
    print('NAO FORMA TRIANGULO')
elif A**2 == B**2 + C**2:
    print('TRIANGULO RETANGULO')
elif A**2 > B**2 + C**2:
    print('TRIANGULO OBTUSANGULO')
elif A**2 < B**2 + C**2:
    print('TRIANGULO ACUTANGULO')

if A == B == C:
    print('TRIANGULO EQUILATERO')
elif (A == B and A != C) or (A == C and A != B) or (B == C and B != A):
    print('TRIANGULO ISOSCELES')
