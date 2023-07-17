#sempre o segundo mais suspeito
while True:
    teste = int(input())
    if teste == 0:
        break
    lista = input().split()
    for c in range (0, len(lista)):
        lista[c] = int(lista[c])
        if c == 0:
            n_p_susp = c+1
            n_s_susp = 0
            p_susp = lista[c]
            s_susp = 0
        else:
            if p_susp > lista[c] and lista[c] > s_susp:
                n_s_susp = c+1
                s_susp = lista[c]
            if lista[c] > p_susp:
                n_s_susp = n_p_susp
                s_susp = p_susp
                n_p_susp = c+1 
                p_susp = lista[c]
    print(n_s_susp)
            
        

