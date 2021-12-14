x1, y1 = [float(v) for v in input().split()]
x2, y2 = [float(v) for v in input().split()]

D = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f'{D:.4f}')
