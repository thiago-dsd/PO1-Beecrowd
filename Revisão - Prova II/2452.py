# Forma matematica:
# A qtd de dias total sera:
# 1) o maior comprimento entre dois pontos dividido inteiro por 2 (+1, se ímpar)
# 2) o maior comprimento entre um extremo e um ponto
# 3) comparar todos esses comprimentos, e sera o total de dias

comp, _ = input().split()
comp = int(comp)
pos = [int(x)-1 for x in input().split()]
lista = ['1' if x in pos else '0' for x in range(comp)]

fatias = ''.join(lista).split('1')
ext1 = fatias.pop(0)
ext2 = fatias.pop(-1)

if len(ext1) >= len(ext2):
    maior_comp = len(ext1)
else:
    maior_comp = len(ext2)

for fatia in fatias:
    tmp = len(fatia) // 2
    if len(fatia) % 2 == 1:
        tmp += 1
    if tmp > maior_comp:
        maior_comp = tmp

print(maior_comp)
