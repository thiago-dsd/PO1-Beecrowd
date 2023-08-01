op = input()
n = 11 # range em n: comeca em 0
s = c = 0  
for _ in range(12):
    for i in range(12):
        if i < n:
            s += float(input())
            c += 1
        else:
            input()
    n -= 1

if op == 'S':
    print(f'{s:.1f}')
else:
    print(f'{s/c:.1f}')
