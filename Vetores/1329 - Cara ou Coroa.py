while True:
    maria = 0
    john = 0
    qnt = int(input())
    if qnt == 0:
        break
    lista = input().split()
    for c in range (0, qnt):
        lista[c] = int(lista[c])
        if lista[c] == 0:
            maria += 1
        else:
            john += 1
    print('Mary won {} times and John won {} times'.format(maria, john))
        

