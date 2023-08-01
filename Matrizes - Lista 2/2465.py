n = int(input())
i, j = [int(x)-1 for x in input().split()]

m = []
for _ in range(n):
    entrada = [int(x) for x in input().split()]
    m.append(entrada)

# pos atual
qtd = 1
q = [(i, j, m[i][j])]
m[i][j] = '*'

while q != []:
    i, j, v = q.pop()
    
    if i-1 >= 0 and m[i-1][j] != '*' and m[i-1][j] >= v:
        q.append((i-1, j, m[i-1][j]))
        m[i-1][j] = '*'
        qtd += 1
    if i+1 < n and m[i+1][j] != '*' and m[i+1][j] >= v:
        q.append((i+1, j, m[i+1][j]))
        m[i+1][j] = '*'
        qtd += 1
    if j-1 >= 0 and m[i][j-1] != '*' and m[i][j-1] >= v:
        q.append((i, j-1, m[i][j-1]))
        m[i][j-1] = '*'
        qtd += 1
    if j+1 < n and m[i][j+1] != '*' and m[i][j+1] >= v:
        q.append((i, j+1, m[i][j+1]))
        m[i][j+1] = '*'
        qtd += 1

print(qtd)
