m, n = [int(x) for x in input().split()]

funcoes = {}
for _ in range(m):
    funcao, sal = input().split()
    funcoes[funcao] = int(sal)

for _ in range(n):
    txt = ''
    tot = 0
    while (entrada := input()) != '.':
        txt += entrada
    for funcao, sal in funcoes.items():
        tot += txt.count(funcao)*sal
    print(tot)
