n = int(input())
mat = []
for _ in range(n):
    lin = [int(x) for x in input().split()]
    mat.append(lin)

esp = set()
for _ in range(2*n):
    i, j = [int(x)-1 for x in input().split()]
    esp.add(mat[i][j])

print(len(esp))
