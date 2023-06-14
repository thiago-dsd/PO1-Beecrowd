listaDePresenca = [0] * 1000001
numRegistros = int(input())
contador = 0
for _ in range (numRegistros):
    numAtual = int(input())
    if listaDePresenca[numAtual] == 0:
        listaDePresenca[numAtual] += 1
        contador += 1
print(contador)

