while True:
    try:
        l, c = input().split()
        l, c = int(l), int(c)
        mat = [None] * l
        for k in range (0, l):
            mat[k] = input().split()
        for i in range (0, l):
            for j in range (0, c):
                mat[i][j] = int(mat[i][j])
                if mat[i][j] == 2:
                    linhaDoDigimon = i
                    colunaDoDigimon = j
                if mat[i][j] == 1:
                    linhaDoPersonagem = i
                    colunaDoPersonagem = j
        tamanho = abs(linhaDoDigimon - linhaDoPersonagem) + abs(colunaDoDigimon - colunaDoPersonagem)
        print(tamanho)
    except EOFError:
        break
        

