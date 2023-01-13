A,G,Ra,Rg = input().split()
A = float(A)
G = float(G)
Ra = float(Ra)
Rg = float(Rg)


if (Rg/G) >= (Ra/A):
    print('G')

else:
    print('A')
