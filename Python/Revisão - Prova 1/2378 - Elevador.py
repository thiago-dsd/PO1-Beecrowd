n, c = input().split()
n = int(n)
c = int(c)
contador = 0
saldo = 0
while contador != n:
    contador += 1
    s, e = input().split()
    s = int(s)
    e = int(e)
    saldo += (e - s)
    if saldo > c:
        print('S')
        break
if saldo <= c:
    print('N')

