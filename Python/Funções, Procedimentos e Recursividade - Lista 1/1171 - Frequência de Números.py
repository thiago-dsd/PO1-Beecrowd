numT = int(input())
lista = [0] * 2001
for _ in range (numT):
    n = int(input())
    lista[n] += 1
for k in range (0, 2001):
    if lista[k] != 0:
        print("{} aparece {} vez(es)".format(k, lista[k]))

