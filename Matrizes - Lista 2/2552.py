# terei que usar matrizes...
while True:
    try:
        n, m = [int(x) for x in input().split()]
    except EOFError:
        break
    else:
        matriz = []
        final = []
        
        for i in range(n):
            colunas = [int(x) for x in input().split()]
            matriz.append(colunas)
        
        for i in range(n):
            tmp = [0]*m
            for j in range(m):
                if matriz[i][j] == 1:
                    tmp[j] = 9
                else:
                    if i-1 >= 0:
                        if matriz[i-1][j] == 1:
                            tmp[j] += 1
                    if i+1 < n:
                        if matriz[i+1][j] == 1:
                            tmp[j] += 1
                    if j-1 >= 0:
                        if matriz[i][j-1] == 1:
                            tmp[j] += 1
                    if j+1 < m:
                        if matriz[i][j+1] == 1:
                            tmp[j] += 1
                            
            final.append(tmp)
        
        for i in final:
            print(''.join([str(x) for x in i]))
