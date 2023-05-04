n = int(input())

#criando uma matriz preenchida com 'None'
mat = [None] * n
for i in range (0, n):
    mat[i] = [None] * n

#determinando o número máximo que sera colocado na matriz
if n >= 4:
    nMax = n - 2
elif n == 3:
    nMax = 2
else:
    nMax = 1

#preenchendo a matriz do elemento central para os adjacentes
cont = 1
for i in range (0, n):
    for j in range (0, n):
        '''if i == 1 or i == n-2 or j == 1 or j == n-2:
            mat[i][j] = 2 
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            mat[i][j] = 1 '''
        if (i == cont - 1) or (i == n - cont) or (j == cont - 1) or (j == n - cont):
            mat[i][j] = cont
        cont += 1
    
        

#printando a matriz
for i in range (0, n):
    for j in range (0, n):
        print('{} '.format(mat[i][j]), end = '')
    print()