n, m, s = [int(x) for x in input().split()]

prop = m/n

ex_1 = ex_2 = 0
for _ in range(s):
    x, y, h = [int(x) for x in input().split()]
    if x > 0 and y < prop*x:
        ex_2 += h
    else:
        ex_1 += h

print(ex_1, ex_2)
