# indo: 
#    F: baixo
#    L: esquerda
#    R: direita
#    U: cima (adicional)
resps = []
prova_real = ['F L F R F E', 'F R F L F F L F F R F L F F L F F F F E']
while True:
    try:
        m, n = [int(x) for x in input().split()]
    except EOFError:
        break
    else:
        matriz = []
        caminho = [] # lista para facilitar o print no fim
        achou_x = False
        for i in range(m):
            linha = input().split()
            if not achou_x:
                for j in range(n):
                    if linha[j] == 'X':
                        i_x = i
                        j_x = j
                        achou_x = True
                        break
            matriz.append(linha)
        
        q = [(i_x, j_x, 'F')]  # inicia direcionado para frente
        while q != []:
            i_at, j_at, indo = q.pop(0)

            # baixo (F)
            if i_at+1 <= m-1 and matriz[i_at+1][j_at] == '0':
                tmp = [i_at+1, j_at]
                matriz[i_at][j_at] = '*'
                if indo == 'F':
                    ...
                elif indo == 'L':
                    caminho.append('L')
                else:  # 'R' ('U' impossível)
                    caminho.append('R')
                    
                caminho.append('F') # sempre vai para a frente
                tmp.append('F') # ele fica direcionado para baixo, independente da direcao ant
                q.append(tuple(tmp))
            
            # Cima (U)
            if i_at-1 >= 0 and matriz[i_at-1][j_at] == '0':
                tmp = [i_at-1, j_at]
                matriz[i_at][j_at] = '*'
                if indo == 'U':
                    ...
                elif indo == 'L':
                    caminho.append('R')
                else:  # 'R' ('F' impossivel)
                    caminho.append('L')
                    
                caminho.append('F')
                tmp.append('U')
                q.append(tuple(tmp))        
        
            # Direita (R)
            if j_at+1 <= n-1 and matriz[i_at][j_at+1] == '0':
                tmp = [i_at, j_at+1]
                matriz[i_at][j_at] = '*'
                if indo == 'R':
                    ...
                elif indo == 'U':
                    caminho.append('R')
                else:  # 'F' ('L' impossivel)
                    caminho.append('L')
                
                caminho.append('F')
                tmp.append('R')
                q.append(tuple(tmp))
            
            # Esquerda (L)
            if j_at-1 >= 0 and matriz[i_at][j_at-1] == '0':
                tmp = [i_at, j_at-1]
                matriz[i_at][j_at] = '*'
                if indo == 'L':
                    ...
                elif indo == 'F':
                    caminho.append('R')
                else:  # 'U' ('R' impossivel)
                    caminho.append('L')
                    
                caminho.append('F')
                tmp.append('L')
                q.append(tuple(tmp))
        
        print(' '.join(caminho), 'E')
