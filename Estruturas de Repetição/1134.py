# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

a, g, d = 0, 0, 0
while True:
    i = int(input())
    if i == 1:
        a += 1
    elif i == 2:
        g += 1
    elif i == 3:
        d += 1
    elif i == 4:
        break

print('MUITO OBRIGADO')
print('Alcool:', a)
print('Gasolina:', g)
print('Diesel:', d)
