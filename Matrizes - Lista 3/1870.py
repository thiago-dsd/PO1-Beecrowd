while True:
    l, c, p = [int(x) for x in input().split()]
    
    if l == 0:
        break
    
    p -= 1
    explodiu = False
    for i in range(l):
        linha = [int(x) for x in input().split()]
        
        if i != 0: # verificar se o balao cair num ventilador na linha de baixo
            if linha[p] != 0:
                explodiu = True
                break
        
        vent_l = vent_r = 0
        for j in range(c):
            if linha[j] != 0:
                if j < p:
                    i_vent_l = j
                    vent_l = linha[j]
                elif j > p:
                    i_vent_r = j
                    vent_r = linha[j]

            if vent_l and vent_r:
                break
        
        if vent_l >= vent_r:
            p += vent_l - vent_r
            if p == i_vent_r:
                explodiu = True                        
                break
        else:
            p -= vent_r - vent_l
            if p == i_vent_l:
                explodiu = True                        
                break

        if p < 0 or p > c-1:
            explodiu = True
            
        if explodiu:
            break

    for _ in range(i, l-1): # consumir linhas adicionais
        input()

    if explodiu:
        print('BOOM', i+1, p+1)
    else:
        print('OUT', p+1)
