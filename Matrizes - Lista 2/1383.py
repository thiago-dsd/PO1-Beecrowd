# todas as somas devem ser iguais a 55 (1+2+3+...+10) = 10(11)/2 = 55

def ver_bloco(m, i, j):
    tmp = set()
    for _i in range(i, i+3):
        for _j in range(j, j+3):
            tmp.add(m[_i][_j])
    return tmp

n = int(input())

for k in range(1, n+1):
    incorreto = False
    m = []
    for _ in range(9):
        ent = [int(x) for x in input().split()]
        m.append(ent)
    
    # verificar linhas
    for i in range(9):
        if len(set((m[i]))) != 9:
            incorreto = True
            break
    
    if not incorreto:
        # verificar colunas
        for j in range(9):
            tmp = set()
            for i in range(9):
                tmp.add(m[i][j])
            if len(tmp) != 9:
                incorreto = True
                break
    
        if not incorreto:
            # verificar blocos
            bloco = (0, 3, 6)
            for i in bloco:
                for j in bloco:
                    tmp = ver_bloco(m, i, j)
                    
                    if len(tmp) != 9:
                        incorreto = True
                        break
                    
                if incorreto:
                    break
                
    print('Instancia', k)
    if incorreto:
        print('NAO')
    else:
        print('SIM')
    print()

