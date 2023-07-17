while True:
    try:
        num = int(input())
        lista = input().split()
        satisf = 0 
        nsatisf = 0
        for c in range (0, num):
            lista[c] = int(lista[c])
            if lista[c] == 0:
                satisf += 1
            else:
                nsatisf += 1
        if satisf > nsatisf:
            print('Y')
        else:
            print('N')
    except EOFError:
        break


