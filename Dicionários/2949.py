n = int(input())

qtds = {x: 0 for x in 'XHEAM'}

for i in range(n):
    _, tipo = input().split()
    qtds[tipo] += 1
    
print(f'{qtds["X"]} Hobbit(s)')
print(f'{qtds["H"]} Humano(s)')
print(f'{qtds["E"]} Elfo(s)')
print(f'{qtds["A"]} Anao(oes)')
print(f'{qtds["M"]} Mago(s)')

