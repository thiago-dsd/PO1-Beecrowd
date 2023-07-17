while True:
    try:
        l, c = input().split()
        l, c = int(l), int(c)
        #captando a matriz dada no enunciado
        mat = [None] * l
        for k in range (0, l):
            mat[k] = input().split()
            
        litrosDeCafe = 0
        #percorrendo e somando os litros de cafe por pé
        for i in range (0, l):
            for j in range (0, c):
                mat[i][j] = int(mat[i][j])
                litrosDeCafe += mat[i][j]
        print("{} saca(s) e {} litro(s)". format(litrosDeCafe // 60, litrosDeCafe % 60))
    except EOFError:
        break

