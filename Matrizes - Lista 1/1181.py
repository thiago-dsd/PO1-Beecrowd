l = int(input())
op = input()
s = c = 0
for i in range(12*l):  # descartar nao usados
    input()
for i in range(l, 144, 12):
    s += int(input())
    c += 1
if op == 'S':
    print(f'{s:.1f}')
else:
    print(f'{s/c:.1f}')
