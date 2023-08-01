# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

# Altura do seguinte maior que atual + pulo: nao consegue
# Se a altura do cano seguinte for muito baixa, o sapo não aguenta a queda
# (muito baixa quanto, atual - pulo?)

p, n = map(int, input().split())
canos = map(int, input().split())
atual = next(canos)  # consome o 1
consegue = True

for c in canos:
    if c > atual + p or c < atual - p:
        consegue = False
        break
    else:
        atual = c

if consegue:
    print('YOU WIN')
else:
    print('GAME OVER')
