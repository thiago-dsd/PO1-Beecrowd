opr = input ()

#criando uma matriz 12x12
mat = [None] * 12 
for i in range (0 , 12):
    mat [i] = [None] * 12
#lendo os elementos e colocando na matriz
for i in range (0,12): 
    for j in range (0,12):
        mat [i][j] = float(input())
numDeQuadrados = 30 
soma = 0
#crio variáveis que mudam conforme a linha
esquerd = 5
dirt = 7

# Soma no triângulo esquerdo que está em cima
for i in range (7,12): 
    for j in range (esquerd, dirt): 
        soma += mat[i][j]
    esquerd -= 1
    dirt += 1
    
#para cada leitura eu adiciono 1 para o quadrado da direita e substraio 1 do quadrado da esquerda

if opr == 'S':
    print("%.1f" % soma)
else :
    print("%.1f" % (soma / numDeQuadrados))

