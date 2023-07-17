numElementos = int(input())
a1 = 1
a2 = 1
lista = [1, 1]
if numElementos == 1:
    print('1')
elif numElementos == 2:
    print('1 1')
else:
    for x in range (numElementos - 2):
        #lista.append(a1)
        Smaior = a2 + a1
        lista.append(Smaior)
        a1 = a2
        a2 = Smaior
    lista = lista[::-1]
    """
    for k in range (len(lista)):
        if k == len(lista)-1:
            print(lista[k], end="")
        else:
            print(lista[k], end=" ")
            """
    print(' '.join(   list(map(str, lista))    ))


