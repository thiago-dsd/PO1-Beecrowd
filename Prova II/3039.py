f = m = 0

n = int(input())
for _ in range(n):
    _, l = input().split()
    if l == 'M':
        m += 1
    else:
        f += 1

print(m, 'carrinhos')
print(f, 'bonecas')
