while True:
    total = 0
    n, m = input().split()
    n = int(n)
    m = int(m)
    if n == m == 0:
        break
    #criando a matriz
    mat = [None] * m
    for k in range (0, m):
        mat[k] = input().split()
    #condições
    #condi 1
    var = 0
    total += 1
    for i in range (0, n):
        var = 0
        for j in range (0, m):
            mat[i][j] = int(mat[i][j])
            if mat[i][j] == 1:
                var += 1
        if var == m:
            total -= 1
            break
    #condi 2
    var = 0
    total += 1
    for j in range (0, m):
        var = 0
        for i in range (0, n):
            mat[i][j] = int(mat[i][j])
            if mat[i][j] == 1:
                var += 1
        if var == 0:
            total -= 1
            break
    #condi 3
    var = 0
    total += 1
    for j in range (0, m):
        var = 0
        for i in range (0, n):
            mat[i][j] = int(mat[i][j])
            if mat[i][j] == 1:
                var += 1
        if var == n:
            total -= 1
            break
    #condi 4
    var = 0
    total += 1
    for i in range (0, n):
        var = 0
        for j in range (0, m):
            mat[i][j] = int(mat[i][j])
            if mat[i][j] == 1:
                var += 1
        if var == 0:
            total -= 1
            break    
    #imprimindo matriz como base
    print(total)
'''
    for i in range (0, m):
        for j in range (0, n):
            print(' {}'.format(mat[i][j]), end='')
            print()
        print()
'''

