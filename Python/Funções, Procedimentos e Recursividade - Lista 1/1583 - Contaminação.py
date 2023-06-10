while True:
    l, c = input().split()
    l, c = int(l), int(c)
    if l == c == 0:
        break
    mat = [0] * l
    for i in range (l):
        mat[i] = [0] * c
        palavraAtual = input()
        for k in range (c):
            mat[i][c] = palavraAtual[c]
            
           
    for i in range (l):
        for j in range (c):
            print(mat[i][j], end="")
    print()
    """
    for k in range (len(lista)):
        print(lista[k])
    print()
    """

"""
while True:
    l, c = input().split()
    l, c = int(l), int(c)
    if l == c == 0:
        break
    lista = []
    for i in range (l):
        palavraAtual = input()
        troca('A', 'T', palavraAtual)
        lista.append(palavraAtual)
    for k in range (len(lista)):
        print(lista[k])
    print()
"""