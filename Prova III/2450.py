n, m = [int(x) for x in input().split()]

mat = []
for i in range(n):
    mat.append([int(x) for x in input().split()])
    
nao = False
for i in range(n):
    if sum(mat[i]) == 0:
        for _i in range(i+1, n):
            for _j in range(m):
                if mat[_i][_j] != 0:
                    nao = True
                    break
    else:
        if not nao:
            for j in range(m):
                if mat[i][j] != 0:
                    for _i in range(i+1, n):
                        if mat[_i][j] != 0:
                            nao = True
                            break

                    break  # verifica apenas na primeira ocorrencia
        else:
            break

if nao:
    print('N')
else:
    print('S')
