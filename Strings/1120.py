while True:
    a, b = input().split()
    if a != '0' and b != '0':
        final = ''
        for i in b:
            if i != a:
                final += i
        
        if final == '':
            final = '0'
            
        print(int(final))  # eliminar 0 repetido
        
    else:
        break
