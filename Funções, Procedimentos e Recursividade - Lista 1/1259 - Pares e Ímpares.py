num = int(input())
pares = []
impares = []
for k in range (num):
    n = int(input())
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
for m in range(len(pares)):
    print(pares[m])
impares.sort()
impares = impares[::-1]
for n in range(len(impares)):
    print(impares[n])

