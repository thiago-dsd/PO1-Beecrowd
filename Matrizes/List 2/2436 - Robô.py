L, C = input().split()
L = int(L)
C = int(C)

a, b = input().split()
a = int(a) - 1
b = int(b) - 1

mat = [None] * L
for i in range (0, L):
    mat[i] = input().split()

while True:
    #marcando a casa da qual veio com 2
    mat[a][b] = '2'
    #next A próxima linha que será alcançada
    nextA = -1
    nextB = -1
    
    #vizinho de cima
    #posição do vizinho
    vizinhoI = a - 1
    vizinhoJ = b
    if vizinhoI >= 0 and mat[vizinhoI][vizinhoJ] == '1':
        nextA = vizinhoI
        nextB = vizinhoJ
    
    #vizinho de baixo
    vizinhoI = a + 1
    vizinhoJ = b
    if vizinhoI < L and mat[vizinhoI][vizinhoJ] == '1':
        nextA = vizinhoI
        nextB = vizinhoJ
        
    #vizinho da direita
    vizinhoI = a
    vizinhoJ = b + 1
    if vizinhoJ < C and mat[vizinhoI][vizinhoJ] == '1':
        nextA = vizinhoI
        nextB = vizinhoJ
        
    #vizinho da esquerda
    vizinhoI = a
    vizinhoJ = b - 1
    if vizinhoJ >= 0 and mat[vizinhoI][vizinhoJ] == '1':
        nextA = vizinhoI
        nextB = vizinhoJ
    
    if nextA == -1:
        print('{} {}'.format(a+1, b+1))
        break
    a = nextA
    b = nextB
