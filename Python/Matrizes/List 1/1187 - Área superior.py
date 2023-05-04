op = input()
mat = [None] * 12
for i in range (0, 12):
    mat[i] = [None] * 12

for i in range (0, 12):
    for j in range (0, 12):
        mat[i][j] = float(input())

soma = 0
numEl = (12*12 - 2*12) / 4
for k in range (1, 6):
    for j in range (0, 5-k):
        soma += mat[k][j]
        
        
for k in range (6, 11):
    for j in range (0, 5-(k-6)):
        soma += mat[k][j]

if op == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/numEl))


