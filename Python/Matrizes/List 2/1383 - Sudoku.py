numRepeticoes = int(input())
contador = 0
for _ in range (numRepeticoes):
    contador += 1
    mat = [None] * 9
    for k in range (0, 9):
        mat[k] = input().split()
        for j in range (0, 9):
            mat[k][j] = int(mat[k][j])

    validadeDaMatriz = True
    
    #conferindo as colunas
    if validadeDaMatriz == True:
        for j in range (0, 9):
            numeros = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range (0, 9):
                numeros[mat[i][j]] += 1
            for k in range (0, 10):
                if numeros[k] != 1:
                    validadeDaMatriz = False
                    break
    
    #conferindo as linhas
    if validadeDaMatriz == True:
        for i in range (0, 9):
            numeros = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for j in range (0, 9):
                numeros[mat[i][j]] += 1
            for k in range (0, 10):
                if numeros[k] != 1:
                    validadeDaMatriz = False
                    break
                
    #BLOCO SUPERIOR DE MATRIZES
    if validadeDaMatriz == True:
        #conferindo matriz superior esquerda
        numeros = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range (0, 3):
            for j in range (0, 3):
                numeros[mat[i][j]] += 1
        for k in range (0, 10):
                if numeros[k] != 1:
                    validadeDaMatriz = False
                    break
            
    if validadeDaMatriz == True:
        #conferindo matriz superior central
        numeros = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range (3, 6):
            for j in range (0, 3):
                numeros[mat[i][j]] += 1
        for k in range (0, 10):
                if numeros[k] != 1:
                    validadeDaMatriz = False
                    break

    if validadeDaMatriz == True:
        #conferindo matriz superior direita
        numeros = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range (6, 9):
            for j in range (0, 3):
                numeros[mat[i][j]] += 1
        for k in range (0, 10):
                if numeros[k] != 1:
                    validadeDaMatriz = False
                    break
    
    #BLOCO CENTRAL DE MATRIZES
    if validadeDaMatriz == True:
        #conferindo matriz CENTRAL esquerda
        numeros = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range (0, 3):
            for j in range (3, 6):
                numeros[mat[i][j]] += 1
        for k in range (0, 10):
                if numeros[k] != 1:
                    validadeDaMatriz = False
                    break

    if validadeDaMatriz == True:
        #conferindo matriz CENTRAL central
        numeros = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range (3, 6):
            for j in range (3, 6):
                numeros[mat[i][j]] += 1
        for k in range (0, 10):
                if numeros[k] != 1:
                    validadeDaMatriz = False
                    break

    if validadeDaMatriz == True:
        #conferindo matriz CENTRAL direita
        numeros = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range (6, 9):
            for j in range (3, 6):
                numeros[mat[i][j]] += 1
        for k in range (0, 10):
                if numeros[k] != 1:
                    validadeDaMatriz = False
                    break
    
    #BLOCO INFERIOR DE MATRIZES

    if validadeDaMatriz == True:
        #conferindo matriz inferior esquerda
        numeros = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range (0, 3):
            for j in range (6, 9):
                numeros[mat[i][j]] += 1
        for k in range (0, 10):
                if numeros[k] != 1:
                    validadeDaMatriz = False
                    break

    if validadeDaMatriz == True:
        #conferindo matriz inferior central
        numeros = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range (3, 6):
            for j in range (6, 9):
                numeros[mat[i][j]] += 1
        for k in range (0, 10):
                if numeros[k] != 1:
                    validadeDaMatriz = False
                    break

    if validadeDaMatriz == True:
        #conferindo matriz inferior direita
        numeros = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range (6, 9):
            for j in range (6, 9):
                numeros[mat[i][j]] += 1
        for k in range (0, 10):
                if numeros[k] != 1:
                    validadeDaMatriz = False
                    break
    
    print('Instancia {}'.format(contador))
    if validadeDaMatriz == True:
        print("SIM")
    else:
        print("NAO")
    print()
