p1c, p1p, p1v = (float(x) for x in input().split())
p1c = int(p1c)
p1p = int(p1p)
p2c, p2p, p2v = (float(x) for x in input().split())
p2c = int(p2c)
p2p = int(p2p)
p1 = p1p*p1v
p2 = p2p*p2v
print(f'VALOR A PAGAR: R$ {(p1+p2):.2f}')
