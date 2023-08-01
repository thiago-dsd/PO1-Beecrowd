# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while (N := int(input())) != 0:
    varetas = []
    c = lados = 0
    for i in range(N):
        x, y = map(int,input().split())
        if y % 2 == 1:  # se n varetas for 2k + 1, o n utilizavel dessas varetas e 2k
            y -= 1
        varetas.append(y)
    for v in varetas:
        qtd, new_v = divmod(v, 4)
        c += qtd  # pega todos os 4k varetas e forma retangulos com elas
        # restara 2 ou 0 sempre, pois todas as qtds sao pares
        if new_v == 2:  # se restarem 2 varetas, pode formar 2 lados de um retangulo
            lados += 2
    c += lados // 4  # todos os values sao 2 -> podem formar lados
    print(c)

