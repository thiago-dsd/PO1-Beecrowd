o = input()

#criando uma matriz
mat = [None] * 12
for i in range (0, 12):
    mat[i] = [None] * 12

#percorrendo os valores
for i in range (0, 12):
    for j in range (0, 12):
        mat [i][j] = float(input())

soma = 0
#somando os valores do intervalo desejado
#triângulo superior
for i in range (5, 0, -1):
    for j in range (12-i, 12):
        soma += mat[i][j]
for i in range (6, 11):
    for j in range (i+1, 12):
        soma += mat[i][j]
#operações aritméticas
nCasas = ((12*12 - 24)/4)
if o == 'S':
    print(soma)
else:
    print(soma/nCasas)
