# nao eh funcao: a seta sai mais de uma vez por um objeto
# inversivel: x -> y e x' -> y' => y != y'

while True:
    t = int(input())
    
    if t == 0:
        break
    
    d = []
    for _ in range(t):
        a, b = input().split(' -> ')
        d.append((a, b))
    
    eh_func = inversivel = True
    for i in range(t):
        c = 0
        for j in range(i+1, t):
            a1, b1 = d[i]
            a2, b2 = d[j]

            if b1 == b2:
                c += 1
            if a1 == a2:
                eh_func = False
        
        if c != 0:
            inversivel = False
    
    if not eh_func:
        print('Not a function.')
    else:
        if inversivel:
            print('Invertible.')
        else:
            print('Not invertible.')
