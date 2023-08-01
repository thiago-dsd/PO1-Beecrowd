# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

A, B, C = map(int, input().split())
X, Y, Z = map(int, input().split())

qtd_a = X // A
qtd_b = Y // B
qtd_c = Z // C

print(qtd_a * qtd_b * qtd_c)

