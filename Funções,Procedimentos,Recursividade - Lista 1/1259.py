# ordenar crescente os pares
# ordenar decrescente os impares

n = int(input())
pares = []
impares = []

for _ in range(n):
    num = int(input())
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()
impares = sorted(impares, reverse=True)

for n in pares:
    print(n)
for n in impares:
    print(n)
