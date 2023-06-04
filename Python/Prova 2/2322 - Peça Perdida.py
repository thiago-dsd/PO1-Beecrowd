num = int(input())
pecas = input().split()
lista = [0]
#criando uma lista com a quantidade de peças + 1
for l in range (0, num):
    lista.append(0)
#print(lista)
#criando um lista com as pecas dadas
for n in range (0, len(pecas)):
    pecas[n] = int(pecas[n])
    lista[pecas[n]] = pecas[n]
#print(pecas)
#print(lista)
for x in range (1, len(lista)):
    if lista[x] == 0:
        print(x)
        break

