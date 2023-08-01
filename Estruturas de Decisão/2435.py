# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

n1, d1, v1 = map(int, input().split())
n2, d2, v2 = map(int, input().split())
# v = d/t => t = d/v
if d1/v1 < d2/v2:  # 1 mais rapido
    print(n1)
else:
    print(n2)
