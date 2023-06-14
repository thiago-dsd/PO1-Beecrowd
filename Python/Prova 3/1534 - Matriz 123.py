while True:
    try:
        l = int(input())
        #pegue uma matriz e encha ela de 3
        mat = [3] * l
        for k in range (0, l):
            mat[k] = [3] * l
        #determine a posição do 1 como 1 e do 2 como ultimo elemento
        posicao1 = 0
        posicao2 = l-1
        #percorra linha por linha da matriz
        for k in range (0, l):
            #coloque o 1 em seu devido lugar e o 2 também
            mat[k][posicao1] = 1
            mat[k][posicao2] = 2
            #depois some 1 na posição do 1, para translocar ele uma cada a direita
            posicao1 += 1
            #e substraia 1 na posicao do 2, para translocar ele uma casa para a esquerda
            posicao2 -= 1
        #pronto! só printar a matriz
        for i in range (0, l):
            for j in range (0, l):
                print("{}".format(mat[i][j]), end="")
            print()
    except EOFError:
        break


