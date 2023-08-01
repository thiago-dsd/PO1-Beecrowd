# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

EFICIENCIA = 12  # km/l = 12 -> 12 * l = km -> l = km / 12

tempo, vel = int(input()), int(input())
dist = tempo * vel
qtd_comb = dist / 12

print(f'{qtd_comb:.3f}')
