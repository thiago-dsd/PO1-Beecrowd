# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
#a - otavio, b - bruno, c - ian
a, b, c = map(float, input().split())

if a < b and a < c:
    print('Otavio')
elif b < a and b < c:
    print('Bruno')
elif c < a and c < b:
    print('Ian')
else:
    print('Empate')

