num = int(input())
lista = input().split()
for s in range (0, num):
    lista[s] = int(lista[s])
menor = lista[0]
pos_menor = 0
for z in range (0, num):
    if lista[z] < menor:
        menor = lista[z]
        pos_menor = lista.index(lista[z])
print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(pos_menor))

