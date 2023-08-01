c = int(input())
for k in range(1, c+1):
    m, n, x, y = [int(x) for x in input().split()]
    x, y = x-1, y-1
    
    mat = []
    for _ in range(m):
        ent = [int(x) for x in input().split()]
        mat.append(ent)

    for i in range(m):
        for j in range(n):
            camada = max(abs(x-i), abs(y-j))
            bonus = 10 - camada
            if bonus <= 0:
                bonus = 1
            mat[i][j] += bonus
    
    print(f'Parede {k}:')
    for i in mat:
        print(' '.join([str(x) for x in i]))

