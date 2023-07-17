letra = input()
lista = input().split()
num_letra = 0
quantidade_total_letras = len(lista)
for c in range (0, quantidade_total_letras):
    if lista[c].count(letra) >= 1:
        num_letra += 1
print('{:.1f}'.format((num_letra/quantidade_total_letras)*100))

