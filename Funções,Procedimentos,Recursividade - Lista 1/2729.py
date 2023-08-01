n = int(input())
for _ in range(n):
    itens = input().split()
    itens = set(itens)
    itens = list(itens)
    itens.sort()
    print(' '.join(itens))
