n = int(input())
for q in range(1, n+1):
    cartas = [int(x) for x in input().split()]
    cartas.sort()  # Roubei! (usado no check 1)
    
    sem_rep = list(set(cartas))
    len_sem_rep = len(sem_rep)
    pontuacao = 0
    
    # Check 1
    if len_sem_rep == 5:
        for i in range(4):  # ir ate o penultimo
            if cartas[i+1] != cartas[i] + 1:
                break
        else:
            pontuacao = 200 + cartas[0]
    
    # Check 2
    elif len_sem_rep == 2:
        qtds = [0] * 13  # 13 cartas
        for i in cartas:  # sempre 5 cartas
            qtds[i-1] += 1
    
        maior_k = maior_v = 0
        for k, v in enumerate(qtds):
            if v > maior_v:
                maior_k = k + 1
                maior_v = v
        
        if maior_v == 4:
            pontuacao = 180 + maior_k
    
        if pontuacao == 0:
            # Check 3
            x, y = sem_rep
            cx = cy = 0
            for i in cartas:
                if i == x:
                    cx += 1
                elif i == y:
                    cy += 1
            if cx == 3 and cy == 2:
                pontuacao = x + 160
            elif cx == 2 and cy == 3:
                pontuacao = y + 160
    
    # check 4
    elif len_sem_rep == 3:
        x, y, z = sem_rep
        cx = cy = cz = 0
        for i in cartas:
            if i == x:
                cx += 1
            elif i == y:
                cy += 1
            elif i == z:
                cz += 1
        if cx == 3:
            pontuacao = x + 140
        elif cy == 3:
            pontuacao = y + 140
        elif cz == 3:
            pontuacao = z + 140

        if pontuacao == 0:
            # check 5
            x, y, z = sem_rep
            cx = cy = cz = 0
            for i in cartas:
                if i == x:
                    cx += 1
                elif i == y:
                    cy += 1
                elif i == z:
                    cz += 1
            if cx == 2 and cy == 2:
                me, ma = sorted([x, y])
                pontuacao = 3*ma + 2*me + 20
            elif cx == 2 and cz == 2:
                me, ma = sorted([x, z])
                pontuacao = 3*ma + 2*me + 20
            elif cy == 2 and cz == 2:
                me, ma = sorted([y, z])
                pontuacao = 3*ma + 2*me + 20    
    

    # check 6
    elif len_sem_rep == 4:
        x, y, z, a = sem_rep
        cx = cy = cz = ca = 0
        for i in cartas:
            if i == x:
                cx += 1
            elif i == y:
                cy += 1
            elif i == z:
                cz += 1
            elif i == a:
                ca += 1
        if cx == 2:
            pontuacao = x
        elif cy == 2:
            pontuacao = y
        elif cz == 2:
            pontuacao = z
        elif ca == 2:
            pontuacao = a
    
    print('Teste', q)
    print(pontuacao)
    print()
