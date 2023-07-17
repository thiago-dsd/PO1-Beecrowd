dicionario = {'A':0, 'E':0, 'H':0, 'M':0, 'X':0}
n = int(input())
for k in range(n):
    nome, tipo = input().split()
    dicionario[tipo] += 1
print("{} Hobbit(s)".format(dicionario['X']))
print("{} Humano(s)".format(dicionario['H']))
print("{} Elfo(s)".format(dicionario['E']))
print("{} Anao(oes)".format(dicionario['A']))
print("{} Mago(s)".format(dicionario['M']))

