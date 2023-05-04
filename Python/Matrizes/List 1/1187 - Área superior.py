op = input()

#criando matriz
mat = [None] * 12
for i in range (0, 12):
    mat[i] = [None] * 12

for i in range (0, 12):
    for j in range (0, 12):
        mat[i][j] = float(input())

#percorrendo linhas da matriz
soma = 0
numEl = (12*12 - 2*12) / 4
for k in range (1, 6):
    for j in range (0, k):
        soma += mat[k][j]     
for m in range (6, 11):
    for o in range (0, 11 -m):
        soma += mat[m][o]

#escolhendo operação que será realizada
if op == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/numEl))


