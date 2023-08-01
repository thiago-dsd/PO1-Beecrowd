# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

x = float(input())

if x < 0 or x > 100:
    print('Fora de intervalo')
else:
    if x <= 25:
        print('Intervalo [0,25]')
    elif x <= 50:
        print('Intervalo (25,50]')
    elif x <= 75:
        print('Intervalo (50,75]')
    elif x <= 100:
        print('Intervalo (75,100]')
