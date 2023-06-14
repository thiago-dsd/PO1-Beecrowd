listaDeFigurinhas = [0] * 301
numRegistros = int(input())
figurinhasDiferentes = 0
figurinhasRepitidas = 0
for _ in range (numRegistros):
    figurinhaAtual = int(input())
    if listaDeFigurinhas[figurinhaAtual] == 0:
        listaDeFigurinhas[figurinhaAtual] += 1
        figurinhasDiferentes += 1
    else:
        figurinhasRepitidas += 1
print(figurinhasDiferentes)
print(figurinhasRepitidas)

