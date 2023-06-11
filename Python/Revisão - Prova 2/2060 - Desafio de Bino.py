multiplos = [0, 0, 0, 0]
num = int(input())
lista = input().split()
for x in range (0, num):
    lista[x] = int(lista[x])
    if lista[x] % 2 == 0:
        multiplos[0] += 1
    if lista[x] % 3 == 0:
        multiplos[1] += 1
    if lista[x] % 4 == 0:
        multiplos[2] += 1
    if lista[x] % 5 == 0:
        multiplos[3] += 1
print('{} Multiplo(s) de 2'.format(multiplos[0]))
print('{} Multiplo(s) de 3'.format(multiplos[1]))
print('{} Multiplo(s) de 4'.format(multiplos[2]))
print('{} Multiplo(s) de 5'.format(multiplos[3]))

