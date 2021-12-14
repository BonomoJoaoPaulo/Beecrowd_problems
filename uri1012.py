A, B, C = [float(x) for x in input().split()]

a_ = A*C/2

b_ = C**2*3.14159

if A > B:
    c_ = (B*C) + ((A-B)/2*C)

else:
    c_ = (A*C) + ((B-A)/2*C)

d_ = B**2

e_ = A*B

print(f'TRIANGULO: {a_:.3f}\n'
    f'CIRCULO: {b_:.3f}\n'
    f'TRAPEZIO: {c_:.3f}\n'
    f'QUADRADO: {d_:.3f}\n'
    f'RETANGULO: {e_:.3f}')
