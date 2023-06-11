while True:
    try:
        lista = []
        palavra = input()
        for c in range (0, len(palavra)):
            lista.append(palavra[c])
            lista.append(' ')
        del lista[len(lista)-1]
        for x in range (0, len(lista)):
            if x == len(lista) - 1:
                print(lista[x])
            else:
                print(lista[x], end='')
        for c in range (0, len(palavra) -1):
            del lista[len(lista)-1]
            del lista[len(lista)-1]
            lista.insert(0, ' ')
            for x in range (0, len(lista)):
                if x == len(lista) - 1:
                    print(lista[x])
                else:
                    print(lista[x], end='')
        print('')
    except EOFError:
        break

