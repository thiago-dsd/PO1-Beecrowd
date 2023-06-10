dicionario = {}
n = int(input())
seCompt = nSeCompt = 0
for _ in range (n):
    op, nome = input().split()
    dicionario[nome] = '+'
    if op == '+':
        seCompt += 1
    else:
        nSeCompt += 1
for i in range (0, n):
    newDict = sorted(dicionario.items())
    print(newDict[i][0])