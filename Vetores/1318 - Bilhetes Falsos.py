while True:
    #convertendo número de bilhetes originais e de pessoas para inteiros
    originais, pessoas = input().split()
    originais = int(originais)
    pessoas = int(pessoas)
    #condição de parada 0,0
    if originais == 0 and pessoas == 0:
        break
    contador = 0
    #perguntando a lista de bilhetes
    bilhetes = input().split()
    for t in range (0, len(bilhetes)):
        bilhetes[t] = int(bilhetes[t])
    #criando a lista de zeros
    lista = []
    for s in range (0, originais+1):
        lista.append(0)
    #print(lista)
    #preenchendo a lista de zeros com 1
    for c in range (0, len(bilhetes)):
        lista[bilhetes[c]] += 1
    #print(bilhetes)
    #print(lista)
    for x in range (1, len(lista)):
        if lista[x] > 1:
            contador += 1
    print(contador)

