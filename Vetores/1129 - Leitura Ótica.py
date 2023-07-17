while True:
    qnt = int(input())
    if qnt == 0:
        break
    for q in range (0, qnt):
        preto = 0
        letra = []
        notas = input().split()
        for i in range (0, len(notas)):
            notas[i] = int(notas[i])
            if notas[i] <= 127:
                preto += 1
                letra.append(i)
        #printando a letra adequada
        if preto == 1:
            if letra[0] == 0:
                print('A')
            elif letra[0] == 1:
                print('B')
            elif letra[0] == 2:
                print('C')
            elif letra[0] == 3:
                print('D')
            else:
                print('E')
        else:
            print('*')
    


