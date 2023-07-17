N = int(input()) #diametro
ALP = input()
A, L, P = ALP.split()
A = int(A)
L = int(L)
P = int(P)
if A < N or L < N or P < N:
    print('N')
else:
    print('S')

