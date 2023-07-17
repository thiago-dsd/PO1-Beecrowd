solProb = [None] * 101
while True:
    n, m = input().split()
    n = int(n)
    m = int(m)
    
    if n == 0 and m == 0:
        break
        
    for i in range(m):
        solProb[i] = 0
        
    ngnResolveuTodos = True
    aoMenosUmProblema = True
    todoProblemaResolvido = True
    naoResolvidoPorTodos = True
    
    for i in range(n):
        solucoes = input().split()
        
        qtdeResolvidosTime = 0
        for j in range(m):
            if solucoes[j] == '1':
                qtdeResolvidosTime += 1 
                solProb[j] += 1
        
        if qtdeResolvidosTime == m: 
            ngnResolveuTodos = False
            
        if qtdeResolvidosTime == 0:
            aoMenosUmProblema = False
    

    for i in range(m):
        if solProb[i] == 0:
            todoProblemaResolvido = False
        if solProb[i] == n:
            naoResolvidoPorTodos = False
    
    critSatis = 0
    if ngnResolveuTodos:
        critSatis += 1
    if aoMenosUmProblema:
        critSatis += 1
    if todoProblemaResolvido:
        critSatis += 1
    if naoResolvidoPorTodos:
        critSatis += 1
    
    print(critSatis)
