n = int(input())
#posição do primeiro jogador, sabemos que ele levantou a bandeira
ip, jp = input().split()
ip = int(ip) - 1
jp = int(jp) - 1
#criando uma matriz para armazenar valores dados
mat = [None] * n
for i in range (n):
    mat[i] = input().split()
#criando uma matriz para armazenar bandeiras
band = [None] * n
for i in range (n):
    band[i] = [None] * n
#percorrendo matrizes e alterando valores
for i in range (n):
    for j in range (n):
        #a matriz das camisas fica com números inteiros
        mat[i][j] = int(mat[i][j])
        #a matriz das bandeiras fica com false, até agora ninguém levantou a bandeira
        band[i][j] = False
        
#mas que o primeiro jogador levantou a bandeira
band[ip][jp] = True
#o primeiro aluno já está com a bandeira levantada
bandeirasLevantadas = 1
#agora criamos a lista para colocar os pratos
pratos = []
#adicionamos o primeiro jogador na lista dos pratos
pratos.append((ip, jp))
#enquanto a pilha de pratos não estiver vazia ela será percorrida
while pratos != []:
    #tiramos o prato de baixo
    (i, j) = pratos.pop(0)
    #analizando o vizinho de cima
    vizinhoI = i - 1
    vizinhoJ = j
    if vizinhoI >= 0 and mat[vizinhoI][vizinhoJ] >= mat[i][j] and band[vizinhoI][vizinhoJ] == False:
        pratos.append((vizinhoI,vizinhoJ))
        bandeirasLevantadas += 1
        band[vizinhoI][vizinhoJ] = True
        
    #analizando o vizinho de baixo
    vizinhoI = i + 1
    vizinhoJ = j
    if vizinhoI < n and mat[vizinhoI][vizinhoJ] >= mat[i][j] and band[vizinhoI][vizinhoJ] == False:
        pratos.append((vizinhoI,vizinhoJ))
        bandeirasLevantadas += 1
        band[vizinhoI][vizinhoJ] = True
        
    #analizando o vizinho da esquerda
    vizinhoI = i
    vizinhoJ = j - 1
    if vizinhoJ >= 0 and mat[vizinhoI][vizinhoJ] >= mat[i][j] and band[vizinhoI][vizinhoJ] == False:
        pratos.append((vizinhoI,vizinhoJ))
        bandeirasLevantadas += 1
        band[vizinhoI][vizinhoJ] = True
        
        
    #analizando o vizinho da direita
    vizinhoI = i 
    vizinhoJ = j + 1 
    if vizinhoJ < n and mat[vizinhoI][vizinhoJ] >= mat[i][j] and band[vizinhoI][vizinhoJ] == False:
        pratos.append((vizinhoI,vizinhoJ))
        bandeirasLevantadas += 1
        band[vizinhoI][vizinhoJ] = True
print(bandeirasLevantadas)
        

