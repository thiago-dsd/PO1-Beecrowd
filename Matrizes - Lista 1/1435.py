while (n := int(input())) != 0:
    c = d = 0
    for i in range(n):
        if i < n / 2:
            c = i + 1
        else:
            c = n - i
        for j in range(n):
            if j < n / 2:
                d = j + 1
            else:
                d = n - j
            
            if c >= d:
                escolhido = d
            else:
                escolhido = c
            
            if j != n-1:
                print('%3d ' % escolhido, end='')
            else:
                print('%3d' % escolhido)
        
    print()
