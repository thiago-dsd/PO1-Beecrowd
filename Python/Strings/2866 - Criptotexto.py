num = int(input())
for c in range (0, num):
    escondida = []
    palavra = input()
    for s in range (0, len(palavra), +1):
        if palavra[s] in "abcdefghijklmnopqrstuvwxyz":
            escondida.append(palavra[s])
    escondida = ''.join(escondida)
    escondida = escondida[::-1]
    print(escondida)
    escondida = []
            

