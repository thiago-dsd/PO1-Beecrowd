n = int(input())

comp = 0

nomes = []
for _ in range(n):
    isComp, nome = input().split()
    nomes.append(nome)
    if isComp == '+':
        comp += 1

nomes.sort()
for nome in nomes:
    print(nome)

ncomp = n - comp
print(f'Se comportaram: {comp} | Nao se comportaram: {ncomp}')
