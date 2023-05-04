while True:
    n = int(input())
    if n == 0:
        break
    mat = [None] * n
    for i in range (0, n):
        for j in range (0, n):
            mat [i][j] = 