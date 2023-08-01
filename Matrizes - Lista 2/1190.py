op = input()
s = c = 0 

# ate a metade
n = 11
for i in range(6):
    for j in range(12):
        if j > n:
            s += float(input())
            c += 1
        else:
            input()
    n -= 1

# depois da metade
n = 6
for i in range(6):
    for j in range(12):
        if j > n:
            s += float(input())
            c += 1
        else:
            input()
    n += 1

if op == 'S':
    print(f'{s:.1f}')
else:
    print(f'{s/c:.1f}')
