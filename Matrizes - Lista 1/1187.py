op = input()
n = s = c = 0  # range em n: comeca em 0
for _ in range(5):  # otimizacao
    for i in range(12):
        if i > n and i < 11-n:
            s += float(input())
            c += 1
        else:
            input()
    n += 1

if op == 'S':
    print(f'{s:.1f}')
else:
    print(f'{s/c:.1f}')
