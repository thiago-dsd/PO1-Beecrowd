while True:
    n, m = [int(x) for x in input().split()]

    if n == 0:
        break
    
    mat = []
    q = []
    for i in range(n):
        linha = input()
        mat.append([x for x in linha])
        for j in range(m):
            if mat[i][j] == 'T':
                q.append((i, j))
    
    while q != []:
        i, j = q.pop(0)
        
        if i >= 1 and mat[i-1][j] == 'A':
            mat[i-1][j] = 'T'
            q.append((i-1, j))
        
        if i <= n-2 and mat[i+1][j] == 'A':
            mat[i+1][j] = 'T'
            q.append((i+1, j))
            
        if j >= 1 and mat[i][j-1] == 'A':
            mat[i][j-1] = 'T'
            q.append((i, j-1))
        
        if j <= m-2 and mat[i][j+1] == 'A':
            mat[i][j+1] = 'T'
            q.append((i, j+1))
    
    for linha in mat:
        print(''.join(linha))
        
    print()
