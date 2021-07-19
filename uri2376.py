# Copa do Mundo - 2376

#oitavas
A, B = input().split()
A = int(A)
B = int(B)
C, D = input().split()
C = int(C)
D = int(D)
E, F = input().split()
E = int(E)
F = int(F)
G, H = input().split()
G = int(G)
H = int(H)
I, J = input().split()
I = int(I)
J = int(J)
K, L = input().split()
K = int(K)
L = int(L)
M, N = input().split()
M = int(M)
N = int(N)
O, P = input().split()
O = int(O)
P = int(P)

#quartas
Q, R = input().split() # (A ou B) vs (C ou D)
Q = int(Q) # A ou B
R = int(R) # C ou D
S, T = input().split() # (E ou F) vs (G ou H)
S = int(S) # E ou F
T = int(T) # G ou H
U, V = input().split() # (I ou J) vs (K ou L)
U = int(U) # I ou J
V = int(V) # K ou L
W, X = input().split() # (M ou N) vs (O ou P)
W = int(W) # M ou N
X = int(X) # O ou P

#semis
Y, Z = input().split() # (A ou B ou C ou D) vs (E ou F ou G ou H)
Y = int(Y) # A ou B ou C ou D
Z = int(Z) # E ou F ou G ou H
a, b = input().split() # (I ou J ou K ou L) vs (M ou N ou O ou P)
a = int(a) # I ou J ou K ou L
b = int(b) # M ou N ou O ou P

#final
c, d = input().split() # (A ou B ou C ou D ou E ou F ou G ou H) vs (I ou J ou K ou L ou M ou N ou O ou P)
c = int(c) # A ou B ou C ou D ou E ou F ou G ou H
d = int(d) # I ou J ou K ou L ou M ou N ou O ou P

if (A>B) and (Q>R) and (Y>Z) and (c>d):
    print('A')
if (A<B) and (Q>R) and (Y>Z) and (c>d):
    print('B')
if (C>D) and (Q<R) and (Y>Z) and (c>d):
    print('C')
if (C<D) and (Q<R) and (Y>Z) and (c>d):
    print('D')
if (E>F) and (S>T) and (Y<Z) and (c>d):
    print('E')
if (E<F) and (S>T) and (Y<Z) and (c>d):
    print('F')
if (G>H) and (S<T) and (Y<Z) and (c>d):
    print('G')
if (G<H) and (S<T) and (Y<Z) and (c>d):
    print('H')
if (I>J) and (U>V) and (a>b) and (c<d):
    print('I')
if (I<J) and (U>V) and (a>b) and (c<d):
    print('J')
if (K>L) and (U<V) and (a>b) and (c<d):
    print('K')
if (K<L) and (U<V) and (a>b) and (c<d):
    print('L')
if (M>N) and (W>X) and (a<b) and (c<d):
    print('M')
if (M<N) and (W>X) and (a<b) and (c<d):
    print('N')
if (O>P) and (W<X) and (a<b) and (c<d):
    print('O')
if (O<P) and (W<X) and (a<b) and (c<d):
    print('P')

# Os 15 inputs, em ordem, sao as linha:
# 5, 8, 11, 14, 17, 20, 23, 26, 31, 34, 37, 40, 45, 48, 53
