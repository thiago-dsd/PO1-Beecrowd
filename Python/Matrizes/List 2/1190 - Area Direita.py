o = input()
soma = 0
#criando a matriz
mat = [None] * 12
for i in range (12):
    mat = [None] * 12

#percorrendo os valores da matriz
for i in range (0, 12):
    for j in range (0, 12):
        mat[i][j] = float(input())
#percorrendo o triângulo superior
c = 0
for i in range (5, 0, -1):
    for j in range (7 + c, 12):
        soma += mat[i][j]
        c += 1
for i in range (6, 11):
    for j in range (i+1, 12):
        soma += mat[i][j]
#fazendo as operações aritméticas
qnt = ((144 - 2*12) / 4)
if o == 'S':
    print(soma)
else:
    print(soma/qnt)