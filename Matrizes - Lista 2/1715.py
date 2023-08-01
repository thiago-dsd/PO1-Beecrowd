n, m = [int(x) for x in input().split()]

c = 0
for i in range(n):
    partidas = [int(x) for x in input().split()]
    for i in partidas:
        if i == 0:
            break
    else:
        c += 1

print(c)
