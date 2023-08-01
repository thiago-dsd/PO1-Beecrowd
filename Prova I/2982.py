# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n = int(input())

soma = 0
for _ in range(n):
    opcao, v = input().split()
    v = int(v)
    if opcao == 'G':
        soma -= v
    else:
        soma += v

if soma >= 0:  # mais ganho do que gasto ou ganho igual
    print('A greve vai parar.')
else:
    print('NAO VAI TER CORTE, VAI TER LUTA!')
