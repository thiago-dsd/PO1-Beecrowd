n = int(input())
o = input()

#criando uma matriz
m = [None] * 12
for i in range (0, 12):
    m[i] = [None] * 12

#percorrendo os valores
for i in range (0, 12):
    for j in range (0, 12):
        m [i][j] = float(input())

#operações aritméticas
soma = 0
for j in range (0, 12):
    soma += m[n][j]
if o == 'S':
    print(soma)
else:
    print(soma/12)