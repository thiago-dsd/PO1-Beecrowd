# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(f'{dist:.4f}')
