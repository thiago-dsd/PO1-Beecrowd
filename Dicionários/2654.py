n = int(input())

nome, p, k, m = input().split()
melhor_p = int(p)
melhor_k = int(k)
melhor_m = int(m)
melhor = nome.strip()

for _ in range(n-1):
    nome, p, k, m = input().split()
    p = int(p)
    k = int(k)
    m = int(m)
    nome = nome.strip()
    troca = False
    
    if p > melhor_p:
        troca = True
    elif p == melhor_p:
        if k > melhor_k:
            troca = True
        elif k == melhor_k:
            if m < melhor_m:
                troca = True
            elif m == melhor_m:
                if nome < melhor:
                    troca = True
        
    if troca:
        melhor_p = p
        melhor_k = k
        melhor_m = m
        melhor = nome

print(melhor)
