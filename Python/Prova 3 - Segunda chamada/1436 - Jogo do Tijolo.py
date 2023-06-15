cont = 0
testes = int(input())
for _ in range(testes):
    vetor = input().split()
    membros = int(vetor[0])
    vetor.remove(vetor[0])
    vetor.sort()
    cont += 1
    print("Case {}: {}".format(cont, vetor[(membros//2)]))

