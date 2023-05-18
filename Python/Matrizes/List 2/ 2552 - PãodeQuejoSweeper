while True:
    try:
        l, c = input().split()
        l = int(l)
        c = int(c)
        
        temPaoDeQueijo = [None] * l
        for j in range (l):
            temPaoDeQueijo[j] = input().split()
            
        qntVizinhos = [None] * l
        for j in range (l):
            qntVizinhos[j] = [None] * c
        
        #percorrendo a matriz com pão de queijo
        for i in range (0, l):
            for j in range (0, c):
                if int(temPaoDeQueijo[i][j]) == 1:
                    qntVizinhos[i][j] = 9
                else:
                    qntVizinhosNaPosicao = 0
                    #analisando o vizinho de cima
                    elementoI = i - 1
                    elementoJ = j
                    if elementoI >= 0 and temPaoDeQueijo[elementoI][elementoJ] == '1':
                        qntVizinhosNaPosicao += 1
                    #analisando o vizinho de baixo
                    elementoI = i + 1
                    elementoJ = j
                    if elementoI < l and temPaoDeQueijo[elementoI][elementoJ] == '1':
                        qntVizinhosNaPosicao += 1
                    #analisando o vizinho da esquerda
                    elementoI = i
                    elementoJ = j - 1
                    if elementoJ >= 0 and temPaoDeQueijo[elementoI][elementoJ] == '1':
                        qntVizinhosNaPosicao += 1
                    #analisando o vizinho de cima
                    elementoI = i
                    elementoJ = j + 1
                    if elementoJ < c and temPaoDeQueijo[elementoI][elementoJ] == '1':
                        qntVizinhosNaPosicao += 1
                    qntVizinhos[i][j] = qntVizinhosNaPosicao
        for i in range (0, l):
            for j in range (0, c):
                print("{}".format(qntVizinhos[i][j]), end="")
            print()
    except EOFError:
        break
