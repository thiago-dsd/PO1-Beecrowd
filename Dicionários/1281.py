n = int(input())

for _ in range(n):
    m = int(input())
    tot = 0
    
    prod = {}
    for _ in range(m):
        nome, valor = input().split()
        prod[nome] = float(valor)
    
    p = int(input())
    for _ in range(p):
        _prod, qtd = input().split()
        tot += prod[_prod] * int(qtd)
    
    print(f'R$ {tot:.2f}')
