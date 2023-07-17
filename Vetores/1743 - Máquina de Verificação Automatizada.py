lista1 = input().split()
lista2 = input().split()
n = 1
for i in range (len(lista1)):
    lista1[i] = int(lista1[i])
    lista2[i] = int(lista2[i])
    if lista1[i] == lista2[i]:
        print('N')
        n = 0
        break
if n != 0:
    print('Y')
    


