numeroDeTestes = int(input())
contador = 0
for _ in range (numeroDeTestes):
    contador += 1
    l, c, xSoco, ySoco = input().split()
    l, c, xSoco, ySoco = int(l), int(c), int(xSoco), int(ySoco)
    xSoco -= 1
    ySoco -= 1
    #criando a matriz com os valores
    mat = [None] * l
    for k in range (0, l):
        mat[k] = input().split()
    for i in range (0, l):
        for j in range (0, c):
            mat[i][j] = int(mat[i][j]) 
            if i == xSoco and j == ySoco:
                mat[i][j] += 10
            elif max(abs(xSoco - i), abs(ySoco - j)) > 8:
                mat[i][j] += 1
            else:
                mat[i][j] += (10 - max(abs(xSoco - i), abs(ySoco - j)))
    print("Parede {}:".format(contador))
    for i in range (0, l):
        for j in range (0, c):
            if j == (c-1):
                print("{}".format(mat[i][j]), end="")
            else:
                print("{}".format(mat[i][j]), end=" ")
        print()

