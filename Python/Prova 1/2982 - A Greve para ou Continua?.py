num = int(input())
saldo = 0
despesas = 0
for c in range (1, num+1):
    c, v = input().split()
    v = int(v)
    if c == 'V':
        saldo += v
    else:
        despesas += v
if saldo >= despesas:
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')

