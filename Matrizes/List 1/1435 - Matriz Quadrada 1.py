while True:
    n = int(input())
    if n == 0:
        break
    #criando uma matriz preenchida com 'None'
    mat = [None] * n
    for i in range (0, n):
        mat[i] = [None] * n

    #preenchendo a matriz
    cont = 1
    for i in range (0, n):
        for j in range (0, n):
            lc = i
            ce = j
            lb = n-(i)-1
            cd = n-(j)-1
            #selecionando o menor valor
            lista = [lc, lb, ce, cd]
            mat[i][j] = min(lista)+1
    #printando a matriz
    for i in range (0, n):
        for j in range (0, n):
            if j == 0:
                print('{:>3}'.format(mat[i][j]), end = '')
            else:
                print(' {:>3}'.format(mat[i][j]), end = '')
        print()
    print()