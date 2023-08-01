# mult matriz: Cij = sum(Ai * Bj)
# forma mais rapida: calcular apenas o valor para a posicao pedida
# Para o A: calcular apenas a linha Ac_i
# Para o B: calcular apenas a coluna Bc_j


n = int(input())
P, Q, R, S, X, Y = [int(x) for x in input().split()]
c_i, c_j = [int(x) for x in input().split()]

A = []
B = []
for i in range(1, n+1):
    Aij = (P*c_i + Q*i) % X
    Bij = (R*i + S*c_j) % Y
    
    A.append(Aij)
    B.append(Bij)

c_ij = 0
for i in range(n):
    c_ij += A[i] * B[i]

print(c_ij)
