op = input()
mat = [None] * 12
for i in range (0, 12):
    mat[i] = [None] * 12

for i in range (0, 12):
    for j in range (0, 12):
        mat[i][j] = float(input())

soma = 0
numEl = (12*12 - 12) / 2
for k in range (1, 12):
    for j in range (12 - k, 12):
        soma += mat[k][j]    

if op == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/numEl))
