# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

nome = input()
fixo = float(input())
vendas = float(input())

# 15/100 = 3/20
total = fixo + 3/20 * vendas

print(f'TOTAL = R$ {total:.2f}')
