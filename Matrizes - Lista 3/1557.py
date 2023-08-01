while True:
    tam = int(input())
    if tam == 0:
        break
    
    maior = 2**((tam-1)*2)
    padding = len(str(maior))
    align = '>' + str(padding)
    
    for i in range(tam):
        for j in range(tam):
            n = 2**(j+i)
            if j != tam-1:
                print(f'{n:{align}}', end=' ')
            else:
                print(f'{n:{align}}')
    print()

