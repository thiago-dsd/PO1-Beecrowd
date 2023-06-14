l, c = input().split()
l, c = int(l), int(c)
valorMarcadosComX = []
#lista mostrando se a linha determinada tem numeros(1) ou se é apenas de zero
listaDeZerosouUM = [0] * l
#captando a matriz dada no enunciado
mat = [None] * l
for k in range (0, l):
    mat[k] = input().split()
#a princípio consideraremos a matriz como válida
validadeDaMatriz = True
#iremos percorrer cada linha em busca do primeiro valor diferente de zero
for i in range (0, l):
    for j in range (0, c):
        mat[i][j] = int(mat[i][j])
        if mat[i][j] != 0:
            #ao achar o primeiro valor != 0 marcamos ele com X
            #adicionamos ele na lista
            #e buscamos a próxima linha
            mat[i][j] = 'X'
            listaDeZerosouUM[i] = 1
            valorMarcadosComX.append((i,j))
            break
#verificando as linhas de zero
for m in range (1, len(listaDeZerosouUM)):
    if listaDeZerosouUM[m-1] == 0 and listaDeZerosouUM[m] == 1:
        validadeDaMatriz = False
for k in range (0, len(valorMarcadosComX)):
    if validadeDaMatriz == False:
        break
    for i in range (valorMarcadosComX[k][0]+1, l):
        if mat[i][valorMarcadosComX[k][1]] != 0:
            validadeDaMatriz = False
            break
if validadeDaMatriz == False:
    print('N')
else:
    print('S')



