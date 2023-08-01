n = int(input())
intervalo = [int(x) for x in input().split()]

ate_n = list(range(1, n+1))
for x in ate_n:
    if x not in intervalo:
        faltante = x
        break

print(faltante)
