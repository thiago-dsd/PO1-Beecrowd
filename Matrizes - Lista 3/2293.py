# possivel utilizacao de programacao dinamica?
# em principio, tentativa por forca bruta
# armazenar resultados de linhas ja na entrada

maior = 0

n, m = [int(x) for x in input().split()]
matriz = []
for i in range(n):
    linha = [int(x) for x in input().split()]
    matriz.append(linha)
    tmp = sum(linha)
    if tmp > maior:
        maior = tmp

for j in range(m):
    tmp = 0
    for i in range(n):
        tmp += matriz[i][j]
    if tmp > maior:
        maior = tmp

print(maior)
