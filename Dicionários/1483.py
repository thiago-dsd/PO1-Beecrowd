while True:
    v, n, m = input().split()
    v = float(v)
    
    if v == 0:
        break
    
    n = n.zfill(4)
    m = m.zfill(4)
    
    ganho = 0
    if n[-4:] == m[-4:]:
        ganho = v * 3000
    elif n[-3:] == m[-3:]:
        ganho = v * 500
    elif n[-2:] == m[-2:]:
        ganho = v * 50
    else:
        _n = int(n[-2:])
        _m = int(m[-2:])
        q1, r1 = divmod(_n, 4)
        q2, r2 = divmod(_m, 4)
        if not _n or not _m:
            if _n >= 97 or _m >= 97:
                ganho = v * 16
        elif (q1 == q2) or (q1 == q2 + 1 and r1 == 0) or (q1 == q2 - 1 and r2 == 0):
            ganho = v * 16
    
    print(f'{ganho:.2f}')

