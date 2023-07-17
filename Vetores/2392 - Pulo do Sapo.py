#comprimento | número de varetas com esse comprimento
pedras, sapos = input().split()
pedras = int(pedras)
sapos = int(sapos)
lista = []
#enchendo a lista de zeros
for s in range (0, pedras+1):
    lista.append(0)
for c in range (0, sapos):
    pos, pulo = input().split()
    pos = int(pos)
    pulo = int(pulo)
    #procurando 
    for i in range (pos, pedras+1, pulo):
        lista[i] = 1
    for i in range (pos, 0, -pulo):
        lista[i] = 1
#printando valores
for printar in range (1, len(lista)):
    print(lista[printar])


