A, B, C = [float(x) for x in input().split()]

delta = B**2 - 4*A*C

if delta < 0 or A == 0:
    print('Impossivel calcular')
else:
    raiz1 = (-B + delta**0.5)/(2*A)
    raiz2 = (-B - delta**0.5)/(2*A)
    print(f'R1 = {raiz1:.5f}\n'
    f'R2 = {raiz2:.5f}')
