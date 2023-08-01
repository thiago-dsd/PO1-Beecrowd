# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# qtd fileiras == tam 1ª fileira
n = int(input())

# 1ª fileira
tmp = list(map(int, input().split()))

# a partir da segunda fileira
for i in range(n-1, 0, -1):
    new = []
    # para cada elemento da fileira
    for j in range(i):
        # verificar j, j+1
        if tmp[j] == tmp[j+1]:
            new.append(1) # preta: 1
        else:
            new.append(-1) # branca: -1
    tmp = new.copy()

# ultimo new: ultima fileira
if new[0] == -1:
    print('branca')
else:
    print('preta')
